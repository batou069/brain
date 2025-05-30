---
tags:
  - data_structures
  - algorithms
  - complexity
  - analysis
  - performance
aliases:
  - Execution Time Complexity
related:
  - "[[Computational_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Big_O_Notation]]"
  - "[[Algorithm_Analysis]]"
  - "[[Performance]]"
worksheet:
  - WS7
date_created: 2025-04-12
---
# Time Complexity

## Definition

**Time Complexity** is a measure within [[Computational_Complexity|computational complexity analysis]] that quantifies the amount of **time** an algorithm takes to run as a function of the length or size of its input (`n`). It's typically expressed using [[Big_O_Notation|asymptotic notation]] (like Big O) to describe the growth rate of the execution time as the input size increases, rather than measuring exact seconds (which depend on hardware, compiler, etc.).

## Key Aspects

- **Measures Execution Time Growth:** Focuses on how the runtime scales with input size.
- **Abstract Units:** Time is usually measured in terms of the number of elementary operations performed (e.g., comparisons, assignments, arithmetic operations), assuming each takes constant time.
- **Input Size (`n`):** The parameter against which time is measured (e.g., number of elements in an array, number of nodes in a tree).
- **Asymptotic Analysis:** Ignores constant factors and lower-order terms, focusing on the dominant term as `n` approaches infinity (e.g., `O(n)`, `O(n log n)`, `O(n^2)`).
- **Worst-Case, Average-Case, Best-Case:**
    - *Worst-Case (Big O):* Maximum time taken for any input of size `n`. Most common analysis.
    - *Average-Case (Theta often used):* Expected time taken over all possible inputs of size `n`. Can be hard to calculate accurately.
    - *Best-Case (Omega):* Minimum time taken for any input of size `n`. Less commonly used.
- **Goal:** Understand how efficient an algorithm is in terms of time and how well it will perform on large inputs.

## Examples

- Linear search in an array: O(n) worst-case time.
- Binary search in a sorted array: O(log n) worst-case time.
- Accessing an array element by index: O(1) time.
- Bubble sort: O(n^2) worst-case time.
- Merge sort: O(n log n) worst-case time.

## Related Concepts
- [[Computational_Complexity]]
- [[Space_Complexity]] (The other main resource measured)
- [[Big_O_Notation]] (Common notation used)
- [[Algorithm_Analysis]]
- [[Performance]] (Time complexity is a major factor in performance)

---
**Source:** Worksheet WS7