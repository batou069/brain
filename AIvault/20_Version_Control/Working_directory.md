---
tags: 
  - version_control
  - git
  - concept
aliases: 
  - Working Tree
  - Worktree
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Staging_area]]"
  - "[[Commit_object]]"
  - "[[git_checkout]]"
  - "[[git_status]]"
  - "[[git_diff]]"
worksheet:
  - WS2
  - WS15
date_created: 2025-04-21
---
# Working Directory

## Definition

In [[Git]], the **Working Directory** (also called the working tree) is the directory on your local filesystem that contains the actual files of your project that you are currently working on. It represents a specific snapshot (usually corresponding to a [[Commit_object|commit]] or branch [[Git_HEAD|HEAD]]) checked out from the [[Repository]].

## Key Aspects / Characteristics

- **Editable Files:** Contains the tangible files you can see, edit, create, and delete using standard tools (text editors, IDEs, file explorers).
- **Checkout Point:** Represents a specific version of the project checked out from the Git [[Repository]]'s history (e.g., using [[git_checkout]]).
- **Tracked vs. Untracked:** Files in the working directory can be:
    - *Tracked:* Files that Git knows about and were present in the last snapshot; Git monitors them for changes.
    - *Untracked:* Files that are present but were not in the last snapshot and have not been staged ([[git_add]]); Git doesn't track their changes unless explicitly told to. Files listed in [[gitignore]] are typically ignored and remain untracked.
- **Source for Staging:** Modifications made to tracked files in the working directory are the source for changes that get promoted to the [[Staging_area]] using [[git_add]].

## Examples / Use Cases

- Editing `main.py` in your text editor.
- Creating a new file `utils.py`.
- Deleting an old configuration file `config.yaml`.
- Running `git status` shows differences between the working directory, [[Staging_area]], and the last commit ([[Git_HEAD|HEAD]]).

## Related Concepts
- [[Git]] (The VCS context)
- [[Repository]] (The `.git` directory storing history, separate from the working files)
- [[Staging_area]] (Intermediate area between working directory and repository)
- [[Commit_object]] (Snapshots stored in the repository, checked out into the working directory)
- [[git_checkout]] (Command to switch branches/commits, updating the working directory)
- [[git_status]], [[git_diff]] (Commands comparing the working directory state)

## Diagrams (Optional)
*(See diagram in [[Staging_area]])*

---
**Source:** Worksheet WS2, WS15