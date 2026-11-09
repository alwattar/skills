---
name: configure-project
description: Adopt unified skills in a project while protecting local settings.
---
# Configure Project

Inspect existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `workflow.config.yaml`, local skills and repositories' constraints.
Use `scripts/install-skills.py --dry-run` first. Show conflicts and preserve local settings.
Document platform capabilities, coding conventions, test commands, documentation language and approval boundaries.
Do not inspect credentials or overwrite user-modified files silently.
**Output:** project configuration, installation evidence and unresolved conflicts.
**Next:** `project-bootstrap` or `workflow-router`.
