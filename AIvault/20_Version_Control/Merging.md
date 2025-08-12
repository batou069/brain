---
tags: version_control, git, concept, workflow
aliases: Merge
related:
  - "[[Git]]"
  - "[[Branching]]"
  - "[[Commit_object]]"
  - "[[Merge_conflict]]"
  - "[[git_merge]]"
  - "[[git_rebase]]"
  - "[[git_log]]]]"
worksheet: WS15
date_created: 2025-04-21
---
# Merging (Git)

## Definition

In [[Git]], **Merging** is the process of integrating changes from different [[Branching|branches]] back together. The `git merge` command takes the independent lines of development created by `git branch` and integrates them into a single branch.

## Key Aspects / Characteristics

- **Integration:** Combines changes from a source branch into a target branch (the currently checked-out branch).
- **Merge Commits:** Often results in a new "merge commit" ([[Commit_object]]) that has two or more parent commits (one from the target branch, one from the source branch). This merge commit represents the combined state.
- **Fast-Forward Merge:** If the target branch hasn't diverged since the source branch was created (i.e., the source branch's history is directly ahead of the target branch's history), Git performs a "fast-forward" merge by simply moving the target branch pointer forward to match the source branch pointer. No merge commit is created.
- **Conflict Resolution:** If both branches modified the same part of the same file in different ways, Git cannot automatically combine the changes, resulting in a [[Merge_conflict]] that the user must resolve manually.
- **History:** Standard merges preserve the distinct history of the merged branch, making it clear where features came from (visible in `git log --graph`).

## Examples / Use Cases

- Integrating a completed feature branch back into the `main` branch:
    ```bash
    git checkout main
    git merge feature/new-login
    ```
- Merging updates from the `main` branch into your feature branch to keep it up-to-date:
    ```bash
    git checkout feature/new-login
    git merge main
    ```

## Related Concepts
- [[Git]] (The VCS)
- [[Branching]] (Merging combines branches)
- [[Commit_object]] (Merges often create special merge commits)
- [[Merge_conflict]] (Potential issue during merging)
- [[git_merge]] (The command to perform a merge)
- [[git_rebase]] (An alternative way to integrate changes, rewrites history)
- [[git_log]] (Used to view merge history)

## Diagrams (Optional)
*(See diagram in [[Branching]])*

---
**Source:** Worksheet WS15