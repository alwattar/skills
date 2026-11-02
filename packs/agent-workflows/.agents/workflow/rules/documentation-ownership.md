# Documentation Ownership

| File | Owns |
|---|---|
| README.md | Actual setup, commands, status and navigation |
| CONTEXT.md | Vocabulary |
| PRODUCT.md | Purpose, actors, capabilities and scope |
| ARCHITECTURE.md | Components, boundaries and flows |
| DATA-MODEL.md | Entities, relationships, lifecycle and evidence/data invariants |
| SECURITY.md | Trust boundaries, prohibited acquisition and security requirements |
| DECISIONS.md | Durable decisions and known rationale |
| AGENTS.md | Operational agent instructions; references owning documents |

One durable fact = one authoritative home. Operational reminders may link to owners; they do not redefine contracts.
Specs live under `specs/`, local tickets under `tickets/`, ADRs under `docs/adrs/`, and audits/handoffs under `docs/engineering/` when needed. Directories are created when an artifact exists, not as speculative scaffolding.
External planning/vault material is reference context. Its exact location is not known yet; do not fabricate links or claim access. Repository documents summarize engineering intent, never duplicate the full vault.
