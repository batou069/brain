---
tags:
  - version_control
  - git
  - concept
  - workflow
aliases:
  - Branch
  - Branches
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Commit_object]]"
  - "[[Merging]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[git_branch]]"
  - "[[git_checkout]]"
  - "[[git_merge]]"
worksheet:
  - WS2
  - WS15
date_created: 2025-04-21
---
# Branching (Git)

## Definition

In [[Git]], **Branching** is the mechanism that allows you to diverge from the main line of development and continue to work independently without altering that main line. A branch is essentially a lightweight, movable pointer to a specific [[Commit_object|commit]]. Creating a new branch creates a new pointer; committing while on that branch moves the pointer forward.

## Key Aspects / Characteristics

- **Isolation:** Allows developers to work on features, bug fixes, or experiments in isolation without affecting other branches (like the main production branch).
- **Lightweight:** Creating and switching branches in Git is extremely fast and cheap because it only involves creating or updating a small pointer file (containing a [[SHA-1]] hash). It doesn't involve copying the entire project directory.
- **Parallel Development:** Enables multiple lines of development to occur simultaneously.
- **Workflow Foundation:** Branching is fundamental to most Git workflows (e.g., Gitflow, GitHub Flow). Common patterns include feature branches, release branches, hotfix branches.
- **Merging:** Changes made on a branch are typically integrated back into another branch (e.g., `main`) using [[Merging]].

## Examples / Use Cases

- Creating a `feature/new-login` branch to develop a new login system.
- Creating a `hotfix/bug-123` branch off the production branch (`main`) to fix a critical bug.
- Experimenting with a new library on a temporary `experiment/try-library-x` branch.

## Related Concepts
- [[Git]] (The VCS)
- [[Repository]] (Stores all branches and commits)
- [[Commit_object]] (Branches point to commits)
- [[Merging]] (Combining changes from different branches)
- [[Git_HEAD|HEAD]] (Indicates the currently active branch or commit)
- [[git_branch]] (Command to list, create, delete branches)
- [[git_checkout]] (Command to switch between branches)
- [[git_merge]] (Command to integrate changes from one branch into another)
- [[Remote_repository|Remote branches]] (Branches tracked from a remote repository)

## Diagrams (Optional)

```puml
@startuml
hide footbox
skinparam monochrome true

commit "C1" as c1
commit "C2" as c2
c1 -> c2 : main
note right of c2 : main

commit "C3" as c3
c2 -> c3 : main
note right of c3 : main

commit "F1" as f1
c2 -> f1 : feature
note bottom of f1 : feature

commit "F2" as f2
f1 -> f2 : feature
note bottom of f2 : feature

commit "C4 (Merge)" as c4
c3 -> c4 : main
f2 -> c4 : main
note right of c4 : main
@enduml
```
---
Source: Worksheet WS2, WS15