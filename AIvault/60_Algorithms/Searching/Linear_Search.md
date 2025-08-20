---
tags:
  - algorithms
  - searching
  - concept
aliases:
  - Sequential Search
related:
  - "[[Searching_Algorithms]]"
  - "[[Binary_Search]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Linear Search

## Definition
**Linear Search**, also known as **sequential search**, is the simplest [[Searching_Algorithms|searching algorithm]]. It sequentially checks each element of a list for the target value until a match is found or until all the elements have been searched.

It is the most basic search algorithm and does not require the list to be sorted.

## Algorithm Steps
1.  Start from the first element of the list (index 0).
2.  Compare the current element with the target value.
3.  If the current element matches the target value, return the current index.
4.  If the current element does not match, move to the next element in the list.
5.  Repeat steps 2-4 until the end of the list is reached.
6.  If the end of the list is reached and the target value has not been found, return a value indicating that the element is not in the list (e.g., -1 or `None`).

## Complexity Analysis
Let $n$ be the number of elements in the list.
- **Time Complexity:**
    - **Best Case:** $O(1)$. The target element is the first element in the list.
    - **Average Case:** $O(n)$. On average, the algorithm will have to check half of the elements.
    - **Worst Case:** $O(n)$. The target element is the last element in the list, or it is not in the list at all.
- **Space Complexity:**
    - **$O(1)$**. It is an in-place algorithm that requires no extra space.

## Python Implementation

```python
def linear_search(arr, target):
    """
    Performs a linear search to find the index of a target value in an array.
    Returns the index of the target if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return its index
    return -1  # Target not found in the array

# Example usage
my_list =
target_value = 10
not_found_value = 99

index_found = linear_search(my_list, target_value)
index_not_found = linear_search(my_list, not_found_value)

print(f"List: {my_list}")
print(f"Searching for {target_value}... Found at index: {index_found}")
print(f"Searching for {not_found_value}... Found at index: {index_not_found}")

# Expected Output:
# List:
# Searching for 10... Found at index: 3
# Searching for 99... Found at index: -1
```

## Advantages and Disadvantages
**Advantages:**
- Very simple to implement.
- Works on any type of list, regardless of whether it is sorted or not.
- Useful for small lists or when the list is unsorted and sorting it first would be more expensive than the search itself.

**Disadvantages:**
- Very inefficient for large lists due to its $O(n)$ time complexity. For sorted lists, [[Binary_Search|Binary Search]] is significantly faster.

---