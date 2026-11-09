#!/usr/bin/env python3
"""Check or rebuild missing/outdated skill guides from canonical bilingual metadata."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def skill_guide(name: str, skill: dict, locale: str, skills: dict) -> str:
    next_names = skill.get("next", [])
    if locale == "en":
        lines = [
            f"# {name}", "", f"**Purpose:** {skill['summary_en']}.", "",
            f"**Stage:** {skill['stage']} · **Instructions:** [SKILL.md](./SKILL.md)", "",
            "## When to use", "", skill["when_en"], "", "## How to use", "",
            f"1. Open the target project and load approved context, constraints, and the skill instructions.",
            f"2. Ask the agent: \"Use {name} to {skill['summary_en'].lower()} for this task; report actual evidence and next steps.\"",
            "3. Follow project safety and approval gates; inspect the output before continuing.", "",
            "## Inputs", "", skill["inputs_en"], "", "## Expected output", "", skill["outputs_en"], "",
            "## Recommended next skills", ""
        ]
        lines += [f"- [{n}](../{n}/README.en.md) — {skills[n]['summary_en']}." for n in next_names] or ["- [handoff](../handoff/README.en.md) — document the outcome."]
        lines += ["", "The registry determines actual sequence and conditions; this list is advisory.",
                  "", "## Registered workflows", "",
                  ", ".join(skill.get("workflows", [])) or "Can run as a standalone skill.",
                  "", "## Safety", "", "Preserve owner approvals, protect secrets, and never claim an unrun check passed."]
    else:
        lines = [
            f"# {name}", "", f"**الهدف:** {skill['summary_ar']}.", "",
            f"**المرحلة:** {skill['stage']} · **تعليمات المهارة:** [SKILL.md](./SKILL.md)", "",
            "## متى تستخدم؟", "", skill["when_ar"], "", "## كيفية الاستخدام", "",
            "1. افتح المشروع المستهدف واقرأ السياق والقيود والتعليمات المعتمدة.",
            f"2. اطلب من الوكيل: «استخدم {name} من أجل {skill['summary_ar']} في هذه المهمة، وقدّم أدلة فعلية واقترح الخطوة التالية».",
            "3. احترم حدود الصلاحيات والموافقات، وراجع المخرجات قبل المتابعة.", "",
            "## المدخلات", "", skill["inputs_ar"], "", "## المخرجات", "", skill["outputs_ar"], "",
            "## المهارات التالية المقترحة", ""
        ]
        lines += [f"- [{n}](../{n}/README.ar.md) — {skills[n]['summary_ar']}." for n in next_names] or ["- [handoff](../handoff/README.ar.md) — لتسليم النتائج."]
        lines += ["", "السجل المركزي يحدد الترتيب والشروط؛ هذه توصيات وليست موافقات.",
                  "", "## المسارات المسجلة", "", "، ".join(skill.get("workflows", [])) or "يمكن تشغيلها مستقلة.",
                  "", "## الأمان", "", "احترم موافقات المالك واحم الأسرار ولا تدعِ نجاح فحص لم يُنفّذ."]
    return "\n".join(lines).rstrip() + "\n"


def check_guide(path: Path, skill: dict, lang: str) -> list[str]:
    if not path.is_file():
        return ["missing"]
    text = path.read_text(encoding="utf-8")
    errors = []
    if skill[f"summary_{lang}"] not in text:
        errors.append("outdated summary")
    if skill[f"when_{lang}"] not in text:
        errors.append("missing trigger")
    if skill[f"inputs_{lang}"] not in text or skill[f"outputs_{lang}"] not in text:
        errors.append("missing input/output contract")
    if "SKILL.md" not in text:
        errors.append("missing canonical skill link")
    for name in skill["next"]:
        if f"../{name}/README.{lang}.md" not in text:
            errors.append(f"missing transition to {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Do not write; report missing/outdated guide contracts")
    args = parser.parse_args()
    data = json.loads((ROOT / "registry/registry.yaml").read_text(encoding="utf-8"))
    failures = []
    changed = 0
    for name, meta in data["skills"].items():
        for lang in ("en", "ar"):
            path = ROOT / "skills" / name / f"README.{lang}.md"
            issues = check_guide(path, meta, lang)
            if issues:
                if args.check:
                    failures.append(str(path.relative_to(ROOT)) + ": " + ", ".join(issues))
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(skill_guide(name, meta, lang, data["skills"]), encoding="utf-8")
                    changed += 1
    for issue in failures:
        print("FAIL:", issue, file=sys.stderr)
    print(f"{'Checked' if args.check else 'Regenerated'} {2 * len(data['skills'])} bilingual skill guides; {changed} rewritten")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
