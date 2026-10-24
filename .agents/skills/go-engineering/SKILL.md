---
name: go-engineering
description: "Language-specific Go practices: errors, interfaces, context cancellation, concurrency, resource lifetimes and testing. Load for Go tasks."
---

# Go engineering skill

Follow the module's Go version and idioms. Handle errors explicitly with contextual wrapping where it helps; do not discard errors without a reason. Pass `context.Context` through operations that need cancellation/deadlines and respect cancellation. Keep interfaces small and typically consumer-owned. Make goroutine lifetimes and channel ownership clear; avoid leaks, blocked sends and data races. Close resources and response bodies appropriately. Prefer simple composition over excessive abstractions. Use table-driven tests when useful, test error paths and boundaries, and run `go test ./...` / race checks when appropriate and available. Do not assume all checks apply to every repository.
