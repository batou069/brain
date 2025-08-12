---
tags:
  - numpy
  - python
  - library
  - numerical_computing
  - data_science
  - core
aliases:
  - Numerical Python
related:
  - "[[Python]]"
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Data_Types]]"
  - "[[NumPy_Vectorization]]"
  - "[[Pandas_MOC|Pandas]]"
  - "[[SciPy_MOC|SciPy]]"
  - "[[Matplotlib_MOC|Matplotlib]]"
worksheet: [WS_NumPy] # Assuming a generic name for the NumPy worksheet
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy (Numerical Python)

## Definition

**NumPy** (Numerical Python) is a fundamental open-source library for numerical computing in [[Python]]. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays efficiently. NumPy is the cornerstone of the scientific Python ecosystem.

## Core Features

- **[[NumPy_ndarray|`ndarray` Object]]:** The heart of NumPy is its powerful N-dimensional array object (`ndarray`). This is a grid of values, all of the same type, indexed by a tuple of non-negative integers.
- **[[NumPy_Vectorization|Vectorized Operations]]:** NumPy allows performing operations on entire arrays without explicit `for` loops in Python. These operations are implemented in pre-compiled C code, leading to significant performance improvements over native Python lists.
- **[[NumPy_Broadcasting|Broadcasting]]:** A powerful mechanism that allows NumPy to work with arrays of different shapes during arithmetic operations, under certain constraints.
- **Mathematical Functions:** A vast library of mathematical functions (e.g., linear algebra, Fourier transform, random number capabilities, trigonometric, exponential, logarithmic). Many of these are implemented as [[NumPy_Universal_Functions|universal functions (ufuncs)]] that operate element-wise.
- **[[NumPy_Data_Types|Data Types (dtypes)]]:** Supports a wide variety of numerical data types (e.g., `int8`, `int32`, `float32`, `float64`, `complex`, `bool`). Homogeneous data types in arrays contribute to efficiency.
- **Integration with Other Libraries:** Serves as the foundation for many other scientific Python libraries like [[Pandas_MOC|Pandas]], [[SciPy_MOC|SciPy]], [[Matplotlib_MOC|Matplotlib]], and Scikit-learn.
- **[[NumPy_Indexing_Slicing|Indexing and Slicing]]:** Provides flexible and powerful ways to access and modify subsets of arrays.

## Why Use NumPy?

- **Performance:** Vectorized operations are much faster than equivalent Python loops due to optimized C implementations and efficient memory layout.
- **Memory Efficiency:** `ndarray`s store data more compactly than Python lists of lists, especially for numerical data, because elements are of the same type and stored contiguously.
- **Convenience:** Provides a rich set of functions for numerical tasks, reducing the amount of code a developer needs to write.
- **Foundation for Scientific Computing:** Essential for data analysis, machine learning, scientific simulation, image processing, etc., in Python.

## Installation

```bash
pip install numpy
```

## Basic Usage Example

```python
import numpy as np

# Create a NumPy array from a Python list
a = np.array()
print(f"Array a: {a}")
print(f"Type of a: {type(a)}")
print(f"Data type of elements in a: {a.dtype}")

# Create a 2x3 array of zeros
zeros_array = np.zeros((2, 3))
print(f"Zeros array:\n{zeros_array}")

# Perform vectorized operations
b = np.array()
sum_ab = a + b # Element-wise addition
print(f"a + b = {sum_ab}")

product_ab = a * b # Element-wise multiplication
print(f"a * b = {product_ab}")

# Universal function
sine_a = np.sin(a)
print(f"sin(a) = {sine_a}")

# Indexing and slicing
print(f"Element at index 2 of a: {a}")
print(f"Slice of a (index 1 to 3): {a[1:4]}")
```

## Related Concepts
- [[NumPy_ndarray]] (The core data structure)
- [[Python]] (The language NumPy extends)
- Scientific Python Ecosystem ([[Pandas_MOC|Pandas]], [[SciPy_MOC|SciPy]], [[Matplotlib_MOC|Matplotlib]])
- [[NumPy_Vectorization]], [[NumPy_Broadcasting]] (Key performance features)

---
**Source:** Worksheet WS_NumPy, NumPy Documentation