---
tags:
  - numpy
  - python
  - function
  - performance
  - comparison
aliases:
  - np.sum vs sum()
related:
  - "[[NumPy_ndarray]]"
  - "[[Python_list]]"
  - "[[NumPy_Universal_Functions]]"
  - "[[NumPy_Vectorization]]"
  - "[[NumPy_Aggregation_Functions]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# `np.sum()` vs. Python's `sum()`

## Definitions

- **Python's built-in `sum(iterable, start=0)`:**
    - Takes an iterable (like a list, tuple) and an optional `start` value.
    - Iterates through the elements of the iterable, adding them one by one to `start`.
    - Implemented in Python, involves Python's object model and iteration protocol.

- **NumPy's `np.sum(a, axis=None, dtype=None, out=None, keepdims=False, initial=<no value>, where=<no value>)`:**
    - A [[NumPy_Universal_Functions|universal function (ufunc)]] (or similar highly optimized function) designed to operate efficiently on [[NumPy_ndarray|NumPy arrays]].
    - Can sum elements along a specified `axis` or sum all elements if `axis` is `None`.
    - Can control the `dtype` of the accumulator and the result.
    - Implemented in compiled C code, leveraging NumPy's contiguous memory layout and vectorized operations.

## Key Differences & Usage (WS_NumPy Question)

| Feature                    | Python `sum()`                              | NumPy `np.sum()`                                        |
| -------------------------- | ------------------------------------------- | ------------------------------------------------------- |
| **Primary Input**          | Generic Python iterables (lists, tuples)    | NumPy `ndarray`s                                        |
| **Speed**                  | Slower for large numerical sequences        | **Much faster** for NumPy arrays                        |
| **Implementation**         | Python loop                                 | Optimized C loop (vectorized)                           |
| **Multi-dim Sum**          | Cumbersome (nested loops or `map` needed)   | Easy: `axis` parameter for row/col/layer sums           |
| **`dtype` Control**        | No direct control (uses Python numbers)     | Yes, `dtype` parameter for accumulator/result           |
| **Overhead**               | Python object/type checking per element     | Minimal once array data is accessed                     |
| **Can it sum `np.array`?** | Yes, but inefficiently (iterates like list) | **Yes (intended use)**                                  |
| **Can it sum `list`?**     | **Yes (intended use)**                      | Yes, implicitly converts list to array first (overhead) |

**Can you use `np.sum` on a regular array (Python list) and `sum` on a `np.array`?**
-   **`np.sum()` on a Python `list`:** Yes. `np.sum()` will first implicitly convert the Python `list` into a NumPy `ndarray` and then perform the sum. This involves an overhead for the conversion.
    ```python
    import numpy as np
    my_list = [1, 2, 3, 4]
    numpy_sum_on_list = np.sum(my_list) # Works, list -> array -> sum
    print(f"np.sum on list: {numpy_sum_on_list}")
    ```
-   **`sum()` on a NumPy `ndarray`:** Yes. Python's `sum()` can iterate over a NumPy array (as `ndarray` is an iterable). However, it will be **significantly slower** than `np.sum()` because it treats the `ndarray` elements as individual Python objects and uses Python's slower iteration and addition mechanisms.
    ```python
    my_np_array = np.array()
    python_sum_on_nparray = sum(my_np_array) # Works, but slow
    print(f"sum() on ndarray: {python_sum_on_nparray}")
    ```

**Why does `np.sum` exist?**
1.  **Performance:** `np.sum()` is implemented in C and operates directly on the contiguous memory of `ndarray`s, leveraging SIMD instructions and avoiding Python's interpreter overhead for each element. This makes it orders of magnitude faster for large arrays. See [[NumPy_Vectorization]].
2.  **Multi-dimensional Operations:** `np.sum()` provides the `axis` parameter, allowing easy summation along specific dimensions (rows, columns, etc.) of multi-dimensional arrays, a common requirement in numerical computing and data analysis. Achieving this with Python's `sum()` would require complex nested loops or comprehensions.
3.  **Data Type Control:** `np.sum()` allows specifying the `dtype` for the accumulator and the result, which can be important for preventing overflow or maintaining precision in numerical calculations. Python's `sum()` uses standard Python numeric types.
4.  **Consistency with NumPy API:** It's part of a suite of optimized aggregation functions (`np.mean`, `np.std`, `np.min`, `np.max`, etc.) that all operate efficiently on `ndarray`s with similar interfaces.

## Performance Illustration (Conceptual)

```mermaid
graph LR
    subgraph Summing Large Numerical Array
        PySum["Python sum(ndarray)"] -- Iterates in Python --> Element1[Elem1 as PyObject];
        Element1 -- Python + --> Element2[Elem2 as PyObject];
        Element2 -- Python + --> ElementN[...];
        style PySum fill:#fdd

        NpSum["np.sum(ndarray)"] -- Operates in C --> ContigData["Contiguous Data Block"];
        ContigData -- Vectorized Sum --> NpResult[Result];
        style NpSum fill:#dfd
    end
    note right of PySum : High overhead per element
    note right of NpSum : Low overhead, optimized loop
```

## Related Concepts
- [[NumPy_ndarray]], [[Python_list]]
- [[NumPy_Universal_Functions]], [[NumPy_Vectorization]]
- [[NumPy_Aggregation_Functions]]
- [[Time_Complexity]], [[Performance]]

---
**Source:** Worksheet WS_NumPy, NumPy Documentation