---
tags:
  - pandas
  - python
  - data_manipulation
  - combining_data
  - concept
  - function
aliases:
  - df.join
  - df.merge
  - Pandas Join
  - Pandas Merge
  - Combining DataFrames Pandas
related:
  - "[[Pandas_DataFrame]]"
  - "[[SQL_Joins]]"
  - "[[pd.concat]]"
  - "[[Pandas_Index_Object]]"
worksheet:
  - WS_Pandas
date_created: 2025-05-27
---
---
tags:
  - pandas
  - python
  - data_manipulation
  - combining_data
  - function
  - concept
aliases:
  - Pandas Join
  - Pandas Merge
  - df.join
  - pd.merge
  - df.merge
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_concat]]"
  - "[[SQL_Joins]]" # Placeholder, for analogy
  - "[[Pandas_Index_Object]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas: `join()` vs. `merge()`

## Definition

Both `DataFrame.join()` and `pandas.merge()` (or `DataFrame.merge()`) are Pandas functions used to combine [[Pandas_DataFrame|DataFrames]] based on common columns or indices, similar to SQL joins. However, they have different primary use cases and default behaviors.

## `DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None)`

- **Purpose:** Primarily used for combining DataFrames based on their **indices** (row labels) or on a key column in one DataFrame and the index in another.
- **Calling Convention:** It's a method of a DataFrame: `df1.join(df2, ...)`
- **Default Behavior:** Joins on the index of `df1` and the index of `df2` if `on` is not specified. Performs a **left join** by default (`how='left'`).
- **`on` parameter:** Can specify a column name or list of column names in the *calling* DataFrame (`df1`) to join on. The `other` DataFrame (`df2`) must then be joined on its index. To join on columns from both, `merge()` is generally more flexible or requires setting an index first.
- **`lsuffix`, `rsuffix`**: Suffixes to apply to overlapping column names from the left and right DataFrames, respectively.

## `pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)`
*(Also available as `DataFrame.merge(right, ...)`)*

- **Purpose:** A more general and flexible function for combining DataFrames, similar to SQL `JOIN` operations. Can join on common columns, different columns in each DataFrame, or on indices.
- **Calling Convention:** Can be a top-level Pandas function `pd.merge(df1, df2, ...)` or a DataFrame method `df1.merge(df2, ...)`.
- **Default Behavior:** Performs an **inner join** by default (`how='inner'`) on common column names found in both DataFrames.
- **Key Parameters for Joining Keys:**
    - `on`: Column name(s) to join on. Must be present in both DataFrames.
    - `left_on`, `right_on`: Column name(s) from the left and right DataFrames respectively to join on (useful if key columns have different names).
    - `left_index=True`, `right_index=True`: Use the index of the left/right DataFrame as the join key.
- **`how` parameter:** Specifies the type of merge/join:
    - `'left'`: Use keys from left frame only; include all rows from left.
    - `'right'`: Use keys from right frame only; include all rows from right.
    - `'outer'`: Use union of keys from both frames.
    - `'inner'` (default): Use intersection of keys from both frames.
    - `'cross'`: Cartesian product of rows from both frames.
- **`suffixes`**: Tuple of suffixes to apply to overlapping column names (default `('_x', '_y')`).
- **`indicator`**: If `True`, adds a column `_merge` indicating the source of each row (`left_only`, `right_only`, `both`).

## AnyBlock Comparison: `join` vs. `merge`

[list2card|addClass(ab-col2)]
- **`df1.join(df2)`**
  - **Primary Join Key:** Index-on-index by default, or calling DataFrame's column(s) on other's index.
  - **Default Join Type:** `'left'`
  - **Flexibility for Column Joins:** Less flexible if joining on different-named columns or multiple columns from both DataFrames without prior index setting.
  - **Convenience:** Simpler syntax for common index-based joins.
  - **Example (Index Join):**
    ```python
    import pandas as pd
    left = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']}, index=['K0', 'K1'])
    right = pd.DataFrame({'C': ['C0', 'C1'], 'D': ['D0', 'D1']}, index=['K0', 'K2'])
    # result = left.join(right) # Left join on index
    #   A   B    C    D
    #K0  A0  B0   C0   D0
    #K1  A1  B1  NaN  NaN
    ```

- **`pd.merge(df1, df2)` or `df1.merge(df2)`**
  - **Primary Join Key:** Common columns by default, or explicitly specified columns/indices.
  - **Default Join Type:** `'inner'`
  - **Flexibility for Column Joins:** Highly flexible; can join on same-named columns, different-named columns (`left_on`, `right_on`), indices (`left_index`, `right_index`), or combinations.
  - **Power:** More options for different join types and handling overlapping columns.
  - **Example (Column Join):**
    ```python
    import pandas as pd
    left = pd.DataFrame({'key': ['K0', 'K1'], 'A': ['A0', 'A1']})
    right = pd.DataFrame({'key': ['K0', 'K2'], 'B': ['B0', 'B1']})
    # result = pd.merge(left, right, on='key', how='outer') # Outer join on 'key' column
    #   key    A    B
    #0  K0   A0   B0
    #1  K1   A1  NaN
    #2  K2  NaN   B1
    ```

## When to Use Which

- **Use `df.join()` when:**
    - You are primarily joining on indices.
    - You want a quick left join on indices (its default behavior).
    - You are joining on a column in the calling DataFrame and the index of the other DataFrame.
- **Use `pd.merge()` (or `df.merge()`) when:**
    - You need more flexibility, similar to SQL joins.
    - Joining on one or more columns (that might have different names in each DataFrame).
    - You need different types of joins (`inner`, `outer`, `right`, `cross`).
    - Combining based on both columns and indices.

In many cases, `merge()` can do everything `join()` can do, but `join()` can be more concise for index-based joins. Many users find `merge()` more intuitive due to its explicit parameters like `left_on`, `right_on`, `left_index`, `right_index`.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Index_Object]]
- [[Pandas_concat]] (For stacking/concatenating DataFrames along an axis)
- [[SQL_Joins]] (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN - analogous concepts)
- Data Combining, Data Integration

---
**Source:** WS_Pandas_Main, Pandas Documentation