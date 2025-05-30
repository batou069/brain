---
tags:
  - testing
  - concept
  - type
aliases:
  - Regression Testing
related:
  - Software_Testing
  - Unit_Test
  - Integration_Test
  - System_Test
  - Automation_Testing
  - CI_CD
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Regression Test

## Definition

**Regression Testing** is a type of [[Software_Testing]] performed after making code changes (e.g., bug fixes, enhancements, configuration changes, environment changes) to ensure that the modifications have **not** adversely affected existing, previously working functionality. It involves re-running previously executed test cases to detect unintended side effects, known as regressions.

## Key Aspects / Characteristics

- **Purpose:** Verify that code changes did not break existing features or introduce new defects in unchanged areas. Build confidence that changes are safe.
- **Trigger:** Performed whenever the software is modified.
- **Scope:** Can range from re-running a small subset of [[Unit_Test|unit tests]] related to the change, to re-running entire [[Integration_Test|integration]] or [[System_Test|system test]] suites.
- **Test Selection:** Choosing which tests to re-run is key. Options include:
    - *Retest All:* Re-run the entire existing test suite (most thorough but potentially time-consuming).
    - *Selective Regression Testing:* Analyze the changes and select only those test cases (related to the changed code or potentially affected areas) to re-run. Requires careful analysis.
    - *Risk-Based Selection:* Prioritize re-running tests covering the most critical or high-risk areas of the application.
- **Automation:** Regression testing is a prime candidate for test automation, as the same tests need to be run repeatedly. Automated regression suites are crucial for [[CI_CD]] pipelines.

## Importance

- **Prevents Re-introducing Bugs:** Ensures that fixing one bug doesn't accidentally bring back an old one or create a new one elsewhere.
- **Maintains Stability:** Helps maintain the stability and reliability of the software as it evolves.
- **Supports Refactoring:** Provides a safety net, allowing developers to refactor code with more confidence, knowing that regressions will likely be caught.

## Related Concepts
- [[Software_Testing]]
- [[Unit_Test]], [[Integration_Test]], [[System_Test]] (Regression tests exist at all levels)
- [[Automation_Testing]] (Essential for effective regression testing)
- [[CI_CD]] (Regression tests are a key part of the pipeline)
- Defect Fixing, Code Maintenance, Refactoring

---
**Source:** Worksheet WS_Testing