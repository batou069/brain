---
tags: 
  - version_control
  - git
  - command
  - remote
aliases: 
related:
  - "[[Git]]"
  - "[[Remote_repository]]"
  - "[[git_pull]]"
  - "[[git_merge]]"
  - "[[git_log]]"
  - "[[git_checkout]]"
  - "[[Branching]]"
worksheet: WS15
date_created: 2025-04-21
---
# git fetch `

## Purpose

The `git fetch` command downloads commits, files, and refs (like branch pointers and tags) from one or more [[Remote_repository|remote repositories]] into your local [[Repository]]. It updates your local copies of remote branches (e.g., `origin/main`, `origin/feature-x`) but **does not** modify your local working branches (e.g., `main`) or your [[Working_directory]].

## Syntax

```bash
git fetch [<options>] [<repository> [<refspec>...]]
```

Common usages:

```bash 
# Fetch updates from the default remote (usually 'origin')
git fetch

# Fetch updates from a specific remote
git fetch <remote_name>

# Fetch updates for a specific branch from origin
git fetch origin <branch_name>

# Fetch all tags along with other objects
git fetch --tags

# Remove local remote-tracking refs that no longer exist on the remote
git fetch --prune
```

## Common Options

| Option   | Description                                                                                |
| -------- | ------------------------------------------------------------------------------------------ |
| <remote> | The name of the remote repository to fetch from (e.g., origin).                            |
|          | Specifies which refs to fetch and which local refs to update.                              |
|          | Fetch from all registered remotes.                                                         |
|          | Before fetching, remove any remote-tracking references that no longer exist on the remote. |
|          | Fetch all tags from the remote (in addition to whatever else is fetched).                  |
## Examples

**Example 1: Fetch updates from origin**
```bash
git fetch origin
``` 
*Downloads new commits and updates remote-tracking branches like `origin/main`, `origin/develop`, etc., in your local repo. Your `main` branch and working directory are untouched.*  

**Example 2: See what has changed on the remote** 
```bash
# Fetch latest changes from origin 
git fetch origin  

# See the difference between your local main and the fetched origin/main 
git log main..origin/main 
# or 
git diff main origin/main
```
Allows you to inspect remote changes before deciding to merge them.

**Example 3: Fetch and prune stale branches**
```bash
git fetch --prune origin
```

Fetches updates and removes any local origin/* branches that have been deleted on the remote repository.

## Related Commands/Concepts

- [[git_pull]] (Fetches and merges/rebases changes into the current local branch)
- [[git_merge]] (Used after fetch to integrate fetched changes into a local branch)
- [[git_rebase]] (Alternative to merge for integrating fetched changes)
- [[git_remote]] (Command to manage remote repositories)
- [[Remote_repository]] (The source of fetched data)    
- Remote-tracking branches (e.g., origin/main) (Local pointers updated by fetch)


## Notes

> [!note] Fetch vs. Pull  
> git fetch is considered safer than [[git_pull]] because it doesn't automatically change your local working branches or [[Working_directory]]. It lets you retrieve remote changes and inspect them (e.g., using git log origin/main) before deciding how or when to integrate them using [[git_merge]] or [[git_rebase]]. git pull is essentially git fetch followed immediately by git merge (or git rebase if configured).

---

**Source:** Worksheet WS15