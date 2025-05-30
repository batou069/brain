---
tags:
  - algorithms
  - concept
  - analysis
  - complexity
  - memory
aliases:
  - In-place Algorithm
  - In-place Sort
related:
  - "[[Algorithm]]"
  - "[[Space_Complexity]]"
  - "[[Sorting_Algorithms]]"
  - "[[Heap_Sort]]"
  - "[[Quick_Sort]]"
  - "[[Bubble_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Selection_Sort]]"
  - "[[Merge_Sort]]" # Not in-place
worksheet: [WS25]
date_created: 2025-04-21
---
# In-place Algorithm

## Definition

An **In-place Algorithm** is an [[Algorithm]] whose [[Space_Complexity|auxiliary space complexity]] (the extra memory required beyond the space used to store the input) is **constant**, i.e., **O(1)**, or sometimes logarithmic, O(log n). In simpler terms, an in-place algorithm transforms the input data using a very small, fixed amount of additional memory, modifying the input structure directly rather than creating a separate copy to hold the results.

## Key Aspects / Characteristics

- **Minimal Extra Space:** Requires little to no additional storage space beyond the input data itself. The amount of extra space used does not grow with the input size `n`.
    - *Strict Definition:* Often O(1) auxiliary space.
    - *Less Strict Definition:* Sometimes O(log n) auxiliary space (e.g., for recursion stack in in-place Quick Sort) is also considered "in-place" in certain contexts, as it's much less than the O(n) space needed for a full copy.
- **Modifies Input:** Operates directly on the input data structure, overwriting or rearranging elements within it to produce the output. The original input is usually lost or transformed.
- **Space Efficiency:** Highly desirable when memory is limited.
- **Sorting Context:** In [[Sorting_Algorithms|sorting]], an in-place sort rearranges the elements within the original array.

## Examples

- **In-place Algorithms:**
    - [[Bubble_Sort]], [[Selection_Sort]], [[Insertion_Sort]], [[Heap_Sort]]: These comparison sorts rearrange elements within the original array using only O(1) auxiliary space for temporary variables during swaps.
    - [[Quick_Sort]]: While the partitioning is done in-place, the recursive calls require O(log n) stack space on average (O(n) worst-case), so it's often considered in-place under the less strict definition.
    - Reversing an array in-place (by swapping elements from ends inwards).
    - Fisher-Yates shuffle (shuffling an array in-place).
- **Not In-place Algorithms:**
    - [[Merge_Sort]]: Typically requires O(n) auxiliary space to merge the sorted subarrays.
    - [[Counting_Sort]], [[Radix_Sort]]: Usually require auxiliary arrays for counting or distribution, often O(n) or O(n+k) space.
    - Creating a separate copy of a data structure.

## Trade-offs

- **Pro:** Saves memory significantly, especially for large datasets.
- **Con:** Modifies the original input data, which might not be desirable if the original is needed later. Can sometimes be slightly more complex to implement correctly compared to out-of-place versions.

## Related Concepts
- [[Algorithm]], [[Space_Complexity]], [[Computational_Complexity]]
- [[Sorting_Algorithms]] (Many are classified as in-place or not)
- Auxiliary Space
- Out-of-place Algorithm (Requires significant extra space, often O(n))

---
**Source:** Worksheet WS25