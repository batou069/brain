---
tags:
  - algorithms
  - searching
  - divide_and_conquer
  - concept
aliases:
  - Half-interval Search
  - Logarithmic Search
related:
  - "[[Searching_Algorithms]]"
  - "[[Linear_Search]]"
  - "[[Divide_and_Conquer]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Binary Search

## Definition
**Binary Search** is a highly efficient [[Searching_Algorithms|searching algorithm]] that finds the position of a target value within a **sorted array**. It works by repeatedly dividing the search interval in half.

It is a classic example of the **[[Divide_and_Conquer|Divide and Conquer]]** paradigm.

## Prerequisite
The input array **must be sorted** for binary search to work correctly.

## Algorithm Steps
1.  Compare the target value with the middle element of the array.
2.  If the target value matches the middle element, its position is found, and the search is complete.
3.  If the target value is less than the middle element, narrow the search to the lower half of the array.
4.  If the target value is greater than the middle element, narrow the search to the upper half of the array.
5.  Repeat steps 1-4 with the new, smaller search interval until the value is found or the interval is empty.

## Complexity Analysis
Let $n$ be the number of elements in the list.
- **Time Complexity:**
    - **Best Case:** $O(1)$. The target element is the middle element of the array.
    - **Average Case:** $O(\log n)$.
    - **Worst Case:** $O(\log n)$.
    - The logarithmic complexity comes from the fact that the search space is halved in each iteration.
- **Space Complexity:**
    - **$O(1)$** for the iterative implementation.
    - **$O(\log n)$** for the recursive implementation due to the call stack.

## Python Implementation (Iterative)

```python
def binary_search(arr, target):
    """
    Performs an iterative binary search to find the index of a target in a sorted array.
    Returns the index of the target if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 # or low + (high - low) // 2 to prevent overflow
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    return -1 # Element is not present in the array

# Example usage
my_list = # Must be sorted
target_value = 10
not_found_value = 99

index_found = binary_search(my_list, target_value)
index_not_found = binary_search(my_list, not_found_value)

print(f"Sorted List: {my_list}")
print(f"Searching for {target_value}... Found at index: {index_found}")
print(f"Searching for {not_found_value}... Found at index: {index_not_found}")

# Expected Output:
# Sorted List:
# Searching for 10... Found at index: 3
# Searching for 99... Found at index: -1
```

## Advantages and Disadvantages
**Advantages:**
- Extremely fast ($O(\log n)$ time complexity) for searching in large, sorted arrays.
- Significantly outperforms [[Linear_Search|Linear Search]] for large datasets.

**Disadvantages:**
- Requires the array to be sorted beforehand. The cost of sorting ($O(n \log n)$) might outweigh the benefit of the fast search if the search is only performed once.
- Not suitable for data structures that do not support efficient random access (like linked lists).

Binary search is a fundamental algorithm in computer science, widely used in applications where fast lookups in large, static, sorted datasets are required.

---