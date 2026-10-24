---
name: spring-boot-engineering
description: Spring Boot patterns for configuration, dependency injection, REST controllers, validation, transactions, persistence, security, messaging, testing and observability.
---

# Spring Boot engineering skill

Inspect Spring Boot version, Java version, dependency management, module layout, profiles, existing conventions and tests first. Use constructor injection, validated configuration, clear controller/service/repository boundaries when they fit current architecture, and DTOs rather than exposing persistence entities unintentionally. Apply Bean Validation at boundaries and explicit authorization at service/API boundaries.

Use transaction boundaries intentionally; understand proxy semantics and avoid self-invocation surprises. Avoid N+1 queries, careless lazy loading, open-session assumptions and returning entities directly. Manage exception mapping in a consistent error model. External effects (messaging, HTTP, email) need retries/idempotency and failure visibility where appropriate. Test slices (MVC/JPA) and full integration context selectively. For integration tests, use realistic dependencies (containers/test services where available) when in-memory substitutes hide important behavior. Keep secrets out of properties committed to Git; use env/secret managers. Respect the project's Boot version and do not upgrade versions without approval.
