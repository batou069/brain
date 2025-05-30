---
tags:
  - pandas
  - dataframe
  - indexing
  - multiindex
  - set_index
  - reset_index
  - indexslice
  - concept
aliases:
  - DataFrame Advanced Indexing
  - Set Index
  - Reset Index
  - IndexSlice
  - MultiIndex Slicing
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[Pandas_MultiIndex]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[Pandas_loc_vs_iloc]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Advanced Indexing

Beyond basic label and integer-location based indexing (`.loc`, `.iloc`), Pandas offers more advanced ways to set, reset, and slice using indexes, especially when dealing with [[Pandas_MultiIndex]] objects.

[list2tab|#Advanced Indexing Operations]
- `df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`
    - **Purpose:** Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length).
    - **Key Parameters:**
        - `keys`: `label` or `array-like` or `list of labels/arrays`. This parameter can be a single column key, a single array of the same length as the calling DataFrame, or a list containing an arbitrary combination of column keys and arrays.
        - `drop`: `bool`, default `True`. Delete columns to be used as the new index.
        - `append`: `bool`, default `False`. Whether to append columns to existing index.
        - `inplace`: `bool`, default `False`. Modify the DataFrame in place (do not create a new object).
        - `verify_integrity`: `bool`, default `False`. Check the new index for duplicates. This can be computationally expensive.
    - **Returns:** `DataFrame` with the new index, or `None` if `inplace=True`.
    - **Example:**
      ```python
      import pandas as pd
      data = {'alpha': ['A', 'B', 'C', 'D'],
              'num': [1, 2, 3, 4],
              'val': [100, 200, 300, 400],
              'category': ['X', 'Y', 'X', 'Y']}
      df = pd.DataFrame(data)
      print("Original DataFrame:\n", df)

      # Set 'alpha' as index
      df_idx_alpha = df.set_index('alpha')
      print("\nIndex set to 'alpha':\n", df_idx_alpha)

      # Set 'alpha' as index, keep 'alpha' as a column
      df_idx_alpha_keep = df.set_index('alpha', drop=False)
      print("\nIndex set to 'alpha' (kept as column):\n", df_idx_alpha_keep)
      
      # Set a MultiIndex using 'category' and 'alpha'
      df_multi_idx = df.set_index(['category', 'alpha'])
      print("\nMultiIndex set using 'category' and 'alpha':\n", df_multi_idx)
      # print(df_multi_idx.index) # To see the MultiIndex object

      # Append to an existing index (less common, usually start fresh or use reset_index first)
      df_with_idx = df.set_index('num')
      df_appended_idx = df_with_idx.set_index('alpha', append=True)
      print("\nAppended 'alpha' to existing 'num' index:\n", df_appended_idx)
      ```
    - >[!tip] `set_index()` is fundamental for structuring your DataFrame for efficient lookups and for creating [[Pandas_MultiIndex]] objects, which allow for hierarchical indexing.

- `df.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')`
    - **Purpose:** Reset the index, or a level of it. For a DataFrame with a regular index, `reset_index` moves the index labels into a new column (named 'index' by default) and replaces the index with a default integer index (`RangeIndex`). For a [[Pandas_MultiIndex]], you can specify which levels to move to columns.
    - **Key Parameters:**
        - `level`: `int`, `str`, `tuple`, or `list`, default `None`. Only remove the given levels from the index. Removes all levels by default.
        - `drop`: `bool`, default `False`. Do not try to insert index into DataFrame columns. This resets the index to the default integer index and *discards* the previous index.
        - `inplace`: `bool`, default `False`. Modify the DataFrame in place.
        - `col_level`: `int` or `str`, default `0`. If the columns have multiple levels, determines which level the labels are inserted into.
        - `col_fill`: `object`, default `''`. If the columns have multiple levels, determines how the other levels are named.
    - **Returns:** `DataFrame` with the new index, or `None` if `inplace=True`.
    - **Example:**
      ```python
      import pandas as pd
      data = {'alpha': ['A', 'B', 'C', 'D'],
              'val': [100, 200, 300, 400],
              'category': ['X', 'Y', 'X', 'Y']}
      df_orig = pd.DataFrame(data)
      df_multi_idx = df_orig.set_index(['category', 'alpha'])
      print("DataFrame with MultiIndex:\n", df_multi_idx)

      # Reset all levels of the index
      df_reset_all = df_multi_idx.reset_index()
      print("\nReset all index levels:\n", df_reset_all)

      # Reset only the 'alpha' level
      df_reset_alpha = df_multi_idx.reset_index(level='alpha')
      print("\nReset 'alpha' level only:\n", df_reset_alpha)

      # Reset the index and drop the original index values
      df_reset_drop = df_multi_idx.reset_index(drop=True)
      print("\nReset index and drop original index values:\n", df_reset_drop)

      # Resetting a simple index
      df_simple_idx = df_orig.set_index('alpha')
      print("\nDataFrame with simple index 'alpha':\n", df_simple_idx)
      df_simple_reset = df_simple_idx.reset_index()
      # The original index 'alpha' becomes a column, new column name is 'alpha'
      print("\nReset simple index 'alpha':\n", df_simple_reset)
      ```
    - >[!note] `reset_index()` is the inverse of `set_index()`. It's useful when you want to treat index labels as regular data columns, or when you want to revert to a simple default integer index.

- Using `pd.IndexSlice` for Complex [[Pandas_MultiIndex]] Slicing
    - **Purpose:** `pd.IndexSlice` (often aliased to `idx`) provides a more intuitive way to perform slicing on a [[Pandas_MultiIndex]] using `.loc[]`. It allows you to specify slices for different levels of the MultiIndex.
    - **Syntax:** `df.loc[idx[<level0_slice>, <level1_slice>, ...], idx[<col_level0_slice>, ...]]`
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      # Create a DataFrame with MultiIndex rows and columns
      row_idx = pd.MultiIndex.from_product([['A', 'B', 'C'], [1, 2]], names=['OuterRow', 'InnerRow'])
      col_idx = pd.MultiIndex.from_product([['X', 'Y'], ['mean', 'std']], names=['OuterCol', 'InnerCol'])
      df = pd.DataFrame(np.round(np.random.randn(6, 4), 2), index=row_idx, columns=col_idx)
      print("DataFrame with MultiIndex rows and columns:\n", df)

      idx = pd.IndexSlice

      # Select all rows for OuterRow 'A'
      slice1 = df.loc[idx['A', :], :] # or df.loc['A']
      print("\nSlice 1 (OuterRow 'A'):\n", slice1)

      # Select InnerRow 1 for all OuterRows
      slice2 = df.loc[idx[:, 1], :]
      print("\nSlice 2 (InnerRow 1 for all OuterRows):\n", slice2)

      # Select OuterRow 'B', InnerRow 2
      slice3 = df.loc[idx['B', 2], :]
      print("\nSlice 3 (OuterRow 'B', InnerRow 2):\n", slice3)

      # Select specific columns: OuterCol 'X', all InnerCols
      slice4 = df.loc[:, idx['X', :]]
      print("\nSlice 4 (OuterCol 'X', all InnerCols):\n", slice4)

      # Select specific columns: OuterCol 'Y', InnerCol 'std'
      slice5 = df.loc[:, idx['Y', 'std']]
      print("\nSlice 5 (OuterCol 'Y', InnerCol 'std'):\n", slice5)

      # Combined row and column slicing
      # OuterRow 'A' to 'B', InnerRow 1; OuterCol 'X', InnerCol 'mean'
      slice6 = df.loc[idx['A':'B', 1], idx['X', 'mean']]
      print("\nSlice 6 (Combined row/col slicing):\n", slice6)
      
      # Slicing with lists
      slice7 = df.loc[idx[['A', 'C'], 1], idx['Y', ['mean', 'std']]]
      print("\nSlice 7 (Slicing with lists):\n", slice7)
      ```
    - >[!warning] When using `pd.IndexSlice`, ensure your index is sorted for predictable slicing performance and results, especially with range slices. You can sort a MultiIndex using `df.sort_index()`.
    - `df.loc[idx["A":"C"], ...]` includes 'C', unlike typical Python slicing.

---