---
tags:
  - version_control
  - git
  - command
  - history
  - inspection
aliases: []
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Repository]]"
  - "[[Branching]]"
  - "[[Merging]]"
  - "[[git_commit]]"
  - "[[git_show]]"
  - "[[git_diff]]"
  - "[[Git_HEAD|HEAD]]"
  - "[[SHA-1]]"
worksheet:
  - WS2
  - WS15
date_created: 2025-04-20
---
# ` git log `

## Purpose

The `git log` command displays the commit history of a Git [[Repository]]. It shows [[Commit_object|commits]] starting from the most recent one (usually the tip of the current branch, [[Git_HEAD|HEAD]]) and working backwards through the commit ancestry. It's essential for understanding the project's evolution, finding specific changes, and navigating the history.

## Syntax

```bash
git log [<options>] [<revision_range>] [[--] <path>...]
```

## Common Options for Formatting Output

| Option             | Description                                                                                             |
| :----------------- | :------------------------------------------------------------------------------------------------------ |
| `-p`, `-u`, `--patch`| Show the patch (diff) introduced with each commit.                                                      |
| `--stat`           | Show summary statistics (files changed, insertions/deletions) for each commit.                            |
| `--shortstat`      | Show only the changed/insertions/deletions line from `--stat`.                                          |
| `--name-only`      | Show only the names of files changed in each commit.                                                    |
| `--name-status`    | Show names and status (Added, Modified, Deleted) of files changed.                                      |
| `--abbrev-commit`  | Show only a partial prefix of the commit [[SHA-1]] hash instead of the full hash.                         |
| `--relative-date`  | Show dates in a relative format (e.g., "2 hours ago") instead of the full date.                         |
| `--graph`          | Draw a text-based graphical representation of the commit history (showing branches and merges).           |
| `--pretty=<format>`| Control the output format. Common formats: `oneline`, `short`, `medium` (default), `full`, `fuller`, `format:<string>`. |
| `--oneline`        | Shortcut for `--pretty=oneline --abbrev-commit`. Shows each commit on a single line (hash and title).     |

## Common Options for Filtering History

| Option             | Description                                                                                             |
| :----------------- | :------------------------------------------------------------------------------------------------------ |
| `-<number>`, `-n <number>` | Limit the number of commits shown.                                                              |
| `--since=<date>`, `--after=<date>` | Show commits more recent than a specific date.                                          |
| `--until=<date>`, `--before=<date>`| Show commits older than a specific date.                                                |
| `--author=<pattern>`| Show commits whose author matches the pattern (regex).                                                  |
| `--committer=<pattern>`| Show commits whose committer matches the pattern.                                                 |
| `--grep=<pattern>` | Show commits whose commit message matches the pattern (regex).                                          |
| `--all`            | Show history from all branches (not just the current one).                                              |
| `<branch_name>`    | Show history reachable from the specified branch tip.                                                   |
| `<commit1>..<commit2>`| Show commits reachable from `<commit2>` but not from `<commit1>`.                                     |
| `<commit1>...<commit2>`| Show commits reachable from either `<commit1>` or `<commit2>` but not both.                           |
| `-- <path>...`     | Show only commits that affect the specified file(s) or directory(ies).                                  |
| `--merges`         | Show only merge commits.                                                                                |
| `--no-merges`      | Do not show merge commits.                                                                              |

## Examples

**Example 1: Show recent history (one-line format)**
```bash
git log --oneline -5
# Output:
# a1b2c3d (HEAD -> main, origin/main) Fix typo in README
# e4f5g6h Add feature X
# c7d8e9f Refactor utility function
# b0a1b2c Merge branch 'develop'
# 9f8e7d6 Initial commit
```

**Example 2: Show history with stats and graph**
```bash
git log --stat --graph
```
*Displays commit graph, author, date, message, and files changed with insertion/deletion counts.*

**Example 3: Show changes introduced by a specific commit**
```bash
git log -p -1 <commit_hash>
# or just use git show <commit_hash>```
*Shows the commit details and the patch (diff) for that single commit.*

**Example 4: Find commits by author affecting a specific file**
```bash
git log --author="John Doe" -- pretty=short -- src/main.c
```
*Shows commits by "John Doe" that modified `src/main.c`, in a short format.*

**Example 5: See differences between branches**
```bash
git log --oneline --graph main..feature-branch
```
*Shows commits that are in `feature-branch` but not yet in `main`.*

## Related Commands/Concepts
- [[Git]], [[Repository]], [[Commit_object]], [[Git_HEAD|HEAD]], [[SHA-1]]
- [[Branching]], [[Merging]] (Log helps visualize branches/merges)
- [[git_commit]] (Creates the commits shown by log)
- [[git_show]] (Shows details and diff for a *single* commit or object)
- [[git_diff]] (Compares two arbitrary states/commits)
- [[git_reflog]] (Shows history of local HEAD movements, useful for recovery)

## Questions / Further Study
>[!question] How would you search through your project for a string or regular expression? (WS2)
> While `git log --grep=<pattern>` searches commit *messages*, to search the *content* of files in your project history or working directory, you typically use:
> - **`git grep <pattern>`:** Searches the tracked files in your [[Working_directory]] or a specific commit/tree for the pattern. Very fast.
>   ```bash
>   # Search working directory
>   git grep "my_function_name"
>
>   # Search all files in commit HEAD~3
>   git grep "my_function_name" HEAD~3
>
>   # Search using regex with line numbers
>   git grep -n -E 'myFunc(tion|Name)'
>   ```
> - **`git log -S<string>` (Pickaxe):** Searches the commit history for commits that *introduced or removed* occurrences of the specified string in the file content diffs. Useful for finding when a specific piece of code was added or deleted.
>   ```bash
>   git log -S"specific_variable_name"
>   ```
> - **`git log -G<regex>`:** Searches the commit history for commits where the *diff* matches the specified regular expression.

---
**Source:** Worksheet WS2, WS15