---
tags: [version_control, git, concept, workflow, issue]
aliases: [Conflict]
related:
  - "[[Git]]"
  - "[[Merging]]"
  - "[[Branching]]"
  - "[[git_merge]]"
  - "[[git_rebase]]"
  - "[[git_status]]"
  - "[[git_diff]]"
worksheet: [WS15]
date_created: 2025-04-11
---
# Merge Conflict

## Definition

In [[Git]], a **Merge Conflict** occurs during a [[Merging|merge]] (or [[git_rebase|rebase]]) operation when Git cannot automatically resolve differences in code between the two branches being integrated. This typically happens when the same lines in the same file have been modified differently on both branches since they diverged.

## Key Aspects / Characteristics

- **Automatic Merge Failure:** 
	- Git successfully merges parts it can figure out but stops when it encounters conflicting changes it cannot reconcile automatically.
- **Conflict Markers:** 
	- Git modifies the affected file(s) to include conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) indicating the differing content from both branches involved.
- **Manual Resolution Required:** 
	- The user must manually edit the conflicted file(s) to resolve the differences, choosing which version to keep, combining them, or writing something entirely new.
- **Staging Resolution:** 
	- After editing the file(s) to resolve the conflict and removing the markers, the user must stage the resolved file using [[git_add]].
- **Completing the Merge:** 
	- Once all conflicts are resolved and staged, the merge can be completed by running [[git_commit]] (if it was a standard merge) or `git rebase --continue` (if it was during a rebase).

## Examples / Use Cases

- Branch A changes line 5 of `config.txt` to `timeout = 10`.
- Branch B changes line 5 of `config.txt` to `timeout = 30`.
- Merging Branch B into Branch A results in a conflict on line 5 of `config.txt`. The file will look something like:

```
<<<<<<< HEAD
timeout = 10

timeout = 30
```
- The user must edit the file to contain the desired final version (e.g., `timeout = 20`), remove the markers, `git add config.txt`, and then `git commit`.

## Related Concepts
- [[Git]] (The VCS)
- [[Merging]], [[git_rebase]] (Operations where conflicts occur)
- [[Branching]] (Conflicts arise from divergent branches)
- [[git_merge]], `git rebase --continue` (Commands involved)
- [[git_status]], [[git_diff]] (Commands to identify conflicted files)
- [[git_add]] (Command to mark conflicts as resolved)

## Questions / Further Study
>[!question] How can merge conflicts be minimized?
> - **Commit Often:** Smaller, focused commits reduce the chance of large conflicts.
> - **Pull/Rebase Frequently:** Regularly integrate changes from the main branch into your feature branch to resolve smaller conflicts sooner.
> - **Communicate:** Talk to teammates about what parts of the codebase you are working on.
> - **Modular Code:** Well-structured, modular code reduces the likelihood that different features will modify the exact same lines.

---
**Source:** Worksheet WS15