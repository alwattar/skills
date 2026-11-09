# RELEASE_REVIEW

**Workflow:** `release-review` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/release-review.md](./release-review.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`release-readiness`](../skills/release-readiness/README.en.md) — required
2. [`security-audit`](../skills/security-audit/README.en.md) — optional if `security-audit` conditions apply
3. [`privacy-review`](../skills/privacy-review/README.en.md) — optional if `privacy-review` conditions apply
4. [`performance-audit`](../skills/performance-audit/README.en.md) — optional if `performance-audit` conditions apply
5. [`verify`](../skills/verify/README.en.md) — required
6. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
