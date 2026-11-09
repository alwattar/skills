# Review Integrity

Independent review means a genuinely fresh conversation context with a bounded explicit evidence packet, not merely a different prompt in the same context.
- Detect support for fresh-context delegation at runtime; never assume it from model or product name.
- If unavailable, record `INDEPENDENT_REVIEW_NOT_RUN`; permit a clearly identified regular review only if allowed.
- Keep reviewer tools read-only; do not grant credentials, deployment access or mutation permissions.
- A reviewer recommendation is evidence, not owner authorization.
- Report uncertainties, contradictory reviewer observations, and unreviewed areas.
