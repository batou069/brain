---
tags:
  - testing
  - concept
  - metric
  - quality
aliases:
  - Code Coverage
  - Test Coverage Analysis
related:
  - Software_Testing
  - White-box_Test
  - Unit_Test
  - Test_Case
  - Statement_Coverage
  - Branch_Coverage
  - Path_Coverage
  - Condition_Coverage
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Test Coverage

## Definition

**Test Coverage** is a metric used in [[Software_Testing]] to describe the degree to which the source code of a program has been executed or exercised by a particular test suite. It helps assess the thoroughness of testing by identifying areas of the software that have not been tested. While often associated with [[White-box_Test|white-box testing]], coverage concepts can also apply at higher levels (e.g., requirements coverage).

## Key Aspects / Characteristics

- **Measurement:** Quantifies the extent of testing based on specific criteria.
- **Purpose:**
    - Identify gaps in testing (untested code).
    - Provide a measure of test suite thoroughness (though not necessarily effectiveness).
    - Help prioritize additional testing efforts.
- **Code Coverage Criteria (Common):**
    - **Statement Coverage:** Percentage of executable statements in the source code executed by tests.
    - **Branch/Decision Coverage:** Percentage of branches (e.g., true/false outcomes of `if` or `while` conditions) executed by tests. Generally considered stronger than statement coverage.
    - **Path Coverage:** Percentage of possible execution paths through a function or program executed by tests. Often infeasible to achieve 100% due to the potentially huge number of paths.
    - **Condition Coverage:** Checks if each boolean sub-expression within a compound condition has been evaluated to both true and false. Variations include Modified Condition/Decision Coverage (MC/DC), important in safety-critical systems.
    - **Function Coverage:** Percentage of functions/methods called by tests.
- **Tools:** Code coverage is typically measured using specialized tools (e.g., `gcov`/`lcov` for C/C++, `coverage.py` for Python, JaCoCo for Java) that instrument the code or analyze execution traces.
- **Interpretation:** High coverage (e.g., 80-90% branch coverage) indicates that most of the code has been executed by tests, but it **does not guarantee** the absence of defects. Tests might execute code without actually verifying its correctness under all conditions. Low coverage clearly indicates inadequate testing.
- **Goal Setting:** Coverage targets are often set (e.g., "achieve 85% branch coverage"), but aiming for 100% might be impractical or yield diminishing returns. Focus should be on covering critical and complex code adequately.

## Example

If a function has an `if-else` statement, 100% statement coverage might be achieved by a single test case that goes through the `if` block. However, 100% branch coverage would require at least two test cases: one where the condition is true (executing the `if` block) and one where it's false (executing the `else` block).

## Related Concepts
- [[Software_Testing]], [[White-box_Test]], [[Unit_Test]]
- [[Test_Case]] (Coverage is achieved by running test cases)
- Coverage Criteria: Statement, Branch, Path, Condition, Function Coverage
- Coverage Tools (`gcov`, `coverage.py`, etc.)
- [[Quality_Assurance]] (Coverage is one quality metric)

---
**Source:** Worksheet WS_Testing