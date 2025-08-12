---
tags: [version_control, git, command, release, pointer]
aliases: []
related:
  - "[[Git]]"
  - "[[Commit_object]]"
  - "[[Repository]]"
  - "[[git_push]]"
  - "[[git_log]]"
  - "[[Semantic_Versioning]]"
worksheet: [WS15]
date_created: 2025-04-21
---
# ` git tag `

## Purpose

The `git tag` command is used to create, list, or delete tags. Tags are typically used to mark specific points in the [[Repository]]'s history as being important, often corresponding to release versions (e.g., `v1.0`, `v2.1.3`). Tags act as human-readable, fixed pointers to specific [[Commit_object|commits]].

## Syntax

```bash
# List existing tags
git tag

# List tags matching a pattern
git tag -l "v1.*"

# Create a lightweight tag pointing to the current commit (HEAD)
git tag <tag_name>

# Create a lightweight tag pointing to a specific commit
git tag <tag_name> <commit_hash>

# Create an annotated tag pointing to the current commit (Recommended for releases)
git tag -a <tag_name> -m "<tag_message>"

# Create an annotated tag pointing to a specific commit
git tag -a <tag_name> <commit_hash> -m "<tag_message>"

# View information about a tag (especially annotated tags)
git show <tag_name>

# Delete a local tag
git tag -d <tag_name>

# Push a specific tag to a remote repository
git push <remote_name> <tag_name>

# Push all local tags to a remote repository
git push <remote_name> --tags
```


## Common Options

| Option         | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| -l \<pattern>  | List tags matching the given glob pattern.                                               |
| -a, --annotate | Create an annotated tag object (includes tagger, date, message, optional GPG signature). |
| -m /<message>  | Provide the message for an annotated tag.                                                |
| -s             | Create a GPG-signed tag (implies -a).                                                    |
| -d, --delete   | Delete the specified local tag.                                                          |
| -v, --verify   | Verify the GPG signature of a tag.                                                       |

## Examples

**Example 1: Create a lightweight tag for the current commit**

```bash
git tag v0.9-beta
```

**Example 2: Create an annotated tag for a release**

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"`
```
This is the recommended way for marking releases as it stores extra metadata.

**Example 3: Tag an older commit**

```bash
# Find the commit hash from the log 
git log --oneline
# a1b2c3d Fix critical bug 
# ...  # Tag that specific commit 
git tag -a v0.9.1 a1b2c3d -m "Version 0.9.1 - Critical bugfix release"
```

**Example 4: Push tags to remote**

```bash
# Push a single tag
git push origin v1.0.0

# Push all local tags not yet on the remote
git push origin --tags
```

## Related Commands/Concepts

- [[Commit_object]] (Tags point to commits)
- [[Repository]] (Tags are stored within the repository)
- [[git_push]] (Needed to share tags with remote repositories)
- [[git_log]] (Can show tags associated with commits
- [[Semantic_Versioning]] (A common convention for naming release tags)
- Lightweight vs. Annotated Tags (Two types of tags)


## Notes

> [!note] Lightweight vs. Annotated Tags
> 
> - **Lightweight:** Just a pointer to a commit, like a branch that doesn't move. Contains only the commit hash. Good for temporary or private markers.
>     
> - **Annotated:** Full objects in the Git database. Contain the tagger's name, email, date, a tagging message, and can be GPG signed. They are generally recommended for public releases or important milestones as they contain more information. git show <tagname> displays this extra info for annotated tags.


> [!note] Pushing Tags  
> By default, git push does not transfer tags to the remote repository. You must explicitly push tags using git push origin <tag_name> or git push origin --tags.

---

**Source:** Worksheet WS15