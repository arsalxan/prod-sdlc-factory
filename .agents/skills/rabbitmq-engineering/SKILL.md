---
name: rabbitmq-engineering
description: "Message-driven system practices: delivery semantics, acknowledgments, retries, dead letters, idempotency, ordering, backpressure and integration tests."
---

# RabbitMQ engineering skill

Inspect exchange/queue/binding topology, durability, routing keys, consumer concurrency, acknowledgement mode, retry/dead-letter policy, message schema and monitoring. Assume delivery can be repeated unless a specific exactly-once guarantee is proved; design idempotent handlers and deduplication where business effects require it. Do not ack before durable processing completes. Avoid infinite requeue loops; classify transient vs permanent errors and set bounded retry/DLX behavior. Consider poison messages, ordering, backpressure, consumer restarts, schema compatibility and observability. Never delete queues or purge messages without explicit authorization. Integration-test real broker behavior where it matters; mocks alone do not validate topology/ack/retry semantics.
