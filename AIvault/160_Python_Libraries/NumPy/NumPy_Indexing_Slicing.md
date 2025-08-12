---
tags:
  - numpy
  - python
  - function
  - concept
  - core
  - performance
  - vectorization
aliases:
  - ufuncs
  - NumPy ufunc
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Vectorization]]"
  - "[[NumPy_Broadcasting]]"
  - "[[NumPy_Data_Types]]"
worksheet: [WS_NumPy] # Implied by efficient operations
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Universal Functions (ufuncs)

## Definition

**Universal Functions (ufuncs)** in NumPy are functions that operate on `ndarray`s in an **element-by-element** fashion. They are a core part of NumPy's power and efficiency, supporting [[NumPy_Vectorization|vectorization]], [[NumPy_Broadcasting|broadcasting]], and type casting. Many standard mathematical operations (addition, subtraction, trigonometric functions, exponentials, logarithms, etc.) are implemented as ufuncs.

## Key Characteristics

1.  **Element-wise Operation:** Apply an operation to each element of the input array(s) independently.
    - Example: `np.add(arr1, arr2)` or `arr1 + arr2` computes `arr1[i] + arr2[i]` for all `i`.
2.  **[[NumPy_Vectorization|Vectorization]]:** Ufuncs are implemented in C (or Fortran) and operate on entire arrays without explicit Python loops. This makes them much faster than performing the same operations element by element in Python.
3.  **[[NumPy_Broadcasting|Broadcasting Support]]:** Ufuncs automatically handle broadcasting when operating on arrays of different but compatible shapes.
4.  **Type Casting:** Ufuncs can perform automatic type casting if input arrays have different [[NumPy_Data_Types|dtypes]], usually promoting to a type that can accommodate both inputs without loss of precision (e.g., `int` + `float` -> `float`). The `out` argument and `dtype` argument can sometimes control output types.
5.  **Output Argument (`out`):** Many ufuncs accept an optional `out` argument, which allows specifying an existing array where the result should be stored. This can save memory by avoiding the creation of a new array for the result.
6.  **Methods:** Ufuncs often have useful methods like:
    - `reduce(array, axis=0, dtype=None, out=None, keepdims=False, initial=<no value>, where=True)`: Applies the ufunc cumulatively along an axis (e.g., `np.add.reduce(arr)` is equivalent to `np.sum(arr)`).
    - `accumulate(array, axis=0, dtype=None, out=None)`: Similar to `reduce`, but stores all intermediate results.
    - `reduceat(array, indices, axis=0, dtype=None, out=None)`: Performs reduce over specified slices.
    - `outer(a, b, **kwargs)`: Applies the ufunc to all pairs of elements from two input arrays.
    - `at(a, indices, b=None)`: Performs unbuffered in-place operation on elements specified by indices.

## Types of Ufuncs

-   **Unary Ufuncs:** Operate on a single input array (e.g., `np.sqrt()`, `np.sin()`, `np.exp()`, `np.negative()`).
-   **Binary Ufuncs:** Operate on two input arrays (e.g., `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`, `np.maximum()`, `np.power()`).

## Example

```python
import numpy as np

a = np.array()
b = np.array()

# Unary ufunc
sqrt_a = np.sqrt(a)
print(f"sqrt(a): {sqrt_a}")

# Binary ufunc (also available via operators)
sum_ab = np.add(a, b) # Equivalent to a + b
print(f"a + b: {sum_ab}")

# Using the 'out' argument
c = np.empty_like(a) # Create an array c with same shape/dtype as a, uninitialized
np.multiply(a, 2, out=c) # Stores result of a * 2 into c
print(f"c (a * 2): {c}")

# Using a ufunc method
total_sum = np.add.reduce(a) # Sum all elements in a
print(f"Sum of a: {total_sum}") # Equivalent to np.sum(a)

cumulative_sum = np.add.accumulate(a)
print(f"Cumulative sum of a: {cumulative_sum}")
```

## Benefits

- **Performance:** Significant speedup over Python loops.
- **Conciseness:** Leads to more readable and compact code.
- **Flexibility:** Broadcasting and type handling simplify operations on arrays of varying shapes/types.

## Related Concepts
- [[NumPy_ndarray]] (Ufuncs operate on these)
- [[NumPy_Vectorization]] (Ufuncs are the primary mechanism for vectorization)
- [[NumPy_Broadcasting]] (Handled by ufuncs)
- [[NumPy_Data_Types]] (Ufuncs handle type promotion and casting)
- Mathematical operations, Element-wise operations

---
**Source:** Worksheet WS_NumPy (Implied), NumPy Documentation