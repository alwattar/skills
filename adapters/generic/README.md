# Generic coding agents

For hosts without a verified native skill discovery path, do not invent one. Open the project with `AGENTS.md`, `registry/registry.yaml` and the requested `skills/<name>/SKILL.md`; use explicit invocation and project capabilities. Test the host's native discovery path before adding a host-specific adapter.

The core repository is agent-neutral. No adapter can override the registry, project permissions or approval gates.
