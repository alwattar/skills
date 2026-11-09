# Contributing to Unified Agent Skills

## Before adding a skill

Search the [registry](../registry/registry.yaml) and [catalog](SKILLS.en.md). Improve an existing capability where possible. Only create a new skill when it owns a distinct, testable responsibility with clear boundaries.

## Contract and names

Use lowercase kebab-case and stable, task-oriented names. Each active skill lives at `skills/<name>/SKILL.md` and has name/description frontmatter. Add full bilingual metadata to the registry: summary, trigger, inputs, expected output, stage, workflows and recommended next skills. Avoid duplicating route ordering inside the skill. One source of truth: the registry.

## Quality bar

- Respect owner approvals and untrusted inputs; never read, echo or commit secrets.
- Distinguish verified facts, unknowns, planned work and source text.
- Preserve project architecture, documented invariants and workflow gates.
- Make testable output and failure behavior explicit.
- No claims of independent subagent reviews unless delegation really ran in fresh context.
- Keep docs and tested behavior consistent.

## Edit workflow

1. Modify or add the skill and its registry entry.
2. Modify the registered workflow only if necessary, with optional conditions and explicit risk gates.
3. Regenerate bilingual skill/workflow guides: `python3 scripts/generate-docs.py`.
4. Run `python3 scripts/validate-skills.py` and `python3 -m unittest discover -s tests -v`.
5. Inspect installation into a disposable test project, then open a PR against the active feature branch.

## Migration and historical material

Never delete distinct historical content without evaluating it. Mark retired skills under `archive/`; convert genuine duplicate methods into canonical skill references. Third-party text requires proper license and attribution; influence alone does not create a runtime dependency.
