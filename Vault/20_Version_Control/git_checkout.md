---
tags: [version_control, git, command, navigation, branch]
aliases: []
related:
  - "[[Git]]"
  - "[[Branching]]"
  - "[[Commit_object]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[Working_directory]]"
  - "[[git_branch]]"
  - "[[git_switch]]"
  - "[[git_restore]]"
worksheet: [WS]
date_created: 2025-04-11
---
# ` git checkout `

## Purpose

The `git checkout` command is primarily used to switch [[Branching|branches]] or restore [[Working_directory|working tree]] files. It updates the files in the working directory to match the version stored in the target branch or [[Commit_object|commit]], and updates [[Git_HEAD|HEAD]] to point to the specified branch or commit.



## Syntax

```bash
# Switch branches
git checkout <branch_name>

# Create and switch to a new branch
git checkout -b <new_branch_name> [<start_point>]

# Switch to a specific commit (Detached HEAD state)
git checkout <commit_hash>
git checkout <tag_name>

# Restore file(s) in the working directory from the index (staging area)
git checkout -- <file_path>...

# Restore file(s) in the working directory from a specific commit/branch
git checkout <commit_or_branch> -- <file_path>...
```

## Common Options

| Option       | Description                                                             |
| ------------ | ----------------------------------------------------------------------- |
| -b <branch>  | Create a new branch named <branch> and switch to it immediately.        |
| -B <branch>  | Create/reset a branch named <branch> and switch to it.                  |
| -- <file>    | Disambiguates between a branch name and a file path. Restores the file. |
| -d, --detach | Checkout a commit for inspection/experimentation ([[Detached_HEAD]]).   |
## Examples

**Example 1: Switch to an existing branch**

```bash
git checkout develop
```
Updates [[Working_directory]] to match the develop branch and sets [[Git_HEAD|HEAD]] to point to develop.

**Example 2: Create and switch to a new feature branch**

```bash
git checkout -b feature/user-auth main
```
Creates a new branch feature/user-auth starting from main and switches to it.

**Example 3: Discard changes in a specific file**

```bash
# Discard changes made since the last commit (restores from index/HEAD)
git checkout -- config.yaml
```

Replaces config.yaml in the [[Working_directory]] with the version from the [[Staging_area]] (or [[Git_HEAD|HEAD]] if not staged).

**Example 4: Checkout a previous commit**

```bash
git checkout a1b2c3d
```

*Updates [[Working_directory]] to match commit `a1b2c3d` and enters [[Detached_HEAD]] state.*

## Related Commands/Concepts
- [[git_branch]] (Manages branches - list, create, delete)
- [[git_switch]] (Newer command specifically for switching branches, preferred over `checkout` for this purpose)
- [[git_restore]] (Newer command specifically for restoring files, preferred over `checkout -- <file>`)
- [[Git_HEAD|HEAD]] (Pointer updated by `checkout`)
- [[Working_directory]] (Files updated by `checkout`)
- [[Detached_HEAD]] (State entered when checking out a commit directly)

## Notes
>[!warning] Overloaded Command
> `git checkout` historically performed multiple unrelated tasks (switching branches, restoring files). Newer Git versions introduced [[git_switch]] (for branches) and [[git_restore]] (for files) to provide clearer separation of concerns. While `git checkout` still works for all cases, using the newer commands is often recommended for clarity.

>[!warning] Discarding Changes
> Using `git checkout -- <file>` discards any uncommitted changes in that file in your [[Working_directory]]. Be sure you want to lose those changes before running it.

---
**Source:** Worksheet WS15