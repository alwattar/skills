# Claude Code skill discovery

Claude Code discovers per-project skills under `.claude/skills/` and user-scoped skills under `~/.claude/skills/`.

Use `scripts/activate-agents.py --host claude-code --target /path/to/project` after installing canonical files, or `--scope user` for a trusted global source. The activation links to one maintained source; it does not vendor or duplicate third-party skill packs.

Project instructions, privacy and approval rules remain authoritative. Never assume fresh-context subagents are available without checking.
