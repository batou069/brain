---
tags:
  - algorithms
  - concept
  - sorting
  - property
aliases:
  - Stable Sort
  - Sorting Stability
related:
  - "[[Sorting_Algorithms]]"
  - "[[60_Algorithms/Comparison_Sort]]"
  - "[[Bubble_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Merge_Sort]]"
  - "[[Counting_Sort]]"
  - "[[Radix_Sort]]"
  - "[[Quick_Sort]]"
  - "[[Heap_Sort]]"
  - "[[Selection_Sort]]"
worksheet:
  - WS25
date_created: 2025-04-21
---
# Stability (Sorting Algorithms)

## Definition

**Stability** is a property of [[Sorting_Algorithms]]. A sorting algorithm is considered **stable** if it preserves the **original relative order** of records (elements) that have **equal keys** (the value being sorted on). If two elements have the same key, a stable sort guarantees that they will appear in the same order in the sorted output as they appeared in the original input array.

## Importance

Stability is important when:

1.  **Sorting on Multiple Criteria:** If you sort data first by one key (e.g., sort employees by department) and then perform a *second* stable sort by another key (e.g., sort by name), the stability ensures that within each name group, the original department order is preserved. An unstable sort might scramble the department order for employees with the same name.
2.  **Maintaining Original Order:** Sometimes the original order of equal elements has some implicit meaning that needs to be retained.

## Example

**Input Data (Pairs of Value, Original Index):**
`(3, a), (2, b), (3, c), (1, d)`

**Sorting by Value:**

- **Stable Sort Output:** `(1, d), (2, b), (3, a), (3, c)`
  *(Note: `(3, a)` comes before `(3, c)` because 'a' came before 'c' in the original input)*

- **Unstable Sort Output (Possible):** `(1, d), (2, b), (3, c), (3, a)`
  *(Note: The relative order of the two '3' elements has been changed)*

## Stability of Common Algorithms

- **Stable:**
    - [[Bubble_Sort]] (if implemented carefully)
    - [[Insertion_Sort]]
    - [[Merge_Sort]]
    - [[Counting_Sort]]
    - [[Radix_Sort]] (if the underlying sort used, like Counting Sort, is stable)
    - Timsort (used in Python)
- **Not Stable (Generally):**
    - [[Selection_Sort]]
    - [[Heap_Sort]]
    - [[Quick_Sort]] (standard implementations are not stable)
    - Shellsort

*(Note: Unstable algorithms can sometimes be modified to become stable, often at the cost of extra space or complexity, e.g., by including the original index as part of the comparison key).*

## Related Concepts
- [[Sorting_Algorithms]]
- [[60_Algorithms/Comparison_Sort]], [[Non-comparison_Sort]]
- Keys (Values being sorted)
- Relative Order

---
**Source:** Worksheet WS25