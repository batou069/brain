---
tags:
  - version_control
  - git
  - command
  - remote
  - workflow
  - core
aliases: []
related:
  - "[[Git]]"
  - "[[git_commit]]"
  - "[[git_remote]]"
  - "[[Remote_repository]]"
  - "[[Branching]]"
  - "[[Repository]]"
  - "[[git_fetch]]"
  - "[[git_pull]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git push `

## Purpose

The `git push` command uploads local [[Repository|repository]] content (commits and associated objects) to a [[Remote_repository]]. It updates the remote references (like branches) to match the local ones, effectively sharing your committed changes with others or backing them up on a remote server.

## Action

1.  Identifies the local commits that are reachable from the specified local branch but are not present on the corresponding remote branch.
2.  Transfers the necessary Git objects (commits, trees, blobs) associated with those new commits to the remote repository.
3.  Updates the specified branch pointer(s) on the remote repository to point to the same commit as the local branch.

## Syntax

```bash
# Push current branch to its configured upstream remote branch
git push

# Explicitly specify remote and local branch (and optionally remote branch name)
git push <remote_name> <local_branch_name>[:<remote_branch_name>]
# Example: Push local 'main' to remote 'origin's 'main' branch
# git push origin main
# Example: Push local 'feature' to remote 'origin's 'new-feature' branch
# git push origin feature:new-feature

# Set the upstream tracking branch for the current local branch while pushing
git push -u <remote_name> <local_branch_name>
# Example: git push -u origin main (first time pushing a new local branch)

# Push all local branches that have matching remote branches
git push --all [<remote_name>]

# Push all tags
git push --tags [<remote_name>]

# Force push (DANGEROUS - overwrites remote history)
git push --force [<remote_name>] [<branch_name>]
git push -f [<remote_name>] [<branch_name>]

# Force push with lease (Safer force push - checks if remote hasn't changed)
git push --force-with-lease [<remote_name>] [<branch_name>]

# Delete a remote branch
git push <remote_name> --delete <branch_name>
# Or (older syntax): git push <remote_name> :<branch_name>```

## Common Options

| Option              | Description                                                                                             |
| :------------------ | :------------------------------------------------------------------------------------------------------ |
| `<remote>`          | The name of the remote repository to push to (defaults to `origin` or configured upstream).             |
| `<branch>`          | The local branch to push. Can specify `local:remote` mapping.                                           |
| `-u`, `--set-upstream`| For every branch pushed, add upstream (tracking) reference. Simplifies future `git pull`/`push`.        |
| `--all`             | Push all branches (that have a configured remote).                                                      |
| `--tags`            | Push all local tags in addition to branches. Tags are not pushed by default.                            |
| `-f`, `--force`     | **DANGEROUS:** Force the update, even if it results in a non-fast-forward update (overwrites remote history). Use with extreme caution, especially on shared branches. |
| `--force-with-lease`| Safer force push. Fails if the remote branch has been updated since your last fetch.                    |
| `--delete`          | Delete the specified branch(es) on the remote.                                                          |
| `-v`, `--verbose`   | Provide more detailed output.                                                                           |
| `--dry-run`         | Show what would be pushed without actually pushing.                                                     |

## Examples

**Example 1: Push committed changes on `main` to `origin`**
```bash
# Assuming 'main' tracks 'origin/main'
git push
# Or explicitly:
# git push origin main
```

**Example 2: Push a new local branch `feature-x` to `origin` and set tracking**
```bash
git push -u origin feature-x
```
*Uploads `feature-x`, creates `feature-x` on `origin`, and sets the local `feature-x` to track `origin/feature-x`.*

**Example 3: Push tags**
```bash
git push --tags origin
```

**Example 4: Delete a remote branch**
```bash
git push origin --delete old-feature
```

## Related Commands/Concepts
- [[Git]]
- [[git_commit]] (Creates the commits that are pushed)
- [[git_remote]] (Manages remote repositories)
- [[Remote_repository]] (The destination for the push)
- [[Branching]] (Pushing updates remote branches)
- [[Repository]] (Local vs. Remote)
- [[git_fetch]], [[git_pull]] (Commands to get changes *from* the remote)
- Fast-Forward vs Non-Fast-Forward Push

## Notes
>[!warning] Non-Fast-Forward Rejection
> By default, Git will reject a push if it is not a "fast-forward" push. This happens if the remote branch has commits that your local branch does not have (meaning the histories have diverged). This prevents you from accidentally overwriting commits made by others. To resolve this, you typically need to [[git_pull]] (or [[git_fetch]] and then [[git_merge]]/[[git_rebase]]) first to integrate the remote changes before pushing again. `--force` overrides this safety check.

---
**Source:** Worksheet WS2