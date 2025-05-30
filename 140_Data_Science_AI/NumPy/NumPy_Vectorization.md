---
tags:
  - numpy
  - python
  - performance
  - concept
  - core
  - array_manipulation
aliases:
  - Vectorization (NumPy)
  - Vectorized Operations
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Universal_Functions]]"
  - "[[NumPy_Broadcasting]]"
  - "[[Python_Loops]]" # Placeholder for contrasting with
  - "[[Performance]]"
  - "[[SIMD]]" # Underlying hardware capability
worksheet: [WS_NumPy] # Implied by performance and operations
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Vectorization

## Definition

**Vectorization** in NumPy refers to the practice of performing batch operations on entire arrays (or sections of arrays) at once, without writing explicit `for` loops in Python. NumPy achieves this by using pre-compiled, highly optimized C (or Fortran) code to execute these operations, often leveraging low-level CPU features like [[SIMD]] (Single Instruction, Multiple Data) instructions. [[NumPy_Universal_Functions|Universal functions (ufuncs)]] are a key mechanism for vectorization.

## Why Vectorization?

The primary reasons for using vectorized operations in NumPy are:

1.  **Performance:**
    -   **Reduced Python Loop Overhead:** Python `for` loops have significant overhead per iteration (type checking, function call dispatch, etc.). Vectorized operations perform the loop in compiled C code, which is much faster.
    -   **Efficient Memory Access:** NumPy arrays store data contiguously, allowing C routines to access elements efficiently.
    -   **[[SIMD]] Instructions:** Modern CPUs can perform the same operation on multiple data elements simultaneously using SIMD instructions. NumPy's C routines can often leverage this.

2.  **Code Conciseness and Readability:**
    -   Vectorized code is often shorter, more closely resembling mathematical notation, and easier to read and understand once familiar with NumPy idioms, compared to explicit loops.

## How it Works (Conceptual)

Instead of:
```python
# Non-vectorized (using Python loop)
python_list_a = [1, 2, 3]
python_list_b = [4, 5, 6]
python_list_c = []
for i in range(len(python_list_a)):
    python_list_c.append(python_list_a[i] + python_list_b[i])
```

You write (vectorized):
```python
import numpy as np
numpy_array_a = np.array()
numpy_array_b = np.array()
numpy_array_c = numpy_array_a + numpy_array_b # The '+' is a ufunc call
```
The `+` operation on NumPy arrays is a call to `np.add()`, a ufunc that internally loops over the elements in optimized C code.

## Examples of Vectorized Operations

- **Arithmetic:** `a + b`, `a - b`, `a * b`, `a / b`, `a ** 2`
- **Logical:** `a > 0`, `(a > 0) & (b < 5)`
- **Mathematical Functions:** `np.sin(a)`, `np.exp(a)`, `np.sqrt(a)`
- **Conditional Assignment:** `a[a < 0] = 0` (uses [[NumPy_Boolean_Indexing]])

## AnyBlock: Performance Comparison Idea

[list2tab]
- Scenario
	Adding two large arrays of numbers.
	One version uses a Python for loop, the other uses NumPy's vectorized addition.
- Python Loop (Conceptual)
	```python
	import time
	list_a = [range(1_000_000)]
	list_b = [range(1_000_000)]
	list_c = []
	start_time = time.time()
	for i in range(len(list_a)):
	  list_c.append(list_a[i] + list_b[i])
	end_time = time.time()
	print(f"Python loop time: {end_time - start_time}s")
	```
	**Behavior:**
	- Iterates 1,000,000 times in Python.
	- Each `+` involves Python object handling.
	- Appending to list can involve reallocations.
- NumPy Vectorization
	```python
	import numpy as np
	import time
	arr_a = np.arange(1_000_000)
	arr_b = np.arange(1_000_000)
	start_time = time.time()
	arr_c = arr_a + arr_b # Vectorized!
	end_time = time.time()
	print(f"NumPy vectorized time: {end_time - start_time}s")
	```
	**Behavior:**
	- Single `+` operation delegates to highly optimized C code.
	- Loop runs in C, directly on data buffers.
	- Often utilizes SIMD.
	- **Result: Significantly faster.**

## Related Concepts
- [[NumPy_ndarray]] (Vectorization operates on these)
- [[NumPy_Universal_Functions]] (The mechanism providing vectorized functions)
- [[NumPy_Broadcasting]] (Allows vectorized operations on arrays of different but compatible shapes)
- [[Performance]], [[Time_Complexity]] (Vectorization dramatically improves these)
- [[Python_Loops]] (What vectorization aims to replace for array operations)
- [[SIMD]] (Hardware feature leveraged by vectorized code)
- C/Fortran (Languages in which NumPy's core routines are often written)

---
**Source:** Worksheet WS_NumPy (Implied), NumPy Documentation