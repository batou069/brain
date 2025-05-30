---
tags:
  - algorithms
  - concept
  - sorting
  - analysis
aliases:
  - Non-comparison Sorting Algorithm
  - Linear Time Sort (Potential)
related:
  - "[[Sorting_Algorithms]]"
  - "[[Comparison_Sort]]"
  - "[[Time_Complexity]]"
  - "[[O_n]]"
  - "[[Counting_Sort]]"
  - "[[Radix_Sort]]"
  - "[[Bucket_Sort]]"
worksheet: [WS25]
date_created: 2025-04-21
---
# Non-comparison Sort

## Definition

A **Non-comparison Sort** is a type of [[Sorting_Algorithms|sorting algorithm]] that determines the sorted order of elements **without** directly comparing elements to each other using comparison operators (`<`, `>`, etc.). Instead, these algorithms typically exploit properties of the elements themselves, such as their integer values within a known range or their digit/character representation.

## Key Aspects / Characteristics

- **No Pairwise Comparisons:** Avoids the element-vs-element comparisons that dominate [[Comparison_Sort|comparison sorts]].
- **Exploits Data Properties:** Relies on assumptions about the data, such as:
    - Keys are integers within a specific range (e.g., 0 to `k`).
    - Keys can be broken down into digits or characters.
    - Keys are uniformly distributed.
- **Potential for Linear Time:** By avoiding comparisons, non-comparison sorts can break the Ω(n log n) lower bound for comparison sorts and achieve linear time complexity (e.g., O(n) or O(n+k)) under their specific constraints.
- **Not General Purpose:** Usually restricted to specific data types (often integers or strings) and may have constraints on the range or distribution of values.

## Examples

- **[[Counting_Sort]]:**
    - *Constraint:* Input elements are integers within a known range (e.g., 0 to `k`).
    - *Mechanism:* Counts the occurrences of each distinct key value, then uses these counts to determine the positions of elements in the output array.
    - *Complexity:* O(n + k) time, O(n + k) space. Linear if `k` is O(n).
- **[[Radix_Sort]]:**
    - *Constraint:* Input elements can be treated as sequences of digits or characters (e.g., integers, strings).
    - *Mechanism:* Sorts elements digit by digit (or character by character) starting from the least significant or most significant position, using a stable sorting algorithm (like Counting Sort) for each digit pass.
    - *Complexity:* O(d * (n + k)) time, where `d` is the number of digits/characters and `k` is the range of values per digit (radix). Linear if `d` and `k` are constant or small relative to `n`.
- **[[Bucket_Sort]]:**
    - *Constraint:* Input elements are drawn from a uniform distribution over a range.
    - *Mechanism:* Distributes elements into a number of "buckets." Each bucket is then sorted individually (e.g., using Insertion Sort), and the sorted buckets are concatenated.
    - *Complexity:* O(n) average time if input is uniformly distributed. Worst-case can be O(n^2) if all elements fall into one bucket.

## Related Concepts
- [[Sorting_Algorithms]]
- [[Comparison_Sort]] (Contrast: uses comparisons)
- [[Time_Complexity]], [[O_n]] (Potential linear time)
- [[Counting_Sort]], [[Radix_Sort]], [[Bucket_Sort]] (Examples)

## Questions / Further Study
>[!question] Explain linear sorts vs. comparison sorts. (WS25)
> See [[Comparison_Sort]]. Linear sorts (non-comparison sorts) avoid direct element comparisons, using data properties (like integer range) to sort, potentially achieving O(n) time. Comparison sorts use `<`, `>`, `=` and have an Ω(n log n) lower bound.

>[!question] If linear sorts are that efficient, why wouldn't we always use them? (WS25)
> See [[Comparison_Sort]]. Linear sorts have constraints on input data type/range, can use significant extra space, and their constant factors might make comparison sorts faster for moderate sizes or non-ideal data distributions.

---
**Source:** Worksheet WS25