---
tags:
  - version_control
  - git
  - command
  - remote
  - workflow
aliases: []
related:
  - "[[Git]]"
  - "[[git_fetch]]"
  - "[[git_merge]]"
  - "[[git_rebase]]"
  - "[[Remote_repository]]"
  - "[[Branching]]"
  - "[[Repository]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git pull `

## Purpose

The `git pull` command is used to fetch changes from a [[Remote_repository]] and **integrate** them into the current local branch. In its default mode, `git pull` is essentially a shortcut for running `git fetch` followed by `git merge FETCH_HEAD`.

## Action (Default: Merge)

1.  **[[git_fetch|Fetches]] Changes:** Runs `git fetch` for the specified remote (or the default upstream remote, usually `origin`) and the current branch. This downloads new commits and updates the corresponding remote-tracking branch (e.g., `origin/main`) in your local repository.
2.  **[[git_merge|Merges]] Changes:** Runs `git merge` to merge the fetched remote-tracking branch (e.g., `origin/main`) into your current local branch (e.g., `main`). This integrates the downloaded changes into your local work.

## Syntax

```bash
# Fetch from and integrate with the configured upstream for the current branch
git pull

# Explicitly specify remote and branch
git pull <remote_name> <remote_branch_name>
# Example: git pull origin main

# Fetch and rebase instead of merge
git pull --rebase [<remote_name>] [<remote_branch_name>]
```

## Common Options

| Option        | Description                                                                                             |
| :------------ | :------------------------------------------------------------------------------------------------------ |
| `<remote>`    | The name of the remote repository to pull from (defaults to `origin` or configured upstream).           |
| `<branch>`    | The name of the remote branch to pull (defaults to the tracked upstream branch for the current local branch). |
| `--rebase`    | Instead of using `git merge` to integrate, use `git rebase`. This reapplies your local commits on top of the fetched remote commits, resulting in a linear history. Can cause issues if pulling into a branch already shared with others. |
| `--ff-only`   | Only update the local branch if the merge can be performed as a fast-forward (i.e., no divergent local commits exist). Prevents merge commits. |
| `-v`, `--verbose`| Show more detailed output about what is being fetched and merged/rebased.                             |

## Examples

**Example 1: Update local `main` branch from `origin`**
```bash
# Assuming current branch is 'main' and it tracks 'origin/main'
git pull
# Equivalent to:
# git fetch origin
# git merge origin/main
```
*Downloads changes from `origin/main` and merges them into the local `main` branch.*

**Example 2: Pull changes from `develop` branch on `origin`**
```bash
git pull origin develop
```
*Fetches `origin/develop` and merges it into the *current* local branch.*

**Example 3: Pull using rebase strategy**
```bash
# Assuming current branch is 'feature-x' tracking 'origin/feature-x'
git pull --rebase
# Equivalent to:
# git fetch origin
# git rebase origin/feature-x
```
*Fetches changes from `origin/feature-x` and reapplies any local commits (that are not on origin) on top of the fetched commits.*

## Related Commands/Concepts
- [[Git]]
- [[git_fetch]] (The first part of `pull`)
- [[git_merge]] (The default integration strategy for `pull`)
- [[git_rebase]] (Alternative integration strategy using `--rebase`)
- [[Remote_repository]], [[Repository]]
- [[Branching]] (Pulling updates a local branch based on a remote one)

## Notes
>[!warning] Pulling into a Dirty Working Directory
> If you have uncommitted local changes, `git pull` (using the default merge strategy) might fail if the incoming changes conflict with your local changes. It's often best to commit or [[git_stash|stash]] your local changes before pulling. `git pull --rebase` requires a clean working directory.

>[!note] Merge vs. Rebase
> Using `git pull` (merge) creates merge commits when integrating remote changes if local commits exist, preserving the exact history but potentially making it look more complex (`git log --graph`). Using `git pull --rebase` creates a linear history by replaying local commits on top of remote changes, which can look cleaner but technically rewrites the history of your local commits (changing their hashes). Rebasing pulled changes on *shared* branches should generally be avoided.

---
**Source:** Worksheet WS2