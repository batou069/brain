---
tags:
  - version_control
  - git
  - command
  - configuration
aliases: []
related:
  - "[[Git]]"
  - "[[Repository]]"
  - "[[gitignore]]"
  - "[[git_commit]]"
worksheet:
  - WS2
date_created: 2025-04-20
---
# ` git config `

## Purpose

The `git config` command is used to get and set Git configuration variables on different levels (system-wide, global/user-level, local/repository-level). These variables control various aspects of Git's behavior and user preferences, such as user identity, editor choice, merge tools, aliases, and more.

## Configuration Levels

Git stores configuration settings in three main locations, checked in this order (later levels override earlier ones):

1.  **System Level:** (`--system`)
    -   Applies to **all users** on the system and all their repositories.
    -   Stored in `/etc/gitconfig` (Linux/macOS) or `C:\ProgramData\Git\config` (Windows).
    -   Requires administrator/root privileges to modify.
    -   Use case: Setting system-wide defaults or policies.

2.  **Global Level (User Level):** (`--global`)
    -   Applies to the **current user** and all their repositories.
    -   Stored in `~/.gitconfig` or `~/.config/git/config` (Linux/macOS) or `C:\Users\<User>\.gitconfig` (Windows).
    -   This is the most common level for setting personal preferences like user name, email, default editor, aliases.

3.  **Local Level (Repository Level):** (`--local` - Default if no level specified)
    -   Applies **only to the current repository**.
    -   Stored in `.git/config` within the repository.
    -   Use case: Setting repository-specific configurations (e.g., different user email for a specific project, remote URLs).

## Common Syntax

```bash
# List all configuration settings (merged from all levels)
git config --list

# List settings from a specific level
git config --list --system
git config --list --global
git config --list --local

# Get the value of a specific setting
git config <setting_name>
# Example: git config user.name

# Set a value for a specific setting (defaults to --local)
git config <setting_name> <value>

# Set a global setting
git config --global <setting_name> <value>

# Set a system setting (needs privileges)
git config --system <setting_name> <value>

# Edit configuration file directly
git config --edit [--global | --system | --local]

# Unset a configuration variable
git config --unset <setting_name> [--global | --system | --local]
```

## Essential Settings (Usually Set Globally)

```bash
# Set your identity (used in commit messages)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set your preferred text editor
git config --global core.editor "vim" # or "nano", "code --wait", etc.

# Set default branch name (recommended: main)
git config --global init.defaultBranch main

# Enable helpful coloring in output
git config --global color.ui auto
```

## Examples

**Example 1: Set global user email**
```bash
git config --global user.email "my_actual_email@domain.com"
```

**Example 2: Check the configured editor**
```bash
git config core.editor
```

**Example 3: Set a local config for a specific repository**
```bash
# Inside my-work-project/
git config user.email "work.email@company.com"
```
*Commits made in this repository will now use the work email, while commits in other repositories will use the global email.*

**Example 4: Create a Git alias**
```bash
# Create 'st' as a shortcut for 'status'
git config --global alias.st status
# Now you can run 'git st' instead of 'git status'
```

## Related Commands/Concepts
- [[Git]]
- [[Repository]] (Local config stored in `.git/config`)
- [[git_commit]] (Uses `user.name` and `user.email` config)
- Aliases, Editor choice, Merge tool config, Color settings

---
**Source:** Worksheet WS2