---
tags: [version_control, git, command, branch, workflow]
aliases: []
related: []
worksheet: [WS]
date_created: 2025-04-11
---
# ` git merge `

## Purpose

The `git merge` command integrates changes from a named [[Commit_object|commit]] (usually the tip of another [[Branching|branch]]) into the current branch ([[Git_HEAD|HEAD]]). It joins two or more development histories together.

## Syntax

```bash
git merge <branch_to_merge> [<options>]
```

## Common Options

| Option       | Description                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \<branch>    | The name of the branch whose changes should be merged into the current branch.                                                                                                                       |
| --commit     | Force creation of a merge commit even if a fast-forward merge is possible.                                                                                                                           |
| --no-commit  | Perform the merge but do not automatically create a merge commit. Allows inspection before committing.                                                                                               |
| --ff         | (Default) Allow fast-forward merges when possible.                                                                                                                                                   |
| --no-ff      | Create a merge commit in all cases, even when a fast-forward is possible. Preserves history of feature branch.                                                                                       |
| --ff-only    | Only perform the merge if it can be resolved as a fast-forward. Abort otherwise.                                                                                                                     |
| --squash     | Combine all changes from the merged branch into a single set of changes in the [[Working_directory]] and [[Staging_area]], without creating a merge commit. Requires a manual git commit afterwards. |
| --abort      | Abort the current merge process (e.g., after encountering conflicts you don't want to resolve).                                                                                                      |
| -m \<msg>    | Specify a custom commit message for the merge commit.                                                                                                                                                |
| -X \<option> | Pass merge strategy specific options (e.g., -Xours, -Xtheirs for conflict resolution).                                                                                                               |

## Examples

**Example 1: Merge a feature branch into main**

```bash
# Switch to the target branch
git checkout main

# Merge the feature branch
git merge feature/login
```
Integrates changes from feature/login into main. May result in a fast-forward or a merge commit.

**Example 2: Merge main into a feature branch (to update it)**

```bash
# Switch to your feature branch
git checkout feature/login

# Merge changes from main
git merge main
```
Brings recent updates from main into your feature branch.

**Example 3: Merge with guaranteed merge commit (no fast-forward)**

```bash
git checkout main
git merge --no-ff feature/login
```
Ensures a merge commit is created, preserving the record that feature/login existed as a separate line of work.

**Example 4: Abort a merge with conflicts**

```bash
git merge develop
# ... Auto-merging file.txt
# ... CONFLICT (content): Merge conflict in file.txt
# ... Automatic merge failed; fix conflicts and then commit the result.

# Decide not to resolve now
git merge --abort
```
Resets the state back to before the merge attempt.

## Related Commands/Concepts

- [[Merging]] (The core concept)
- [[Branching]] (Merging integrates branches)
- [[Merge_conflict]] (Potential issue during merge)
- [[git_branch]], [[git_checkout]] (Commands to manage and switch branches before merging)
- [[git_rebase]] (Alternative method for integrating changes)
- [[git_log]] (View merge history)
- [[Git_HEAD|HEAD]] (The target branch for the merge)
---

**Source:** Worksheet WS15
