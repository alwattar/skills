# DOCS_ONLY

**Workflow:** `docs-only` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/docs-only.md](./docs-only.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`doc-impact`](../skills/doc-impact/README.en.md) — required
2. [`doc-sync`](../skills/doc-sync/README.en.md) — required
3. [`verify`](../skills/verify/README.en.md) — required
4. [`code-review`](../skills/code-review/README.en.md) — required
5. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
