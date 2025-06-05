---
tags:
  - algorithms
  - concept
  - analysis
  - complexity
aliases:
  - Best Case Complexity
  - Worst Case Complexity
  - Average Case Complexity
related:
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Algorithm_Analysis]]"
  - "[[Big_O_Notation]]" # Often Worst Case
  - "[[Omega_Notation]]" # Often Best Case
  - "[[Theta_Notation]]" # Often Average Case or Tight Bound
worksheet: [WS25]
date_created: 2025-04-21
---
# Best, Worst, and Average Case Analysis

## Definition

When analyzing the [[Computational_Complexity|complexity]] (usually [[Time_Complexity]]) of an algorithm, we often consider its performance under different input scenarios relative to the input size `n`:

1.  **Best Case:** The scenario or specific input(s) of size `n` for which the algorithm performs the **minimum** number of operations. It provides a lower bound on the algorithm's runtime. Often denoted using Big Omega (`Ω`) notation.
2.  **Worst Case:** The scenario or specific input(s) of size `n` for which the algorithm performs the **maximum** number of operations. It provides an upper bound guarantee on the runtime – the algorithm will never take longer than this. Often denoted using Big O (`O`) notation.
3.  **Average Case:** The expected number of operations performed averaged over **all possible inputs** of size `n`, assuming a certain probability distribution for the inputs (often assumed to be uniform). It aims to describe the typical behavior. Often denoted using Big Theta (`Θ`) notation if the average is tightly bounded, or sometimes Big O (`O`).

## Importance

- **Worst Case:** Crucial for applications requiring performance guarantees (real-time systems). Tells us the maximum resources the algorithm might need.
- **Average Case:** Often reflects the practical performance experienced when running the algorithm on typical data. Can be harder to calculate accurately as it requires assumptions about input distribution.
- **Best Case:** Less practically useful, but helps understand the full range of the algorithm's behavior. An algorithm might have a very good best case but a terrible worst or average case.

## Examples

**1. Linear Search (Searching for `key` in an array of size `n`)**
    - **Best Case:** `key` is the first element checked. O(1).
    - **Worst Case:** `key` is the last element checked, or not present at all. O(n).
    - **Average Case:** `key` is found roughly halfway through on average (assuming uniform probability). O(n).

**2. [[Quick_Sort]]**
    - **Best Case:** Pivots always partition the array perfectly in half. O(n log n).
    - **Worst Case:** Pivots are always the smallest or largest element (e.g., array is already sorted or reverse sorted, and naive pivot selection is used). Leads to highly unbalanced partitions. O(n^2).
    - **Average Case:** Pivots chosen randomly or using good strategies (like median-of-three) lead to balanced partitions on average. O(n log n).

**3. [[Insertion_Sort]]**
    - **Best Case:** Array is already sorted. O(n) (only needs one pass).
    - **Worst Case:** Array is sorted in reverse order. O(n^2).
    - **Average Case:** O(n^2).

## Related Concepts
- [[Computational_Complexity]], [[Time_Complexity]], [[Space_Complexity]]
- [[Algorithm_Analysis]]
- [[Big_O_Notation]] (Worst-case upper bound)
- [[Omega_Notation]] (Best-case lower bound)
- [[Theta_Notation]] (Tight bound, often used for average case)

---
**Source:** Worksheet WS25