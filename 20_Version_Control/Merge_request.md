 ---
tags: 
  - version_control
  - git
  - concept
  - workflow
  - collaboration
  - platform
aliases: 
  - Pull Request
  - PR
  - MR
related: Git
  - Merging
  - Branching
  - Remote_repository
  - Code_review
  - GitHub
  - GitLab
  - Bitbucket
worksheet: WS15
date_created: 2025-04-21
---
# Merge Request / Pull Request

## Definition

A **Merge Request (MR)** (term used by GitLab) or **Pull Request (PR)** (term used by GitHub, Bitbucket) is a feature provided by Git hosting platforms that facilitates proposing and discussing changes before they are integrated ([[Merging|merged]]) into a target [[Branching|branch]] in a shared [[Remote_repository]]. It's a mechanism for [[Code_review]] and collaboration around code changes.

## Key Aspects / Characteristics

- **Proposal for Integration:** A developer creates an MR/PR to notify collaborators that they have completed work on a branch and want it merged into another branch (e.g., merging `feature/x` into `main`).
- **Code Review Platform:** Provides a web interface to view the proposed changes (diffs), leave comments line-by-line or overall, discuss the implementation, and request modifications.
- **Discussion & Iteration:** Facilitates discussion among team members. The author can push further commits to the source branch to address feedback, and these updates automatically appear in the MR/PR.
- **Automated Checks:** Often integrated with [[CI/CD]] pipelines to automatically run tests, linters, and other checks on the proposed changes.
- **Approval & Merging:** Designated reviewers can approve the changes. Once approved (and checks pass), a maintainer can often merge the changes directly through the web interface (which performs a `git merge` or `git rebase` on the server).
- **Not a Core Git Feature:** MRs/PRs are features of hosting platforms (like [[GitHub]], [[GitLab]]), not part of the core Git software itself.

## Examples / Use Cases

- A developer finishes work on a feature branch (`dev/feature-a`) pushed to the shared remote repository.
- They open a Pull Request on GitHub targeting the `main` branch.
- Other team members review the code, leave comments, and request changes.
- The developer pushes fixes to `dev/feature-a`.
- Once approved and tests pass, a maintainer clicks the "Merge" button on GitHub.

## Related Concepts
- [[Git]] (The underlying VCS)
- [[Merging]] (The action the MR/PR ultimately facilitates)
- [[Branching]] (MRs/PRs typically propose merging one branch into another)
- [[Remote_repository]] (Where the shared code and MR/PRs are hosted)
- [[Code_review]] (The primary purpose of MRs/PRs)
- [[GitHub]], [[GitLab]], [[Bitbucket]] (Platforms providing MR/PR functionality)
- [[CI/CD]] (Often integrated with MRs/PRs for automated checks)

---
**Source:** Worksheet WS15

    