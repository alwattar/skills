# Unified Path Contract

Canonical paths relative to the installed project's root:
- Skills: `skills/<name>/SKILL.md`
- One registry: `registry/registry.yaml` (JSON syntax, valid YAML)
- Workflows: `workflows/<name>.md`
- Review personas: `reviewers/<name>.md`
- Policies: `policies/<name>.md`
- Templates: `templates/<name>.md`
- Runtime tools: `tools/`
- Project profile: `workflow.config.yaml`
- Source documentation: `README.en.md` and `README.ar.md`
- User data and project artifacts: remain in the *consumer project*, not the reusable skills repository.

Skill relationships, optional steps and workflow ordering are owned only by `registry/registry.yaml`. Do not duplicate the graph in multiple sources. Keep per-skill guides generated from the registry; preserve project AGENTS.md and owner approvals.
