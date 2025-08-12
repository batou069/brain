---
tags:
  - algorithms
  - concept
  - sorting
  - comparison_sort
  - non-comparison_sort
aliases:
  - Sorting Algorithm Overview
related:
  - "[[Algorithm]]"
  - "[[Computational_Complexity]]"
  - "[[Time_Complexity]]"
  - "[[Space_Complexity]]"
  - "[[Best_Worst_Average_Case]]"
  - "[[Stability_Sorting]]"
  - "[[In-place_Algorithm]]"
  - "[[60_Algorithms/Comparison_Sort]]"
  - "[[Non-comparison_Sort]]"
  - "[[Bubble_Sort]]"
  - "[[Selection_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Merge_Sort]]"
  - "[[Quick_Sort]]"
  - "[[Heap_Sort]]"
  - "[[Counting_Sort]]"
  - "[[Radix_Sort]]"
  - "[[Bucket_Sort]]"
worksheet:
  - WS25
date_created: 2025-04-21
---
# Sorting Algorithms

## Definition

A **Sorting Algorithm** is an [[Algorithm]] that puts elements of a list or array into a certain **order** (e.g., numerical order, lexicographical order). Efficient sorting is important for optimizing the use of other algorithms (like binary search) and for producing human-readable output.

## Key Characteristics & Classification

Sorting algorithms are often classified and compared based on several characteristics:

- **[[Time_Complexity]]:** How the execution time scales with the number of items (`n`). Measured in [[Best_Worst_Average_Case|best, average, and worst-case]] scenarios (e.g., O(n^2), O(n log n)).
- **[[Space_Complexity]]:** The amount of extra memory space required (beyond the input array). [[In-place_Algorithm|In-place]] algorithms use O(1) or O(log n) auxiliary space.
- **[[Stability_Sorting|Stability]]:** A stable sort maintains the relative order of records with equal keys (values). Important if sorting data based on multiple criteria.
- **[[60_Algorithms/Comparison_Sort|Comparison vs. Non-comparison]]:**
    - *Comparison Sorts:* Determine order solely by comparing pairs of elements (using `<`, `>`, `=` operators). Their theoretical best worst-case time complexity is Ω(n log n).
    - *[[Non-comparison_Sort|Non-comparison Sorts]]:* Use assumptions about the data (e.g., integer keys within a known range) to sort without direct comparisons. Can achieve better than O(n log n) time complexity (e.g., O(n)) under specific conditions.
- **[[In-place_Algorithm|In-place vs. Out-of-place]]:** In-place algorithms rearrange items within the original array with minimal extra storage. Out-of-place algorithms require significant extra space (e.g., for a temporary array).
- **Recursive vs. Iterative:** Implementation strategy.
- **Adaptive:** Whether the algorithm performs better if the input is already partially sorted.

## Common Sorting Algorithms

**Comparison Sorts (Often O(n^2) or O(n log n)):**
- [[Bubble_Sort]]: Simple, inefficient (O(n^2)). Stable. In-place.
- [[Selection_Sort]]: Simple, inefficient (O(n^2)). Not stable. In-place.
- [[Insertion_Sort]]: Efficient for small or nearly sorted lists (O(n^2) worst/average, O(n) best). Stable. In-place. Adaptive.
- [[Merge_Sort]]: Efficient (O(n log n) always). Stable. Out-of-place (typically O(n) space). Not adaptive. [[Divide_and_Conquer]].
- [[Quick_Sort]]: Efficient on average (O(n log n)). Not stable. In-place (typically O(log n) stack space). Worst-case O(n^2) but rare with good pivot selection. [[Divide_and_Conquer]]. Often fastest in practice.
- [[Heap_Sort]]: Efficient (O(n log n) always). Not stable. In-place (O(1) space).

**Non-Comparison Sorts (Can be O(n) under constraints):**
- [[Counting_Sort]]: For integers within a fixed, small range. Stable. O(n+k) time, O(k) space (k=range size).
- [[Radix_Sort]]: Sorts based on individual digits/bits. Uses a stable subroutine like Counting Sort. O(d*(n+k)) time (d=digits, k=radix).
- [[Bucket_Sort]]: Distributes elements into buckets, sorts buckets, then concatenates. Efficient if input is uniformly distributed. Average O(n).

## Related Concepts
- [[Algorithm]], [[Computational_Complexity]]
- [[Time_Complexity]], [[Space_Complexity]], [[Best_Worst_Average_Case]]
- [[Stability_Sorting]], [[In-place_Algorithm]]
- [[60_Algorithms/Comparison_Sort]], [[Non-comparison_Sort]]
- [[Divide_and_Conquer]]

## Questions / Further Study
>[!question] What are the criteria For choosing between 2 sorting algorithms? (WS25)
> Key criteria include:
> 1.  **[[Time_Complexity]]:** Average, worst-case, and best-case performance needs based on expected input size. O(n log n) is generally preferred for large datasets over O(n^2).
> 2.  **[[Space_Complexity]]:** Memory constraints; is an [[In-place_Algorithm|in-place]] sort required (O(1) or O(log n) space), or is O(n) extra space acceptable?
> 3.  **[[Stability_Sorting|Stability]]:** Is preserving the relative order of equal elements necessary?
> 4.  **Data Characteristics:** Is the data nearly sorted (Insertion Sort might be good)? Are keys integers in a small range (Counting Sort)? Is the data uniformly distributed (Bucket Sort)?
> 5.  **Implementation Complexity:** Some algorithms are simpler to implement than others.
> 6.  **Guarantees vs. Average Case:** Is guaranteed O(n log n) performance needed (Merge Sort, Heap Sort), or is excellent average performance with rare quadratic worst-case acceptable (Quick Sort)?

---
**Source:** Worksheet WS25