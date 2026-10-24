---
description: "Quality gates. Trigger when user asks to run tests, build, type checks, lint, static analysis, or final QA."
---

# Command workflow: Quality gates

**Use when:** Trigger when user asks to run tests, build, type checks, lint, static analysis, or final QA.

1. Discover project-specific test/build/CI commands.
2. Choose applicable unit, integration, build, type, lint/static analysis, contract/e2e/regression/security/performance/acceptance checks according to specs/risk.
3. Record actual command, code/environment state, exit status and evidence.
4. Report `PASSED`, `FAILED`, `BLOCKED`, or `NOT_APPLICABLE` for each gate with rationale. A skipped required gate is not passed.
5. Do not make post-review fixes without authorization.
