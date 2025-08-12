---
tags: [version_control, git, command]
aliases: []
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Staging_area]]"
  - "[[git_add]]"
  - "[[git_log]]"
  - "[[git_push]]"
worksheet: [WS2, WS34]
date_created: 2025-04-21
---
# ` git commit `

## Purpose

The `git commit` command captures a snapshot of the project's currently staged changes ([[Staging_area]]) and saves it permanently to the [[Repository]]'s history. Each commit represents a specific version of the project.

## Syntax

```bash
git commit [OPTIONS]
```

Most commonly used with the -m flag:

```bash
git commit -m "Your descriptive commit message"
```

## Common Options

| Option        | Description                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------ |
| -m <message>  | Use the given <message> as the commit message.                                                   |
| -a, --all     | Stage files that have been modified or deleted, then commit. Does not add new (untracked) files. |
| --amend       | Modify the most recent commit. Useful for fixing typos or adding forgotten changes.              |
| -v, --verbose | Show the diff of the changes being committed in the commit message editor.                       |
## Examples

**Example 1: Basic Commit with Message**
```bash
# First, stage changes
git add file1.txt modified_file.py

# Then, commit them
git commit -m "Implement feature X and update documentation"
```

This creates a new [[Commit_object]] containing the changes staged with git add.

**Example 2: Committing All Tracked Changes**

```bash
# Stage modified/deleted tracked files and commit in one step
git commit -a -m "Refactor module Y and fix related bugs"
```

Note: This will not add new files that haven't been tracked before.

**Example 3: Amending the Last Commit**

```bash
# Oops, forgot to add one file to the last commit
git add forgotten_file.c

# Amend the previous commit to include this file and/or change the message
git commit --amend -m "Corrected commit message and added forgotten_file.c"
```

This replaces the previous commit with a new one. Be cautious if the original commit was already [[git_push|pushed]].

## Related Commands/Concepts

- [[git_add]] (To stage changes before committing)
    
- [[Staging_area]] (The area where changes are prepared for commit)
    
- [[Commit_object]] (The actual snapshot stored in the repository)
    
- [[git_log]] (To view the commit history)
    
- [[git_status]] (To see which changes are staged or unstaged)
    
- [[git_reset]] (To unstage changes or move [[Git_HEAD|HEAD]])
    

## Notes

> [!note] Commit Messages  
> Writing clear, concise, and informative commit messages is crucial for understanding the project's history. Often follows a convention (e.g., imperative mood: "Fix bug" not "Fixed bug").

> [!question] Why add before commit?  
> The [[Staging_area]] allows you to craft your commits precisely. You might make several edits but only want to group related changes into a single, logical [[Commit_object]]. git add lets you select which changes go into the next commit.

---

**Source:** Worksheet WS2, WS34