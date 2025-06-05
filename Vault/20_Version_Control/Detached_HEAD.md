---
tags:
  - version_control
  - git
  - concept
  - state
  - HEAD
aliases:
  - Detached HEAD State
related:
  - "[[Git]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[Commit_object]]"
  - "[[Branching]]"
  - "[[git_checkout]]"
  - "[[git_log]]"
  - "[[git_switch]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# Detached HEAD

## Definition

In [[Git]], **Detached HEAD** is a state where the special [[Git_HEAD|HEAD]] pointer (which normally points to the tip of the current local branch) is pointing **directly to a specific [[Commit_object|commit]]** instead of pointing to a named [[Branching|branch]]. This typically happens when you explicitly check out a commit hash, a tag, or a remote branch directly.

## How it Occurs

You enter a detached HEAD state primarily by using [[git_checkout]] (or the newer [[git_switch]] with `--detach`) with something that isn't a local branch name:

```bash
# Checkout a specific commit hash
git checkout a1b2c3d4

# Checkout a tag
git checkout v1.0.1

# Checkout a remote branch directly (creates detached HEAD at origin/develop's commit)
git checkout origin/develop
```

When this happens, Git usually issues a warning message like:
```
Note: switching to 'a1b2c3d4'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false
HEAD is now at a1b2c3d4 Commit message...
```

## Implications

- **Looking Around:** Detached HEAD is useful for inspecting the state of the repository at a specific past commit or tag without affecting any branches.
- **Experimental Commits:** You *can* make new commits while in a detached HEAD state. These new commits build upon the commit HEAD points to, but they **do not belong to any named branch**.
- **Losing Commits:** If you make commits in a detached HEAD state and then switch back to an existing branch (e.g., `git checkout main`) **without** creating a new branch for your detached commits, those commits become "orphaned." They still exist in the repository for a while but are not reachable from any branch or tag, making them hard to find and eventually subject to garbage collection (deletion).
- **Creating a Branch:** If you make valuable commits in a detached HEAD state, you should create a new branch *before* switching away to preserve them:
  ```bash
  # While in detached HEAD after making commits:
  git checkout -b new-feature-branch # Creates new branch pointing to current HEAD
  # or (newer syntax)
  # git switch -c new-feature-branch
  ```

## Related Concepts
- [[Git]], [[Git_HEAD|HEAD]]
- [[Commit_object]] (HEAD points directly to one)
- [[Branching]] (Detached HEAD is *not* on a branch)
- [[git_checkout]], [[git_switch]] (Commands that can cause detached HEAD)
- [[git_log]] (Can view history from detached HEAD)
- Garbage Collection (Orphaned commits can be deleted)

---
**Source:** Worksheet WS2 (Implied)