---
name: git-workflow
description: "Safe local Git workflows: inspect repository state, diffs, branches and commit history; preserve unrelated changes. Use for any task involving Git, branching, commits, rebases or merge conflict analysis."
---

# Git workflow skill

Always begin with read-only inspection: `git rev-parse --show-toplevel`, `git status --short --branch`, `git diff --stat`, and relevant focused diffs. Don't assume a clean worktree. Preserve unrelated changes and inspect files before modifying them.

Use narrow staging by explicit paths; avoid `git add .` when the worktree contains unrelated changes. Confirm staged diff before commit. Do not reset hard, clean untracked files, force-push, rewrite shared history, delete branches, or discard changes without explicit operation-specific permission. Explain conflicts and resolve only those within assigned scope. A commit is not a remote push. A push/merge/release needs its own authorization as described in `AGENTS.md`.

Check identity/upstream/target branch before publishing. Never commit secrets or generated credentials. Prefer small cohesive commits when commits are requested or appropriate under the user's authorization.
