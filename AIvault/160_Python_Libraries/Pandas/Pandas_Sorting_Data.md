---
tags:
  - pandas
  - dataframe
  - series
  - sorting
  - concept
aliases:
  - DataFrame Sorting
  - Series Sorting
  - Sort Values
  - Sort Index
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Sorting Data

Pandas DataFrames and Series can be sorted by their values or by their index. This is crucial for data analysis, presentation, and for certain types of operations that require sorted data.

[list2tab]
- `df.sort_values()`
    - **Purpose:** Sort a DataFrame or Series by its values.
    - **Key Parameters:**
        - `by`: `str` or `list` of `str`. Name or list of names to sort by. If `axis` is 0 or 'index', then `by` may contain index levels and/or column labels. If `axis` is 1 or 'columns', then `by` may contain column levels and/or index labels.
        - `axis`: `{0 or 'index', 1 or 'columns'}`, default `0`. Axis to be sorted.
        - `ascending`: `bool` or `list` of `bool`, default `True`. Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, it must match the length of the `by`.
        - `inplace`: `bool`, default `False`. If `True`, perform operation in-place.
        - `kind`: `{'quicksort', 'mergesort', 'heapsort', 'stable'}`, default `'quicksort'`. Choice of sorting algorithm. `stable` is an alias for `mergesort`. For DataFrames, this option is only applied when sorting on a single column or label.
        - `na_position`: `{'first', 'last'}`, default `'last'`. Puts NaNs at the beginning if `first`; `last` puts NaNs at the end.
    - **Returns:** DataFrame or Series, sorted by values.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      data = {'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
              'col2': [2, 1, 9, 8, 7, 4],
              'col3': [0, 1, 9, 4, 2, 3]}
      df = pd.DataFrame(data)

      # Sort by 'col1'
      df_sorted_col1 = df.sort_values(by='col1')
      print("Sorted by col1 (NaNs last by default):\n", df_sorted_col1)

      # Sort by 'col1' with NaNs first
      df_sorted_col1_nan_first = df.sort_values(by='col1', na_position='first')
      print("\nSorted by col1 (NaNs first):\n", df_sorted_col1_nan_first)

      # Sort by 'col2' descending
      df_sorted_col2_desc = df.sort_values(by='col2', ascending=False)
      print("\nSorted by col2 descending:\n", df_sorted_col2_desc)

      # Sort by multiple columns
      df_sorted_multi = df.sort_values(by=['col1', 'col2'], ascending=[True, False])
      print("\nSorted by col1 (asc) then col2 (desc):\n", df_sorted_multi)
      ```
    - >[!note] Sorting on multiple columns can be powerful for creating well-ordered views of your data.

- `df.sort_index()`
    - **Purpose:** Sort a DataFrame or Series by its index labels.
    - **Key Parameters:**
        - `axis`: `{0 or 'index', 1 or 'columns'}`, default `0`. Axis to be sorted.
        - `level`: `int` or `level name` or `list of ints` or `list of level names`. If not `None`, sort on values in specified index level(s).
        - `ascending`: `bool`, default `True`. Sort ascending vs. descending.
        - `inplace`: `bool`, default `False`. If `True`, perform operation in-place.
        - `kind`: `{'quicksort', 'mergesort', 'heapsort', 'stable'}`, default `'quicksort'`. Choice of sorting algorithm. `stable` is an alias for `mergesort`.
        - `na_position`: `{'first', 'last'}`, default `'last'`. Puts NaNs at the beginning if `first`; `last` puts NaNs at the end. (Note: Only relevant if the index contains NaNs).
        - `sort_remaining`: `bool`, default `True`. If `True` and sorting by level and index is multilevel, sort by other levels too (in order) after sorting by specified level.
    - **Returns:** DataFrame or Series, sorted by index.
    - **Example:**
      ```python
      import pandas as pd

      data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
      df = pd.DataFrame(data, index=[10, 5, 8])
      print("Original DataFrame:\n", df)

      # Sort by index ascending
      df_sorted_index = df.sort_index()
      print("\nSorted by index ascending:\n", df_sorted_index)

      # Sort by index descending
      df_sorted_index_desc = df.sort_index(ascending=False)
      print("\nSorted by index descending:\n", df_sorted_index_desc)

      # Sorting columns by their names (axis=1)
      df_sorted_columns = df.sort_index(axis=1, ascending=False)
      print("\nColumns sorted descending:\n", df_sorted_columns)

      # MultiIndex example
      arrays = [
          ['foo', 'foo', 'bar', 'bar'],
          ['one', 'two', 'one', 'two']
      ]
      index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
      s = pd.Series(np.random.randn(4), index=index)
      print("\nOriginal Series with MultiIndex:\n", s)
      s_sorted_level1 = s.sort_index(level='second')
      print("\nSorted by 'second' level of MultiIndex:\n", s_sorted_level1)
      ```
    - >[!tip] `sort_index()` is essential when the order of rows or columns based on their labels is important, especially after operations that might disorder them, like concatenation or merging with unaligned indexes.

## Use Case
Ordering data is a fundamental step in data processing and analysis.
- **Analysis:** Many analytical techniques require or benefit from sorted data (e.g., time series analysis, cumulative distributions).
- **Presentation:** Sorted data is often easier to read and understand in tables and reports.
- **Performance:** Some algorithms perform better on sorted data.
- **Duplicate Detection:** Sorting can make it easier to identify duplicate rows.
- **Joining/Merging:** While not strictly necessary for Pandas joins/merges (as they handle alignment), presorting can sometimes be a preliminary step in understanding data before combining.

---