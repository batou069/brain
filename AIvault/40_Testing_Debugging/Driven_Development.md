---
tags:
  - testing
  - concept
  - technique
  - development_methodology
  - agile
aliases:
  - TDD
  - Test-driven Design
related:
  - Unit_Test
  - Refactoring
  - Agile_Development
  - Red_Green_Refactor
  - Test_Framework
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Test-Driven Development (TDD)

## Definition

**Test-Driven Development (TDD)** is a software development process where developers write **automated tests** (typically [[Unit_Test|unit tests]]) **before** they write the production code required to make those tests pass. It follows a short, iterative cycle known as "Red-Green-Refactor".

## The TDD Cycle (Red-Green-Refactor)

1.  **Red:** Write a small, automated test case for a specific piece of desired functionality. Run the test; it should **fail** because the corresponding production code doesn't exist yet (or doesn't implement the feature correctly). This ensures the test is actually testing something and can fail.
2.  **Green:** Write the **minimum amount** of production code necessary to make the failing test pass. The focus here is solely on passing the test, not necessarily on writing perfect or elegant code yet. Run all tests; they should now pass.
3.  **Refactor:** Improve the production code written in the "Green" step (and potentially the test code) by removing duplication, improving clarity, enhancing design, and optimizing performance, while ensuring all tests **continue to pass**.

This cycle is repeated for each small piece of functionality.

## Key Aspects / Characteristics

- **Test-First Approach:** Tests are written before the code they verify.
- **Short Iterations:** The Red-Green-Refactor cycle is very short, often measured in minutes.
- **Focus on Requirements:** Each test defines a small requirement or behavior the code must fulfill.
- **Safety Net:** Creates a comprehensive suite of regression tests automatically as development progresses.
- **Drives Design:** Writing tests first often encourages developers to create more modular, decoupled, and testable designs, as they have to consider how to instantiate and test components in isolation.
- **Executable Specification:** The test suite acts as a detailed, executable specification of the system's behavior at the unit level.

## Advantages

- Leads to high [[Test_Coverage]] naturally.
- Provides rapid feedback on code changes.
- Creates a robust [[Regression_Test|regression testing]] suite.
- Encourages better, more testable code design.
- Improves developer confidence when changing or refactoring code.
- Can serve as documentation.

## Disadvantages

- Can have a steeper learning curve initially.
- Might feel slower at the very beginning of a project.
- Requires discipline to stick to the cycle.
- May not be as suitable for all types of development (e.g., exploratory programming, GUI testing can be harder).
- Doesn't eliminate the need for other forms of testing (integration, system, acceptance).

## Related Concepts
- [[Unit_Test]] (The primary type of test written in TDD)
- [[Refactoring]] (A core step in the TDD cycle)
- [[Agile_Development]] (TDD is a common practice in Agile methodologies)
- Red-Green-Refactor (The TDD mantra)
- [[Test_Framework]] (Tools used to write and run TDD tests)

---
**Source:** Worksheet WS_Testing