---
name: security-engineering
description: "Threat-aware secure implementation/review: input validation, authn/authz, secret handling, injection, data protection, dependency risk and safe operational behavior. Use when security or sensitive data is relevant."
---

# Security engineering skill

Identify trust boundaries, assets, actors, data sensitivity, authorization checks, inputs, outputs, and failure modes. Apply least privilege, secure defaults, input validation, output encoding, safe error messages, secret management, dependency hygiene, and auditability as relevant. Check authentication vs authorization, object-level access, mass assignment, injection, SSRF/path traversal, unsafe deserialization, insecure CORS/cookies, sensitive logging, race conditions and data exposure where applicable.

Do not invent compliance requirements. Ground review in approved specs, threat model, project standards and authoritative documentation. Report severity and evidence; distinguish exploitable confirmed issue from hardening suggestion. Do not probe live external systems destructively. Never print or commit secrets. Follow factory destructive-operation and remote-write permissions.
