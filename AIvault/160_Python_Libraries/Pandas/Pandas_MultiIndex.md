---
tags:
  - pandas
  - python
  - data_structure
  - indexing
  - concept
  - hierarchical_indexing
aliases:
  - MultiIndex Pandas
  - Hierarchical Indexing Pandas
  - pd.MultiIndex
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[Pandas_groupby]]"
  - "[[Pandas_pivot_table]]"
  - "[[Pandas_stack_unstack]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `MultiIndex` (Hierarchical Indexing)

## Definition

A **`MultiIndex`** in Pandas allows multiple levels of indexing on an axis (rows or columns) of a [[Pandas_DataFrame|DataFrame]] or [[Pandas_Series|Series]], enabling representation of higher-dimensional data in a 2D structure.

## Key Aspects

- **Multiple Index Levels:** An axis can have two or more levels of labels.
- **Tuple-based Indexing:** Access elements using tuples of labels.
- **Creation:** Via `pd.MultiIndex.from_arrays()`, `from_tuples()`, `from_product()`, or implicitly by `groupby()` with multiple keys, `pivot_table()`, or `set_index()` with multiple columns.
- **Slicing:** Use `.loc[]` with tuples or `slice(None)`. `pd.IndexSlice` helps.

## AnyBlock Examples: `MultiIndex`

[list2tab]
- Creating a MultiIndex Series
  ```python
  import pandas as pd
  import numpy as np
  arrays = [
      np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
      np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])
  ]
  multi_idx = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
  s = pd.Series(np.random.randn(8), index=multi_idx)
  print("Series with MultiIndex:\n", s)
  ```
  **Output:**
  ```
  Series with MultiIndex:
  first  second
  bar    one      -0.291827
         two      -0.215853
  baz    one       0.932087
         two      -0.000359
  foo    one       0.098669
         two       0.149499
  qux    one       0.247093
         two      -0.222313
  dtype: float64
  ```

- Creating a MultiIndex DataFrame
  ```python
  iterables = [['A', 'B'], ['cat', 'dog'], ['white', 'black']]
  idx = pd.MultiIndex.from_product(iterables, names=['letter', 'animal', 'color'])
  df = pd.DataFrame(np.random.randn(8, 2), index=idx, columns=['Val1', 'Val2'])
  print("\nDataFrame with MultiIndex (rows):\n", df)
  ```

- Selecting from MultiIndex DataFrame
  ```python
  # Using df from "Creating a MultiIndex DataFrame" example
  print("\nData for letter 'A':\n", df.loc['A'])
  print("\nData for ('A', 'dog'):\n", df.loc[('A', 'dog')])
  idx_slice = pd.IndexSlice
  print("\nAll 'dog's where letter is 'B':\n", df.loc[idx_slice['B', 'dog', :]])
  ```

- `set_index()` with multiple columns
  ```python
  data_simple = {'Group': ['G1','G1','G2','G2'], 'SubGroup': ['A','B','A','B'], 'Value':}
  df_simple = pd.DataFrame(data_simple)
  df_multi_from_cols = df_simple.set_index(['Group', 'SubGroup'])
  print("\nDataFrame with MultiIndex from set_index():\n", df_multi_from_cols)
  ```

## Use Cases

- Representing higher-dimensional data.
- Grouped data analysis.
- Sophisticated pivot tables.
- Time series with multiple date/time components.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]], [[Pandas_Index_Object]]
- [[Pandas_groupby]], [[Pandas_pivot_table]]
- [[Pandas_stack_unstack]]
- Hierarchical Data

---
**Source:** WS_Pandas_Main, Pandas Documentation