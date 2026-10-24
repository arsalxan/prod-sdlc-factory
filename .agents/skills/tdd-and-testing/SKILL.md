---
name: tdd-and-testing
description: Test-driven development and quality-gate planning across unit, integration, regression, contract, end-to-end, static and performance/security tests. Use for planning/implementing/testing code.
---

# TDD and testing skill

## Planning

Translate approved acceptance criteria into observable checks before code. Select unit tests for isolated logic and integration tests when there is a meaningful boundary (API/database, service/queue, frontend/backend, service-to-service, filesystem/external adapter). Add contract, end-to-end, regression, security, performance or reliability tests only where requirements/risk justify them.

## Loop

1. Define expected behavior and test cases, including invalid inputs and edge cases.
2. Add the smallest useful test and run it to confirm it fails for the expected reason where feasible.
3. Implement the minimal change.
4. Run targeted test(s), then relevant suite/regressions.
5. Refactor while preserving green tests.
6. Report exact commands, results, environment, failures and skipped checks.

Do not fake an integration test where no integration boundary exists. Reuse existing project test frameworks/commands. Isolate test databases and external effects. Never destroy production or user data to make tests pass. A command invocation is not evidence of a pass; capture exit status/output. Test evidence only applies to the code/version and environment actually tested.

## Final gates

Discover and evaluate unit/integration suites, build/compile, type checking, lint, static analysis, migration validation, contract/end-to-end/security/performance tests and acceptance checks as applicable. Status must be `PASSED`, `FAILED`, `BLOCKED`, or `NOT_APPLICABLE` with reason. Never silently mark skipped required checks as passed.
