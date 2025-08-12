---
tags: 
  - version_control
  - git
  - concept
  - pointer
aliases: HEAD
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Commit_object]]"
  - "[[Branching]]"
  - "[[git_checkout]]"
  - "[[git_log]]"
  - "[[git_reset]]"
  - "[[Detached_HEAD]]"
worksheet: 
  - WS2
  - WS15
date_created: 2025-04-21
---
# Git HEAD

## Definition

In [[Git]], **HEAD** is a special pointer within the [[Repository]] that indicates your current position in the project's history. It usually points to the tip of the currently checked-out [[Branching|branch]], but it can also point directly to a specific [[Commit_object|commit]] (a state known as [[Detached_HEAD|detached HEAD]]).

## Key Aspects / Characteristics

- **Current Location:** Represents what snapshot of the project is currently reflected in your [[Working_directory]].
- **Symbolic Reference (Usually):** Most of the time, HEAD is a *symbolic reference* to a branch name (e.g., `main`, `feature/x`). This means HEAD points *to* the branch pointer, and the branch pointer points *to* the latest commit on that branch. When you make a new commit, the branch pointer moves forward, and HEAD automatically moves with it because it points to the branch.
- **Direct Reference (Detached HEAD):** If you check out a specific commit hash or a tag directly ([[git_checkout]] `a1b2c3d` or `git checkout v1.0`), HEAD will point *directly* to that commit's [[SHA-1]] hash. This is called a [[Detached_HEAD]] state. Committing in this state creates a new commit that isn't on any named branch.
- **Reference Point:** Many Git commands use HEAD as a default reference point (e.g., [[git_log]] starts from HEAD, [[git_reset]] modifies HEAD or the branch it points to).

## Examples / Use Cases

- `git checkout main`: HEAD now points to the `main` branch pointer.
- `git checkout my-feature`: HEAD now points to the `my-feature` branch pointer.
- `git checkout a1b2c3d`: HEAD now points directly to commit `a1b2c3d` ([[Detached_HEAD]]).
- `git log HEAD^`: Shows the log starting from the parent of the commit HEAD points to.
- `git reset HEAD~1`: Moves the current branch pointer (and HEAD with it) back one commit.

## Related Concepts
- [[Git]] (The VCS)
- [[Repository]] (Where HEAD resides, usually in `.git/HEAD`)
- [[Commit_object]] (What HEAD ultimately points to, directly or indirectly)
- [[Branching]] (HEAD usually points to the current branch)
- [[git_checkout]] (Command used to move HEAD)
- [[git_reset]] (Command that can move HEAD and/or the branch it points to)
- [[Detached_HEAD]] (State where HEAD points directly to a commit)

## Questions / Further Study
>[!question] What is the difference between the HEAD and the master? (WS2)
> - **[[Git_HEAD|HEAD]]** is a *dynamic pointer* indicating your current location in the repository's history. It usually points to the branch you currently have checked out.
> - **`master`** (or increasingly, `main`) is the *name of a specific branch* (a pointer to a specific commit, usually the tip of the main line of development).
> If you are currently working on the `master` branch, then HEAD will be pointing to `master`. If you [[git_checkout|checkout]] another branch, say `develop`, then HEAD will point to `develop`, while the `master` branch pointer remains unchanged (pointing to the latest commit on the master branch).

---
**Source:** Worksheet WS2, WS15