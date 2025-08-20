---
tags:
  - algorithms
  - sorting
  - non_comparison_sort
  - concept
aliases:
  - Bin Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Insertion_Sort]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Bucket Sort

## Definition
**Bucket Sort**, or **bin sort**, is a [[Sorting_Algorithms|sorting algorithm]] that works by distributing the elements of an array into a number of "buckets". Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort algorithm. Finally, the elements from the sorted buckets are concatenated to form the final sorted array.

Bucket sort is most effective when the input data is uniformly distributed over a range.

## Algorithm Steps
1.  **Setup Buckets:** Create an array of empty buckets (e.g., lists). The number of buckets is typically chosen based on the number of elements or the range of data.
2.  **Distribute Elements:** Iterate through the input array and place each element into its corresponding bucket. A mapping function is used to determine the correct bucket for each element. For numbers uniformly distributed in $[0, 1)$, a common mapping is `bucket_index = floor(num_buckets * element_value)`.
3.  **Sort Buckets:** Sort each non-empty bucket individually. A simple sorting algorithm like [[Insertion_Sort|Insertion Sort]] is often used for this step because the number of elements in each bucket is expected to be small.
4.  **Concatenate:** Concatenate the sorted elements from all buckets in order to get the final sorted array.

## Complexity Analysis
Let $n$ be the number of elements and $k$ be the number of buckets.
- **Time Complexity:**
    - **Best Case:** $O(n + k)$. This occurs when elements are perfectly distributed among the buckets.
    - **Average Case:** $O(n + k)$. This assumes the input is drawn from a uniform distribution. The time is dominated by creating buckets and distributing elements ($O(n+k)$) and then sorting small buckets, which is linear on average.
    - **Worst Case:** $O(n^2)$. This occurs when all elements fall into a single bucket. The performance then becomes dominated by the sorting algorithm used for the buckets (e.g., $O(n^2)$ for Insertion Sort).
- **Space Complexity:**
    - **$O(n + k)$**. Requires space for the buckets and the elements within them.

## Properties
- **Stable:** Yes, if the sorting algorithm used for the individual buckets is stable.
- **In-place:** No. Requires auxiliary space for the buckets.
- **Comparison Sort:** It is generally considered a [[Non-comparison_Sort|non-comparison sort]] because the initial distribution step does not rely on comparisons. However, it uses a comparison sort as a subroutine.

## Python Implementation

```python
def insertion_sort(bucket):
    """A simple insertion sort for sorting individual buckets."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    """
    Sorts an array of floats (assumed to be in [0, 1)) using Bucket Sort.
    """
    if not arr:
        return []

    # 1. Setup Buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # 2. Distribute Elements into buckets
    for num in arr:
        bucket_index = int(num_buckets * num)
        buckets[bucket_index].append(num)

    # 3. Sort Buckets and 4. Concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = insertion_sort(bucket)
        sorted_arr.extend(sorted_bucket)
        
    return sorted_arr

# Example usage
my_list = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_list = bucket_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list: [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
# Sorted list:   [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
```

## Advantages and Disadvantages
**Advantages:**
- Can be very fast (linear time complexity on average) for uniformly distributed data.
- Can be parallelized easily by sorting buckets in parallel.

**Disadvantages:**
- Performance degrades significantly if the data is not uniformly distributed (worst case is $O(n^2)$).
- Requires extra space for the buckets.
- The implementation needs to be adapted for different data ranges or types (e.g., negative numbers, non-floating point numbers).

---