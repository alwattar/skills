#!/usr/bin/env python3
"""Validate canonical skill graph, bilingual documentation and safety ordering."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STAGES = {"routing", "discover", "design", "plan", "build", "verify", "synchronize", "deliver"}
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def validate(root: Path = ROOT) -> tuple[list[str], dict]:
    errors: list[str] = []
    try:
        registry = json.loads((root / "registry/registry.yaml").read_text(encoding="utf-8"))
        json.loads((root / "registry/schema.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"Cannot read registry/schema: {exc}"], {}
    skills = registry.get("skills", {})
    workflows = registry.get("workflows", {})
    conditions = registry.get("conditions", {})
    if registry.get("schema_version") != 1 or not isinstance(skills, dict) or not isinstance(workflows, dict):
        errors.append("Invalid registry structure/version")
        return errors, registry
    known = set(skills)
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    for name in sorted(actual - known):
        errors.append(f"Unregistered active skill: {name}")
    for name in sorted(known - actual):
        errors.append(f"Missing active SKILL.md: {name}")
    for name, item in skills.items():
        if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", name):
            errors.append(f"Invalid skill name: {name}")
        if item.get("path") != f"skills/{name}/SKILL.md":
            errors.append(f"Noncanonical skill path: {name}")
        if item.get("stage") not in STAGES:
            errors.append(f"Unknown stage for {name}")
        for field in ("summary_en", "summary_ar", "when_en", "when_ar", "inputs_en", "inputs_ar", "outputs_en", "outputs_ar"):
            if not isinstance(item.get(field), str) or len(item[field].strip()) < 5:
                errors.append(f"Missing bilingual contract {name}.{field}")
        source = root / f"skills/{name}/SKILL.md"
        if source.is_file():
            content = source.read_text(encoding="utf-8")
            fm = FRONTMATTER.match(content)
            if not fm or not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", fm.group(1)):
                errors.append(f"Missing/mismatched SKILL.md frontmatter name for {name}")
            if not fm or "description:" not in fm.group(1):
                errors.append(f"Missing SKILL.md description for {name}")
        for lang in ("en", "ar"):
            doc = root / f"skills/{name}/README.{lang}.md"
            if not doc.is_file():
                errors.append(f"Missing {lang} guide for {name}")
                continue
            text = doc.read_text(encoding="utf-8")
            if item.get(f"summary_{lang}", "") not in text:
                errors.append(f"Outdated {lang} summary for {name}")
            if not ("SKILL.md" in text and "README." in text or not item.get("next")):
                errors.append(f"Missing usage/next links in {lang} guide: {name}")
            for next_name in item.get("next", []):
                if f"../{next_name}/README.{lang}.md" not in text:
                    errors.append(f"Missing next-skill link {name} -> {next_name} in {lang} guide")
        for nxt in item.get("next", []):
            if nxt not in known or nxt == name:
                errors.append(f"Invalid recommended next skill: {name} -> {nxt}")
    route_ids: set[str] = set()
    for name, route in workflows.items():
        if route.get("route") in route_ids:
            errors.append(f"Duplicate workflow route {route['route']}")
        route_ids.add(route.get("route"))
        if not (root / route.get("description", "__missing__")).is_file():
            errors.append(f"Missing canonical workflow description for {name}")
        for lang in ("en", "ar"):
            if not (root / f"workflows/{name}.{lang}.md").is_file():
                errors.append(f"Missing {lang} workflow guide: {name}")
        steps = route.get("steps", [])
        if not isinstance(steps, list) or not steps:
            errors.append(f"Missing workflow steps: {name}")
            continue
        for entry in steps:
            skill = entry.get("skill")
            if skill not in known:
                errors.append(f"Unknown workflow skill {name}: {skill}")
            if not isinstance(entry.get("optional"), bool):
                errors.append(f"Nonboolean optional flag in {name}: {skill}")
            if entry.get("optional") and not conditions.get(skill):
                errors.append(f"Undeclared optional condition in {name}: {skill}")
        order = [entry.get("skill") for entry in steps]
        if "implement" in order:
            if "review-design" in order and order.index("review-design") > order.index("implement"):
                errors.append(f"Design review runs after implementation: {name}")
            if "threat-model" in order and order.index("threat-model") > order.index("implement"):
                errors.append(f"Threat modeling runs after implementation: {name}")
            if "privacy-review" in order and order.index("privacy-review") > order.index("implement"):
                errors.append(f"Privacy review runs after implementation: {name}")
            if "verify" in order and order.index("verify") < order.index("implement"):
                errors.append(f"Verification before implementation: {name}")
        if "resolve-findings" in order and "review-design" in order and order.index("resolve-findings") < order.index("review-design"):
            errors.append(f"Findings resolved before review: {name}")
    safety = workflows.get("security-change", {}).get("steps", [])
    sec_order = [entry.get("skill") for entry in safety]
    if not all(x in sec_order for x in ("threat-model", "implement", "security-audit", "verify")):
        errors.append("Security workflow is missing mandatory gates")
    else:
        if not (sec_order.index("threat-model") < sec_order.index("implement") < sec_order.index("security-audit") < sec_order.index("verify")):
            errors.append("Security workflow gate order is unsafe")
        if next((e.get("optional") for e in safety if e.get("skill") == "threat-model"), True):
            errors.append("Security-change threat model cannot be optional")
    for path in ("README.en.md", "README.ar.md", "AGENTS.md", "docs/ARCHITECTURE.en.md",
                 "docs/ARCHITECTURE.ar.md", "docs/SKILLS.en.md", "docs/SKILLS.ar.md",
                 "docs/WORKFLOWS.en.md", "docs/WORKFLOWS.ar.md", "docs/CONTRIBUTING.en.md",
                 "docs/CONTRIBUTING.ar.md", "policies/review-integrity.md"):
        if not (root / path).is_file():
            errors.append(f"Missing required documentation: {path}")
    if "review-design" in skills:
        for reviewer in ("clarity", "architecture", "security", "simplification", "implementation-readiness"):
            if not (root / f"reviewers/{reviewer}.md").is_file():
                errors.append(f"Missing reviewer perspective: {reviewer}")
    return errors, registry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print validation report as JSON")
    args = parser.parse_args()
    errors, reg = validate()
    report = {"valid": not errors, "skills": len(reg.get("skills", {})), "workflows": len(reg.get("workflows", {})), "errors": errors}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    elif errors:
        for err in errors:
            print("FAIL:", err, file=sys.stderr)
    else:
        print(f"PASS: {report['skills']} active skills, {report['workflows']} workflows, bilingual guides and security gates")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
