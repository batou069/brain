---
tags:
  - version_control
  - git
  - command
  - remote
  - configuration
  - file_management
aliases: []
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[Remote_repository]]"
  - "[[git_clone]]"
  - "[[git_fetch]]"
  - "[[git_pull]]"
  - "[[git_push]]"
  - "[[Working_directory]]"
  - "[[Staging_area]]"
  - "[[git_mv]]"
  - "[[git_add]]"
  - "[[rm]]"
worksheet:
  - WS2
date_created: 2025-04-21
---
# ` git remote `

## Purpose

The `git remote` command is used to manage the set of **remote repositories** whose branches you track. A remote repository is generally a version of your project hosted on the internet or network somewhere else (e.g., on GitHub, GitLab, Bitbucket, or a private server). This command allows you to view, add, rename, and remove remote repository connections.

## Syntax

```bash
# List the shortnames of existing remotes
git remote

# List remotes with their URLs
git remote -v

# Show information about a specific remote
git remote show <remote_name>
# Example: git remote show origin

# Add a new remote connection
git remote add <shortname> <url>
# Example: git remote add upstream https://github.com/original/repo.git

# Rename a remote
git remote rename <old_name> <new_name>
# Example: git remote rename origin upstream

# Remove a remote connection
git remote remove <remote_name>
# or
git remote rm <remote_name>
# Example: git remote remove old_backup

# Change the URL of a remote
git remote set-url <remote_name> <new_url>
# Example: git remote set-url origin git@github.com:user/repo.git
```

## Key Concepts

- **Remote:** A pointer/reference to another copy of the same Git repository, usually hosted on a different server.
- **Shortname:** A local alias or nickname given to a remote repository's URL (e.g., `origin` is the conventional default shortname for the repository you cloned from).
- **URL:** The address (HTTPS or SSH) where the remote repository is located.
- **Tracking:** Remotes allow you to track branches from other repositories, enabling collaboration and synchronization using [[git_fetch]], [[git_pull]], and [[git_push]].

## Examples

**Example 1: View existing remotes**
```bash
git remote -v
# Output might be:
# origin  https://github.com/myuser/myrepo.git (fetch)
# origin  https://github.com/myuser/myrepo.git (push)
```

**Example 2: Add a remote for the original upstream repository**
```bash
# Assuming you forked a project and cloned your fork
git remote add upstream https://github.com/original-owner/original-repo.git
git remote -v
# Output might now include:
# origin  https://github.com/myuser/myrepo.git (fetch)
# origin  https://github.com/myuser/myrepo.git (push)
# upstream        https://github.com/original-owner/original-repo.git (fetch)
# upstream        https://github.com/original-owner/original-repo.git (push)
```
*This allows you to easily fetch updates from the original project using `git fetch upstream`.*

**Example 3: Change remote URL from HTTPS to SSH**
```bash
git remote set-url origin git@github.com:myuser/myrepo.git
```

**Example 4: Remove a remote connection**
```bash
git remote remove old-remote
```

## Related Commands/Concepts
- [[Git]]
- [[Remote_repository]] (The concept being managed)
- [[Repository]] (Local repo stores remote info in `.git/config`)
- [[git_clone]] (Automatically adds the `origin` remote)
- [[git_fetch]], [[git_pull]], [[git_push]] (Commands that interact with remotes)
- URL (HTTPS, SSH protocols)

---
**Source:** Worksheet WS2

# ` git rm `

## Purpose

The `git rm` command removes files from both the Git [[Staging_area|index (staging area)]] **and** the [[Working_directory]]. It is used to tell Git to stop tracking a file and also delete it from your filesystem.

## Action

Using `git rm <file>` performs two main actions:
1.  Deletes the file from your [[Working_directory]] (like the standard `rm` command).
2.  Removes the file from the [[Staging_area]] (index), effectively staging the deletion for the next commit.

## Syntax

```bash
# Remove file from working directory and staging area
git rm <file_path>...

# Remove file only from staging area (keep it in working directory)
# Useful if you accidentally staged a file you want to keep but not track
git rm --cached <file_path>...

# Force removal (e.g., if file has staged changes different from HEAD)
git rm -f <file_path>...
git rm --force <file_path>...

# Recursively remove directory contents
git rm -r <directory_path>...
```

## Common Options

| Option        | Description                                                                                             |
| :------------ | :------------------------------------------------------------------------------------------------------ |
| `<pathspec>`  | Specifies the file(s) or directory(ies) to remove.                                                      |
| `--cached`    | **Unstage only:** Remove the file only from the index (staging area), leaving the file untouched in the working directory. |
| `-f`, `--force` | Override safety checks. Force removal even if the file has staged modifications or is not up-to-date with the `HEAD` commit. |
| `-r`          | Allow recursive removal when a directory name is given.                                                 |
| `-n`, `--dry-run`| Show which files would be removed without actually removing them.                                       |

## Examples

**Example 1: Remove a tracked file completely**
```bash
# Remove unwanted_file.txt from tracking and delete it from disk
git rm unwanted_file.txt
# Now run 'git status' - it will show:
# deleted: unwanted_file.txt
# (This deletion is staged)
```

**Example 2: Stop tracking a file but keep it locally**
```bash
# Assume config.log was accidentally added and committed before
# Add config.log to .gitignore first!
echo "config.log" >> .gitignore
git add .gitignore
git commit -m "Ignore config.log"

# Now remove config.log from Git tracking, but keep the actual file
git rm --cached config.log
# Now run 'git status' - it might show config.log as untracked (and ignored)
# Commit the removal from index
git commit -m "Stop tracking config.log"
```

**Example 3: Remove a directory recursively**
```bash
# Remove the 'old_docs/' directory and all its contents from Git and disk
git rm -r old_docs/
```

## Related Commands/Concepts
- [[Git]]
- [[Working_directory]], [[Staging_area]] (Affected by the command)
- [[git_mv]] (Moves/renames tracked files)
- [[git_add]] (Adds files to staging area)
- [[rm]] (Standard OS command for removing files)
- [[gitignore]] (Often used in conjunction with `git rm --cached` to untrack files)

## Notes
>[!warning] Data Loss
> `git rm` (without `--cached`) deletes files from your working directory. Be sure you want to remove the file permanently or have a backup if needed. The file's history remains in Git until commits are garbage collected (which doesn't happen immediately).

---
**Source:** Worksheet WS2