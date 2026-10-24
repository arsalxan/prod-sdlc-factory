# prod-sdlc-factory

A repository for a self-routing, evidence-driven software development lifecycle (SDLC) factory.

The goal is to let a user state an outcome once—such as `Use prod-sdlc-factory to build a Spring Boot service`—and have the factory choose the appropriate workflow, agents, skills, commands, tools, hooks, and quality gates without requiring the user to coordinate them manually.

## Core design principles

1. **Single entry point:** the factory controller interprets the request and routes it to the right workflow.
2. **Automatic discovery:** inspect the workspace, project instructions, repository state, available capabilities, and existing test/build configuration before acting.
3. **Progressive context:** read requirements, repository content, and skill references incrementally; do not load everything by default.
4. **Approval gates:** specifications, technology-stack selection, and implementation plans require explicit user approval before the next gated stage begins.
5. **Generic agents, reusable skills:** agents own responsibilities; skills supply technology- or task-specific knowledge. Load skills only when relevant and available.
6. **Traceability:** map approved requirements to specifications, plans, implementation, tests, and review findings.
7. **Evidence-driven completion:** report actual commands, results, failures, blockers, and unverified items. Never mark a required gate as passing without evidence.
8. **Test-driven work:** plan and perform unit and applicable integration tests before or alongside implementation planning; add other tests based on requirements and risk.
9. **User-controlled review fixes:** Breaker and Reviewer findings are reported with evidence and severity. Post-review Bug Fixer changes require explicit user authorization.
10. **Least privilege:** constrain workspace access and tools; confirm destructive file operations and database destruction explicitly. Project instructions cannot override factory-wide safety rules.
11. **Safe recovery:** verify saved documentation and code state before resuming. Resume automatically when verification succeeds; investigate mismatches instead of trusting stale checkpoints.
12. **Avoid overengineering:** choose agents, skills, commands, integrations, and quality gates only when they add clear value.
13. **GitHub-aware workflow:** support Git/GitHub operations through reusable skills, with explicit authorization for sensitive actions such as pushing, merging, publishing, or changing repository settings.
14. **No silent scope changes:** material changes to approved behavior, architecture, stack, or plan return to the appropriate approval gate.

## Technology and host strategy

The core design should remain modular and portable where possible. Reusable skills should follow the Agent Skills convention (`<skill-name>/SKILL.md`) with metadata and task-specific instructions. Host-specific entry points, subagent definitions, hooks, and command adapters should be added for the selected coding-agent runtime rather than assuming every host supports the same mechanisms.

The factory will include GitHub-oriented capabilities for repository discovery, branch and commit workflows, issues, pull requests, CI checks, releases, and safe handling of remote operations. Exact capabilities will be enabled only when the necessary CLI, authentication, permissions, and host integrations are available.

## Intended lifecycle

1. Discover workspace and request intent.
2. Select the appropriate workflow: new project, feature, bug fix, review-only, authorized fixes, resume, or direct question.
3. For new projects, gather requirements incrementally and decide whether phase planning is useful.
4. Produce modular specifications and obtain explicit approval.
5. recommend a suitable technology stack, reconcile alternatives, and obtain approval.
6. Offer a high-level diagram only when useful, no suitable diagram exists, and the user explicitly approves its creation.
7. Produce an implementation plan using complexity-aware planning and relevant skills; include unit tests and applicable integration tests.
8. Obtain explicit plan approval.
9. Implement in bounded tasks using TDD and relevant skills.
10. Run the Breaker workflow and follow its authorization rules.
11. Review implementation against approved specifications; report findings with severity and evidence.
12. Fix post-review findings only when authorized, then independently re-verify them.
13. Run applicable final QA gates: tests, integrations, build, type checks, lint/static analysis, and other project-required checks.
14. Report release readiness separately from QA; deployment requires its own authorization when applicable.
15. Save compact checkpoints, decisions, handoffs, and discussion records for recovery.

This lifecycle is a design target. Implementations should mark steps as conditional or not applicable when justified; they must not silently skip a mandatory approval gate.

## Build sequence

The factory will be built incrementally, one reviewed artifact at a time:

1. Repository charter and design boundaries — this file.
2. Core factory instructions and non-negotiable policies.
3. Single entry-point skill and request router.
4. Capability registry and skill-loading rules.
5. Workflow state machine, approval gates, and task-state schema.
6. Agent specifications: controller/orchestrator, phase/divide, phase describer, specs, stack chooser, diagram, planner, complexity assessor, implementer, breaker, fixer, reviewer, bug fixer, and QA.
7. Reusable skills: Git/GitHub, testing, security, architecture, and technology-specific skills for Java, Python, Go, Rust, and React as needed.
8. Commands and host-specific invocation adapters.
9. Hooks and executable safety/verification guards.
10. Templates and state/recovery records.
11. GitHub integration and optional MCP configuration.
12. Validation, sample workflows, documentation, and packaging.

The precise directory tree and host-specific files will be finalized as their corresponding steps are built. Do not create every planned file in advance; each artifact should be added and validated in its own step.

## Scope and approval boundary

This repository is being designed incrementally. A file being present does not itself authorize implementation, execution, destructive actions, deployment, or a change to an approved requirement. Proposals, open questions, accepted decisions, and rejected alternatives should remain distinguishable in discussion records.
