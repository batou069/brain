---
tags: [version_control, git, command, state, cleanup, danger]
aliases: []
related:
  - "[[Git]]"
  - "[[Working_directory]]"
  - "[[gitignore]]"
  - "[[git_status]]"
  - "[[git_reset]]"
worksheet: [WS15]
date_created: 2025-04-21
---
# ` git clean `

## Purpose

The `git clean` command removes untracked files from your [[Working_directory]]. Untracked files are those that exist in your working directory but have not been added to the Git [[Repository]] (i.e., they are not tracked by Git and don't appear in [[gitignore]]). It's useful for getting rid of build artifacts, log files, or other generated files that you don't want to commit.

## Syntax

```bash
# Dry run: Show what would be deleted without actually deleting
git clean -n

# Interactive mode: Ask confirmation for each file/directory
git clean -i

# Remove untracked files (use with caution!)
git clean -f

# Remove untracked directories as well
git clean -f -d
# or
git clean -fd

# Remove untracked files, including ignored files (use with extreme caution!)
git clean -f -x

# Remove untracked files, including ignored files specified in .gitignore but not other ignore rules
git clean -f -X
```

## Common Options

| Option            | Description                                                                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| -n, --dry-run     | Don't actually remove anything, just show what would be done.                                                                                 |
| -f, --force       | Required to actually delete files unless clean.requireForce config is false. Prevents accidental deletion.                                    |
| -i, --interactive | Show what would be done and provide an interactive interface to clean files.                                                                  |
| -d                | Remove untracked directories in addition to untracked files.                                                                                  |
| -x                | Remove ignored files as well. This includes files matching patterns in [[gitignore]] and $GIT_DIR/info/exclude. **Use with extreme caution.** |
| -X                | Remove only files ignored by Git's standard ignore rules ([[gitignore]], etc.), but not untracked non-ignored files.                          |

## Examples

**Example 1: See which untracked files would be removed**

```bash
git clean -n 
# Would remove build/output.o 
# Would remove temp.log
```

**Example 2: Remove untracked files**

```bash
# WARNING: This deletes files permanently! 
git clean -f 
# Removing build/output.o 
# Removing temp.log
```

**Example 3: Remove untracked files and directories**


```bash
# WARNING: This deletes files and directories permanently!
git clean -fd
# Removing build/
# Removing temp.log
```

**Example 4: Remove untracked files AND ignored files (DANGEROUS)**

```bash
# WARNING: This deletes ignored files like logs or credentials if not careful!
git clean -fx
```

## Related Commands/Concepts
- [[Working_directory]] (Where `git clean` operates)
- [[gitignore]] (Files listed here are usually *not* removed by `clean` unless `-x` is used)
- [[git_status]] (Shows untracked files that `clean` might remove)
- [[git_reset]] `--hard` (Resets tracked files, while `clean` removes untracked files)

## Notes
>[!danger] Permanent Deletion
> `git clean` permanently deletes files from your [[Working_directory]]. Unlike `git reset --hard` which affects tracked files whose history is stored in Git (and potentially recoverable via reflog), cleaned files are generally **gone for good** unless backed up elsewhere. Always use `git clean -n` (dry run) first to be sure what will be deleted. The `-f` (force) flag is required for safety.

---
**Source:** Worksheet WS15