---
tags:
  - testing
  - concept
  - type
aliases:
  - Progression Testing
  - New Feature Testing
related:
  - Software_Testing
  - Regression_Test
  - Functional_Requirement
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Progression Tests

## Definition

**Progression Testing** refers to testing performed to verify that **newly added features or functionalities** work as specified, or that changes made to existing functionality meet the new requirements. It focuses on testing the *progress* made in the software development.

## Key Aspects / Characteristics

- **Focus:** New features, enhancements, changed functionality.
- **Purpose:** Verify that the new or modified code meets its specific requirements.
- **Contrast with Regression:** While [[Regression_Test|regression testing]] checks that *old* functionality hasn't broken, progression testing checks that *new* functionality works correctly.
- **Timing:** Occurs after new code or modifications have been implemented.
- **Basis:** Requirements and specifications for the new or changed features.

## Relationship with Other Testing

- Progression testing often involves writing new [[Test_Case|test cases]] specifically designed for the new features.
- These new test cases, once they pass and the feature is considered stable, often become part of the suite used for future [[Regression_Test|regression testing]].
- It can occur at various levels ([[Unit_Test]], [[Integration_Test]], [[System_Test]]).

## Example

- A new "Password Reset" feature is added to a website.
- **Progression Testing:** Involves executing test cases specifically designed to verify the password reset workflow (e.g., requesting a reset link, receiving the email, clicking the link, entering a new password, confirming the change, attempting login with the new password).
- **Regression Testing (done afterwards or concurrently):** Involves re-running existing tests for login, registration, profile updates, etc., to ensure the password reset changes didn't break those other features.

## Related Concepts
- [[Software_Testing]]
- [[Regression_Test]] (The complementary activity)
- [[Functional_Requirement]] (Progression tests verify these)
- [[Test_Case]]

---
**Source:** Worksheet WS_Testing