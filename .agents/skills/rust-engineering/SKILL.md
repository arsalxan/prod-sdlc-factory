---
name: rust-engineering
description: "Language-specific Rust practices: ownership, borrowing, error handling, lifetimes, concurrency, unsafe blocks and tests. Load for Rust tasks."
---

# Rust engineering skill

Respect the declared toolchain and edition. Prefer ownership and borrowing patterns that make invariants clear; clone only when justified. Use `Result` for recoverable errors and propagate/annotate errors meaningfully; avoid `unwrap`/`expect` on expected runtime failures in production paths. Keep `unsafe` rare, documented with invariants, and locally auditable. Consider thread safety (`Send`/`Sync`), locks, poisoning and async cancellation where relevant. Avoid unnecessary allocations and complicated lifetimes if a simpler design exists. Test edge/error conditions; run formatting, tests, linting and relevant feature configurations. Preserve crate/API compatibility unless change is approved.
