---
tags: [version_control, git, command, branch]
aliases: []
related:
  - "[[Git]]"
  - "[[Branching]]"
  - "[[Commit_object]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[git_checkout]]"
  - "[[git_switch]]"
  - "[[git_merge]]"
  - "[[git_log]]"
worksheet: [WS15]
date_created: 2025-04-11
---
# ` git branch `

## Purpose

The `git branch` command is used to list, create, or delete [[Branching|branches]]. It operates on the branch pointers within the Git [[Repository]].

## Syntax

```bash
# List local branches
git branch

# List remote-tracking branches
git branch -r

# List all branches (local and remote-tracking)
git branch -a

# Create a new branch pointing to the current HEAD
git branch <branch_name>

# Create a new branch pointing to a specific commit/branch
git branch <branch_name> <start_point>

# Delete a merged branch
git branch -d <branch_name>

# Force delete a branch (potentially unmerged)
git branch -D <branch_name>

# Rename a branch
git branch -m <old_name> <new_name>
````## Syntax

```bash
Untitled [OPTIONS] [ARGUMENTS]
```

## Common Options

| Option       | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| -r           | List remote-tracking branches (e.g., origin/main).                        |
| -a           | List all branches (local and remote-tracking).                            |
| -v, -vv      | Show more information, like the last commit and tracking status.          |
| -d, --delete | Delete a branch. Fails if the branch has unmerged changes.                |
| -D           | Force delete a branch, even if it has unmerged changes. Use with caution. |
| -m, --move   | Move/rename a branch.                                                     |
| -M           | Force move/rename a branch, even if the new name exists.                  |
| --merged     | List branches whose tips are reachable from the current [[Git_HEAD        |
| --no-merged  | List branches whose tips are not reachable from the current [[Git_HEAD    |

## Examples

**Example 1: List local branches**
```bash
git branch
```
Shows a list of local branches, with an asterisk () indicating the currently checked-out branch.*

**Example 2: Create a new branch**

```bash
git branch feature/new-ui`
```
Creates a new branch named feature/new-ui pointing to the same commit as the current [[Git_HEAD|HEAD]]. This command does not switch to the new branch.

**Example 3: Delete a feature branch after merging**

```bash
# Assuming 'feature/login' has been merged into main
git checkout main
git branch -d feature/login
```

# Untitled MOC (Map of Content)

This note serves as a central hub for all topics related to **Untitled**.

Deletes the local branch feature/login.

**Example 4: List branches not yet merged into main**

```bash
git checkout main
git branch --no-merged
```
*Shows branches containing work not yet integrated into `main`.*

## Related Commands/Concepts
- [[Branching]] (The core concept managed by this command)
- [[git_checkout]] / [[git_switch]] (Commands to switch *to* a branch)
- [[git_push]] (Used with `--delete` option to delete remote branches)
- [[git_merge]] (Command to integrate branches)
- [[Git_HEAD|HEAD]] (The current commit, often the starting point for new branches)

## Notes
>[!note] Creating vs. Switching
> `git branch <name>` only *creates* the branch pointer. It does *not* switch your [[Working_directory]] to that branch. To create and switch in one step, use `git checkout -b <name>` or `git switch -c <name>`.

---
**Source:** Worksheet WS15
