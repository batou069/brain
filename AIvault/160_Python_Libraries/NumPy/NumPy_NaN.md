---
tags:
  - numpy
  - python
  - data_type
  - concept
  - missing_data
  - floating_point
aliases:
  - NaN
  - Not a Number (NumPy)
  - np.nan
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Data_Types]]" # NaN is a float concept
  - "[[IEEE_754]]" # Placeholder (Floating point standard)
  - "[[Missing_Data_Handling]]" # Placeholder
  - "[[np.isnan]]"
worksheet: [WS_NumPy]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy `NaN` (Not a Number)

## Definition

**`NaN`** (Not a Number) is a special floating-point value defined by the [[IEEE_754]] standard for floating-point arithmetic. In NumPy, `np.nan` represents this value. It is used to signify undefined or unrepresentable results of numerical operations, often indicating missing data or outcomes of invalid calculations (like `0/0`, `sqrt(-1)` in real numbers).

## Key Properties and Behavior

- **Floating-Point Type:** `NaN` is inherently a **floating-point** concept. You cannot have a `NaN` in a NumPy array of integer `dtype` directly (it would usually cause a type error or be converted if the array is upcast to float).
  ```python
  import numpy as np
  print(np.nan)        # Output: nan
  print(type(np.nan))  # Output: <class 'float'>
  ```
- **Comparison Anomaly:** A defining characteristic of `NaN` is that it is **not equal to anything, including itself**.
  ```python
  print(np.nan == np.nan) # Output: False
  print(np.nan != np.nan) # Output: True
  ```
  This means you cannot reliably check for `NaN` using `x == np.nan`.
- **Checking for `NaN`:** The correct way to check if a value is `NaN` is using NumPy's `np.isnan()` function.
  ```python
  val = np.nan
  print(np.isnan(val))   # Output: True
  other_val = 5.0
  print(np.isnan(other_val)) # Output: False
  ```
- **Propagation in Operations:** Arithmetic operations involving `NaN` usually result in `NaN`.
  ```python
  print(1 + np.nan)   # Output: nan
  print(np.nan * 0)   # Output: nan (some operations like 0*nan might be nan or implementation defined)
  ```
- **Aggregation Functions:** Standard NumPy aggregation functions (`np.sum`, `np.mean`, `np.min`, `np.max`, etc.) will typically return `NaN` if any of the input data contains `NaN`.
  ```python
  arr_with_nan = np.array([1.0, 2.0, np.nan, 4.0])
  print(np.sum(arr_with_nan))  # Output: nan
  print(np.mean(arr_with_nan)) # Output: nan
  ```
- **NaN-Ignoring Functions:** NumPy provides "nan-safe" versions of aggregation functions that ignore `NaN` values during calculation (e.g., `np.nansum`, `np.nanmean`, `np.nanmin`, `np.nanmax`).
  ```python
  print(np.nansum(arr_with_nan)) # Output: 7.0
  print(np.nanmean(arr_with_nan))# Output: 2.333...
  ```

## Use Cases

- Representing missing or undefined data points in numerical datasets.
- Indicating the result of mathematically undefined operations (e.g., `0.0 / 0.0`).
- Placeholder for values that need to be imputed or handled specially during data analysis.

## Related Concepts
- [[NumPy_ndarray]], [[NumPy_Data_Types]] (NaN is float)
- [[IEEE_754]] (Standard defining NaN)
- [[Missing_Data_Handling]] (NaN is a common way to represent missing values)
- [[np.isnan]] (Function to detect NaN)
- Nan-safe functions (`np.nansum`, `np.nanmean`, etc.)

## Questions / Further Study
>[!question] What is the type of `NaN`? (WS_NumPy)
> In NumPy (`np.nan`), its type is **`float`** (specifically, it's often represented internally as a `float64` if not specified otherwise by an array's `dtype`).
> ```python
> import numpy as np
> print(type(np.nan)) # Output: <class 'float'>
> arr = np.array([np.nan])
> print(arr.dtype)    # Output: float64
> ```

---
**Source:** Worksheet WS_NumPy, NumPy Documentation, IEEE 754 Standard