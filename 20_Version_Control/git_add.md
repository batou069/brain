---
tags:
  - version_control
  - git
  - command
  - core
aliases: []
related:
  - "[[Git]]"
  - "[[Staging_area]]"
  - "[[Working_directory]]"
  - "[[git_commit]]"
  - "[[git_status]]"
  - "[[git_reset]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git add `

## Purpose

The `git add` command moves changes from the [[Working_directory]] to the [[Staging_area]] (also known as the index). It tells Git that you want to include updates to particular files (or parts of files) in the next [[git_commit|commit]]. Staging allows you to carefully craft your commits, grouping related changes together even if you've made other unrelated modifications in your working directory.

## Syntax

```bash
# Stage changes in specific file(s)
git add <file_path>...

# Stage all changes (new, modified, deleted) in the current directory and subdirectories
git add .

# Stage all changes in the entire repository
git add -A
git add --all

# Stage already tracked files that have been modified or deleted (but not new files)
git add -u
git add --update

# Interactively stage parts (hunks) of files
git add -p
git add --patch
```

## Common Options

| Option        | Description                                                                                                |
| :------------ | :--------------------------------------------------------------------------------------------------------- |
| `<pathspec>`  | Specifies the file(s) or directory(ies) to add. Can use patterns.                                          |
| `.`           | Adds all changes in the current directory and below.                                                       |
| `-A`, `--all` | Stages all changes (new, modified, deleted files) throughout the entire repository relative to the current directory. |
| `-u`, `--update`| Stages modifications and deletions of already tracked files, but ignores new (untracked) files.            |
| `-p`, `--patch` | Interactively review hunks of changes and choose whether to stage them. Very useful for granular commits. |
| `-i`, `--interactive` | Enter interactive mode to choose files and hunks to stage.                                           |
| `-n`, `--dry-run`| Show what would be added without actually adding anything.                                               |

## Examples

**Example 1: Stage a specific file**
```bash
# Modify file1.txt and create new_file.txt
git add file1.txt
```
*Adds the current content of `file1.txt` to the staging area. `new_file.txt` remains untracked.*

**Example 2: Stage all changes in current directory**
```bash
git add .
```
*Stages modifications to `file1.txt` AND adds the new file `new_file.txt` to the staging area (if they are in or below the current directory).*

**Example 3: Stage only modified/deleted tracked files**
```bash
# Modify tracked_file.py and delete old_tracked.log
git add -u
```
*Stages the changes to `tracked_file.py` and the deletion of `old_tracked.log`. Any new untracked files are ignored.*

**Example 4: Interactively stage parts of a file**
```bash
git add -p main.py
```
*Git will show each chunk ("hunk") of changes in `main.py` and ask if you want to stage it (y/n/s/q/e...).*

## Related Commands/Concepts
- [[Git]]
- [[Staging_area]] (The destination for `git add`)
- [[Working_directory]] (The source of changes for `git add`)
- [[git_commit]] (Consumes the changes staged by `git add`)
- [[git_status]] (Shows which files are staged, modified, untracked)
- [[git_reset]] (Used to *unstage* files, the opposite of `add`)
- [[gitignore]] (Specifies intentionally untracked files that `git add .` or `git add -A` usually ignore)

---
**Source:** Worksheet WS2