# Skill invocation and routing

All active skills use `skills/<name>/SKILL.md` and a shared [registry](../registry/registry.yaml).

## User-invoked and model-invoked

- User-invoked skills set `disable-model-invocation: true` and require a direct user request in supporting hosts.
- Model-invoked skills omit that field and can be selected by an authorized agent.
- The registry chooses the smallest workflow matching intent and safety gates. A slash-command does not bypass approval or privacy checks.

## Relationships

The registry is the single source of truth for stages, optional conditions, route order, and recommended follow-up skills. A skill's bilingual README explains how to use it and which related skills may follow.

## Scope

Skills do not automatically install external packages or grant deployment, financial or credential access. Source attributions are recorded under `docs/SOURCES.md`, not represented as separately installed runtime packs.
