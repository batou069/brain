---
tags:
  - version_control
  - git
  - concept
  - architecture
aliases:
  - Distributed Version Control System
  - DVCS
related:
  - "[[Version_Control]]"
  - "[[Centralized_Version_Control]]"
  - "[[Git]]"
  - "[[Mercurial]]"
  - "[[Repository]]"
  - "[[git_clone]]"
  - "[[git_push]]"
  - "[[git_pull]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# Distributed Version Control System (DVCS)

## Definition

A **Distributed Version Control System (DVCS)** is a form of [[Version_Control]] where every developer's working copy of the code is also a complete [[Repository]], containing the full history of all changes. This contrasts with [[Centralized_Version_Control|centralized systems]], where the history resides solely on a central server.

## Key Aspects / Characteristics

- **Full Local History:** Each user has a complete copy of the project's history on their local machine.
- **Offline Operations:** Most operations (committing, viewing history, creating branches, merging branches) are performed locally and are therefore very fast and do not require a network connection.
- **No Single Point of Failure:** If the central server (if one is used for collaboration) goes down, developers can still work locally and even synchronize directly with other developers' repositories. The full history exists in multiple places.
- **Flexible Workflows:** Enables more flexible workflows, as developers can share changes between repositories without needing a central intermediary. Common workflows involve fetching/pulling changes from and pushing changes to designated shared repositories (like those on GitHub/GitLab).
- **[[Branching]] and [[Merging]]:** DVCS tools like [[Git]] and [[Mercurial]] typically have very strong and efficient branching and merging capabilities, essential for managing distributed development.
- **Collaboration Model:** While distributed, collaboration often revolves around one or more shared "central" repositories (e.g., on GitHub) that developers push to and pull from, but this central repo is technically just another clone, not fundamentally different from local ones.

## Examples

- **[[Git]]** (Most popular DVCS)
- **[[Mercurial]] (Hg)**
- Bazaar (Bzr)
- Fossil

## DVCS vs. Centralized VCS

| Feature             | Distributed VCS (e.g., Git)     | [[Centralized_Version_Control|Centralized VCS]] (e.g., SVN, CVS) |
| :------------------ | :------------------------------ | :----------------------------------- |
| **Repository**      | Full copy on each client        | Single central repository            |
| **Commit**          | Local operation (fast)          | Requires network connection to server|
| **Branching/Merge** | Fast, cheap, core feature       | Often slower, more complex           |
| **Offline Work**    | Most operations possible        | Limited (usually only editing)       |
| **Speed**           | Generally faster (local ops)    | Slower (network dependency)          |
| **Backup**          | Implicit (many full copies)     | Relies on central server backup      |
| **Single Failure Pt**| No                              | Yes (central server)                 |

## Related Concepts
- [[Version_Control]]
- [[Centralized_Version_Control]] (Contrasting architecture)
- [[Git]], [[Mercurial]] (Examples)
- [[Repository]] (Each clone is a full repo)
- [[git_clone]], [[git_push]], [[git_pull]], [[git_fetch]] (Commands supporting distributed workflows)

---
**Source:** Worksheet WS2 (Implied)