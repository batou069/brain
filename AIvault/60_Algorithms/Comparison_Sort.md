---
tags:
  - algorithms
  - concept
  - sorting
  - analysis
aliases:
  - Comparison Sorting Algorithm
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Time_Complexity]]"
  - "[[O_n_log_n]]"
  - "[[Bubble_Sort]]"
  - "[[Selection_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Merge_Sort]]"
  - "[[Quick_Sort]]"
  - "[[Heap_Sort]]"
  - "[[Decision_Tree_Model]]" # Used for lower bound proof
worksheet: [WS25]
date_created: 2025-04-21
---
# Comparison Sort

## Definition

A **Comparison Sort** is a type of [[Sorting_Algorithms|sorting algorithm]] that determines the sorted order of a list of elements solely based on **pairwise comparisons** between elements. It uses comparison operators (like `<`, `>`, `<=`, `>=`) to decide the relative order of elements.

## Key Aspects / Characteristics

- **Comparison-Based:** Relies only on comparing elements to each other. It doesn't make assumptions about the internal structure or range of the elements (unlike [[Non-comparison_Sort|non-comparison sorts]]).
- **Generality:** Can sort any data type for which a consistent comparison operation (total order or weak order) is defined.
- **Lower Bound:** It can be proven (using a [[Decision_Tree_Model]]) that any deterministic comparison sort algorithm requires **at least Ω(n log n)** comparisons in the worst case to sort `n` elements. This means algorithms like [[Merge_Sort]] and [[Heap_Sort]] are asymptotically optimal in terms of worst-case time complexity for comparison sorts.
- **Common Algorithms:** Most widely known sorting algorithms fall into this category.

## Examples

- [[Bubble_Sort]]
- [[Selection_Sort]]
- [[Insertion_Sort]]
- [[Merge_Sort]]
- [[Quick_Sort]]
- [[Heap_Sort]]
- Shellsort
- Introsort

## Related Concepts
- [[Sorting_Algorithms]]
- [[Non-comparison_Sort]] (Contrast: Uses properties other than comparisons)
- [[Time_Complexity]], [[O_n_log_n]] (Theoretical lower bound)
- [[Decision_Tree_Model]] (Used for the lower bound proof)

## Questions / Further Study
>[!question] Explain linear sorts vs. comparison sorts. (WS25)
> - **[[60_Algorithms/Comparison_Sort|Comparison Sorts]]** determine the order by comparing pairs of elements (`<`, `>`, `=`). They work for any data type with a defined comparison. Their theoretical best worst-case time complexity is Ω(n log n). Examples: Merge Sort, Quick Sort, Heap Sort, Bubble Sort.
> - **[[Non-comparison_Sort|Linear Sorts (Non-comparison Sorts)]]** do not rely on comparing elements directly. They use assumptions about the data (e.g., integers within a known range) to determine the sorted order, often by using keys as array indices or distributing elements into buckets. They can achieve linear time complexity, O(n), under specific conditions. Examples: Counting Sort, Radix Sort, Bucket Sort.

>[!question] If linear sorts are that efficient, why wouldn't we always use them? (WS25)
> We don't always use linear (non-comparison) sorts because:
> 1.  **Constraints:** They often have strict constraints on the input data type and range (e.g., Counting Sort requires integers within a reasonably small range `k`). They are not general-purpose.
> 2.  **Space Complexity:** Some linear sorts (like Counting Sort, Radix Sort) can require significant auxiliary space (e.g., O(n+k) or O(k)), which might be prohibitive.
> 3.  **Not Always Faster:** While asymptotically faster (O(n) vs O(n log n)), the constant factors hidden in the Big O notation might make a well-implemented comparison sort like Quick Sort faster for moderate input sizes or if the range `k` for Counting/Radix sort is very large.
> 4.  **Stability Requirement:** Radix Sort relies on using a stable underlying sort, adding complexity.

>[!question] Why are all comparison sorts O(n log n)? Can't we get O(n) with comparison sorts? (WS25)
> It's more accurate to say that the **worst-case lower bound** for comparison sorts is **Ω(n log n)** (Omega, lower bound), meaning no comparison sort can *guarantee* better than O(n log n) performance in the worst case.
> - **Why Ω(n log n)?** This comes from analyzing the [[Decision_Tree_Model]] for sorting. To sort `n` distinct items, there are `n!` (n factorial) possible permutations (orderings). A comparison sort must be able to distinguish between all these permutations. Each comparison (`a < b`?) has two outcomes (true/false), effectively branching in a decision tree. The minimum depth of a binary tree required to distinguish `n!` leaves is `log2(n!)`. Using Stirling's approximation for `n!`, `log2(n!)` is approximately `n log2(n)`. Therefore, any comparison sort needs at least roughly `n log n` comparisons in the worst case to determine the correct sorted order among all possibilities.
> - **Can we get O(n)?** No comparison sort can achieve O(n) time complexity in the *worst* or *average* case for general inputs, due to the Ω(n log n) lower bound. However, some comparison sorts (like [[Insertion_Sort]] or [[Bubble_Sort]]) can achieve O(n) time in the *best case* (e.g., when the input array is already sorted).

---
**Source:** Worksheet WS25