---
tags:
  - version_control
  - git
  - command
  - remote
  - core
aliases: []
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Remote_repository]]"
  - "[[Working_directory]]"
  - "[[git_remote]]"
  - "[[git_pull]]"
  - "[[git_fetch]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git clone `

## Purpose

The `git clone` command creates a **copy** (a clone) of an existing Git [[Repository|repository]], typically one hosted remotely ([[Remote_repository]]). It downloads the entire project history (all commits, branches, tags) from the remote repository and creates a new local repository on your machine, along with a [[Working_directory]] checked out to the default branch.

## Syntax

```bash
# Clone repository into a directory with the same name as the repo
git clone <repository_url>

# Clone repository into a specific directory name
git clone <repository_url> <directory_name>

# Clone only a specific branch
git clone -b <branch_name> --single-branch <repository_url> [<directory_name>]

# Clone with limited depth (shallow clone)
git clone --depth <number> <repository_url> [<directory_name>]
```

## Key Actions Performed

1.  **Creates Directory:** Creates a new directory on your local filesystem (either named after the repo or using `<directory_name>` if provided).
2.  **Initializes Local Repo:** Runs `git init` inside the new directory to create a local `.git` repository structure.
3.  **Adds Remote:** Automatically adds a [[git_remote|remote]] named `origin` pointing back to the `<repository_url>` you cloned from. You can verify this with `git remote -v`.
4.  **Fetches All Data:** Downloads all objects (commits, trees, blobs) and references (branches, tags) from the remote repository into your local `.git` directory.
5.  **Checks Out Default Branch:** Creates a local [[Working_directory]] by checking out the default branch (usually `main` or `master`) from the downloaded history (specifically, the branch that `HEAD` points to on the remote repository). It also sets up a local branch (e.g., `main`) to track the corresponding remote branch (`origin/main`).

## Examples

**Example 1: Clone a repository from GitHub**
```bash
git clone https://github.com/user/repo-name.git
```
*Creates a directory named `repo-name`, downloads the entire history, sets up `origin` remote, and checks out the default branch.*

**Example 2: Clone into a specific directory**
```bash
git clone git@gitlab.com:team/project.git my-local-project
```
*Creates a directory named `my-local-project` and clones the repository into it.*

**Example 3: Clone only the `develop` branch (shallow history)**
```bash
git clone -b develop --single-branch --depth 1 https://github.com/user/repo-name.git
```
*Clones only the `develop` branch and only retrieves the most recent commit history (depth 1), saving download time and disk space.*

## Related Commands/Concepts
- [[Git]]
- [[Repository]], [[Remote_repository]]
- [[Working_directory]]
- [[git_init]] (Used implicitly by clone)
- [[git_remote]] (Used implicitly to set up `origin`)
- [[git_fetch]] (Clone performs an initial fetch)
- [[git_pull]] (Used later to get updates *after* cloning)

---
**Source:** Worksheet WS2