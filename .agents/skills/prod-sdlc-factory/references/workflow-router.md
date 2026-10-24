# Workflow Router Reference

This document defines the routing logic used by the Controller Orchestrator to classify user intent and select the smallest safe workflow. It supplements `.factory/registry/commands.yaml` with detailed routing signals and decision rules.

## Routing decision sequence

1. **Read available context** — workspace, Git status, existing checkpoint, project instructions, and user goal.
2. **Classify intent** — match the user goal against the signals below.
3. **Select the workflow** — choose the smallest workflow that safely satisfies the goal.
4. **Load capabilities** — select relevant agents, skills, and commands from the registries.
5. **Check for blockers** — if a required approval or capability is missing, report the blocker before proceeding.

---

## Intent classification signals

### Direct question or explanation
- **Signals:** user asks how something works, asks for a definition, requests a summary, or asks about the factory itself.
- **Workflow:** `direct_response` — answer directly; do not launch an SDLC pipeline.
- **Required approval gates:** none.

### Resume interrupted work
- **Signals:** "resume", "continue", "pick up where we left off", or an existing checkpoint is referenced.
- **Workflow:** `resume` (commands/resume.md)
- **First action:** Locate and verify checkpoint; verify actual code/worktree state; resolve discrepancies before proceeding.
- **Required approval gates:** reuse prior approvals only if artifact versions are unchanged.

### New project
- **Signals:** no existing project code, "build a", "create a new", "start a service/app/system", requirements not yet specified.
- **Workflow:** `new-project` (commands/new-project.md)
- **Required approval gates:** GATE-SPECS → GATE-STACK → GATE-DIAGRAM (conditional) → GATE-PLAN.

### Feature or material change to existing project
- **Signals:** existing project detected, "add", "implement", "extend", "change", "migrate", named component or endpoint.
- **Workflow:** `feature-change` (commands/feature-change.md)
- **Required approval gates:** GATE-PLAN (at minimum); GATE-SPECS if material requirement change; GATE-STACK if stack change.

### Bug diagnosis
- **Signals:** "why is", "investigate", "diagnose", "not working", "failing", "error", fix not yet explicitly authorized.
- **Workflow:** `bug-diagnosis` (commands/bug-diagnosis.md)
- **Required approval gates:** none to diagnose; GATE-PLAN required before repair.
- **Important:** diagnosis does not authorize code changes.

### Authorized fix
- **Signals:** user explicitly says "fix", "repair", references a confirmed finding or diagnosis, or a Breaker/Reviewer finding has been explicitly authorized.
- **Workflow:** `authorized-fix` (commands/authorized-fix.md)
- **Required approval gates:** explicit finding authorization is itself the gate; GATE-PLAN if bounded task plan required.

### Review only
- **Signals:** "review", "audit", "check", "inspect", no code change requested, or a completed implementation needs independent review.
- **Workflow:** `review-only` (commands/review-only.md)
- **Required approval gates:** none to review; GATE-REVIEW-FIX required before any post-review code change.
- **Important:** no code changes during review.

### Quality gates / QA run
- **Signals:** "run tests", "check quality", "lint", "build", "CI", "type-check", "run all gates", post-implementation QA.
- **Workflow:** `quality-gates` (commands/quality-gates.md)
- **Required approval gates:** none to run checks; failures do not authorize automatic fixes.

### GitHub workflow
- **Signals:** "commit", "push", "pull request", "PR", "issue", "branch", "merge", "GitHub Actions", "CI/CD", "release".
- **Workflow:** `github-workflow` (commands/github-workflow.md)
- **Required approval gates:** GATE-GITHUB-WRITE for any remote write operation; GATE-DEPLOY for production deployment.
- **Pre-condition:** verify `git` availability and `gh` auth status before any remote action.

### Release readiness
- **Signals:** "release readiness", "is it ready to ship", "deployment checklist", "go/no-go".
- **Workflow:** `release-readiness` (commands/release-readiness.md)
- **Required approval gates:** GATE-DEPLOY for actual deployment (not implied by a readiness assessment).

---

## Ambiguity handling

If the user's intent could map to two meaningfully different workflows (for example, "fix the bug" without a prior diagnosis vs. "fix the authorized finding BRK-001"), ask one focused question to resolve the ambiguity. Do not ask the user to name the internal agent, skill, or command.

## Mixed-intent requests

When a request combines multiple intents (for example, "review and then fix any critical bugs"), use the primary workflow for the first action (review-only), report findings, and wait for user authorization before routing to a repair workflow. Do not attempt both workflows in a single uninterrupted pass unless the user explicitly authorized the combined action in advance.

## Unknown or missing capability

If a required skill or capability is missing from the registry:

1. Identify the specific gap.
2. State what generic fallback, if any, is safe and feasible.
3. Proceed generically only when the risk is low and the result is clearly useful.
4. Report the gap in the handoff so the user can decide whether to add the capability.

Never invent skill content or pretend a missing capability was loaded.
