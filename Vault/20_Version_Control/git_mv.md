---
tags:
  - version_control
  - git
  - command
  - file_management
aliases: []
related:
  - "[[Git]]"
  - "[[Working_directory]]"
  - "[[Staging_area]]"
  - "[[git_rm]]"
  - "[[git_add]]"
  - "[[mv]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git mv `

## Purpose

The `git mv` command **moves or renames** a file, directory, or symbolic link within the Git [[Working_directory]] and simultaneously updates the Git [[Staging_area|index (staging area)]] to record the move/rename operation.

## Action

Using `git mv source destination` is essentially equivalent to performing these three steps manually:
1.  Renaming/moving the file using the standard OS command (e.g., `mv source destination` on Linux/macOS).
2.  Removing the old file path from the Git index (`git rm --cached source`).
3.  Adding the new file path to the Git index (`git add destination`).

`git mv` bundles these steps into a single, convenient command.

## Syntax

```bash
# Rename a file
git mv <old_filename> <new_filename>

# Move a file into a directory
git mv <file_path> <directory_path>/

# Move and rename a file
git mv <old_path/old_filename> <new_path/new_filename>
```

## Key Aspects

- **Tracks Renames/Moves:** Records the operation as a rename/move, which Git can often detect later (e.g., when viewing history or diffs, Git might show it as a rename rather than a deletion and addition, although detection depends on similarity).
- **Updates Index:** Automatically stages the change (removal of old path, addition of new path). The change still needs to be committed using [[git_commit]].
- **Working Directory:** Modifies the actual files/directories in your working directory.
- **Safety:** Prevents overwriting existing files unless the `-f` (force) option is used.

## Examples

**Example 1: Rename a file**
```bash
# Rename old_name.txt to new_name.txt
git mv old_name.txt new_name.txt
# Now run 'git status' - it will show:
# Renamed: old_name.txt -> new_name.txt
# (This change is already staged)
```

**Example 2: Move a file into a subdirectory**
```bash
# Assume 'src/' directory exists
git mv main.c src/
# Now run 'git status' - it will show:
# Renamed: main.c -> src/main.c
```

**Example 3: Move and rename**
```bash
git mv docs/README.txt docs/Project_Info.md
```

## Related Commands/Concepts
- [[Git]]
- [[Working_directory]], [[Staging_area]] (Affected by the command)
- [[git_rm]] (Removes files)
- [[git_add]] (Stages files)
- [[mv]] (Standard OS command for moving/renaming)
- File Renaming/Moving

---
**Source:** Worksheet WS2