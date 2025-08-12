---
tags:
  - testing
  - concept
  - level
  - technique
aliases:
  - Unit Testing
related:
  - Software_Testing
  - Integration_Test
  - White-box_Test
  - Test_Case
  - Stubs
  - Mocks
  - Test_Framework
  - TDD
  - PyUnit
  - Pytest
  - JUnit
worksheet:
  - WS_Testing
  - WS24
date_created: 2025-04-14
---
# Unit Test

## Definition

**Unit Testing** is a level of [[Software_Testing]] where individual, isolatable components or units of source code (typically functions, methods, classes, or modules) are tested in isolation from the rest of the system to determine if they behave correctly.

## Key Aspects / Characteristics

- **Focus:** Smallest testable parts of the software.
- **Isolation:** The unit under test is isolated from its dependencies (e.g., other classes, database, network services) using [[Stubs]], [[Mocks]], or other test doubles. This ensures that the test verifies the unit itself, not its collaborators.
- **Automation:** Unit tests are almost always automated using a testing framework (e.g., [[PyUnit]]/`unittest`, [[Pytest]] for Python; JUnit for Java; NUnit for .NET; Google Test for C++).
- **Developer Responsibility:** Typically written and executed by the developers of the code being tested, often alongside the development process ([[Test-Driven_Development|TDD]]).
- **Speed:** Automated unit tests are usually very fast to execute, allowing them to be run frequently (e.g., on every build or commit).
- **Techniques:** Often employs [[White-box_Test|white-box testing]] techniques (as developers know the code), but can also use [[Black-box_Test|black-box techniques]] based on the unit's specification.
- **Goal:** Verify that each unit works correctly in isolation, catch bugs early, provide documentation for the unit's behavior, and facilitate refactoring by providing a safety net ([[Regression_Test]]).

## Advantages

- Finds bugs early in the development cycle when they are cheapest to fix.
- Acts as executable documentation for code units.
- Provides a safety net for refactoring and code changes (regression detection).
- Encourages modular and testable design.
- Fast execution allows for frequent feedback.

## Disadvantages

- Does not test the integration between units.
- Can require significant effort to write and maintain, especially setting up isolation (mocks/stubs).
- May not catch higher-level system or usability issues.
- Can sometimes lead to testing trivial code or focusing too much on implementation details.

## Quality Requirements (WS24)

- **Fast:** Should run quickly to provide rapid feedback.
- **Independent/Isolated:** Tests should not depend on each other or external systems; they should be runnable in any order.
- **Repeatable:** Should produce the same result every time they are run (given the same code). Avoid dependencies on time, random numbers, or unstable external factors.
- **Self-Validating:** Test should automatically determine if it passed or failed without manual inspection (e.g., using [[Assertions]]).
- **Timely/Thorough (from FIRST principles):** Tests should be written timely (ideally alongside or before the code - TDD) and be thorough enough to cover important logic, boundary conditions, and expected failure modes of the unit.

## Related Concepts
- [[Software_Testing]] Levels ([[Integration_Test]], [[System_Test]])
- [[White-box_Test]], [[Black-box_Test]]
- [[Test_Frameworks]] ([[PyUnit]], [[Pytest]], JUnit, etc.)
- Test Doubles ([[Stubs]], [[Mocks]], [[Dummies]], [[Fakes]])
- [[Test-Driven_Development]] (TDD)
- [[Assertions]]
- [[Regression_Test]]

## Questions / Further Study
>[!question] What should you check in your unit testing? (WS24)
> Unit tests should primarily check:
> - **Correctness:** Does the unit produce the expected output for given inputs?
> - **Boundary Conditions:** How does the unit behave with edge-case inputs (e.g., zero, null, empty strings, min/max values)?
> - **Error Handling:** Does the unit handle expected error conditions gracefully (e.g., throwing exceptions, returning error codes)?
> - **Logic Paths:** Have important conditional logic paths within the unit been exercised? (Often guided by [[Code_Coverage]]).
> - **State Changes:** If the unit modifies state (e.g., an object's member variables), are the changes correct?

---
**Source:** Worksheet WS_Testing, WS24