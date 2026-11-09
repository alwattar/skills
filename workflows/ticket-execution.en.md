# TICKET_EXECUTION

**Workflow:** `ticket-execution` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/ticket-execution.md](./ticket-execution.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`ticket-intake`](../skills/ticket-intake/README.en.md) — required
2. [`ticket-triage`](../skills/ticket-triage/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
