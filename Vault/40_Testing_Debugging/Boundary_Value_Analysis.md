---
tags:
  - testing
  - concept
  - technique
  - black-box
  - test_design
aliases:
  - Boundary Testing
  - BVA
related:
  - Equivalence_Classes
  - Black-box_Test
  - Test_Case
  - Test_Data
  - Requirements
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Boundary Value Analysis (BVA)

## Definition

**Boundary Value Analysis (BVA)** is a [[Black-box_Test|black-box]] test design technique that focuses on testing at the "edges" or boundaries of input (or output) equivalence partitions. Experience shows that errors often occur at these boundaries (e.g., using `<` instead of `<=`, off-by-one errors). BVA complements [[Equivalence_Classes|Equivalence Partitioning]] by selecting test cases specifically at the edges of the identified classes.

## Key Aspects / Characteristics

- **Focus on Edges:** Concentrates testing effort on the boundary values of input/output domains.
- **Assumption:** Errors are more likely to occur at the boundaries of equivalence classes than in the "middle" of a class.
- **Complements Equivalence Partitioning:** BVA test cases are derived from the boundaries of the equivalence classes identified using Equivalence Partitioning.
- **Test Case Selection:** For a given range or partition [min, max]:
    - **Two-Value BVA (Common):** Test `min`, `max`, `min-1`, `max+1`.
    - **Three-Value BVA:** Test `min`, `max`, `min+1`, `max-1`, `min-1`, `max+1`. (Also tests values just inside the boundary).
- **Applies To:** Ordered ranges (numbers, dates, character sequences), counts, loops, etc.

## Example

**Requirement:** A function accepts an integer percentage discount between 0 and 100 (inclusive).

**Equivalence Classes:**
- Invalid: < 0
- Valid: [0, 100]
- Invalid: > 100

**Boundary Values for the Valid Range [0, 100]:**
- Minimum: 0
- Maximum: 100

**Test Cases Derived using BVA (Two-Value):**
- Test `min-1`: `-1` (Covers invalid class < 0)
- Test `min`: `0` (Lower boundary of valid class)
- Test `max`: `100` (Upper boundary of valid class)
- Test `max+1`: `101` (Covers invalid class > 100)

**(Optional Three-Value BVA adds):**
- Test `min+1`: `1` (Just inside lower boundary)
- Test `max-1`: `99` (Just inside upper boundary)

Combining with a mid-range value from Equivalence Partitioning (e.g., 50) gives a good set of tests: `-1, 0, 1, 50, 99, 100, 101`.

## Related Concepts
- [[Equivalence_Classes]] (BVA tests the boundaries of these classes)
- [[Black-box_Test]] (BVA is a black-box technique)
- [[Test_Case]] Design
- [[Test_Data]] Selection
- [[Requirements]] Analysis

---
**Source:** Worksheet WS_Testing