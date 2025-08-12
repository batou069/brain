---
tags:
  - pandas
  - python
  - data_manipulation
  - function
  - concept
  - dataframe
  - series
aliases:
  - df.rename
  - Series.rename
  - Pandas Rename Columns
  - Pandas Rename Index
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[Data_Cleaning]]"
  - "[[Data_Preprocessing]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `rename()`

## Definition

The `rename()` method in Pandas is used to alter axis labels (row index labels or column names) of a [[Pandas_DataFrame|DataFrame]] or the index labels of a [[Pandas_Series|Series]]. It can rename labels using a mapping (dictionary or Series) or a function.

## `DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')`
## `Series.rename(index=None, inplace=False, level=None, name=None)`

- **`mapper`**: Dictionary-like or function to apply to the labels of the axis specified by `axis`.
- **`index`**: Dictionary-like or function to apply to the row index labels. Alternative to `mapper` with `axis=0`.
- **`columns`**: Dictionary-like or function to apply to the column labels. Alternative to `mapper` with `axis=1`.
- **`axis`**: (Default `0` or `'index'`) The axis to target for renaming if `mapper` is used. `0` for index, `1` for columns.
- **`inplace`**: (Default `False`) If `True`, modifies the object in-place.
- **`level`**: For MultiIndex, specifies the level to rename.
- **`errors`**: (Default `'ignore'`) If `'raise'`, will raise `KeyError` if a label in the mapper is not found in the axis. `'ignore'` will silently skip non-existent labels.
- **`name` (Series only)**: Scalar to set as the new name of the Series.

## AnyBlock Examples: `rename()`

[list2tab]
- Setup
  ```python
  import pandas as pd
  df = pd.DataFrame({
      'Alpha':,
      'Beta':,
      'Gamma':
  }, index=['row_x', 'row_y', 'row_z'])
  print("Original DataFrame:\n", df)

  s = pd.Series(, index=['old_a', 'old_b', 'old_c'], name="Values")
  print("\nOriginal Series:\n", s)
  ```

- Renaming Columns in DataFrame
  ```python
  # Using a dictionary for 'columns' parameter
  df_renamed_cols = df.rename(columns={'Alpha': 'Col_A', 'Beta': 'Col_B'})
  print("\nDataFrame with columns renamed (dict):\n", df_renamed_cols)

  # Using a function for 'columns' (e.g., convert to lowercase)
  df_cols_lower = df.rename(columns=str.lower)
  print("\nDataFrame with columns to lowercase (function):\n", df_cols_lower)
  ```
  **Output:**
  ```
  DataFrame with columns renamed (dict):
         Col_A  Col_B  Gamma
  row_x      1      4      7
  row_y      2      5      8
  row_z      3      6      9

  DataFrame with columns to lowercase (function):
         alpha  beta  gamma
  row_x      1     4      7
  row_y      2     5      8
  row_z      3     6      9
  ```

- Renaming Index Labels in DataFrame
  ```python
  # Using a dictionary for 'index' parameter
  df_renamed_index = df.rename(index={'row_x': 'X', 'row_z': 'Z'})
  print("\nDataFrame with index renamed (dict):\n", df_renamed_index)

  # Using a function for 'index' (e.g., add prefix)
  df_index_prefixed = df.rename(index=lambda label: "idx_" + label)
  print("\nDataFrame with index prefixed (function):\n", df_index_prefixed)
  ```
  **Output:**
  ```
  DataFrame with index renamed (dict):
         Alpha  Beta  Gamma
  X          1     4      7
  row_y      2     5      8
  Z          3     6      9

  DataFrame with index prefixed (function):
             Alpha  Beta  Gamma
  idx_row_x      1     4      7
  idx_row_y      2     5      8
  idx_row_z      3     6      9
  ```

- Renaming Index Labels in Series
  ```python
  # Using a dictionary
  s_renamed_dict = s.rename({'old_a': 'new_A', 'old_c': 'new_C'})
  print("\nSeries with index renamed (dict):\n", s_renamed_dict)

  # Using a function
  s_renamed_func = s.rename(lambda x: x.upper().replace("OLD_", ""))
  print("\nSeries with index renamed (function):\n", s_renamed_func)
  ```
  **Output:**
  ```
  Series with index renamed (dict):
  new_A    10
  old_b    20
  new_C    30
  Name: Values, dtype: int64

  Series with index renamed (function):
  A    10
  B    20
  C    30
  Name: Values, dtype: int64
  ```
- Renaming Series Name
  ```python
  s_new_name = s.rename("New Series Name")
  print("\nSeries with new name:\n", s_new_name)
  print(f"New Series name attribute: {s_new_name.name}")
  ```
  **Output:**
  ```
  Series with new name:
  old_a    10
  old_b    20
  old_c    30
  Name: New Series Name, dtype: int64
  New Series name attribute: New Series Name
  ```

## Key Considerations

- **Returns New Object:** By default (`inplace=False`), `rename()` returns a new DataFrame or Series with the modified labels, leaving the original object unchanged.
- **Mapping vs. Function:** Dictionaries are useful for specific, targeted renames. Functions are good for applying a consistent transformation to all labels on an axis.
- **`axis` parameter:** For DataFrames, when using the `mapper` argument, you must specify `axis='index'` (or `0`) or `axis='columns'` (or `1`). Using the dedicated `index` or `columns` arguments is often clearer.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]], [[Pandas_Index_Object]]
- [[Data_Cleaning]], [[Data_Preprocessing]], [[Data_Manipulation]]
- Python Dictionaries, Lambda Functions (Used for mapping)

---
**Source:** WS_Pandas_Main, Pandas Documentation