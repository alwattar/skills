# Codex skill discovery

Codex discovers per-project skills under `.agents/skills/` and user-scoped skills under `~/.agents/skills/`.

The unified repository keeps canonical skill sources in `skills/<name>/`. Use `scripts/activate-agents.py --host codex --target /path/to/project` after installation, or `--scope user` from a trusted source checkout. The activation creates safe links rather than duplicating skill implementations. It never replaces an unrelated existing skill.

Read the project's `AGENTS.md` for route selection, registry paths and approval limits. Fresh-context review capabilities must be detected at runtime; the host name is not proof.
