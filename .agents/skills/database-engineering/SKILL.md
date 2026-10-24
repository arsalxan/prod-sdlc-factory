---
name: database-engineering
description: Database schema, migrations, transactions, indexing, query behavior, consistency and safe testing practices. Use whenever persistence/query/migration behavior is relevant.
---

# Database engineering skill

Inspect the current data model, engine/version, migrations, schema history, transaction boundaries, query patterns, constraints, indexes, data volume assumptions and rollback strategy. Preserve data integrity and compatibility. Consider NULL/unique semantics, foreign keys, isolation/locking, concurrent updates, N+1 queries, pagination, index selectivity and safe migrations. Avoid destructive changes; file/DB deletion and destructive migration require explicit authorization.

For tests, prefer isolated disposable databases and reproducible fixtures. Don't assume in-memory DB behavior perfectly matches production. Include migration upgrade/rollback checks when appropriate. Validate query plans/performance only where risk warrants it. Never run cleanup against production merely to reset a test.
