---
tags:
  - pandas
  - dataframe
  - reshaping
  - pivoting
  - stacking
  - unstacking
  - melting
  - get_dummies
  - concept
  - indexing
  - multiindex
  - set_index
  - reset_index
  - indexslice
aliases:
  - DataFrame Reshaping
  - Pivot
  - Unpivot
  - Stack
  - Unstack
  - Melt
  - Dummies
  - DataFrame Advanced Indexing
  - Set Index
  - Reset Index
  - IndexSlice
  - MultiIndex Slicing
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_MultiIndex]]"
  - "[[Pandas_pivot_table]]"
  - "[[Pandas_String_Methods_Advanced]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[Pandas_loc_vs_iloc]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Reshaping Data (More Depth)

Reshaping data involves changing the layout of a [[Pandas_DataFrame]] from one format to another. This can mean pivoting rows to columns, columns to rows, or transforming data between "wide" and "long" formats. These operations are crucial for data cleaning, analysis, and preparing data for specific tools or visualizations.

[list2tab|#Reshaping Methods]
- `df.stack(level=-1, dropna=True)`
    - **Purpose:** Pivot a level of the column labels to the row index, resulting in a [[Pandas_Series]] or DataFrame with a new inner-most row level. This makes the DataFrame "taller" or "longer".
    - **Key Parameters:**
        - `level`: `int`, `str`, `list` of these, default `-1` (inner-most level). Level(s) of column labels to stack.
        - `dropna`: `bool`, default `True`. Whether to drop rows in the resulting Frame/Series with missing values. Stacking a column level onto the index will create combinations of row and column values that may not exist; `dropna=True` removes these.
    - **Returns:** `DataFrame` or `Series`.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      # DataFrame with MultiIndex columns
      header = pd.MultiIndex.from_product([['Year1', 'Year2'], ['SensorA', 'SensorB']], names=['Year', 'Sensor'])
      data = np.round(np.random.rand(3, 4) * 100)
      df_wide = pd.DataFrame(data, index=['Loc1', 'Loc2', 'Loc3'], columns=header)
      print("Original Wide DataFrame:\n", df_wide)

      # Stack the inner-most column level ('Sensor')
      df_stacked_sensor = df_wide.stack(level='Sensor')
      print("\nStacked by 'Sensor' level:\n", df_stacked_sensor)
      
      # Stack all column levels (results in a Series)
      s_stacked_all = df_wide.stack(level=['Year', 'Sensor'])
      print("\nStacked by all column levels (Series):\n", s_stacked_all)

      # Example with a simple column index
      df_simple = pd.DataFrame({'A': [1,2], 'B': [3,4]}, index=['row1', 'row2'])
      print("\nSimple DataFrame:\n", df_simple)
      stacked_simple = df_simple.stack()
      print("\nStacked Simple DataFrame:\n", stacked_simple) # Results in a Series
      ```
    - >[!note] `stack()` is often used to convert data from a "wide" format (many columns representing different variables or time points) to a "long" format (fewer columns, with one column for variable names and another for values). This is a common precursor to using tools that prefer long-format data, like `seaborn` for plotting.

- `df.unstack(level=-1, fill_value=None)`
    - **Purpose:** Pivot a level of the row index to the column labels, resulting in a DataFrame with a new inner-most column level. This makes the DataFrame "wider". It's the inverse operation of `stack()`.
    - **Key Parameters:**
        - `level`: `int`, `str`, `list` of these, default `-1` (inner-most level). Level(s) of row index to unstack.
        - `fill_value`: Scalar, optional. Value to use for missing values that arise from unstacking.
    - **Returns:** `DataFrame`.
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np
      
      # Using the stacked DataFrame from the stack() example
      header = pd.MultiIndex.from_product([['Year1', 'Year2'], ['SensorA', 'SensorB']], names=['Year', 'Sensor'])
      data = np.round(np.random.rand(3, 4) * 100)
      df_wide = pd.DataFrame(data, index=['Loc1', 'Loc2', 'Loc3'], columns=header)
      df_stacked_sensor = df_wide.stack(level='Sensor')
      print("Stacked DataFrame (input for unstack):\n", df_stacked_sensor)

      # Unstack the 'Sensor' level (which was moved to index by stack)
      df_unstacked_sensor = df_stacked_sensor.unstack(level='Sensor')
      print("\nUnstacked by 'Sensor' level:\n", df_unstacked_sensor) # Recovers original structure

      # Unstacking a specific level from a MultiIndex Series
      index = pd.MultiIndex.from_tuples([('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')], names=['Outer', 'Inner'])
      s = pd.Series(np.arange(1.0, 5.0), index=index)
      print("\nOriginal Series with MultiIndex:\n", s)
      
      df_unstacked_inner = s.unstack(level='Inner')
      print("\nUnstacked by 'Inner' level:\n", df_unstacked_inner)

      df_unstacked_outer = s.unstack(level='Outer', fill_value=0)
      print("\nUnstacked by 'Outer' level (with fill_value):\n", df_unstacked_outer)
      ```
    - >[!tip] `unstack()` is used to convert "long" format data back to "wide" format. It's particularly useful when you have a [[Pandas_MultiIndex]] on the rows and want to move one of those levels to become column headers.

- `pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`
    - **Purpose:** Unpivot a DataFrame from wide to long format. `melt` is useful when you have one or more columns that are identifiers (`id_vars`), and other columns are measures (`value_vars`). The "unpivoted" columns become two new columns: one for the variable name (`var_name`) and one for the variable value (`value_name`).
    - **Key Parameters:**
        - `frame`: `DataFrame` to melt.
        - `id_vars`: `tuple`, `list`, or `ndarray`, optional. Column(s) to use as identifier variables.
        - `value_vars`: `tuple`, `list`, or `ndarray`, optional. Column(s) to unpivot. If not specified, uses all columns that are not set as `id_vars`.
        - `var_name`: Scalar, default `None`. Name to use for the 'variable' column. If `None` it uses `frame.columns.name` or `'variable'`.
        - `value_name`: Scalar, default `'value'`. Name to use for the 'value' column.
        - `ignore_index`: `bool`, default `True`. If `True`, original index is ignored. If `False`, original index is preserved.
    - **Returns:** `DataFrame` (unpivoted).
    - **Example:**
      ```python
      import pandas as pd
      df = pd.DataFrame({'Student': ['Alice', 'Bob', 'Charlie'],
                         'Math_Score': [85, 90, 78],
                         'Science_Score': [92, 88, 95],
                         'History_Score': [80, 75, 88]})
      print("Original Wide DataFrame:\n", df)

      df_long = pd.melt(df, id_vars=['Student'], 
                        value_vars=['Math_Score', 'Science_Score', 'History_Score'],
                        var_name='Subject', value_name='Score')
      print("\nMelted (Long) DataFrame:\n", df_long)

      # If value_vars is not specified, it melts all columns not in id_vars
      df_long_auto_value_vars = pd.melt(df, id_vars=['Student'],
                                        var_name='Subject_Auto', value_name='Score_Auto')
      print("\nMelted (auto value_vars):\n", df_long_auto_value_vars)
      ```
    - >[!note] `melt` is the canonical way to transform data from a wide format (e.g., one row per subject, multiple columns for different measurements) to a long format (e.g., one row per subject-measurement combination). This is often required for statistical modeling or plotting with tools like `seaborn`. `pivot_table` is its inverse.

- `pd.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)`
    - **Purpose:** Convert categorical variable(s) into dummy/indicator variables (also known as one-hot encoding).
    - **Key Parameters:**
        - `data`: Array-like, `Series`, or `DataFrame`.
        - `prefix`: `str`, `list` of `str`, or `dict` of `str`, default `None`. String to append DataFrame column names.
        - `prefix_sep`: `str`, default `'_'`. If appending prefix, separator/delimiter to use.
        - `dummy_na`: `bool`, default `False`. Add a column to indicate NaNs, if `False` NaNs are ignored.
        - `columns`: `list-like`, default `None`. Column names in the DataFrame to be encoded. If `columns` is `None` then all columns with `object` or `category` dtype will be converted.
        - `drop_first`: `bool`, default `False`. Whether to get k-1 dummies out of k categorical levels by removing the first level. This is useful to avoid multicollinearity in some statistical models.
        - `dtype`: Data type for new columns. Only `bool` and `integer` types are supported. `bool` is default.
    - **Returns:** `DataFrame`.
    - **Example:**
      ```python
      import pandas as pd
      
      # On a Series
      s = pd.Series(['A', 'B', 'A', 'C', 'B', pd.NA])
      print("Original Series:\n", s)
      s_dummies = pd.get_dummies(s, prefix='Category', dummy_na=True)
      print("\nDummies from Series:\n", s_dummies)

      # On a DataFrame
      df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
                         'Size': ['S', 'M', 'L', 'S', 'M'],
                         'Value': [10, 15, 20, 12, 18]})
      print("\nOriginal DataFrame:\n", df)

      # Get dummies for specific columns
      df_dummies_specific = pd.get_dummies(df, columns=['Color', 'Size'], drop_first=True)
      print("\nDummies from DataFrame (specific cols, drop_first=True):\n", df_dummies_specific)

      # Get dummies for all object/category columns automatically
      df['Color'] = df['Color'].astype('category') # Ensure 'Color' is category type
      df_dummies_auto = pd.get_dummies(df, prefix_sep='-')
      print("\nDummies from DataFrame (auto, custom sep):\n", df_dummies_auto)
      ```
    - >[!tip] `pd.get_dummies()` is essential for preparing categorical data for machine learning algorithms that require numerical input. `drop_first=True` helps prevent perfect multicollinearity. For string columns that contain multiple labels within a single string (e.g., "action|comedy"), use `Series.str.get_dummies()` instead (see [[Pandas_String_Methods_Advanced]]).

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