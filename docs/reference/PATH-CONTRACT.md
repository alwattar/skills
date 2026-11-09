# Workflow Path Contract

These paths are canonical and repository-root-relative:

- Skills: `.agents/skills/<skill-name>/SKILL.md`
- Workflow registry: `.agents/workflow/WORKFLOW-REGISTRY.yaml`
- Shared rules: `.agents/workflow/rules/`
- Workflow descriptions: `.agents/workflow/workflows/`
- Templates: `.agents/workflow/templates/`
- Adapters: `.agents/workflow/adapters/`

Do not resolve these paths relative to the currently loaded `SKILL.md`.
Resolve them from the repository root.

There is intentionally only one workflow/skill registry:
`.agents/workflow/WORKFLOW-REGISTRY.yaml`.

Repository profile: `workflow.config.yaml`. Route sequences and conditional-step policies belong only to the registry. Workflow descriptions explain prerequisites/gates and link to the registry rather than maintaining a second sequence.
Artifact locations: `specs/`, `tickets/`, `docs/adrs/`, `docs/engineering/`; create on use.
