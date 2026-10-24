---
name: architecture-design
description: Designs maintainable system boundaries and integration flows from approved requirements without overengineering. Use for new architecture or material structural change.
---

# Architecture design skill

Start from approved requirements and selected stack. Define system context/container boundaries, responsibilities, interfaces, data ownership, key interactions, state/consistency needs, failure handling, security/trust boundaries and deployment/observability concerns at the level needed. Prefer simple designs that satisfy quality attributes. Avoid introducing services, queues, caches, frameworks or abstractions without a supported need.

Identify trade-offs, alternatives and risks. Keep WHAT from approved specs distinct from HOW in architecture. Material architecture changes that affect approved decisions require review/approval. Reuse suitable current diagrams; do not generate a diagram unless the agreed conditions and user approval are met. Capture decisions in ADR-style records when durable.
