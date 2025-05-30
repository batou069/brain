---
tags:
  - pandas
  - python
  - data_manipulation
  - function_application
  - concept
aliases:
  - Pandas apply()
  - Pandas map()
  - Pandas applymap()
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Python_Lambda_Functions]]" # Placeholder
  - "[[NumPy_Universal_Functions]]" # For element-wise operations on NumPy arrays
worksheet: [WS_Pandas_Functions] # Assuming
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas: `apply()`, `map()`, and `applymap()`

## Definition

Pandas provides several methods for applying functions to its data structures ([[Pandas_Series|Series]] and [[Pandas_DataFrame|DataFrames]]). The choice of method depends on whether you want to apply the function element-wise, row/column-wise, or Series-wise.

## 1. `DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)`

- **Purpose:** Applies a function `func` along an axis of a DataFrame.
- **`func`**: Function to apply to each column (if `axis=0`, default) or to each row (if `axis=1`).
    - If `axis=0` (or `'index'`): `func` receives each **column as a Series**.
    - If `axis=1` (or `'columns'`): `func` receives each **row as a Series**.
- **`axis`**: Axis along which the function is applied.
    - `0` or `'index'`: Apply function to each column.
    - `1` or `'columns'`: Apply function to each row.
- **`raw`**: If `True`, passes the underlying NumPy array to `func`. Can improve performance if `func` is a NumPy ufunc.
- **`result_type`**: `'expand'`, `'reduce'`, `'broadcast'`. Controls shape of result if `func` returns list-like.
- **Return Value:** Usually a Series (if function returns a scalar per column/row) or a DataFrame (if function returns a Series per column/row).

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(3, 4), columns=['A', 'B', 'C', 'D'])

# Apply np.mean to each column (axis=0 default)
col_means = df.apply(np.mean)
print("Column means:\n", col_means)

# Apply a lambda function to each row to find max value in row
row_max = df.apply(lambda row_series: row_series.max(), axis=1)
print("\nMax value per row:\n", row_max)

# Apply a function that returns a Series
def min_max(x): # x is a Series (column or row)
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
col_min_max = df.apply(min_max) # result_type might be needed for desired shape
print("\nMin and Max per column:\n", col_min_max)
```

## 2. `Series.map(arg, na_action=None)`

- **Purpose:** Used for substituting each value in a **Series** with another value. It's an element-wise operation specific to Series.
- **`arg`**:
    - **Function:** Applied element-wise to each value in the Series.
    - **Dictionary or Series:** Values in the calling Series are replaced according to the mapping defined in `arg`. Keys not found in `arg` become `NaN`.
- **`na_action`**: If `'ignore'`, `NaN` values are not passed to the mapping function.
- **Return Value:** A new Series.

```python
s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])

# Map using a dictionary
mapping_dict = {'cat': 'kitten', 'dog': 'puppy'}
s_mapped_dict = s.map(mapping_dict) # 'rabbit' and np.nan become NaN
print("Series mapped with dict:\n", s_mapped_dict)

# Map using a function (e.g., lambda)
s_mapped_func = s.map(lambda x: str(x).upper() if pd.notnull(x) else x)
print("\nSeries mapped with function (uppercase):\n", s_mapped_func)

# Use .str accessor for pure string operations on strings
# s_upper_str = s.str.upper() # Handles NaN correctly
```

## 3. `DataFrame.applymap(func, na_action=None, **kwargs)`

- **Purpose:** Applies a function `func` **element-wise** to every element in a **DataFrame**.
- **`func`**: Function that takes a single value and returns a single value.
- **`na_action`**: If `'ignore'`, `NaN` values in the DataFrame are not passed to `func`.
- **Return Value:** A new DataFrame with the function applied to each element.
- **Deprecated (Pandas 2.1.0+):** `applymap` is deprecated. For element-wise operations on DataFrames, it's recommended to use `DataFrame.map()` (which behaves like `applymap` starting Pandas 2.1.0) or select columns and use `Series.map()` or `Series.apply()` if the function is more complex.

```python
df_numbers = pd.DataFrame([[1, 2.2, 3], [4, 5.5, 6], [7, 8.8, 9]], columns=['A','B','C'])
print("Original DataFrame for applymap:\n", df_numbers)

# Apply a function to square each element (using applymap - old way)
# df_squared = df_numbers.applymap(lambda x: x**2)
# print("\nDataFrame squared (applymap):\n", df_squared)

# Modern way for element-wise on DataFrame (using .map if func is scalar->scalar)
# or using ufuncs for numerical data
df_squared_modern = df_numbers.map(lambda x: x**2 if isinstance(x, (int, float)) else x) # More careful
# OR simply for numeric data:
df_squared_numpy = df_numbers ** 2
print("\nDataFrame squared (using element-wise power or .map):\n", df_squared_numpy)

# Applying str.upper to a DataFrame of strings
# df_strings = pd.DataFrame({'X': ['a','b'], 'Y': ['c','d']})
# df_strings_upper = df_strings.map(str.upper) # Using new DataFrame.map
# print("\nString DataFrame uppercase:\n", df_strings_upper)
```

## AnyBlock Summary Table: `apply` vs. `map` vs. `applymap`

| Method        | Operates On | Input to Function     | Primary Use Case                                 | Output Structure         |
|---------------|-------------|-----------------------|--------------------------------------------------|--------------------------|
| **`df.apply()`**| DataFrame   | Series (row or col)   | Row/Column-wise aggregations or transformations  | Series or DataFrame      |
| **`series.map()`**| Series      | Scalar (each element) | Element-wise mapping/substitution for a Series | Series                   |
| **`df.applymap()`**| DataFrame   | Scalar (each element) | Element-wise transformation for entire DataFrame | DataFrame (same shape)   |
| **`df.map()` (New)**| DataFrame | Scalar (each element) | Element-wise transformation for entire DataFrame (replaces `applymap`) | DataFrame (same shape) |

> [!NOTE]
> - For element-wise numerical operations on DataFrames/Series, often direct NumPy ufuncs or Pandas arithmetic operators (`+`, `*`, etc.) are the most efficient and idiomatic (e.g., `df * 2`, `np.sqrt(df)`).
> - For string operations on a Series, use the `.str` accessor (e.g., `series.str.lower()`).
> - `apply` is more general and powerful but can be slower than vectorized operations or `.map`/`.str` methods for specific tasks.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Python_Lambda_Functions]] (Often used with these methods)
- [[NumPy_Universal_Functions]] (Alternative for element-wise numerical tasks)
- [[NumPy_Vectorization]]
- Iteration (These methods often help avoid explicit Python loops)

---
**Source:** Pandas Documentation