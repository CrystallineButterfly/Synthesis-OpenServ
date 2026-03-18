"""Project-specific context for OpenImpact Dispatcher."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "OpenImpact Dispatcher",
    "track": "OpenServ",
    "pitch": "A load-bearing service fabric for discovery, scheduling, execution receipts, and build-story outputs across the whole swarm.",
    "overlap_targets": [
        "Octant",
        "Filecoin",
        "ERC-8004 Receipts",
        "Olas",
        "Uniswap Agentic Finance",
        "Markee"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
