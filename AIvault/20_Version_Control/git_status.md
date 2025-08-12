---
tags:
  - version_control
  - git
  - command
  - inspection
  - state
  - core
aliases: []
related:
  - "[[Git]]"
  - "[[Working_directory]]"
  - "[[Staging_area]]"
  - "[[Commit_object]]"
  - "[[git_add]]"
  - "[[git_commit]]"
  - "[[git_diff]]"
  - "[[git_reset]]"
  - "[[gitignore]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git status `

## Purpose

The `git status` command displays the state of the [[Working_directory]] and the [[Staging_area]] (index). It lets you see which changes have been staged, which haven't, which files aren't being tracked by Git, and information about the current branch relative to its upstream counterpart. It is one of the most frequently used Git commands.

## Information Provided

`git status` typically shows:

-   **Current Branch:** The name of the branch you are currently working on.
-   **Upstream Status:** Whether your current branch is up-to-date with, ahead of, or behind its remote tracking branch (e.g., `origin/main`). Requires an upstream branch to be configured (usually done by `git clone` or `git push -u`).
-   **Changes to be Committed:** Files that are **staged** (in the index) and ready for the next [[git_commit]]. These changes were added using [[git_add]]. (`git diff --staged` shows the content differences).
-   **Changes not Staged for Commit:** Files that have been **modified** in the [[Working_directory]] but have **not** been staged yet. (`git diff` shows the content differences). Also lists tracked files that have been deleted in the working directory but not yet staged for removal (`git rm`).
-   **Untracked Files:** Files that are present in the [[Working_directory]] but have **not** been tracked by Git before (i.e., never added/committed) and are not listed in [[gitignore]]. Git doesn't know anything about their history.

## Syntax

```bash
# Show standard status output
git status

# Show status in a shorter format
git status -s
git status --short

# Show branch and tracking info even in short format
git status -sb
git status --short --branch
```

## Example Output (Standard)

```bash
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   CONTRIBUTING.md
        modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/main.c

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        config.yaml
        docs/draft.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

## Example Output (`--short`)

```bash
 M README.md
 M src/main.c
A  CONTRIBUTING.md
?? config.yaml
?? docs/draft.txt
```
*(Status codes: `M`=Modified, `A`=Added, `D`=Deleted, `R`=Renamed, `C`=Copied, `U`=Unmerged, `??`=Untracked)*
*(First column: Staging area status. Second column: Working directory status)*

## Related Commands/Concepts
- [[Git]]
- [[Working_directory]], [[Staging_area]], [[Commit_object]] (States reported on)
- [[git_add]] (Moves changes *to* the staging area)
- [[git_commit]] (Records staged changes)
- [[git_diff]] (Shows the *content* of the changes summarized by `status`)
- [[git_reset]] (Used to unstage changes)
- [[git_restore]] (Newer command often suggested by `status` for unstaging or discarding changes)
- [[gitignore]] (Affects which files appear as "Untracked")

---
**Source:** Worksheet WS2