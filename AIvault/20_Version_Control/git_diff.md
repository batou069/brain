---
tags:
  - version_control
  - git
  - command
  - comparison
  - state
aliases: []
related:
  - "[[Git]]"
  - "[[Working_directory]]"
  - "[[Staging_area]]"
  - "[[Commit_object]]"
  - "[[git_status]]"
  - "[[git_add]]"
  - "[[git_commit]]"
  - "[[git_log]]"
  - "[[Branching]]"
worksheet:
  - WS2
  - WS15
date_created: 2025-04-20
---
# ` git diff `

## Purpose

The `git diff` command is used to show changes between different states tracked by Git. It can compare the [[Working_directory]], the [[Staging_area]] (index), and [[Commit_object|commits]] (including branches and tags). It essentially shows the differences (additions, deletions, modifications) between two sets of content.

## Common Usage Forms

1.  **Changes in Working Directory vs. Staging Area:**
    ```bash
    git diff
    ```
    - Shows changes made in the [[Working_directory]] that have **not** yet been staged (i.e., not yet run through `git add`). Displays differences between working files and the index.

2.  **Changes in Staging Area vs. Last Commit:**
    ```bash
    git diff --staged
    # or
    git diff --cached
    ```
    - Shows changes that **have been staged** (added to the index via `git add`) but **not yet committed**. Displays differences between the index and the `HEAD` commit. This shows exactly what *would* be included if you ran `git commit` right now.

3.  **Changes in Working Directory vs. Last Commit:**
    ```bash
    git diff HEAD
    ```
    - Shows **all** changes made in the [[Working_directory]] since the last commit (`HEAD`), regardless of whether they have been staged or not. Compares working files directly against the `HEAD` commit.

4.  **Changes Between Two Commits:**
    ```bash
    git diff <commit1> <commit2>
    # Example: git diff HEAD~1 HEAD  (Changes introduced by the last commit)
    # Example: git diff my-branch main (Changes on my-branch not yet in main)
    ```
    - Shows the differences introduced between `<commit1>` and `<commit2>`. Order matters.

5.  **Changes in a Specific File:**
    ```bash
    # Working directory vs. Staging Area for <file>
    git diff -- <file_path>

    # Staging Area vs. Last Commit for <file>
    git diff --staged -- <file_path>

    # Between two commits for <file>
    git diff <commit1> <commit2> -- <file_path>
    ```
    - Limits the output to show changes only within the specified file(s). The `--` is used to separate commit/branch names from file paths unambiguously.

## Output Format

- The output is typically in a **diff format** (similar to the output of the Unix `diff` command).
- Lines starting with `-` indicate lines removed from the first version.
- Lines starting with `+` indicate lines added in the second version.
- Context lines (unchanged) may also be shown.
- Header lines provide metadata about the files being compared.

## Related Commands/Concepts
- [[Git]]
- [[Working_directory]], [[Staging_area]], [[Commit_object]], [[Git_HEAD|HEAD]] (States being compared)
- [[git_status]] (Provides a summary of changes, `git diff` shows the details)
- [[git_add]] (Stages changes, affecting `git diff` vs `git diff --staged`)
- [[git_commit]] (Creates commits that can be compared)
- [[git_log]] (Used to find commit hashes for comparison)
- [[Branching]] (Compare branches using `git diff branch1 branch2`)

---
**Source:** Worksheet WS2, WS15