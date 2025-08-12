140_Data_Science_AI/Regularization/L1_L2_Regularization.md
````markdown
[[L1_L2_Regularization]]
````

Filename: 140_Data_Science_AI/Learning_Paradigms/Supervised_Learning.md
````markdown
[[Supervised_Learning]]
````

Filename: 140_Data_Science_AI/Learning_Paradigms/Unsupervised_Learning.md
````markdown
[[Unsupervised_Learning]]
````

Filename: 140_Data_Science_AI/Learning_Paradigms/Reinforcement_Learning.md
````markdown
[[Reinforcement_Learning]]
````

Filename: 140_Data_Science_AI/Models/Regression_Models.md
````markdown
[[Regression_Models]]
````

Filename: 140_Data_Science_AI/Models/Classification_Models.md
````markdown
[[Classification_Models]]
````

Filename: 140_Data_Science_AI/Unsupervised_Learning/Clustering_Methods.md
````markdown
[[Clustering_Methods]]
````

Filename: 140_Data_Science_AI/Dimensionality_Reduction/Dimensionality_Reduction.md
````markdown
[[Dimensionality_Reduction]]
````

Filename: 140_Data_Science_AI/Evaluation/Model_Evaluation.md
````markdown
[[Model_Evaluation]]
````

Filename: 140_Data_Science_AI/Concepts/Overfitting_Underfitting.md
````markdown
[[Overfitting_Underfitting]]
````

Filename: 140_Data_Science_AI/Concepts/Bias_Variance_Tradeoff.md
````markdown
[[Bias_Variance_Tradeoff]]
````

Filename: 140_Data_Science_AI/Ensemble_Methods/Ensemble_Methods.md
````markdown
---
tags: [data_science, machine_learning, ensemble_methods, bagging, boosting, stacking, concept]
aliases: [Ensemble Learning]
related:
  - "[[Decision_Trees]]"
  - "[[Random_Forest]]"
  - "[[Gradient_Boosting]]"
  - "[[Bias_Variance_Tradeoff]]"
  - "[[Overfitting_Underfitting]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Ensemble Methods

## Definition
**Ensemble learning** (or **ensemble methods**) is a machine learning technique where multiple individual models, often called "weak learners" or "base estimators," are strategically combined to produce one optimal predictive model. The goal is to achieve better performance than any of the constituent models could on their own.

The intuition is that by combining diverse and independent models, their individual errors can cancel each other out, leading to a more robust, accurate, and generalizable final prediction.

## Main Types of Ensemble Methods
[list2tab|#Ensemble Types]
- Bagging
    - **Stands for:** Bootstrap Aggregating.
    - **How it works:**
        1.  **Bootstrap:** Create multiple random subsets of the original training data by sampling with replacement.
        2.  **Aggregate:** Train a separate base model (e.g., a [[Decision_Trees|Decision Tree]]) on each subset.
        3.  **Combine:** The final prediction is made by averaging the predictions of all models (for regression) or by taking a majority vote (for classification).
    - **Primary Goal:** To reduce **variance** and combat [[Overfitting_Underfitting|overfitting]]. It is most effective with unstable models that have high variance (like deep decision trees).
    - **Example:** **[[Random_Forest|Random Forest]]** is a popular bagging method that uses decision trees as base learners and adds an extra layer of randomness by selecting a random subset of features at each split.
- Boosting
    - **Description:** Models are built sequentially, where each subsequent model attempts to correct the errors of its predecessor.
    - **How it works:**
        1.  Train a simple base model on the data.
        2.  Identify the errors made by the model.
        3.  Train a new model that focuses on the instances where the previous model performed poorly (by giving them higher weights).
        4.  Combine all models, typically through a weighted sum, to make the final prediction.
    - **Primary Goal:** To reduce **bias** and build a strong, complex model from simple ones (weak learners).
    - **Examples:**
        - **AdaBoost (Adaptive Boosting)**
        - **[[Gradient_Boosting|Gradient Boosting Machines (GBM)]]**
        - **XGBoost, LightGBM, CatBoost** (highly optimized implementations of gradient boosting).
- Stacking
    - **Description:** Stacking (or Stacked Generalization) involves training a new model to combine the predictions of several other base models.
    - **How it works:**
        1.  Train several different base models (e.g., a logistic regression, an SVM, a random forest) on the training data.
        2.  Use these base models to make predictions on a hold-out set (or through cross-validation).
        3.  These predictions are then used as input features to train a final "meta-model" (or "blender").
    - **Primary Goal:** To leverage the strengths of different types of models by learning how to best combine their predictions.

## Why Ensembles Work
- **Wisdom of the Crowd:** The collective knowledge of a diverse group is often better than that of a single expert.
- **Reduced Variance (Bagging):** Averaging the predictions of multiple models smooths out noise and reduces the impact of individual model errors.
- **Reduced Bias (Boosting):** Sequentially focusing on errors allows the ensemble to capture complex patterns that individual weak models would miss.
- **Improved Robustness:** The final model is less sensitive to the specifics of a single training set or the weaknesses of a single algorithm.

Ensemble methods, particularly gradient boosting and random forests, are responsible for many state-of-the-art results on tabular data and are widely used in both industry and machine learning competitions.

---
````

***

### **Section 3: 60_Algorithms**

`````markdown

Filename: 60_Algorithms/Sorting/Merge_Sort.md````markdown
---
tags: [algorithms, sorting, divide_and_conquer, stable_sort, concept]
aliases: [Mergesort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Divide_and_Conquer]]"
  - "[[Recursion]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Counting_Sort.md````markdown
---
tags: [algorithms, sorting, non_comparison_sort, linear_time_sort, concept]
aliases: [Count Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Radix_Sort]]" # Often used as a subroutine in Radix Sort
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Bucket_Sort.md````markdown
---
tags: [algorithms, sorting, non_comparison_sort, concept]
aliases: [Bin Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Insertion_Sort]]" # Often used to sort individual buckets
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Radix_Sort.md
````markdown
---
tags: [algorithms, sorting, non_comparison_sort, linear_time_sort, concept]
aliases: [Radix Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Non-comparison_Sort]]"
  - "[[Counting_Sort]]" # Used as a subroutine
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Insertion_Sort.md
````markdown
---
tags: [algorithms, sorting, in_place_sort, stable_sort, concept]
aliases: [Insertion Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Selection_Sort.md
````markdown
---
tags: [algorithms, sorting, in_place_sort, concept]
aliases: [Selection Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Sorting/Bubble_Sort.md
````markdown
---
tags: [algorithms, sorting, in_place_sort, stable_sort, concept]
aliases: [Sinking Sort]
related:
  - "[[Sorting_Algorithms]]"
  - "[[Computational_Complexity]]"
  - "[[Stability_Sorting]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Searching/Linear_Search.md
````markdown
---
tags: [algorithms, searching, concept]
aliases: [Sequential Search]
related:
  - "[[Searching_Algorithms]]"
  - "[[Binary_Search]]" # Contrast with
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Searching/Binary_Search.md
````markdown
---
tags: [algorithms, searching, divide_and_conquer, concept]
aliases: [Half-interval Search, Logarithmic Search]
related:
  - "[[Searching_Algorithms]]"
  - "[[Linear_Search]]" # Contrast with
  - "[[Divide_and_Conquer]]"
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

Filename: 60_Algorithms/Graph/Breadth_First_Search_BFS.md
````markdown
---
tags: [algorithms, searching, graph_traversal, bfs, concept]
aliases: [BFS]
related:
  - "[[Graph_Theory]]"
  - "[[Depth_First_Search_DFS]]" # Contrast with
  - "[[Queue_ADT]]" # Data structure used
  - "[[Shortest_Path_Unweighted]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Breadth-First Search (BFS)

## Definition
**Breadth-First Search (BFS)** is an algorithm for traversing or searching tree or [[Graph_Theory|graph]] data structures. It starts at a selected node (the "source" or "root") and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It explores the graph "layer by layer," visiting all nodes at distance 1 from the source, then all nodes at distance 2, and so on.

## Data Structure Used
BFS uses a **[[Queue_ADT|Queue]]** (First-In, First-Out) data structure to keep track of the nodes to visit next.

## Algorithm Steps
1.  **Initialization:**
    - Create a [[Queue_ADT|queue]] and add the starting node to it.
    - Create a set or boolean array `visited` to keep track of visited nodes, and mark the starting node as visited.
2.  **Loop:** While the queue is not empty:
    - **Dequeue:** Remove the node at the front of the queue (let's call it `current_node`).
    - **Process:** Process `current_node` (e.g., print it, check if it's the target).
    - **Enqueue Neighbors:** For each neighbor of `current_node`:
        - If the neighbor has not been visited yet:
            - Mark the neighbor as visited.
            - Add the neighbor to the back of the queue.
3.  **Termination:** The algorithm terminates when the queue is empty, meaning all reachable nodes have been visited.

## Complexity Analysis
Let $V$ be the number of vertices (nodes) and $E$ be the number of edges in the graph.
- **Time Complexity:** $O(V + E)$
    - Each vertex is enqueued and dequeued exactly once ($O(V)$).
    - Every edge is explored once when its source vertex is dequeued ($O(E)$).
- **Space Complexity:** $O(V)$
    - In the worst case, the queue can hold all vertices of the graph (e.g., in a star graph, all neighbors of the central node are enqueued). The `visited` set also takes $O(V)$ space.

## Python Implementation

```python
from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.
    
    :param graph: A dictionary representing the adjacency list of the graph.
    :param start_node: The node to start the traversal from.
    :return: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return []
        
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    traversal_order = []
    
    while queue:
        current_node = queue.popleft() # Dequeue from the front
        traversal_order.append(current_node)
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Enqueue to the back
                
    return traversal_order

# Example usage
# Graph represented as an adjacency list
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
bfs_path = bfs(my_graph, start)
print(f"Graph: {my_graph}")
print(f"BFS traversal starting from node '{start}': {bfs_path}")

# Expected Output:
# Graph: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# BFS traversal starting from node 'A': ['A', 'B', 'C', 'D', 'E', 'F']
```

## Applications
- **Shortest Path in Unweighted Graphs:** BFS is guaranteed to find the shortest path (in terms of number of edges) from a source node to all other reachable nodes in an unweighted graph.
- **Network Broadcasting:** Simulating the broadcast of a message through a network.
- **Web Crawlers:** Used to discover all pages on a website, exploring level by level starting from a homepage.
- **Finding Connected Components:** Can be used to find all nodes in a connected component of a graph.
- **Social Networks:** Finding all friends at a certain "degree" of connection away from a person.
- **Solving Puzzles:** Finding the shortest solution to puzzles like Rubik's Cubes or mazes, where states are nodes and moves are edges.

---
````

Filename: 60_Algorithms/Graph/Depth_First_Search_DFS.md
````markdown
---
tags: [algorithms, searching, graph_traversal, dfs, concept]
aliases: [DFS]
related:
  - "[[Graph_Theory]]"
  - "[[Breadth_First_Search_BFS]]" # Contrast with
  - "[[Stack_ADT]]" # Data structure used (implicitly in recursion)
  - "[[Recursion]]"
  - "[[Topological_Sort]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Depth-First Search (DFS)

## Definition
**Depth-First Search (DFS)** is an algorithm for traversing or searching tree or [[Graph_Theory|graph]] data structures. The algorithm starts at a selected node (the "source" or "root") and explores as far as possible along each branch before backtracking.

It goes "deep" into the graph first, following one path to its end, then backtracks to explore other paths.

## Data Structure Used
DFS implicitly uses a **[[Stack_ADT|Stack]]** (Last-In, First-Out). This is often implemented using [[Recursion|recursion]] (which uses the call stack), but can also be implemented iteratively with an explicit stack.

## Algorithm Steps (Recursive)
1.  **Initialization:**
    - Create a set or boolean array `visited` to keep track of visited nodes.
2.  **DFS Function (`dfs_visit(node)`):**
    - Mark the current `node` as visited.
    - Process the `node` (e.g., print it).
    - For each neighbor of the `node`:
        - If the neighbor has not been visited, recursively call `dfs_visit(neighbor)`.
3.  **Start:** Call `dfs_visit(start_node)`. If the graph might be disconnected, loop through all nodes and call `dfs_visit` if the node hasn't been visited yet.

## Complexity Analysis
Let $V$ be the number of vertices (nodes) and $E$ be the number of edges in the graph.
- **Time Complexity:** $O(V + E)$
    - Each vertex is visited exactly once ($O(V)$).
    - Every edge is explored once ($O(E)$).
- **Space Complexity:** $O(V)$
    - In the worst case, the recursion depth (call stack) can be up to $V$ for a path-like graph. The `visited` set also takes $O(V)$ space.

## Python Implementation (Recursive)

```python
def dfs_recursive(graph, node, visited, traversal_order):
    """
    Recursive helper function for DFS.
    """
    visited.add(node)
    traversal_order.append(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

def dfs(graph, start_node):
    """
    Performs a Depth-First Search on a graph.
    
    :param graph: A dictionary representing the adjacency list of the graph.
    :param start_node: The node to start the traversal from.
    :return: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return []
        
    visited = set()
    traversal_order = []
    dfs_recursive(graph, start_node, visited, traversal_order)
    return traversal_order

# Example usage
# Graph represented as an adjacency list
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
dfs_path = dfs(my_graph, start)
print(f"Graph: {my_graph}")
print(f"DFS traversal starting from node '{start}': {dfs_path}")

# Expected Output:
# Graph: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# DFS traversal starting from node 'A': ['A', 'B', 'D', 'E', 'F', 'C']
# Note: The exact traversal order can vary depending on the order of neighbors in the adjacency list.
# For example, ['A', 'C', 'F', 'E', 'B', 'D'] is also a valid DFS path.
```

## Applications
- **Cycle Detection:** Detecting cycles in a graph.
- **[[Topological_Sort|Topological Sorting]]:** For Directed Acyclic Graphs (DAGs), DFS is the basis for topological sorting, which provides a linear ordering of vertices.
- **Path Finding:** Finding a path between two nodes in a graph.
- **Solving Puzzles with a Single Solution Path:** Such as mazes. DFS will explore one path to its conclusion.
- **Finding Connected Components:** Can be used to find all nodes in a connected component.
- **Flood Fill Algorithm:** Used in paint programs to fill a contiguous area with a color.

## BFS vs. DFS
- **Structure:** BFS explores layer by layer; DFS explores branch by branch.
- **Data Structure:** BFS uses a queue; DFS uses a stack (often via recursion).
- **Path Finding:** BFS is guaranteed to find the shortest path in an unweighted graph. DFS is not.
- **Space:** BFS can use a lot of memory if the branching factor is large. DFS can use a lot of memory (stack depth) if the paths are very long.

---
````

Filename: 60_Algorithms/Paradigms/Dynamic_Programming.md
````markdown
---
tags: [algorithms, paradigms, dynamic_programming, optimization, concept]
aliases: [DP]
related:
  - "[[Recursion]]"
  - "[[Memoization]]"
  - "[[Tabulation]]"
  - "[[Computational_Complexity]]"
worksheet: [WS_Math_Foundations_2]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Dynamic Programming

## Definition
**Dynamic Programming (DP)** is a powerful algorithmic technique for solving complex problems by breaking them down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution.

This approach is particularly useful for optimization problems that exhibit two key properties:
1.  **Overlapping Subproblems:** The problem can be broken down into subproblems that are reused several times.
2.  **Optimal Substructure:** The optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems.

## Main Approaches
There are two main ways to implement a dynamic programming algorithm:

[list2tab|#DP Approaches]
- Memoization (Top-Down)
    - **Description:** This is a recursive approach. The main function is written recursively to solve the problem in a natural way. The results of the subproblems are stored in a lookup table (e.g., a dictionary or array). Before computing a subproblem, the algorithm first checks if the solution is already in the table. If it is, it's returned directly. If not, it's computed and then stored in the table before being returned.
    - **Analogy:** Solving a problem by breaking it down, and writing down the answer to any smaller problem you solve so you don't have to solve it again.
- Tabulation (Bottom-Up)
    - **Description:** This is an iterative approach. The algorithm starts by solving the smallest possible subproblems and builds up to the solution of the main problem. It fills a table (the "DP table") in a specific order, ensuring that when it needs to solve a subproblem, the solutions to all its prerequisite subproblems are already available in the table.
    - **Analogy:** Building a solution from the ground up, starting with the simplest cases and using them to construct solutions to bigger and bigger cases.

## Example: Fibonacci Sequence
The Fibonacci sequence is a classic example to illustrate DP. The naive recursive solution is $F(n) = F(n-1) + F(n-2)$, which has exponential time complexity $O(2^n)$ due to recomputing the same subproblems many times.

### Python Implementation (with DP)

```python
# 1. Naive Recursive (for comparison - very slow)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 2. DP with Memoization (Top-Down)
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result

# 3. DP with Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    # DP table (array)
    dp = * (n + 1)
    dp = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage
n = 35
# print(f"Naive Fib({n}): {fib_naive(n)}") # This would be very slow
print(f"Memoized Fib({n}): {fib_memo(n)}")
print(f"Tabulated Fib({n}): {fib_tab(n)}")

# Expected Output:
# Memoized Fib(35): 9227465
# Tabulated Fib(35): 9227465
```
Both DP approaches reduce the time complexity from $O(2^n)$ to $O(n)$ and space complexity to $O(n)$ (or $O(1)$ if we only store the last two values in the tabulation method).

## Common DP Problems
- **Fibonacci Sequence**
- **Longest Common Subsequence (LCS):** Finding the longest subsequence common to two sequences.
- **Longest Increasing Subsequence (LIS):** Finding the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
- **Edit Distance (Levenshtein Distance):** Finding the minimum number of edits (insertions, deletions, substitutions) to change one word into another.
- **Knapsack Problem (0/1):** Given items with weights and values, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Matrix Chain Multiplication:** Finding the most efficient way to multiply a chain of matrices (see [[Matrix_Multiplication_Associativity]]).
- **Shortest Path in a DAG:** Finding the shortest path from a source to all other vertices in a Directed Acyclic Graph.

Dynamic programming is a powerful technique for solving a wide range of optimization and counting problems in computer science.

---
````````