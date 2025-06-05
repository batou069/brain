---
tags: [version_control, git, command, history, undo]
aliases: []
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[git_commit]]"
  - "[[git_reset]]"
  - "[[git_log]]"
worksheet: [WS15]
date_created: 2025-04-21
---
# ` git revert `

## Purpose

The `git revert` command is used to undo the changes introduced by one or more existing [[Commit_object|commits]] by creating a *new* commit that applies the inverse changes. It does not delete or alter the original commit(s) in the project history; instead, it adds a new commit that effectively cancels out the specified commit(s).

## Syntax

```bash
git revert <commit_to_revert>... [<options>]
```

## Common Options

| Option                                     | Description                                                                                                                                                           |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \<commit>                                  | The commit(s) to revert. Can be a hash, branch name, tag, [[Git_HEAD                                                                                                  |
| -e, --edit                                 | (Default) Open the commit message editor before creating the revert commit.                                                                                           |
| --no-edit                                  | Create the revert commit without opening the editor. Uses a default message.                                                                                          |
| -n, --no-commit                            | Apply the inverse changes to the [[Working_directory]] and [[Staging_area]] but do not create the revert commit automatically. Allows modifying or combining reverts. |
| -m parent-number, --mainline parent-number | Required when reverting a merge commit. Specifies which parent's line of history should be considered the "mainline" to revert against. Usually 1.                    |

## Examples

**Example 1: Revert the most recent commit**

```bash
git revert HEAD
```

Creates a new commit that undoes the changes introduced by the commit [[Git_HEAD|HEAD]] points to. Opens an editor for the new commit message.

**Example 2: Revert an older commit**

```bash
# Find the hash of the commit to revert
git log --oneline
# ...
# a1b2c3d Add buggy feature X
# ...

# Revert that specific commit
git revert a1b2c3d
```

Creates a new commit that undoes the changes from commit a1b2c3d.

**Example 3: Revert without creating a commit immediately**

```bash
git revert -n HEAD~2 
# Inspect changes, potentially make further modifications 
# ... 
git commit -m "Revert changes from HEAD~2 and add clarification"
```

Applies the inverse changes but lets you modify them or combine multiple reverts before committing.

## Related Commands/Concepts

- [[Commit_object]] (Revert targets existing commits and creates a new one)
- [[git_reset]] (Alternative way to undo changes, but rewrites history, unlike revert)
- [[git_commit]] (Used to finalize the revert commit)
- [[git_log]] (Used to find commits to revert and view the revert commit afterwards)

## Notes

> [!note] Revert vs. Reset
> 
> - **git revert:** Creates a new commit that undoes previous changes. It's safe for shared/public history because it doesn't alter existing commits. It adds to the history.
>     
> - **[[git_reset]]**: Moves the current branch pointer back to an earlier commit, potentially discarding commits or leaving changes in the working directory/staging area. It rewrites history and should generally **not** be used on branches that have already been pushed and shared with others, as it can cause major problems for collaborators.
>     

> [!warning] Reverting Merge Commits  
> Reverting a merge commit can be complex. You need to specify which parent branch's changes you want to keep using the -m option. Reverting a merge undoes the data changes brought in by the merge, but it doesn't undo the fact that the histories were joined.