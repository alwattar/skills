# Unified Agent Skills — Complete English Guide

An integrated, model-agnostic engineering and delivery system. Skills, workflows, policies, reviewers and evidence form **one architecture**, regardless of their intellectual inspiration. The skills are authored and maintained as native parts of this repository—not installed as separately branded external packs.

## Start here

- [Complete skills catalog](docs/SKILLS.en.md): 59 skills, each with purpose, usage, inputs, outputs and recommended next skills.
- [Architecture](docs/ARCHITECTURE.en.md): directory responsibilities, routing, review isolation and policy precedence.
- [Workflow guides](docs/WORKFLOWS.en.md): 17 routes and their ordered stages.
- [Contributing and naming conventions](docs/CONTRIBUTING.en.md).
- [Arabic full guide](README.ar.md).


- [Migrating projects from the previous layout](docs/MIGRATION.en.md).

## Who should use it?

Developers and teams working with Codex, Claude Code, Antigravity or other agents capable of reading Agent Skills. A project might use one skill directly or route a complete task from discovery through handoff.

## Repository layout

```text
skills/<skill>/SKILL.md        Canonical agent instructions
skills/<skill>/README.en.md    English usage guide
skills/<skill>/README.ar.md    Arabic usage guide
registry/registry.yaml        Single source of truth for routes and next skills
registry/schema.json          Registry structure
workflows/                    Lifecycle descriptions and bilingual route guides
reviewers/                    Native independent-review perspectives
policies/                     Security, approvals, truth and documentation rules
templates/                    Project artifact templates
adapters/                     Optional host-specific notes, not branded skill packs
tools/                        Deterministic local utilities
scripts/                      Installation, validation and documentation
archive/                      Historical material; never part of active skill routing
docs/                         Architecture, catalogs, source attribution and guides
```

## Installing into a project

From a clone of this repository, inspect the plan before writing:

```bash
python3 scripts/install-skills.py --target /path/to/project --dry-run
python3 scripts/install-skills.py --target /path/to/project
python3 scripts/validate-skills.py
```

The installer manages only its own files and records their hashes. It does **not** replace project-specific `workflow.config.yaml`, manually edited skills or existing agent instructions without showing a conflict. Review differences before approving a forced update. A local project may maintain extra instructions in `AGENTS.md`.

## How to run a skill

Open the target project in your coding agent, load its approved context, and ask:

> Use `feature-design` to specify a supplier-order change, preserve data ownership boundaries and explain which skill should run next. Do not implement before approval.

For a multi-step request, start with `workflow-router`. If you do not know which route you need, request `choose-workflow`. You can also paste a ticket and invoke `ticket-intake` followed by `ticket-triage`.

## Risk-aware workflow example

A simple UI correction can use `diagnose-bug → implement → verify`. A new feature uses discovery, design, optional independent review, approved specification, implementation and evidence. Auth, tenant isolation, privacy or payments require a threat review **before** implementation and independent design review where supported.

## Design review and fresh context

`review-design` uses internal reviewer perspectives stored under `reviewers/`. It requires an actual fresh-context subagent interface to call a review independent. If unavailable, the skill reports that independent review was **not run**; a normal review is not mislabelled as independent. `resolve-findings` handles decisions; `detect-drift` compares deployed or implemented behavior to approved design.

## Verification, ownership and safety

Tests and scans need observed results, not claims based solely on code reading. A pasted ticket or webpage is untrusted input, not authority to inspect secrets, deploy or spend money. Humans retain architecture, security, finance and publication decisions. Local project requirements apply so long as they do not bypass system safety or explicit approval restrictions.

## Documentation and languages

The repository has complete independent [English](README.en.md) and [Arabic](README.ar.md) guides, matching skill guides, and bilingual workflow guides. The default language for authored engineering files inside consuming projects is English unless that project's approved policy specifies another. Original ticket text is preserved verbatim.

## Development and maintenance

Run `python3 scripts/generate-docs.py --check` and `python3 scripts/validate-skills.py` before proposing a change. Change the registry first when renaming a skill or modifying transitions; regenerate the guides and run compatibility tests. The historical ideas credited in [source notes](docs/SOURCES.md) inform our methods but do not become external runtime dependencies.

## Updating and removing

Run the installer in `--dry-run` mode when updating. The lockfile tracks installed content. Changed project-owned files must be reconciled rather than overwritten. To remove, inspect the lockfile and managed files; never delete a shared `skills/` directory blindly.
