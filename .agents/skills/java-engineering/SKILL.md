---
name: java-engineering
description: "Language-specific engineering guidance for Java: null handling, type design, exceptions, resources, concurrency, collections, immutability and Java tests. Load for Java tasks."
---

# Java engineering skill

- Prefer clear types and explicit contracts; avoid raw types and unchecked casts unless unavoidable and documented.
- Handle nullable values deliberately. Use validation, clear preconditions, or `Optional` at suitable API boundaries; do not use `Optional` as a field/parameter default everywhere or as a substitute for null policy.
- Catch exceptions only when handling, translating, or adding useful context. Do not swallow exceptions or use exceptions for normal branching. Preserve causes and avoid leaking sensitive details.
- Close resources reliably using try-with-resources. Consider stream lifecycle and ownership.
- Treat mutable state and shared collections carefully. Assess concurrency, visibility, thread safety and synchronization; avoid shared mutable state unless justified.
- Favor small cohesive methods, clear names, composition where useful, and existing project style. Do not add frameworks/abstractions without need.
- Test null/empty/invalid inputs, exception behavior, boundaries and invariants. Use unit tests for logic and integration tests for actual boundaries such as persistence, messaging and HTTP.
- Follow the selected Java version and existing build (Maven/Gradle); do not assume APIs newer than configured language level.
