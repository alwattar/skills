# Using the unified skills with coding agents

The library has one canonical representation in `skills/` and the registry. Host discovery directories contain only symlinks to those skills, not independent packages.

## Project-local Codex + Claude Code

```bash
python3 scripts/install-skills.py --target /path/to/project --dry-run
python3 scripts/install-skills.py --target /path/to/project
python3 scripts/activate-agents.py --target /path/to/project --host codex --host claude-code --dry-run
python3 scripts/activate-agents.py --target /path/to/project --host codex --host claude-code
```

## User-wide discovery

From a trusted checkout of this repository:

```bash
python3 scripts/activate-agents.py --scope user --host codex --host claude-code --dry-run
python3 scripts/activate-agents.py --scope user --host codex --host claude-code
```

User-wide links target the trusted source checkout. If it moves, re-run activation after inspecting the links. A Git update to source skills changes what global links load, so review changes before updating a trusted checkout.

## Limits

- This mechanism uses symlinks and may require OS permissions on Windows.
- It does not install the full project workflow registry into the user's home directory. For multi-step workflows, the agent needs project context and an accessible registry.
- No automatic Antigravity paths are assumed until that host is verified.
- Existing user-owned skill locations are never overwritten.
- Independent design review remains contingent on runtime support for genuine fresh-context subagents.
