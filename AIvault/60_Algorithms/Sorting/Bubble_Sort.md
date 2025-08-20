---
tags:
  - algorithms
  - sorting
  - in_place_sort
  - stable_sort
  - concept
aliases:
  - Sinking Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Bubble Sort

## Definition
**Bubble Sort** is a simple [[Sorting_Algorithms|sorting algorithm]] that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller (or larger, depending on sorting order) elements "bubble" to the top of the list.

## Algorithm Steps
1.  Start at the beginning of the array.
2.  Compare the first element with the second. If the first is greater than the second, swap them.
3.  Move to the next pair of elements (second and third) and repeat the comparison and swap if necessary.
4.  Continue this process until the end of the array is reached. After this first pass, the largest element will have "bubbled" to the end of the array.
5.  Repeat the entire process for the array, but now excluding the last element (which is already in its correct place).
6.  Continue the passes, with each pass requiring one less comparison, until no swaps are needed in a full pass, which indicates the array is sorted.

## Complexity Analysis
- **Time Complexity:**
    - **Best Case:** $O(n)$. This occurs when the array is already sorted and an optimized version of the algorithm (which stops if no swaps occur in a pass) is used.
    - **Average Case:** $O(n^2)$.
    - **Worst Case:** $O(n^2)$. This occurs when the array is sorted in reverse order.
- **Space Complexity:**
    - **$O(1)$**. It is an in-place sorting algorithm.

## Properties
- **Stable:** Yes. It is a [[Stability_Sorting|stable sort]].
- **In-place:** Yes.
- **Comparison Sort:** Yes.
- **Adaptive:** Yes, the optimized version can terminate early if the list becomes sorted.

## Python Implementation (Optimized)

```python
def bubble_sort(arr):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm (optimized).
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # A flag to optimize. If no swaps in a pass, array is sorted.
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break # Exit the loop if the list is already sorted
            
    return arr

# Example usage
my_list =
sorted_list = bubble_sort(my_list.copy()) # Use copy to keep original
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Very simple to understand and implement.
- In-place with $O(1)$ extra space.
- Stable sort.
- Can be efficient for nearly sorted lists (adaptive).

**Disadvantages:**
- Extremely inefficient for large or reverse-sorted lists due to its $O(n^2)$ complexity.
- Generally performs worse than other simple sorts like [[Insertion_Sort|Insertion Sort]] and [[Selection_Sort|Selection Sort]].

Bubble Sort is primarily used for educational purposes to introduce sorting concepts. It is rarely used in practice due to its poor performance.

---