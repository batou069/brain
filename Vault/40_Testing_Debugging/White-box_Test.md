---
tags:
  - testing
  - concept
  - technique
aliases:
  - White-box Testing
  - Structural Testing
  - Glass-box Testing
  - Code-based Testing
related:
  - Black-box_Test
  - Gray-box_Testing
  - Software_Testing
  - Code_Coverage
  - Statement_Coverage
  - Branch_Coverage
  - Path_Coverage
  - Unit_Test
  - Integration_Test
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# White-box Testing

## Definition

**White-box Testing** (also known as structural, glass-box, or code-based testing) is a software testing technique where the tester designs test cases based on the **internal structure, design, and code** of the software component being tested. The tester has knowledge of the source code, algorithms, control flow, and data structures.

## Key Aspects / Characteristics

- **Focus:** Internal logic, code paths, conditions, loops, data flow. Aims to verify that internal operations perform according to specification and that all internal components have been adequately exercised.
- **Perspective:** Tests from a developer's perspective.
- **Basis:** Source code, detailed design documents, control flow graphs.
- **Requires Code Knowledge:** Tester needs programming skills and access to the source code.
- **Applicability:** Primarily used during [[Unit_Test|unit testing]] and [[Integration_Test|integration testing]] by developers.
- **Coverage Metrics:** Often guided by [[Code_Coverage|code coverage]] metrics:
    - Statement Coverage: Ensure every statement is executed.
    - Branch/Decision Coverage: Ensure every branch (e.g., true/false paths of an `if` statement) is executed.
    - Path Coverage: Ensure every possible execution path through a function is tested (often infeasible).
    - Condition Coverage: Ensure each boolean sub-expression in a condition evaluates to both true and false.
- **Techniques:** Test cases are designed to exercise specific code paths, conditions, loops, and data structures.

## Advantages

- Can find hidden errors in code paths not easily reachable through black-box techniques.
- Allows for thorough testing of logic and conditions.
- Facilitates optimization by revealing inefficient code.
- Enables quantifiable coverage measurement.

## Disadvantages

- Requires skilled programmers with knowledge of the code.
- Tests are tightly coupled to the implementation; changes in the code often require changes to the tests.
- Cannot directly detect missing requirements or specification errors (focus is on *existing* code).
- Testing all possible paths can be infeasible (path explosion).
- High coverage doesn't guarantee absence of defects or fulfillment of requirements.

## Related Concepts
- [[Black-box_Test]] (Tests based on external behavior)
- [[Gray-box_Testing]] (Combines aspects of black-box and white-box)
- [[Software_Testing]]
- [[Code_Coverage]] (Statement, Branch, Path, Condition Coverage)
- [[Unit_Test]], [[Integration_Test]] (Levels where white-box is common)

---
**Source:** Worksheet WS_Testing