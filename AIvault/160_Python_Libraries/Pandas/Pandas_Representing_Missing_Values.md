---
tags:
  - pandas
  - python
  - data_cleaning
  - missing_data
  - concept
  - data_type
aliases:
  - Pandas Missing Data Representation
  - How Pandas Shows Missing Values
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[NumPy_NaN]]"
  - "[[None_Python]]" # Placeholder
  - "[[Pandas_NaT]]" # Placeholder (Not a Time)
  - "[[Pandas_Handling_Missing_Data]]"
  - "[[NumPy_Data_Types]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas: Representation of Missing Values

## Definition (WS_Pandas_Main Question 6)

Pandas uses different sentinels or representations for missing data depending on the data type (`dtype`) of the [[Pandas_Series|Series]] or the column in a [[Pandas_DataFrame|DataFrame]].

## Common Representations of Missing Values

[list2card|addClass(ab-col3)]
- **`np.nan` (Not a Number)**
  - **Type:** Floating-point value ([[NumPy_NaN]]).
  - **Usage:** This is the **primary way Pandas represents missing values in numerical arrays** (arrays with `float` dtypes like `float64`, `float32`).
  - **Behavior:**
    - Arithmetic operations involving `np.nan` typically result in `np.nan`.
    - `np.nan == np.nan` is `False`. Use `pd.isnull()` or `np.isnan()` to check.
  - **Automatic Upcasting:** If you introduce a missing value (e.g., `None` or `np.nan`) into an integer Series, Pandas will usually upcast the Series to a `float` dtype to accommodate `np.nan`.
  ```python
  import pandas as pd
  import numpy as np
  s_float = pd.Series([1.0, 2.5, np.nan, 4.0]) # dtype: float64
  s_int_to_float = pd.Series([1, 2, None, 4])  # dtype: float64 (None becomes NaN)
  ```

- **`None` (Python's NoneType)**
  - **Type:** Python's `None` object.
  - **Usage:** Can be used to represent missing values in Series/DataFrames with an **`object` dtype**. This is common for columns containing strings or mixed Python objects.
  - **Behavior:** `None` is treated as a missing value by functions like `isnull()`, `dropna()`, `fillna()`.
  ```python
  s_object = pd.Series(['apple', None, 'banana', 'cherry']) # dtype: object
  ```

- **`pd.NaT` (Not a Time)**
  - **Type:** Pandas-specific datetime missing value sentinel.
  - **Usage:** Represents missing values in **datetime-like arrays** (Series/DataFrames with `datetime64[ns]` or `timedelta64[ns]` dtypes).
  - **Behavior:** Analogous to `np.nan` for datetime operations.
  ```python
  s_datetime = pd.to_datetime(['2023-01-01', None, '2023-01-03'])
  # Index: DatetimeIndex(['2023-01-01', 'NaT', '2023-01-03'], dtype='datetime64[ns]', freq=None)
  # The second element is pd.NaT
  ```

- **Boolean `pd.NA` (Experimental)**
  - **Type:** Pandas' experimental nullable integer/boolean data type sentinel.
  - **Usage:** With Pandas' newer nullable data types like `pd.BooleanDtype()`, `pd.Int64Dtype()`, etc., missing values are represented by `pd.NA`.
  - **Behavior:** `pd.NA` behaves more consistently in boolean contexts compared to `np.nan`. For example, `pd.NA | True` is `True`, while `np.nan | True` might be `True` or `np.nan` depending on context.
  ```python
  # s_boolean = pd.Series([True, False, pd.NA], dtype=pd.BooleanDtype())
  # s_integer = pd.Series([1, None, 3], dtype=pd.Int64Dtype()) # None becomes pd.NA
  ```
  > [!NOTE]
  > Nullable dtypes (`BooleanDtype`, `Int64Dtype`, `StringDtype`, etc.) are designed to handle missing values more consistently within their specific type domains, avoiding automatic upcasting to `float` or `object`.

## Summary

| Data Type of Column/Series | Missing Value Representation |
| :------------------------- | :--------------------------- |
| `float` (e.g., `float64`)  | `np.nan`                     |
| `int` (e.g., `int64`)      | Upcasts to `float64` and uses `np.nan` (unless using nullable integer dtypes) |
| `bool`                     | Upcasts to `object` and uses `None`/`True`/`False`, or `object` containing `np.nan` if mixed with floats. (Unless using `BooleanDtype` which uses `pd.NA`) |
| `object` (e.g., strings)   | `None` or `np.nan`           |
| `datetime64[ns]`           | `pd.NaT`                     |
| `timedelta64[ns]`          | `pd.NaT`                     |
| `pd.BooleanDtype()`        | `pd.NA`                      |
| `pd.Int64Dtype()`, etc.    | `pd.NA`                      |
| `pd.StringDtype()`         | `pd.NA`                      |

## Related Concepts
- [[Pandas_Handling_Missing_Data]] (Methods to detect and handle these)
- [[NumPy_NaN]], [[None_Python]], [[Pandas_NaT]]
- [[NumPy_Data_Types]], Pandas Nullable Data Types
- [[Data_Cleaning]]

---
**Source:** WS_Pandas_Main, Pandas Documentation