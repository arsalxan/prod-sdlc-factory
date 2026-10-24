---
description: "Resume checkpoint. Trigger when user asks to continue existing factory work or a previous session is detected."
---

# Command workflow: Resume checkpoint

**Use when:** Trigger when user asks to continue existing factory work or a previous session is detected.

1. Read checkpoint and verify schema, repo identity, branch/worktree, approved artifact versions, docs, code, and relevant tests.
2. If verified, resume the recorded next action automatically.
3. If mismatch, investigate and preserve changes; ask only for genuine blocker/conflict/approval.
4. Update checkpoint after meaningful work.
