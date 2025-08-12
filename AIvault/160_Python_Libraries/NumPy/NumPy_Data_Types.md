---
tags:
  - numpy
  - python
  - data_type
  - concept
  - memory
aliases:
  - NumPy dtypes
  - dtypes
related:
  - "[[NumPy]]"
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Array_vs_List]]" # Homogeneity
  - "[[Data_Types_C]]" # Similar concept of fixed-size types
  - "[[Type_Casting_NumPy]]" # Placeholder
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Data Types (dtypes)

## Definition

In [[NumPy]], the **data type** (or **`dtype`**) of an `ndarray` specifies the kind of data its elements represent (e.g., integer, floating-point, boolean, complex) and the amount of memory each element occupies. Unlike Python `list`s, all elements in a single NumPy `ndarray` must have the **same data type**. This homogeneity is crucial for NumPy's performance and memory efficiency.

## Key Aspects

- **Homogeneity:** All elements in an array share the same `dtype`.
- **Fixed Size:** Each `dtype` has a fixed size in bytes (e.g., `int32` uses 4 bytes, `float64` uses 8 bytes).
- **`dtype` Object:** A special object in NumPy (`numpy.dtype`) that describes the data type. It contains information like:
    - Type (e.g., integer, float)
    - Size (in bytes)
    - Byte order (endianness)
- **Specification:** Data types can be specified when creating arrays using strings, Python types, or NumPy `dtype` objects:
    - `np.array([1, 2], dtype='int16')`
    - `np.array([1, 2], dtype=np.int16)`
    - `np.zeros(5, dtype=float)`
- **Default Data Type:** If not specified, NumPy attempts to infer a suitable `dtype` from the input data. For integers, it often defaults to the platform's native integer size (e.g., `int64` on a 64-bit system or `int32` on a 32-bit system). For floating-point numbers, it usually defaults to `float64`. See [[NumPy_Default_Data_Type]].
- **Type Promotion:** During operations involving arrays of different dtypes, NumPy may promote one or both arrays to a more general type to avoid data loss (e.g., `int32` + `float32` results in `float32` or `float64`).

## Common NumPy Data Types (WS_NumPy Question 4)

NumPy offers a wide range of numerical data types. Here are some common ones and their differences:

| NumPy `dtype` String | Alias / Python Type | Description                                   | Size (Typical Bytes) | Range (Approximate) Example                 |
| :------------------- | :------------------ | :-------------------------------------------- | :------------------- | :------------------------------------------ |
| `'bool'`             | `bool`, `np.bool_`  | Boolean (True or False)                       | 1                    | True, False                                 |
| `'int8'`             | `np.int8`           | 8-bit signed integer                          | 1                    | -128 to 127                                 |
| `'uint8'`            | `np.uint8`          | 8-bit unsigned integer                        | 1                    | 0 to 255                                    |
| `'int16'`            | `np.int16`          | 16-bit signed integer                         | 2                    | -32,768 to 32,767                           |
| `'uint16'`           | `np.uint16`         | 16-bit unsigned integer                       | 2                    | 0 to 65,535                                 |
| `'int32'`            | `int`, `np.int32`   | 32-bit signed integer                         | 4                    | -2.1B to 2.1B                               |
| `'uint32'`           | `np.uint32`         | 32-bit unsigned integer                       | 4                    | 0 to 4.2B                                   |
| `'int64'`            | `np.int64`          | 64-bit signed integer                         | 8                    | -9E18 to 9E18                               |
| `'uint64'`           | `np.uint64`         | 64-bit unsigned integer                       | 8                    | 0 to 1.8E19                                 |
| `'intc'`             | `np.intc`           | C `int` (platform dependent, usually `int32` or `int64`) | Platform Dep.        | Platform Dep.                               |
| `'intp'`             | `np.intp`           | Integer for indexing (platform dependent, same as `ssize_t`) | Platform Dep.        | Platform Dep.                               |
| `'float16'`          | `np.float16`        | Half-precision float                          | 2                    | Limited range/precision                     |
| `'float32'`          | `float`, `np.float32`| Single-precision float                        | 4                    | Approx. ±3.4e38, ~7 decimal digits precision |
| `'float64'`          | `np.float64`, `np.double`| Double-precision float (Python `float` default) | 8                    | Approx. ±1.8e308, ~15-17 decimal digits precision |
| `'float_'`           | `np.float_`         | Shorthand for `float64`                       | 8                    | Same as `float64`                           |
| `'complex64'`        | `np.complex64`      | Complex number (two `float32`s)               | 8                    | Complex numbers                             |
| `'complex128'`       | `np.complex128`, `np.complex_`| Complex number (two `float64`s)       | 16                   | Complex numbers                             |
| `'S<N>'`             | `np.string_`        | Fixed-length byte string (N = length)         | N                    | e.g., `'S5'` is a 5-byte string            |
| `'U<N>'`             | `np.unicode_`       | Fixed-length Unicode string (N = length in characters, actual bytes depend on encoding/platform) | N * (char_size) | e.g., `'U10'` is a 10-char Unicode string  |
| `'object'`           | `object`, `np.object_`| Python object                                 | Ptr Size             | Can hold any Python object (loses NumPy performance benefits) |

**Differences:**
- **Size:** Affects memory usage and potential range of values.
- **Signed vs. Unsigned (Integers):** Determines if negative numbers can be represented.
- **Precision (Floats):** `float32` (single) has less precision and smaller range than `float64` (double). `float16` is even more limited.
- **`intc`, `intp`:** Platform-dependent sizes matching C types, useful for interoperability.
- **Fixed-Length Strings (`S`, `U`):** Store strings with a predefined maximum length.
- **`object` dtype:** Allows storing arbitrary Python objects, sacrificing NumPy's performance and memory benefits for elements stored this way. It essentially makes the `ndarray` behave more like a Python list of pointers.

## Related Concepts
- [[NumPy]], [[NumPy_ndarray]]
- [[NumPy_Array_vs_List]] (Homogeneity is a key differentiator)
- [[Data_Types_C]] (Conceptual similarity)
- [[Type_Casting_NumPy]] (Changing dtypes)
- [[Memory_Management]] (Dtypes determine memory layout)

## Questions / Further Study
>[!question] What is the default data type in NumPy? (WS_NumPy)
> If no `dtype` is specified during array creation:
> - For **integer** inputs, NumPy typically defaults to `np.int_`, which is an alias for the C `long` type on the platform (usually `np.int32` on 32-bit systems and `np.int64` on 64-bit systems).
> - For **floating-point** inputs, NumPy typically defaults to `np.float_`, which is an alias for `np.float64` (double-precision, same as Python's `float`).
> - If the input contains a mix of integers and floats, the array will be promoted to a float type.
> - If the input contains strings that cannot be converted to numbers, it might become an `object` dtype or a fixed-length string dtype.

>[!question] Why are data types so important in NumPy? Can you convert data types? How does it work? (WS_NumPy)
> **Importance:**
> 1.  **Performance:** Homogeneous data types allow NumPy to store data in contiguous memory blocks. This enables optimized C/Fortran routines to perform vectorized operations very quickly, without the type-checking overhead of Python loops on heterogeneous lists.
> 2.  **Memory Efficiency:** Storing raw numbers (e.g., a 4-byte integer) is much more memory-efficient than storing Python `int` objects, which have significant overhead.
> 3.  **Correctness:** Ensures that operations are performed as expected for numerical computations (e.g., arithmetic operations).
> **Conversion:** Yes, you can convert data types using:
> - **`astype()` method:** This is the primary way. It creates a *new array* with the specified data type, copying the data and converting it.
>   ```python
>   arr_int = np.array()
>   arr_float = arr_int.astype(np.float64)
>   arr_str = arr_float.astype('U3') # Convert to Unicode string of length 3
>   ```
> - **When creating an array:** Specify `dtype` argument: `np.array([1.0, 2.7, 3.1], dtype=np.int32)` (will truncate floats).
> **How it Works:**
> - When converting, NumPy attempts to interpret the existing values as the new type.
> - **Widening conversion** (e.g., `int` to `float`, `float32` to `float64`) is usually safe and preserves information.
> - **Narrowing conversion** (e.g., `float` to `int`, `int64` to `int8`) can lead to **data loss or truncation**:
>     - `float` to `int`: Fractional part is truncated (e.g., `3.9` becomes `3`).
>     - Larger int to smaller int: Values may wrap around or be clipped if they exceed the range of the new type (behavior can depend on casting rules like `'safe'`, `'unsafe'`).
>     - Number to String: Converts the number to its string representation.
>     - String to Number: Attempts to parse the string; fails if not a valid number representation for the target type.

---
**Source:** Worksheet WS_NumPy, NumPy Documentation