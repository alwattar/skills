# SECURITY_AUDIT

**Workflow:** `security-audit` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/security-audit.md](./security-audit.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`threat-model`](../skills/threat-model/README.en.md) — optional if `threat-model` conditions apply
2. [`secrets-safety`](../skills/secrets-safety/README.en.md) — optional if `secrets-safety` conditions apply
3. [`dependency-audit`](../skills/dependency-audit/README.en.md) — optional if `dependency-audit` conditions apply
4. [`privacy-review`](../skills/privacy-review/README.en.md) — optional if `privacy-review` conditions apply
5. [`security-audit`](../skills/security-audit/README.en.md) — required
6. [`verify`](../skills/verify/README.en.md) — required
7. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
