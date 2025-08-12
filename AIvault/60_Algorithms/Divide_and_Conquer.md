---
tags:
  - algorithms
  - concept
  - technique
  - paradigm
  - recursion
aliases:
  - Divide and Conquer Algorithm
related:
  - "[[Algorithm]]"
  - "[[Recursion_C]]"
  - "[[Merge_Sort]]"
  - "[[Quick_Sort]]"
  - "[[Binary_Search]]"
  - "[[Time_Complexity]]"
  - "[[Master_Theorem]]" # For analyzing D&C recurrence relations
worksheet: [WS25]
date_created: 2025-04-21
---
# Divide and Conquer

## Definition

**Divide and Conquer (D&C)** is an algorithm design paradigm based on multi-branched [[Recursion_C|recursion]]. A divide-and-conquer algorithm works by recursively breaking down a problem into two or more smaller, self-similar subproblems, solving the subproblems recursively, and then combining their solutions to solve the original problem.

## General Steps

The process typically involves three steps at each recursive level:

1.  **Divide:** Break the given problem into smaller subproblems of the same (or related) type.
2.  **Conquer:** Solve the subproblems by calling the algorithm recursively. If the subproblems are small enough (reaching a [[Stop_Condition_C|base case]]), solve them directly.
3.  **Combine:** Combine the solutions of the subproblems to create the solution for the original problem.

## Key Aspects / Characteristics

- **Recursive Structure:** Naturally lends itself to recursive implementation.
- **Problem Decomposition:** Breaks large problems into more manageable pieces.
- **Efficiency:** Often leads to efficient algorithms, particularly when the divide and combine steps are relatively fast compared to solving the subproblems. [[Time_Complexity]] is often analyzed using recurrence relations (e.g., solvable by the [[Master_Theorem]]). Common complexities include O(n log n) and O(log n).
- **Parallelism:** Subproblems are often independent and can potentially be solved in parallel.

## Examples

- **[[Merge_Sort]]:**
    - *Divide:* Split the array into two halves.
    - *Conquer:* Recursively sort the two halves using Merge Sort.
    - *Combine:* Merge the two sorted halves into a single sorted array (O(n) step).
    - *Complexity:* O(n log n)
- **[[Quick_Sort]]:**
    - *Divide:* Partition the array around a pivot element, such that elements smaller than the pivot are to its left and larger elements are to its right.
    - *Conquer:* Recursively sort the subarrays to the left and right of the pivot using Quick Sort.
    - *Combine:* Trivial; the array is already sorted once the subarrays are sorted.
    - *Complexity:* O(n log n) average, O(n^2) worst.
- **[[Binary_Search]]:**
    - *Divide:* Compare the target value with the middle element of the sorted array.
    - *Conquer:* Recursively search either the left or right half (discarding the other half).
    - *Combine:* Trivial (result is found or not found).
    - *Complexity:* O(log n)
- **Closest Pair of Points:** Can be solved efficiently using D&C.
- **Strassen's Algorithm:** For faster matrix multiplication.
- **Fast Fourier Transform (FFT):**

## Related Concepts
- [[Algorithm]] Design Paradigms
- [[Recursion_C]] (Core implementation technique)
- [[Merge_Sort]], [[Quick_Sort]], [[Binary_Search]] (Classic D&C algorithms)
- [[Time_Complexity]], Recurrence Relations, [[Master_Theorem]] (Analysis tools)
- [[Dynamic_Programming]] (Another paradigm, often contrasted with D&C; DP solves overlapping subproblems by storing results).

---
**Source:** Worksheet WS25