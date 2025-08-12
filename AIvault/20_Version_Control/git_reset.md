---
tags: [version_control, git, command, history, undo, state, danger]
aliases: []
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[Staging_area]]"
  - "[[Working_directory]]"
  - "[[git_revert]]"
  - "[[git_checkout]]"
  - "[[git_log]]"
worksheet: [WS15]
date_created: 2025-04-21
---
# ` git reset `

## Purpose

The `git reset` command is used to reset the current [[Git_HEAD|HEAD]] to a specified state. It can be used to move the HEAD pointer (and the current branch pointer), update the [[Staging_area]] (index), and optionally update the [[Working_directory]]. It's a powerful command primarily used for undoing changes locally, but it **rewrites history** and should be used with caution, especially on shared branches.

## Syntax

```bash
# Move HEAD (& current branch) to <commit>, update index, update working directory
git reset --hard [<commit>]

# Move HEAD (& current branch) to <commit>, update index, keep working directory changes
git reset --mixed [<commit>]  # Default mode

# Move HEAD (& current branch) to <commit>, keep index, keep working directory changes
git reset --soft [<commit>]

# Unstage file(s) from index, keep working directory changes (HEAD is not moved)
git reset HEAD [<file>...]
git reset [<file>...] # Same as above
```

## Modes

## Examples

**Example 1: Unstage a file**

```bash
# Accidentally staged config.ini 
git add .  
# Unstage config.ini but keep changes in working directory 
git reset HEAD config.ini 
# or simply: git reset config.ini
```

**Example 2: Undo the last commit, keeping changes as unstaged**

```bash
# Default mode is --mixed
git reset HEAD~1
```

Moves the branch pointer back one commit. The changes from the undone commit are now in the [[Working_directory]] but not staged.

**Example 3: Undo the last commit, keeping changes staged**

```bash
git reset --soft HEAD~1
```

Moves the branch pointer back one commit. The changes from the undone commit remain in the [[Staging_area]], ready to be re-committed (perhaps squashed with other changes).

**Example 4: Completely discard the last commit and its changes (DANGEROUS)**

```bash
# WARNING: This permanently deletes the changes from the last commit!
git reset --hard HEAD~1
```

*Moves the branch pointer back one commit and makes the [[Staging_area]] and [[Working_directory]] match that older commit, discarding all subsequent changes.*

## Related Commands/Concepts
- [[Git_HEAD|HEAD]], [[Staging_area]], [[Working_directory]] (The three states managed by Git, affected by reset)
- [[Commit_object]] (Reset moves HEAD relative to commits)
- [[git_revert]] (Alternative for undoing commits *without* rewriting history, safer for shared branches)
- [[git_checkout]] / [[git_restore]] (Can also be used to discard working directory changes for specific files)
- [[git_log]] (Used to find the target commit for a reset)

## Notes
>[!danger] Rewriting History
> `git reset` (especially `--hard` and `--mixed`, or `--soft` followed by a different commit) changes the commit history of the current branch. **Never use `git reset` to discard commits that have already been pushed to a shared remote repository.** Doing so forces collaborators into complex recovery situations. Use [[git_revert]] instead for changes that are already public. `git reset` is generally safe for commits that exist only in your local repository.

---
**Source:** Worksheet WS15