---
tags:
  - algorithms
  - sorting
  - in_place_sort
  - concept
aliases:
  - Selection Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Selection Sort

## Definition
**Selection Sort** is a simple, in-place [[Sorting_Algorithms|sorting algorithm]]. The algorithm divides the input list into two parts: a sorted sublist which is built up from left to right at the front (left) of the list, and a sublist of the remaining unsorted items that occupy the rest of the list.

Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

## Algorithm Steps
1.  Iterate from the first element (`arr[0]`) to the second-to-last element (`arr[n-2]`). Let the current index be `i`.
2.  Assume the element at index `i` is the minimum in the unsorted part of the array.
3.  Iterate through the rest of the unsorted part of the array (from `i+1` to `n-1`) to find the actual minimum element.
4.  If a new minimum is found, record its index.
5.  After scanning the unsorted part, swap the element at index `i` with the minimum element found.
6.  The element at index `i` is now considered part of the sorted sub-array. Repeat for the next `i`.

## Complexity Analysis
- **Time Complexity:**
    - **Best Case:** $O(n^2)$
    - **Average Case:** $O(n^2)$
    - **Worst Case:** $O(n^2)$
    - The complexity is always $O(n^2)$ because the nested loops to find the minimum element must always iterate through the entire unsorted portion of the list, regardless of whether the list is already sorted or not.
- **Space Complexity:**
    - **$O(1)$**. It is an in-place sorting algorithm.

## Properties
- **Stable:** No. It is generally an unstable sort. For example, if the list is `[5a, 5b, 2]` and we are sorting, the `2` will be swapped with `5a`, changing the relative order of `5a` and `5b`.
- **In-place:** Yes.
- **Comparison Sort:** Yes.
- **Swaps:** It is noted for minimizing the number of swaps (at most $n-1$ swaps). This can be useful if writing to memory is a very expensive operation.

## Python Implementation

```python
def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Example usage
my_list =
sorted_list = selection_sort(my_list.copy()) # Use copy to keep original
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Simple to understand and implement.
- In-place with $O(1)$ extra space.
- Performs a minimal number of swaps ($O(n)$), which can be advantageous if memory writes are costly.

**Disadvantages:**
- Inefficient for large lists with its $O(n^2)$ time complexity in all cases.
- Not a stable sort.
- Performance is not affected by the initial sortedness of the data.

Due to its poor time complexity, Selection Sort is generally not used for large datasets but can be useful for its simplicity in educational contexts or for small lists.

---