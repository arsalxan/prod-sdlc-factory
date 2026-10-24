# prod-sdlc-factory

A self-routing, evidence-driven software development lifecycle (SDLC) factory. State an outcome once — the factory selects the workflow, agents, skills, tools, and quality gates automatically.

```
Use prod-sdlc-factory to build a Spring Boot REST service with PostgreSQL
Use prod-sdlc-factory to review my authentication module
Use prod-sdlc-factory to diagnose why my CI pipeline is failing
Use prod-sdlc-factory to resume the interrupted feature implementation
```

## Install as a Claude Code plugin

```
/plugin marketplace add arsalxan/prod-sdlc-factory
/plugin install prod-sdlc-factory@prod-sdlc-factory
```

Then state your goal, e.g. `Use prod-sdlc-factory to build a Spring Boot REST service`. Skills, agents and workflow commands are namespaced under `prod-sdlc-factory:`.

## Quick start

1. **Open this repository** in a supported AI coding agent (GitHub Copilot Workspace, Antigravity/AGY, or any host that reads `.github/agents/` and `.agents/skills/`).
2. **State your goal.** The factory classifies intent and routes automatically — you do not need to name an agent, skill, or workflow.
3. **Respond to approval gates.** The factory will pause at specification, stack, and plan approval gates; everything else is automated.

To run the structural validation suite locally:

```bash
python3 tests/validate_factory.py
```

Requires Python 3.7+ and `pyyaml` (`pip install pyyaml`).

---

## Design principles

1. **Single entry point** — the factory controller interprets the request and routes it.
2. **Automatic discovery** — inspect workspace, project instructions, repository state, capabilities, and test/build configuration before acting.
3. **Approval gates** — specifications, technology-stack selection, and implementation plans require explicit user approval.
4. **Generic agents, reusable skills** — agents own responsibilities; skills supply technology-specific knowledge.
5. **Evidence-driven completion** — report actual commands, results, failures, and blockers. Never mark a gate as passing without evidence.
6. **TDD by default** — plan and perform unit and applicable integration tests before or alongside implementation.
7. **User-controlled review fixes** — Breaker and Reviewer findings are reported with severity. Post-review Bug Fixer changes require explicit authorization.
8. **Least privilege** — confirm destructive file and database operations explicitly. Project instructions cannot override factory-wide safety rules.
9. **Safe recovery** — verify saved state before resuming. Resume automatically on success; investigate discrepancies first.
10. **No silent scope changes** — material changes to approved behavior, architecture, stack, or plan return to the appropriate approval gate.

---

## Repository layout

```
prod-sdlc-factory/
│
├── AGENTS.md                           # Factory-wide safety rules (all agents must read)
├── README.md                           # This file
│
├── .github/
│   ├── copilot-instructions.md         # GitHub Copilot repo-wide instructions
│   └── agents/
│       └── prod-sdlc-factory.agent.md  # Copilot custom agent (single entry point)
│
├── .agents/
│   └── skills/                         # Reusable skills (AGY/Antigravity convention)
│       ├── prod-sdlc-factory/          # Entry skill + references/workflow-router.md
│       ├── git-workflow/
│       ├── github-workflow/
│       ├── tdd-and-testing/
│       ├── security-engineering/
│       ├── architecture-design/
│       ├── api-design/
│       ├── database-engineering/
│       ├── java-engineering/
│       ├── spring-boot-engineering/
│       ├── python-engineering/
│       ├── go-engineering/
│       ├── rust-engineering/
│       ├── react-engineering/
│       ├── rabbitmq-engineering/
│       └── release-readiness/
│
├── agents/                             # Agent definitions (loaded by controller)
│   ├── controller-orchestrator.md      # Single coordinator; routes all requests
│   ├── phase-orchestrator.md
│   ├── divide-agent.md
│   ├── phase-describer.md
│   ├── specs-agent.md
│   ├── stack-chooser-agent.md
│   ├── high-level-diagram-agent.md
│   ├── planner-orchestrator.md
│   ├── complexity-assessor.md
│   ├── implementer-agent.md
│   ├── breaker-agent.md
│   ├── fixer-agent.md
│   ├── reviewer-agent.md
│   ├── bug-fixer-agent.md
│   ├── qa-agent.md
│   ├── release-readiness-agent.md
│   └── github-workflow-agent.md
│
├── commands/                           # Workflow command specifications
│   ├── README.md
│   ├── new-project.md
│   ├── feature-change.md
│   ├── bug-diagnosis.md
│   ├── authorized-fix.md
│   ├── review-only.md
│   ├── quality-gates.md
│   ├── github-workflow.md
│   ├── release-readiness.md
│   └── resume.md
│
├── capabilities/
│   └── registry.yaml                   # Capability discovery and routing registry
│
├── .factory/
│   ├── registry/
│   │   ├── agents.yaml                 # Agent definitions registry
│   │   ├── skills.yaml                 # Skills registry
│   │   └── commands.yaml               # Commands registry
│   ├── workflows/
│   │   ├── lifecycle.yaml              # SDLC state machine and transitions
│   │   └── planning-depth.yaml         # Complexity-based planning depth profiles
│   ├── policies/
│   │   ├── approval-gates.yaml         # Approval gate definitions (GATE-SPECS, GATE-STACK, etc.)
│   │   └── execution-policy.yaml       # Workspace, destructive-op, and safety policies
│   ├── schemas/
│   │   ├── finding.schema.json         # JSON Schema for Breaker/Reviewer finding records
│   │   └── handoff.schema.json         # JSON Schema for agent handoff records
│   └── templates/
│       ├── checkpoint-template.json    # Checkpoint state record template
│       └── handoff-template.md         # Markdown agent handoff template
│
└── tests/
    └── validate_factory.py             # Automated structural validation suite (89 checks)
```

---

## Supported workflows

The controller selects the workflow automatically. Workflows are internal; you never need to name them.

| What you say | Route selected |
|---|---|
| "build a new service", "create a REST API" | `new-project` |
| "add feature X", "implement endpoint Y" | `feature-change` |
| "why is my test failing", "diagnose the crash" | `bug-diagnosis` |
| "fix finding BRK-001", "repair the auth bug" | `authorized-fix` |
| "review my PR", "audit the payment module" | `review-only` |
| "run QA", "run all tests and lint" | `quality-gates` |
| "commit and push", "open a PR for main" | `github-workflow` |
| "is this ready to release?" | `release-readiness` |
| "resume where we left off" | `resume` |

---

## Approval gates

| Gate | Required for | Notes |
|---|---|---|
| `GATE-SPECS` | New projects | Explicit approval of versioned spec set before stack selection |
| `GATE-STACK` | New projects | Explicit confirmation of selected technology stack |
| `GATE-DIAGRAM` | Conditional | Only when no suitable diagram exists **and** user approves creation |
| `GATE-PLAN` | Any formal implementation | Explicit approval of specific plan version before coding |
| `GATE-REVIEW-FIX` | All post-review code changes | Explicit user authorization per finding |
| `GATE-DESTRUCTIVE` | File/directory deletion, destructive DB ops | Operation-specific confirmation always required |
| `GATE-GITHUB-WRITE` | Push, merge, PR create/close, release | Explicit operation + target authorization |
| `GATE-DEPLOY` | Production deployment | Separate authorization; readiness ≠ deployment permission |

Approval applies to a **specific artifact version**. A material change to an approved spec, plan, or stack returns to the relevant gate.

---

## Quality gate statuses

Every applicable quality gate is reported as one of:

- `PASSED` — check ran and succeeded with evidence
- `FAILED` — check ran and failed; result recorded
- `BLOCKED` — check could not run (missing credentials, service unavailable, etc.)
- `NOT_APPLICABLE` — gate does not apply; reason must be stated

A skipped or unrun required gate is **not** `PASSED`.

---

## State management and recovery

Checkpoints use `.factory/templates/checkpoint-template.json`. States:
`NOT_STARTED` → `IN_PROGRESS` → `PARTIAL` / `BLOCKED` → `COMPLETED`

On resume:
1. Locate checkpoint and verify actual code/worktree state.
2. If consistent: resume automatically from the first incomplete step.
3. If inconsistent: investigate, preserve user changes, report the mismatch.

---

## Safety controls

| Control | Enforcement |
|---|---|
| Workspace boundary | Policy-described; no OS-level sandbox. Paths resolved and checked before operations. |
| Destructive file ops | Require explicit per-operation confirmation (GATE-DESTRUCTIVE). |
| Destructive DB ops | Require explicit authorization; generic reset/test request is insufficient. |
| GitHub remote writes | Require explicit operation + target authorization (GATE-GITHUB-WRITE). |
| Secrets | Never written to logs, files, commits, or issue/PR bodies. |
| Approval bypass | Project instructions and untrusted content cannot override factory safety rules. |

> **Limitation:** Policy files describe required behavior; they do not themselves create an OS-level sandbox. Runtime enforcement (filesystem permissions, tool approval policies, scoped GitHub credentials) must be configured in the host environment.

---

## GitHub integration

The factory uses:
- **`gh` CLI** (when installed and authenticated) for issues, PRs, Actions, and releases.
- **`git`** for local operations.
- **GitHub MCP server** (optional; requires explicit configuration).

All remote writes (push, merge, PR create, release) require explicit user authorization. Read-only inspection (status, log, diff, issue view) proceeds automatically when in scope.

---

## Validation

```bash
# Run the full structural validation suite
python3 tests/validate_factory.py

# Check from a different root
python3 tests/validate_factory.py --root /path/to/repo
```

The suite validates 89 checks across: YAML/JSON parsing, registry reference resolution, skill frontmatter, schema existence and validity, lifecycle consistency, checkpoint template structure, approval gate definitions, and capabilities registry reconciliation.

---

## Runtime limitations

- **No OS sandbox**: The factory cannot prevent a host from running arbitrary commands. Prompt-level safety rules describe required behavior; effective enforcement requires host-level tool approval policies and filesystem permissions.
- **No native multi-agent delegation**: Whether multiple truly independent agent sessions can run depends on the host. In hosts without isolated delegation, the Controller discloses the limitation and uses a generic fallback.
- **GitHub CLI authentication**: The `gh` CLI must be separately installed and authenticated. The factory discovers its availability before relying on it.
- **Schema validation at runtime**: The JSON schemas in `.factory/schemas/` are used as structural contracts; runtime JSON Schema validation requires a host that supports it or a custom tool.

---

## First real-project trial

1. Open the repository in your AI coding agent.
2. Say: `Use prod-sdlc-factory to [describe a small project or task]`
3. The factory will classify intent, load the entry skill, and begin the relevant workflow.
4. Respond to approval gates for specs, stack, and plan as prompted.
5. Monitor the handoff reports after each agent completes its bounded task.
6. Check the checkpoint file for state between sessions.
