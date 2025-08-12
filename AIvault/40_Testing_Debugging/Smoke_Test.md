---
tags:
  - testing
  - concept
  - type
  - build
aliases:
  - Smoke Testing
  - Build Verification Test
  - BVT
  - Sanity Check
related:
  - Software_Testing
  - Build_Process_C
  - CI_CD
  - Regression_Test
  - Acceptance_Test
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Smoke Test

## Definition

**Smoke Testing** (also known as Build Verification Testing - BVT, or sometimes informally as a sanity check) is a preliminary type of [[Software_Testing]] performed on a new software build to ensure its basic, critical functionalities work correctly and the build is stable enough for further, more rigorous testing (like [[Regression_Test|regression]] or [[System_Test|system testing]]). The name originates from hardware testing, where a new device was powered on to see if it started smoking (indicating a major problem).

## Key Aspects / Characteristics

- **Purpose:** Determine if the build is fundamentally stable and testable. Answers the question: "Does the build start and perform its most crucial functions without immediately crashing or failing?"
- **Scope:** Covers the most important, high-level functionalities. It is *not* exhaustive. Focuses on breadth rather than depth.
- **Timing:** Performed immediately after a new build is created and deployed to a test environment, *before* extensive testing begins.
- **Outcome:** A quick pass/fail decision. If the smoke test fails, the build is typically rejected and sent back to development without further testing, saving time and effort.
- **Automation:** Often automated as part of a [[CI_CD]] pipeline's build verification stage.
- **Subset of Tests:** Smoke tests usually consist of a small subset of critical test cases drawn from the main test suite, covering core features like startup, login, main navigation, key transactions, etc.

## Advantages

- Provides rapid feedback on build stability.
- Saves testing effort by quickly identifying and rejecting unstable builds.
- Increases confidence before committing to more time-consuming test cycles.
- Fits well into automated [[CI_CD]] processes.

## Disadvantages

- Does not provide deep testing coverage.
- Will not find subtle or detailed bugs.
- Passing a smoke test only indicates basic stability, not overall quality or correctness.

## Related Concepts
- [[Software_Testing]]
- [[Build_Process_C]], [[CI_CD]] (Context where smoke tests are crucial)
- [[Regression_Test]], [[System_Test]], [[Acceptance_Test]] (More detailed testing that follows a successful smoke test)
- Sanity Check (Similar concept, sometimes used interchangeably, though sanity checks might be slightly less formal or narrower in scope).

---
**Source:** Worksheet WS_Testing