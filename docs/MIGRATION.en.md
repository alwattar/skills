# Migrating an existing project to Unified Agent Skills

This repository used to expose a separately installed portable workflow folder under `.agents/`. The new system is one unified collection with native skills in `skills/`, a single registry under `registry/` and shared workflows, reviewers and policies.

## Safe procedure

1. Record the current project commit and back up all agent configuration files. Do not back up credentials into this public repository.
2. Run `python3 scripts/install-skills.py --target /path/to/project --dry-run`. If the installer reports `.agents/workflow/WORKFLOW-REGISTRY.yaml`, **do not** force installation.
3. Review the old `.agents/` tree. Keep project-owned custom skills, instructions, tickets, audit artifacts and settings. Identify files copied by the previous pack and changes made after installation.
4. In a dedicated project branch, relocate or remove **only verified old managed files** after backing them up; never delete `.agents/` wholesale. Preserve the existing `tickets/` records.
5. Inspect `AGENTS.md` for `<!-- agent-workflows:start -->` and `<!-- agent-workflows:end -->` and remove or replace only that owned section. Preserve all unrelated instructions and local approvals. Review any `CLAUDE.md` and `GEMINI.md` pointers that still reference the old locations.
6. Run the dry run again, resolve any conflicts without overwriting unowned files, then execute the installer.
7. Confirm that `workflow.config.yaml` retains its project-specific values, and validate the installed registry, skill discovery and a sample local ticket.
8. Commit the project migration independently of any feature code. Keep a reversible backup and test commands.

## Do not assume

- An older user's copied `.agents` content is automatically owned by the new installer.
- A renamed skill implies that project-owned custom instructions can be discarded.
- Global installation through one host (Claude Code, Codex) configures every host.
- Markdown policies provide filesystem sandbox protection.

The migration is intentionally **manual and fail-closed** for pre-existing old installations. This preserves work and avoids duplicate active routers. For newly created projects, the unified installer handles ordinary idempotent updates automatically.
