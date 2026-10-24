---
name: python-engineering
description: "Language-specific Python practices: types, exceptions, mutable defaults, resource management, packaging, concurrency and tests. Load for Python tasks."
---

# Python engineering skill

- Follow the configured Python version and package manager. Avoid using APIs not supported by the declared version.
- Use type hints for public APIs and non-trivial code; respect existing typing strictness.
- Avoid mutable default arguments; use `None` or a suitable factory where needed.
- Catch narrow, expected exception types. Do not use broad `except Exception` to hide failures. Preserve causes when translating errors.
- Manage files, sockets and other resources with context managers. Consider cleanup on failure.
- Be deliberate about mutation, iteration, generators, async behavior and shared state. Do not block an async event loop with blocking I/O unintentionally.
- Avoid import-time side effects and secret/config hardcoding. Keep modules cohesive.
- Test boundaries, missing/invalid values, exceptions and side effects; use integration tests at real system boundaries and isolated test data.
