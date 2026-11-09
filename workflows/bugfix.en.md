# BUGFIX

**Workflow:** `bugfix` · **Risk profile:** `low`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/bugfix.md](./bugfix.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`diagnose-bug`](../skills/diagnose-bug/README.en.md) — required
2. [`tdd`](../skills/tdd/README.en.md) — optional if `tdd` conditions apply
3. [`implement`](../skills/implement/README.en.md) — required
4. [`security-audit`](../skills/security-audit/README.en.md) — optional if `security-audit` conditions apply
5. [`accessibility-audit`](../skills/accessibility-audit/README.en.md) — optional if `accessibility-audit` conditions apply
6. [`performance-audit`](../skills/performance-audit/README.en.md) — optional if `performance-audit` conditions apply
7. [`verify`](../skills/verify/README.en.md) — required
8. [`code-review`](../skills/code-review/README.en.md) — required
9. [`decision-capture`](../skills/decision-capture/README.en.md) — optional if `decision-capture` conditions apply
10. [`doc-sync`](../skills/doc-sync/README.en.md) — optional if `doc-sync` conditions apply
11. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
