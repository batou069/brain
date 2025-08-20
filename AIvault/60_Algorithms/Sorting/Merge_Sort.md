---
tags:
  - algorithms
  - sorting
  - divide_and_conquer
  - stable_sort
  - concept
aliases:
  - Mergesort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Divide_and_Conquer]]"
  - "[[Recursion]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Merge Sort

## Definition
**Merge Sort** is an efficient, comparison-based [[Sorting_Algorithms|sorting algorithm]]. It is a classic example of the **[[Divide_and_Conquer|Divide and Conquer]]** paradigm. The algorithm divides the unsorted list into $n$ sublists, each containing one element (which are considered sorted), and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

## Algorithm Steps
1.  **Divide:** If the list has more than one element, divide the unsorted list into two halves.
2.  **Conquer:** [[Recursion|Recursively]] call merge sort for the two halves until you have sublists of size 1. A list of one element is inherently sorted.
3.  **Combine (Merge):** Merge the two sorted sublists back into one sorted list. This is the key step. The merge operation works by comparing the first elements of the two sublists, taking the smaller one, and adding it to the result. This is repeated until one sublist is empty, at which point the remaining elements of the other sublist are appended.

## Complexity Analysis
- **Time Complexity:**
    - **Best Case:** $O(n \log n)$
    - **Average Case:** $O(n \log n)$
    - **Worst Case:** $O(n \log n)$
    - The time complexity is consistently $O(n \log n)$ because the list is always divided in half, leading to $\log n$ levels of recursion, and the merge step at each level takes $O(n)$ time in total.
- **Space Complexity:**
    - **$O(n)$**. Merge sort requires additional space to store the merged sublists. It is not an in-place sorting algorithm.

## Properties
- **Stable:** Yes. Merge sort is a [[Stability_Sorting|stable sort]], meaning that elements with equal values appear in the same order in the sorted output as they did in the input.
- **In-place:** No.
- **Comparison Sort:** Yes.

## Python Implementation

```python
def merge_sort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.
    """
    if len(arr) > 1:
        # 1. Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 2. Conquer (Recursive calls)
        merge_sort(left_half)
        merge_sort(right_half)

        # 3. Combine (Merge)
        i = j = k = 0 # i for left_half, j for right_half, k for main arr

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Example usage
my_list =
sorted_list = merge_sort(my_list.copy()) # Use copy to keep original
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Guaranteed $O(n \log n)$ performance, making it very reliable.
- It is a stable sort.
- Well-suited for sorting linked lists where inserting elements in the middle is efficient.
- Can be parallelized.

**Disadvantages:**
- Requires $O(n)$ extra space, which can be a significant drawback for large datasets.
- For smaller lists, simpler algorithms like Insertion Sort can be faster due to less overhead.

---