---
tags:
  - pandas
  - python
  - indexing
  - selection
  - data_manipulation
  - performance
  - concept
aliases:
  - df.at
  - df.iat
  - Pandas Fast Scalar Access
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_loc_vs_iloc]]"
  - "[[Label_Based_Indexing]]"
  - "[[Position_Based_Indexing]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `.at[]` and `.iat[]` (Fast Scalar Access)

## Definition

Pandas provides two specialized accessors, `.at[]` and `.iat[]`, for **fast access to a single scalar value** within a [[Pandas_DataFrame|DataFrame]] or [[Pandas_Series|Series]]. They are optimized for retrieving or setting individual elements and are generally faster for this specific purpose than using `.loc[]` or `.iloc[]`.

1.  **`.at[]` (Label-based Scalar Access):**
    -   Accesses a single value using **row and column labels**.
    -   Syntax: `df.at[row_label, column_label]` or `series.at[label]`

2.  **`.iat[]` (Integer Position-based Scalar Access):**
    -   Accesses a single value using **integer positions** (0-indexed).
    -   Syntax: `df.iat[row_position, column_position]` or `series.iat[position]`

## Key Characteristics

- **Scalar Only:** Designed strictly for accessing or setting a *single* value. They cannot be used for slicing or selecting multiple elements.
- **Performance:** Generally faster than `.loc[]` or `.iloc[]` for single-value access because they bypass some of the more complex indexing logic required for handling slices, lists, or boolean arrays.
- **Label vs. Position:**
    - `.at[]` uses labels (like `.loc[]` for scalars).
    - `.iat[]` uses integer positions (like `.iloc[]` for scalars).
- **Direct Value Access:** Returns the actual scalar value, not a Series or DataFrame containing a single value.
- **Setting Values:** Can be used on the left side of an assignment to set a single cell's value.

## AnyBlock Examples: `.at` and `.iat`

[list2tab]
- Setup
  ```python
  import pandas as pd
  df = pd.DataFrame({
      'A':,
      'B':,
      'C':
  }, index=['x', 'y', 'z'])
  print("Original DataFrame df:\n", df)

  s = pd.Series(, index=['a', 'b', 'c'])
  print("\nOriginal Series s:\n", s)
  ```
  **Output:**
  ```
  Original DataFrame df:
      A   B   C
  x  10  40  70
  y  20  50  80
  z  30  60  90

  Original Series s:
  a    100
  b    200
  c    300
  dtype: int64
  ```

- Using `.at[]` (Label-based)
  ```python
  # Get a single value from DataFrame
  val_df_at = df.at['y', 'B']
  print(f"\nValue at df.at['y', 'B']: {val_df_at}") # Output: 50

  # Set a single value in DataFrame
  df.at['z', 'C'] = 999
  print("\nDataFrame after df.at['z', 'C'] = 999:\n", df)

  # Get a single value from Series
  val_s_at = s.at['b']
  print(f"\nValue at s.at['b']: {val_s_at}") # Output: 200

  # Set a single value in Series
  s.at['a'] = 101
  print("\nSeries after s.at['a'] = 101:\n", s)
  ```
  **Output (Relevant Parts):**
  ```
  Value at df.at['y', 'B']: 50

  DataFrame after df.at['z', 'C'] = 999:
      A   B    C
  x  10  40   70
  y  20  50   80
  z  30  60  999

  Value at s.at['b']: 200

  Series after s.at['a'] = 101:
  a    101
  b    200
  c    300
  dtype: int64
  ```

- Using `.iat[]` (Integer Position-based)
  ```python
  # Get a single value from DataFrame
  val_df_iat = df.iat # Row at pos 1 ('y'), Col at pos 2 ('C')
  print(f"\nValue at df.iat: {val_df_iat}") # Output: 80 (before modification by .at) or 999 (if run after .at example)

  # Set a single value in DataFrame
  df.iat = 11
  print("\nDataFrame after df.iat = 11:\n", df)

  # Get a single value from Series
  val_s_iat = s.iat # Element at pos 2 (label 'c')
  print(f"\nValue at s.iat: {val_s_iat}") # Output: 300

  # Set a single value in Series
  s.iat = 202
  print("\nSeries after s.iat = 202:\n", s)
  ```
  **Output (Relevant Parts, assuming df and s from previous `.at` modifications):**
  ```
  Value at df.iat: 80 %% Or 999 if run sequentially after .at example modification

  DataFrame after df.iat = 11:
      A   B    C
  x  11  40   70
  y  20  50   80
  z  30  60  999

  Value at s.iat: 300

  Series after s.iat = 202:
  a    101
  b    202
  c    300
  dtype: int64
  ```

## When to Use

- Use `.at[]` or `.iat[]` when you need to get or set a **single specific value** and performance for this operation is critical.
- For selecting slices, multiple elements, or using boolean conditions, stick to `.loc[]` and `.iloc[]`.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Indexing_Selection]] (General overview)
- [[Pandas_loc_vs_iloc]] (Comparison with general-purpose indexers)
- [[Label_Based_Indexing]], [[Position_Based_Indexing]]
- [[Performance]] (These accessors are optimized for scalar access)

---
**Source:** WS_Pandas_Main, Pandas Documentation