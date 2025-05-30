---
tags:
  - version_control
  - git
  - command
  - repository
  - core
aliases: []
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Working_directory]]"
  - "[[git_clone]]"
  - "[[git_add]]"
  - "[[git_commit]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git init `

## Purpose

The `git init` command creates a **new, empty Git [[Repository]]** or reinitializes an existing one. It is the first command you typically run when starting a new project with Git or when converting an existing, untracked project into a Git repository.

## Action

Executing `git init` in a directory performs the following main action:
- It creates a hidden subdirectory named **`.git`**.
- This `.git` directory contains all the necessary repository files and metadata for Git to start tracking changes, including:
    - Subdirectories for objects (commits, trees, blobs), refs (branches, tags).
    - Template files.
    - Configuration files (`.git/config`).
    - Hooks directory (`.git/hooks`).
    - The `HEAD` file (pointing initially to the default branch, which might not exist yet).

`git init` **does not** track any files yet. It only sets up the necessary infrastructure (`.git` directory) for version control. You need to use [[git_add]] and [[git_commit]] afterwards to start tracking files and recording history.

## Syntax

```bash
# Initialize an empty Git repository in the current directory
git init

# Initialize an empty Git repository in a specific new/existing directory
git init <directory>

# Initialize as a "bare" repository (no working directory - used for servers/sharing)
git init --bare [<directory>]
```

## Examples

**Example 1: Initialize a new repository in the current directory**
```bash
mkdir my_new_project
cd my_new_project
git init
# Output: Initialized empty Git repository in /path/to/my_new_project/.git/
```
*Creates the `.git` subdirectory inside `my_new_project/`.*

**Example 2: Convert an existing project directory**
```bash
cd existing_project_folder
git init
# Output: Initialized empty Git repository in /path/to/existing_project_folder/.git/
# Now you can run 'git add .' and 'git commit' to track existing files.
```

## Related Commands/Concepts
- [[Git]]
- [[Repository]] (The `.git` directory created by `init`)
- [[Working_directory]] (The directory containing `.git`)
- [[git_clone]] (Alternative way to get a repository, by copying an existing remote one)
- [[git_add]], [[git_commit]] (Commands used *after* `init` to start tracking history)

## Questions / Further Study
>[!question] Explain the outcome of `mkdir rep; cd rep; git init;` (WS2)
> 1.  `mkdir rep`: Creates a new, empty directory named `rep`.
> 2.  `cd rep`: Changes the current working directory to the newly created `rep` directory.
> 3.  `git init`: Initializes an empty Git repository *within* the `rep` directory. This creates a hidden subdirectory named `.git` inside `rep`. The `rep` directory is now a Git [[Working_directory]] associated with this new, empty [[Repository]]. No files are tracked yet.

---
**Source:** Worksheet WS2