---
tags:
  - pandas
  - python
  - data_manipulation
  - function
  - dataframe
  - series
aliases:
  - df.drop
  - pandas drop rows
  - pandas drop columns
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Indexing_Selection]]" # For selecting what *not* to drop
  - "[[Data_Cleaning]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `DataFrame.drop()` / `Series.drop()`

## Definition

The `drop()` method in Pandas is used to remove specified labels (rows or columns) from a [[Pandas_DataFrame|DataFrame]] or elements from a [[Pandas_Series|Series]] based on their index labels.

## `DataFrame.drop()`

**Syntax:**
```python
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
```

-   **`labels`**: Single label or list-like of index/column labels to drop.
-   **`axis`**:
    -   `0` or `'index'`: Drop rows (default).
    -   `1` or `'columns'`: Drop columns.
-   **`index`**: Alternative to `labels` for dropping rows. Single label or list-like.
-   **`columns`**: Alternative to `labels` for dropping columns. Single label or list-like.
-   `level`: For MultiIndex, level from which the labels will be removed.
-   **`inplace`**: (Default `False`) If `True`, performs operation in-place and returns `None`. If `False`, returns a new DataFrame with the labels dropped.
-   `errors`: (Default `'raise'`) If `'ignore'`, suppress errors and only existing labels are dropped.

## `Series.drop()`

**Syntax:**
```python
Series.drop(labels=None, axis=0, index=None, level=None, inplace=False, errors='raise')
```
-   Similar parameters to `DataFrame.drop()`, but `axis` is implicitly `0` (or `'index'`) as Series are 1D. `columns` parameter is not applicable.

## AnyBlock Examples: `drop()`

[list2tab]
- Setup DataFrame & Series
  ```python
  import pandas as pd
  import numpy as np

  data_df = {
      'A': np.arange(1, 5),
      'B': np.arange(5, 9),
      'C': np.arange(9, 13),
      'D': ['x', 'y', 'z', 'w']
  }
  df = pd.DataFrame(data_df, index=['row1', 'row2', 'row3', 'row4'])
  print("Original DataFrame df:\n", df)

  s = pd.Series(, index=['a', 'b', 'c', 'd'], name="MySeries")
  print("\nOriginal Series s:\n", s)
  ```
  **Output:**
  ```
  Original DataFrame df:
        A  B   C  D
  row1  1  5   9  x
  row2  2  6  10  y
  row3  3  7  11  z
  row4  4  8  12  w

  Original Series s:
  a    10
  b    20
  c    30
  d    40
  Name: MySeries, dtype: int64
  ```

- Dropping Rows from DataFrame
  ```python
  # Drop a single row by label
  df_drop_row1 = df.drop(labels='row1') # or df.drop(index='row1')
  print("\nAfter dropping 'row1':\n", df_drop_row1)

  # Drop multiple rows by label
  df_drop_rows_multi = df.drop(index=['row2', 'row4'])
  print("\nAfter dropping 'row2' and 'row4':\n", df_drop_rows_multi)

  # Drop row in-place (modifies df directly)
  # df_copy = df.copy()
  # df_copy.drop('row1', inplace=True)
  # print("\nOriginal df modified after inplace drop (on copy):\n", df_copy)
  ```
  **Output (for first two):**
  ```
  After dropping 'row1':
        A  B   C  D
  row2  2  6  10  y
  row3  3  7  11  z
  row4  4  8  12  w

  After dropping 'row2' and 'row4':
        A  B   C  D
  row1  1  5   9  x
  row3  3  7  11  z
  ```

- Dropping Columns from DataFrame
  ```python
  # Drop a single column by label
  df_drop_col_B = df.drop(labels='B', axis=1) # or df.drop(columns='B')
  print("\nAfter dropping column 'B':\n", df_drop_col_B)

  # Drop multiple columns by label
  df_drop_cols_multi = df.drop(columns=['A', 'D'])
  print("\nAfter dropping columns 'A' and 'D':\n", df_drop_cols_multi)
  ```
  **Output:**
  ```
  After dropping column 'B':
        A   C  D
  row1  1   9  x
  row2  2  10  y
  row3  3  11  z
  row4  4  12  w

  After dropping columns 'A' and 'D':
        B   C
  row1  5   9
  row2  6  10
  row3  7  11
  row4  8  12
  ```

- Dropping from Series
  ```python
  # Drop a single element by label
  s_drop_b = s.drop(labels='b')
  print("\nSeries after dropping label 'b':\n", s_drop_b)

  # Drop multiple elements by label
  s_drop_multi = s.drop(labels=['a', 'd'])
  print("\nSeries after dropping labels 'a' and 'd':\n", s_drop_multi)
  ```
  **Output:**
  ```
  Series after dropping label 'b':
  a    10
  c    30
  d    40
  Name: MySeries, dtype: int64

  Series after dropping labels 'a' and 'd':
  b    20
  c    30
  Name: MySeries, dtype: int64
  ```

## Key Considerations

- **`inplace=False` by Default:** Most Pandas operations, including `drop()`, return a *new* object by default, leaving the original unchanged. This is generally safer. Use `inplace=True` with caution.
- **Specifying `axis`:** Crucial for DataFrames to distinguish between dropping rows (`axis=0`) or columns (`axis=1`). Using the `index` or `columns` parameters can be more explicit.
- **Error Handling:** If a label specified for dropping does not exist, `drop()` will raise a `KeyError` by default. Use `errors='ignore'` to suppress this, but be aware that it might hide typos or incorrect label specifications.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Indexing_Selection]] (Can be used to select data *to keep*, achieving a similar result to dropping)
- [[Data_Cleaning]], [[Data_Manipulation]]

---
**Source:** WS_Pandas_Main, Pandas Documentation