#!/usr/bin/env python3
"""Validate that every registered skill, workflow and skill reference exists."""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "packs" / "agent-workflows"
REGISTRY = PACK / ".agents/workflow/WORKFLOW-REGISTRY.yaml"


def main() -> int:
    if not REGISTRY.is_file():
        print("Missing registry", file=sys.stderr)
        return 1
    text = REGISTRY.read_text(encoding="utf-8")
    skills_section = text.split("\nskills:\n", 1)
    if len(skills_section) != 2:
        print("Missing skills section", file=sys.stderr)
        return 1
    skill_entries = re.findall(r"(?m)^  ([a-z][a-z-]+): \{stage: ([a-z]+), path: ([^}]+)\}$",
                               skills_section[1])
    names = [name for name, _, _ in skill_entries]
    errors = []
    if len(names) != len(set(names)):
        errors.append("Duplicate skill registry names")
    for name, stage, path in skill_entries:
        file = PACK / path
        if not file.is_file():
            errors.append("Missing skill: " + str(file))
            continue
        raw = file.read_text(encoding="utf-8")
        if not raw.startswith("---\n") or "\nname: " + name + "\n" not in raw:
            errors.append("Malformed skill frontmatter: " + path)
    skill_files = list((PACK / ".agents/skills").glob("*/SKILL.md"))
    unregistered = sorted(f.parent.name for f in skill_files if f.parent.name not in names)
    if unregistered:
        errors.append("Unregistered skills: " + ", ".join(unregistered))

    registry_workflows = text.split("\nconditions:\n", 1)[0]
    routes = re.findall(r"(?m)^    route: ([A-Z_]+)$", registry_workflows)
    if len(routes) != len(set(routes)):
        errors.append("Duplicate workflow routes")
    workflow_files = re.findall(r"(?m)^    description: (.+)$", registry_workflows)
    for name in workflow_files:
        if not (PACK / name).is_file():
            errors.append("Missing workflow: " + name)
    for raw in re.findall(r"(?m)^    sequence: \[(.+)\]$", registry_workflows):
        try:
            steps = next(csv.reader([raw], skipinitialspace=True))
        except csv.Error:
            errors.append("Bad sequence: " + raw)
            continue
        for value in steps:
            step = value.strip().strip('"').rstrip("?")
            if step not in names:
                errors.append("Unknown skill in workflow: " + step)
    required = ["ticket-intake", "ticket-triage", "security-audit",
                "privacy-review", "campaign-planning", "seo-guardian"]
    for name in required:
        if name not in names:
            errors.append("Required skill missing: " + name)
    if "TICKET_EXECUTION" not in routes:
        errors.append("Ticket routing not registered")
    if not (PACK / ".agents/tools/intake_ticket.py").is_file():
        errors.append("Ticket CLI missing")
    if not (ROOT / "scripts/install-agent-workflows.py").is_file():
        errors.append("Installer missing")

    if errors:
        print("\n".join("FAIL: " + x for x in errors), file=sys.stderr)
        return 1
    print("PASS: " + str(len(names)) + " skills, " + str(len(routes))
          + " workflows, " + str(len(workflow_files)) + " workflow files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
