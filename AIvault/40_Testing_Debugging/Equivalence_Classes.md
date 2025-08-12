---
tags:
  - testing
  - concept
  - technique
  - black-box
  - test_design
aliases:
  - Equivalence Partitioning
  - EC
related:
  - Boundary_Value_Analysis
  - Black-box_Test
  - Test_Case
  - Test_Data
  - Requirements
worksheet:
  - WS_Testing
date_created: 2025-04-14
---
# Equivalence Classes (Equivalence Partitioning)

## Definition

**Equivalence Partitioning** (or creating **Equivalence Classes**) is a [[Black-box_Test|black-box]] test design technique used to reduce the number of [[Test_Case|test cases]] required while maintaining reasonable coverage. It works by dividing the input data (or output data) domain of a software component into partitions or "classes" of data from which test cases can be derived. The assumption is that all values within a given equivalence class will be processed **in the same way** by the software, so testing just one representative value from each class is sufficient to cover that class.

## Key Aspects / Characteristics

- **Partitioning:** Input/output domains are divided into groups (classes) where the system's behavior is expected to be equivalent for all members of a group.
- **Assumption:** If one value in a class works correctly, all other values in that class are assumed to work correctly. If one value in a class reveals a defect, other values in that class are likely to reveal the same defect.
- **Test Case Reduction:** Significantly reduces the number of test cases needed compared to testing every possible input value.
- **Basis:** Derived from requirements and specifications defining input ranges, types, and expected behaviors.
- **Types of Classes:** Partitions are identified for:
    - **Valid Inputs:** Classes representing expected, acceptable inputs.
    - **Invalid Inputs:** Classes representing erroneous, unexpected, or unacceptable inputs (e.g., out-of-range values, incorrect formats, nulls).
- **Coverage:** Aims to select at least one test case to cover each identified equivalence class.

## How to Identify Classes

1.  **Input Ranges:** If an input specifies a range (e.g., age 18-65), identify classes: below the range (<18), within the range (18-65), above the range (>65).
2.  **Specific Values:** If an input must be one of a set of specific values (e.g., color = RED, GREEN, BLUE), identify classes: one for each valid value, and one for an invalid value (e.g., YELLOW).
3.  **Boolean Conditions:** If an input is a boolean, identify classes: True, False.
4.  **Number of Items:** If a certain number of items must be processed (e.g., 1 to 10 items), identify classes: zero items, one item, multiple items within range, more items than allowed.
5.  **Different Processing:** Any input or condition that suggests different handling by the software defines a boundary between classes.

## Example

**Requirement:** A function accepts an integer percentage discount between 0 and 100 (inclusive).

**Equivalence Classes:**
- **Valid:**
    - EC1: Integer between 0 and 100 (e.g., choose `50`)
- **Invalid:**
    - EC2: Integer less than 0 (e.g., choose `-10`)
    - EC3: Integer greater than 100 (e.g., choose `110`)
    - EC4: Non-integer input (e.g., choose `abc`, `5.5` - *if input method allows*)

**Test Cases Derived:** Test with `-10`, `50`, `110`, and potentially non-integer input if applicable.

## Related Concepts
- [[Boundary_Value_Analysis]] (Often used in conjunction with EC)
- [[Black-box_Test]] (EC is a black-box technique)
- [[Test_Case]] Design
- [[Test_Data]] Selection
- [[Requirements]] Analysis

---
**Source:** Worksheet WS_Testing