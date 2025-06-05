---
tags:
  - version_control
  - concept
aliases:
  - Repo
related:
  - "[[Version_Control]]"
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Branching]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[Working_directory]]"
  - "[[Staging_area]]"
  - "[[git_clone]]"
  - "[[git_init]]"
  - "[[Remote_repository]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# Repository

## Definition

In [[Version_Control]] systems like [[Git]], a **Repository** (often shortened to "repo") is a data structure that stores the metadata and history for a set of files or directory structure. It contains all the [[Commit_object|commits]] (snapshots of the project over time), branches, tags, and other information needed to manage the project's versions.

## Key Aspects / Characteristics

- **History Storage:** The primary function is to store the complete history of the project.
- **Metadata:** Contains information *about* the history, such as commit messages, authors, dates, and relationships between commits.
- **Objects:** In Git, the repository primarily consists of objects (blobs, trees, commits, tags) stored typically in a hidden `.git` directory within the project's [[Working_directory]].
- **Local vs. Remote:** Developers usually work with a *local* repository on their machine. They synchronize changes with one or more *[[Remote_repository|remote repositories]]* (often hosted on platforms like GitHub, GitLab, Bitbucket) for collaboration and backup.
- **Initialization:** Created using [[git_init]] (for a new project) or [[git_clone]] (to copy an existing remote repository).

## Examples / Use Cases

- A project's `.git` directory is its local Git repository.
- A project hosted on GitHub resides in a remote repository.

## Related Concepts
- [[Git]] (The VCS that uses repositories)
- [[Working_directory]] (The user's view of the files)
- [[Staging_area]] (Where changes are prepared before committing to the repository)
- [[Commit_object]] (The snapshots stored *in* the repository)
- [[Branching]] (Different lines of development stored in the repository)
- [[Git_HEAD|HEAD]] (Pointer to the current commit/branch within the repository)
- [[git_init]], [[git_clone]] (Commands to create repositories)
- [[Remote_repository]] (A repository hosted elsewhere, used for collaboration)

## Questions / Further Study
>[!question] Which files belong to the Git repository? Which files do not? (WS2)
> - **Belong:** The files and metadata stored within the hidden `.git` directory constitute the repository itself. This includes commit objects, tree objects, blob objects (file contents), branch pointers, tags, configuration, hooks, etc.
> - **Do Not Belong (directly):** The files you see and edit in your [[Working_directory]] are *not* technically *part* of the repository database itself, but rather a checkout (a specific version) *from* the repository. Files listed in [[gitignore]] are intentionally ignored by Git and are not tracked in the repository. The [[Staging_area]] is also conceptually separate, holding information about the *next* commit.

>[!question] What happens when you clone a Git repository? (WS2)
> When you run [[git_clone]], Git does the following:
> 1. Creates a new directory on your local machine (usually named after the repository).
> 2. Initializes a new local Git [[Repository]] within that directory (creates the `.git` folder).
> 3. Copies *all* the data (commits, branches, tags - the entire history) from the specified [[Remote_repository]] into your new local repository.
> 4. Sets up a connection (a "remote" named `origin` by default) pointing back to the URL you cloned from.
> 5. Checks out the latest version of the default branch (usually `main` or `master`) into your [[Working_directory]], so you have the actual project files to work with.

---
**Source:** Worksheet WS2