---
tags:
  - algorithms
  - sorting
  - in_place_sort
  - stable_sort
  - concept
aliases:
  - Insertion Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Insertion Sort

## Definition
**Insertion Sort** is a simple, intuitive [[Sorting_Algorithms|sorting algorithm]] that builds the final sorted array one item at a time. It iterates through an input array and removes one element per iteration, finds the location it belongs in the sorted part of the array, and inserts it there.

It is much less efficient on large lists than more advanced algorithms such as Quick Sort, Heap Sort, or [[Merge_Sort|Merge Sort]]. However, it has several advantages that make it useful in specific situations.

## Algorithm Steps
1.  Iterate from the second element (`arr[1]`) to the end of the array (`arr[n-1]`).
2.  In each iteration, the current element (let's call it `key`) is conceptually removed from the array.
3.  Compare `key` with the elements in the sorted sub-array to its left (`arr[0...i-1]`).
4.  Shift all elements in the sorted sub-array that are greater than `key` one position to the right.
5.  Insert `key` into the now-empty position.

## Complexity Analysis
- **Time Complexity:**
    - **Best Case:** $O(n)$. This occurs when the array is already sorted. The algorithm just iterates through the list once.
    - **Average Case:** $O(n^2)$.
    - **Worst Case:** $O(n^2)$. This occurs when the array is sorted in reverse order.
- **Space Complexity:**
    - **$O(1)$**. It is an in-place sorting algorithm.

## Properties
- **Stable:** Yes. It is a [[Stability_Sorting|stable sort]].
- **In-place:** Yes.
- **Comparison Sort:** Yes.
- **Adaptive:** It is efficient for data sets that are already substantially sorted. The time complexity is $O(nk)$ when each element in the input is no more than $k$ places away from its sorted position.
- **Online:** It can sort a list as it receives it.

## Python Implementation

```python
def insertion_sort(arr):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
my_list =
sorted_list = insertion_sort(my_list.copy()) # Use copy to keep original
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Simple implementation.
- Efficient for small data sets.
- Efficient for data sets that are already nearly sorted (adaptive).
- More efficient in practice than other simple quadratic ($O(n^2)$) algorithms like Selection Sort or Bubble Sort.
- Stable and in-place.
- Can sort items as they are received (online).

**Disadvantages:**
- Inefficient for large lists ($O(n^2)$ complexity).

It is often used as the recursive base case for more complex algorithms, like Timsort (Python's default sort) and Introsort, which switch to Insertion Sort for small partitions.

---