---
tags:
  - algorithms
  - sorting
  - non_comparison_sort
  - linear_time_sort
  - concept
aliases:
  - Radix Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Counting_Sort]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Radix Sort

## Definition
**Radix Sort** is a [[Non-comparison_Sort|non-comparison]] integer [[Sorting_Algorithms|sorting algorithm]] that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value. It processes individual digits of the numbers.

There are two main variations:
1.  **LSD (Least Significant Digit) Radix Sort:** Starts sorting from the least significant digit (the rightmost digit) and moves towards the most significant digit.
2.  **MSD (Most Significant Digit) Radix Sort:** Starts from the most significant digit and moves towards the least significant.

LSD Radix Sort is more common and generally simpler to implement.

## Algorithm Steps (LSD Radix Sort)
1.  **Find Maximum:** Find the maximum number in the input array to determine the number of digits in the largest number.
2.  **Iterate through Digits:** Loop from the least significant digit to the most significant digit (i.e., for `exp = 1, 10, 100, ...`).
3.  **Stable Sort:** In each iteration, use a stable sorting algorithm to sort the input array based on the current digit. **[[Counting_Sort|Counting Sort]]** is typically used for this step because it is stable and efficient for sorting digits (which have a small, fixed range of 0-9).
4.  **Repeat:** After sorting by the most significant digit, the entire array will be sorted.

## Complexity Analysis
Let $n$ be the number of elements, $d$ be the number of digits in the largest number, and $b$ be the base of the number system (e.g., $b=10$ for decimal numbers).
- **Time Complexity:**
    - **Best, Average, Worst Case:** $O(d \cdot (n + b))$
    - The outer loop runs $d$ times (once for each digit).
    - The inner stable sort (Counting Sort) takes $O(n+b)$ time.
    - If $d$ is a constant (e.g., for 32-bit integers, $d$ is fixed) and $b$ is fixed (e.g., 10), the complexity is effectively linear, $O(n)$.
- **Space Complexity:**
    - **$O(n + b)$**. This is required by the underlying stable sort (Counting Sort).

## Properties
- **Stable:** Yes. The stability of the underlying sort (like Counting Sort) is crucial for Radix Sort to work correctly.
- **In-place:** No.
- **Comparison Sort:** No.

## Python Implementation (LSD Radix Sort)

```python
def counting_sort_for_radix(arr, exp):
    """
    A modified counting sort to sort arr[] based on the digit represented by exp.
    exp is 10^i where i is the current digit number.
    """
    n = len(arr)
    output = * n
    count = * 10 # Digits 0-9

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to current digit
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Sorts an array of non-negative integers using LSD Radix Sort.
    """
    if not arr:
        return []
        
    # 1. Find the maximum number to know number of digits
    max_val = max(arr)

    # 2. Do counting sort for every digit.
    # exp is 10^i where i is current digit number
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Example usage
my_list =
sorted_list = radix_sort(my_list.copy()) # Use copy to keep original
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Very fast (linear time complexity) for sorting integers or strings.
- It is a stable sort.

**Disadvantages:**
- Not as flexible as comparison-based sorts like Merge Sort or Quick Sort. It's primarily for integers or data that can be mapped to integers (like strings).
- Requires extra space for the counting sort subroutine.
- The constant factors in the complexity ($d$ and $b$) can make it slower than comparison sorts for small lists or for numbers with many digits.

---