# REFACTOR

**Workflow:** `refactor` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/refactor.md](./refactor.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`architecture-decision`](../skills/architecture-decision/README.en.md) — optional if `architecture-decision` conditions apply
2. [`doc-impact`](../skills/doc-impact/README.en.md) — optional if `doc-impact` conditions apply
3. [`implement`](../skills/implement/README.en.md) — required
4. [`verify`](../skills/verify/README.en.md) — required
5. [`code-review`](../skills/code-review/README.en.md) — required
6. [`decision-capture`](../skills/decision-capture/README.en.md) — optional if `decision-capture` conditions apply
7. [`doc-sync`](../skills/doc-sync/README.en.md) — optional if `doc-sync` conditions apply
8. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
