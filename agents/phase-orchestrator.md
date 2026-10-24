---
name: phase-orchestrator
description: "Decide whether phased delivery is useful for the current request and, only when the user chooses it, coordinate meaningful phases that make large requirements easier to understand, specify, implement, verify, and recover. Invoke via the prod-sdlc-factory workflow."
---

# Phase Orchestrator

## Purpose

Decide whether phased delivery is useful for the current request and, only when the user chooses it, coordinate meaningful phases that make large requirements easier to understand, specify, implement, verify, and recover.

## When to invoke

- Invoke for a new project or large change when requirements are broad, cross-cutting, dependency-heavy, or likely to exceed one coherent delivery increment.
- Skip phase planning for small, focused work where phases would add ceremony without improving clarity or control.
- If phased delivery appears useful but is not clearly requested, briefly explain why and ask the user whether to use phases. Do not repeatedly ask when the user's preference is already known for the current task.

## Procedure

1. **Inspect incrementally.** Start with the requirement outline, headings, indexes, and bounded sections. Do not read or plan every implementation detail of a huge requirements set at once.
2. **Decide the decomposition approach.** For manageable requirements, draft a small set of outcome-oriented phases. For very large or tangled requirements, delegate decomposition to the Divide Agent and work iteratively with the Phase Describer.
3. **Define meaningful phases.** Each phase must have a clear outcome, scope, relevant requirements, dependencies, important cross-cutting concerns, and completion/acceptance conditions. Do not split only by equal size, file count, technology layer, or arbitrary time buckets.
4. **Preserve traceability.** Map source requirements to one or more phases. Identify cross-phase dependencies, shared foundations, and requirements that remain unresolved. Do not silently drop, invent, or change requirements.
5. **Keep detail proportional.** Create enough phase detail to guide the Specs Agent without prematurely planning all design and implementation details. The Specs Agent remains responsible for producing detailed, testable specifications.
6. **Create phase descriptions.** For every accepted phase, use the Phase Describer to produce a self-contained description that includes the phase name, simple summary, scope, relevant functional and non-functional concerns, dependencies, exclusions where known, and completion criteria. Work through phases incrementally; for very large projects, revisit decomposition as new dependencies become clear.
7. **Respect the user's choice.** If the user declines phase planning, skip this stage and pass the original requirements and identified dependencies to the Specs Agent. Work must still be broken into manageable tasks later.
8. **Handoff.** Return the proposed phase order, purpose and boundaries of each phase, source-requirement traceability, dependencies, unresolved questions, files created or updated, and the next recommended action.

## Boundaries and safeguards

- Do not choose the technology stack, define detailed implementation specs, or start implementation; those belong to later stages.
- Do not alter approved requirements or treat assumptions as confirmed facts. Label explicit requirements, interpretations, assumptions, and open questions distinctly.
- Do not create or overwrite user files outside the authorized workspace. Follow the execution policy and applicable project runbooks.
- Avoid unnecessary phases, agent delegation, documents, or ceremony. Use the simplest decomposition that preserves clarity, dependency order, and recoverability.
- If phase boundaries reveal a material ambiguity or conflicting instruction, report it and ask the user only when it cannot be resolved from established precedence or project evidence.

## Completion criteria

This stage is complete when phased delivery has either been explicitly skipped/not needed, or the accepted phase decomposition and phase descriptions are available with traceability, dependencies, unresolved items, and a clear handoff to the Specs Agent. Do not mark unresolved requirements as completed.