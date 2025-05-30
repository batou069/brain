---
tags: 
  - version_control
  - git
  - concept
  - object
aliases: 
  - Commit
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Staging_area]]"
  - "[[Working_directory]]"
  - "[[git_commit]]"
  - "[[git_log]]"
  - "[[Branching]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[SHA-1]]"
worksheet: 
  - WS2
  - WS15
date_created: 2025-04-21
---
# Commit Object

## Definition

In [[Git]], a **Commit Object** represents a specific snapshot (version) of the entire project's tracked files at a particular point in time. It is the fundamental unit of history in a Git [[Repository]]. Each commit points to the previous commit(s), forming a directed acyclic graph (DAG) of the project's history.

## Key Aspects / Characteristics

- **Snapshot, Not Diff:** A commit primarily stores a reference (via a tree object) to the complete state of all tracked files at the time of the commit, not just the changes from the previous version (though Git can efficiently calculate diffs).
- **Metadata:** Contains metadata such as:
    - A unique [[SHA-1]] hash identifying the commit.
    - A pointer (SHA-1 hash) to the *tree object* representing the root directory snapshot.
    - Pointers (SHA-1 hashes) to parent commit(s) (usually one, but more for merge commits).
    - Author name and email, and timestamp.
    - Committer name and email, and timestamp (can differ from author, e.g., during rebasing).
    - The commit message explaining the changes.
- **Immutability:** Once created, a commit object cannot be changed. Operations like `git commit --amend` or `git rebase` actually create *new* commit objects.
- **History Chain:** Commits link backward to their parent(s), forming the project history. [[Branching|Branches]] are essentially just pointers to specific commits.

## Examples / Use Cases

- Running [[git_commit]] creates a new commit object based on the current [[Staging_area]].
- Running [[git_log]] displays the history by traversing the chain of commit objects.
- Checking out a specific commit [[SHA-1]] hash places the corresponding project snapshot into the [[Working_directory]].

## Related Concepts
- [[Git]] (The VCS)
- [[Repository]] (Stores the commit objects)
- [[Staging_area]] (The state used to create a commit)
- [[git_commit]] (The command to create a commit object)
- [[git_log]] (Command to view commits)
- [[Branching]] (Branches are pointers to commits)
- [[Git_HEAD|HEAD]] (Pointer to the currently checked-out commit or branch)
- [[SHA-1]] (Hashing algorithm used for commit IDs)
- Tree Object, Blob Object (Other Git object types referenced by commits)

## Questions / Further Study
>[!question] What is a commit in Git? How is it different from saving a file? How often should you commit? (WS2)
> - **What:** A [[Commit_object|commit]] is a permanent snapshot of your entire project (all tracked files) at a specific point in time, stored in the Git [[Repository]] along with metadata (author, message, parent commit).
> - **Difference from Save:** Saving a file just updates that single file on disk in your [[Working_directory]]. A commit records the state of *all* staged files across the project into the version history, creating a historical marker you can return to.
> - **Frequency:** Commit often! Each commit should represent a small, logical, self-contained change (e.g., fix a specific bug, implement a small feature, refactor a function, update documentation). Frequent commits make history easier to understand, facilitate reverting changes, and reduce the complexity of [[Merging|merging]]. Don't wait until you've made hundreds of changes. Commit after completing any distinct piece of work.

>[!question] How do you refer to a specific commit? (WS2)
> You primarily refer to a commit using its unique [[SHA-1]] hash (e.g., `a1b2c3d4e5f6...`). You can usually use a short, unique prefix (e.g., `a1b2c3d`). You can also refer to commits using:
> - Branch names (e.g., `main`, `feature-x`), which point to the latest commit on that branch.
> - Tag names (e.g., `v1.0`), which are pointers to specific commits.
> - Relative references like [[Git_HEAD|HEAD]] (current commit), `HEAD^` (first parent of HEAD), `HEAD~2` (grandparent of HEAD).

---
**Source:** Worksheet WS2, WS15