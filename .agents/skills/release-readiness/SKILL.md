---
name: release-readiness
description: Assesses release preparedness, deployment documentation and rollback/operations risks without deploying by implication.
---

# Release readiness skill

Compare deployment artifacts, configuration, secrets, migrations, rollback/restore, health checks, monitoring, alerting, runbooks, backwards compatibility, smoke tests, support ownership, vulnerabilities and accepted known issues with the approved release scope. State evidence and readiness result (`READY`, `READY_WITH_ACCEPTED_RISKS`, `NOT_READY`, `BLOCKED`, `NOT_ASSESSED`). A green unit-test suite alone is not proof of release readiness. Do not deploy, publish or change production resources unless the user explicitly authorizes that action. Ensure unresolved critical/high findings are made visible and never label a known failing requirement as passing.
