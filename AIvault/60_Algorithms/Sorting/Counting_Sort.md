---
tags:
  - algorithms
  - sorting
  - non_comparison_sort
  - linear_time_sort
  - concept
aliases:
  - Count Sort
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Radix_Sort]]"
  - "[[Computational_Complexity]]"
worksheet:
  - WS_Math_Foundations_2
date_created: 2025-08-20
---
# Counting Sort

## Definition
**Counting Sort** is an integer [[Sorting_Algorithms|sorting algorithm]] that operates by counting the number of occurrences of each distinct element in the input array. It is a [[Non-comparison_Sort|non-comparison sort]], meaning it does not sort by comparing elements to each other.

It is only efficient when the range of input values (let's say from 0 to $k$) is not significantly larger than the number of elements to be sorted ($n$).

## Algorithm Steps
1.  **Find Range:** Find the maximum value ($k$) in the input array to determine the range of values.
2.  **Create Count Array:** Create an auxiliary "count" array of size $k+1$, initialized to all zeros.
3.  **Store Counts:** Iterate through the input array. For each element, increment the corresponding counter in the count array. After this step, `count[i]` contains the number of occurrences of element `i`.
4.  **Store Cumulative Counts:** Modify the count array such that each element at index `i` stores the sum of previous counts. `count[i]` now contains the number of elements less than or equal to `i`. This gives the final position of each element.
5.  **Build Output Array:** Create an output array of the same size as the input. Iterate through the input array in reverse order. For each element `x`, place it in the output array at the position given by `count[x] - 1`. Then, decrement `count[x]`. Iterating in reverse makes the sort stable.
6.  **Copy Back:** Copy the sorted elements from the output array back to the original array.

## Complexity Analysis
Let $n$ be the number of elements in the input array and $k$ be the range of the input values (max value - min value).
- **Time Complexity:**
    - **Best, Average, Worst Case:** $O(n + k)$
    - The algorithm iterates through the input array a few times ($O(n)$) and the count array once ($O(k)$). If $k$ is on the order of $n$ ($k=O(n)$), the complexity is linear, $O(n)$.
- **Space Complexity:**
    - **$O(k)$**. Requires an auxiliary count array of size $k$.

## Properties
- **Stable:** Yes, if implemented correctly (by processing the input array in reverse when building the output).
- **In-place:** No. Requires auxiliary count and output arrays.
- **Comparison Sort:** No. It uses the values of the elements as indices into an array.

## Python Implementation

```python
def counting_sort(arr):
    """
    Sorts an array of non-negative integers using Counting Sort.
    """
    if not arr:
        return []

    # 1. Find the maximum element to determine the range
    max_val = max(arr)
    
    # 2. Create a count array
    count_size = max_val + 1
    count = * count_size
    
    # 3. Store the count of each element
    for num in arr:
        count[num] += 1
        
    # 4. Store the cumulative count
    for i in range(1, count_size):
        count[i] += count[i - 1]
        
    # 5. Build the output array
    output = * len(arr)
    # Iterate in reverse to make it stable
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1
        
    return output

# Example usage
my_list =
sorted_list = counting_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list:   {sorted_list}")

# Expected Output:
# Original list:
# Sorted list:  
```

## Advantages and Disadvantages
**Advantages:**
- Very fast (linear time complexity) when the range of data ($k$) is not significantly larger than the number of items ($n$).
- It is a stable sort.

**Disadvantages:**
- Not suitable for data with a very large range of values, as it would require a huge, impractical count array (e.g., sorting 32-bit integers would require an array of size $2^{32}$).
- Does not work for non-integer data like floats or strings.
- Not an in-place sort.

It is often used as a subroutine in [[Radix_Sort|Radix Sort]], which allows it to handle larger ranges of integers efficiently.

---