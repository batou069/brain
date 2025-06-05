---
tags:
  - pandas
  - python
  - indexing
  - selection
  - data_manipulation
  - concept
aliases:
  - .loc vs .iloc
  - Pandas loc
  - Pandas iloc
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[Pandas_Index_Object]]"
  - "[[Label_Based_Indexing]]"
  - "[[Position_Based_Indexing]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas: `.loc` vs. `.iloc`

## Definition

`.loc` and `.iloc` are the primary accessors for **label-based** and **integer position-based** indexing and selection in Pandas [[Pandas_DataFrame|DataFrames]] and [[Pandas_Series|Series]], respectively. They provide explicit and unambiguous ways to select data, avoiding potential confusion that can arise with direct bracket indexing `[]`, especially when dealing with integer-based labels.

## Why Do You Need `.loc` and `.iloc`? Can't You Index Directly? (WS_Pandas_Main Question 5)

While direct bracket indexing `df[]` *can* be used, it has some ambiguities and limitations, particularly for row selection in DataFrames:

1.  **Ambiguity with Integer Indexes:** If a DataFrame has an integer index (e.g., `0, 1, 2, ...`), `df[0]` is ambiguous: does it mean the row with *label* `0`, or the row at *integer position* `0`? Pandas tries to infer, but this can lead to errors or unexpected behavior. `.loc[0]` clearly means label `0`, and `.iloc[0]` clearly means position `0`.
2.  **Selecting Rows and Columns Simultaneously:** Direct `df[]` primarily selects columns (e.g., `df['colA']` or `df[['colA', 'colB']]`). To select rows and columns simultaneously with `[]`, you usually need to chain operations or use boolean indexing for rows first, which can be less direct than `df.loc[row_selector, col_selector]`.
3.  **Slicing Behavior:**
    -   `df.loc[start_label:end_label]`: Slicing is **inclusive** of both `start_label` and `end_label`.
    -   `df.iloc[start_pos:end_pos]`: Slicing is **exclusive** of `end_pos` (like Python list slicing).
    -   Direct `df[start:end]` attempts integer-positional slicing for rows, which can be confusing if the index is not a simple range.
4.  **Setting Values:** `.loc` and `.iloc` are the recommended ways to set values for specific slices or cells, ensuring the operation works as intended without triggering `SettingWithCopyWarning`.

**In summary, `.loc` and `.iloc` provide:**
- **Explicitness:** Clear distinction between label-based and position-based selection.
- **Power:** Robust support for selecting rows, columns, or both using various selector types (single, list, slice, boolean).
- **Consistency:** More predictable behavior across different index types.

## `.loc[]`: Label-Based Indexing

- Selects data based on **index labels** (for rows) and **column names** (for columns).
- **Syntax:** `df.loc[row_labels, column_labels]`
- **Row/Column Selectors:**
    - Single label: `'label_A'`
    - List of labels: `['label_A', 'label_C']`
    - Slice of labels: `'label_A':'label_D'` (inclusive of end label)
    - Boolean array/Series (aligned with the axis labels)
    - Callable function
- Raises `KeyError` if labels are not found.

## `.iloc[]`: Integer Position-Based Indexing

- Selects data based on **integer positions** (0-indexed).
- **Syntax:** `df.iloc[row_positions, column_positions]`
- **Row/Column Selectors:**
    - Single integer: `0`, `-1`
    - List of integers: `[0, 2, 4]`
    - Slice of integers: `0:5` (exclusive of end position)
    - Boolean array/Series (interpreted positionally)
    - Callable function
- Raises `IndexError` if positions are out of bounds.

## AnyBlock: `.loc` vs `.iloc` Comparison

[list2card|addClass(ab-col2)]
- **`.loc[]` (Label-Based)**
  - **Access by:** Index labels, Column names
  - **Slicing:** `start_label:end_label` (end is **inclusive**)
  - **Example:**
    ```python
    import pandas as pd
    df = pd.DataFrame({
        'A':, 
        'B':}, 
        index=['x','y','z'])
    #    A   B
    # x  10  40
    # y  20  50
    # z  30  60
    
    print(df.loc['y'])       # Row with label 'y'
    print(df.loc[['x','z'], 'A']) # Rows 'x','z', column 'A'
    print(df.loc['x':'y'])   # Rows 'x' through 'y' (inclusive)
    ```
- **`.iloc[]` (Integer Position-Based)**
  - **Access by:** Integer positions (0-indexed)
  - **Slicing:** `start_pos:end_pos` (end is **exclusive**)
  - **Example:**
    ```python
    # (using df from .loc example)
    print(df.iloc)      # Row at position 1 (which is 'y')
    print(df.iloc[, 0]) # Rows at pos 0,2, column at pos 0
    print(df.iloc[0:2])    # Rows at pos 0,1 (exclusive end)
    ```

## When to Use Which

- Use **`.loc`** when you know the labels of your rows/columns and want to select based on those names. This is generally more robust to changes in data order if labels are meaningful.
- Use **`.iloc`** when you need to select data based on its integer position, regardless of the labels. Useful when the index is not meaningful or when you need to perform positional operations.
- Avoid relying on `df[]` for row selection with integer indexes due to ambiguity; use `.loc` or `.iloc` instead for clarity.

---
**Source:** WS_Pandas_Main, Pandas Documentation