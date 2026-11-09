# Architecture: one system, one registry

## Goals

A portable and cohesive set of autonomous agent skills, usable across languages, projects and coding assistants without runtime dependencies on branded external skills packs.

## Components

1. `skills/`: each active skill is a focused capability with a `SKILL.md` interface and bilingual operational guides; no duplicate active names.
2. `registry/registry.yaml`: canonical skills, stages, workflows, conditions, suggestions and bilingual descriptions. Uses JSON syntax (a valid YAML subset) so validators need no external YAML parser.
3. `workflows/`: human-readable route rationale, prerequisites and completion gates; ordering lives only in the registry.
4. `policies/`: shared truth, review integrity, privacy, owner approvals and documentation language.
5. `reviewers/`: local read-only critique perspectives; fresh-context delegation is optional capability, never faked.
6. `adapters/`: host-specific integration constraints; adapters must not redefine skill identities or policies.
7. `templates/`, `tools/`, `scripts/`: reusable artifacts, deterministic utilities and safe installation/validation.
8. `archive/`: preserved legacy texts, experiments and source material excluded from active routing.

## Execution model

Request → `workflow-router` → smallest authorized workflow → staged skills → validation/evidence → handoff. Required checks cannot be skipped through optional routing. For security-sensitive changes, assess the threat model and privacy **before** implementation. Independent reviews need true context separation; if unavailable report a gap rather than claiming independence.

## Skill contract

Each active skill declares identity, stage, invocation conditions, inputs, outputs, recommended transitions and workflow membership via the registry and its SKILL.md. The per-skill English and Arabic guides are projections of the same metadata. Transition suggestions never constitute approval.

## Project boundaries

Project files and secrets remain in each consuming project. The installer installs shared implementation files separately from project-owned `workflow.config.yaml` and agent instructions. No runtime mechanism may treat text policy as a replacement for operating-system sandboxing.

## Source inspiration

Concepts such as independent fresh-context design critique, modular engineering discipline and security gatekeeping are adapted as our own mechanisms. Attribution and applicable third-party licenses remain documented; no third-party plugin is an operational requirement.
