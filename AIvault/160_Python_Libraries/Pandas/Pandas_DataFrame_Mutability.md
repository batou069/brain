---
tags:
  - pandas
  - python
  - data_structure
  - concept
  - mutability
aliases:
  - Is Pandas DataFrame Mutable?
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Immutable_Object]]"
  - "[[Mutable_Object]]" # Placeholder
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `DataFrame` Mutability

## Definition of Mutability

- **[[Mutable_Object|Mutable objects]]** can be changed after they are created.
- **[[Immutable_Object|Immutable objects]]** cannot be changed after they are created. Any operation that appears to modify an immutable object actually creates a new object.

## Is a Pandas `DataFrame` Mutable or Immutable? (WS_Pandas_Main Question 4)

A Pandas [[Pandas_DataFrame|`DataFrame`]] is generally considered **mutable** in terms of its **data/values** and its **shape** (columns/rows can be added or removed). However, the [[Pandas_Index_Object|`Index` objects]] (for rows and columns) are themselves immutable.

[list2card|addClass(ab-col2)]
- **Mutable Aspects (Value/Data Mutability):**
  - **Values can be changed:** You can modify the data within the cells of a DataFrame.
    ```python
    import pandas as pd
    df = pd.DataFrame({'A':, 'B':})
    df.loc[0, 'A'] = 100 # Modifies the value
    # df is now:
    #      A  B
    # 0  100  3
    # 1    2  4
    ```
  - **Columns can be added or deleted:**
    ```python
    df['C'] = # Adds a new column 'C'
    del df['B']      # Deletes column 'B'
    # df_dropped_col = df.drop(columns=['A']) # Returns a new df, original unchanged unless inplace=True
    ```
  - **Rows can be added or deleted:**
    ```python
    # Appending rows usually creates a new DataFrame, but...
    # df.loc['new_row'] = [val1, val2] # Can add a new row (if index allows)
    # df_dropped_row = df.drop(index=['some_row']) # Returns new df unless inplace=True
    ```
    > [!NOTE]
    > While rows can be added/deleted, operations like `append()` or `drop()` often return a *new* DataFrame by default. To modify in-place, `inplace=True` is sometimes available, or direct assignment to slices (`.loc`, `.iloc`) is used.

- **Mutable Aspects (Size/Shape Mutability):**
  - The number of rows and columns can change, as shown above. This means the "shape" of the DataFrame is mutable.

- **Immutable Aspects:**
  - **[[Pandas_Index_Object|Index Objects]]:** The `df.index` and `df.columns` (which are `Index` objects) are immutable. You cannot change an individual label within an existing Index object directly (e.g., `df.index[0] = 'new_label'` will raise an error). To change index/column labels, you typically assign a *new* Index object to `df.index` or `df.columns`, or use methods like `df.rename()`.
    ```python
    # df.index = 'new_label' # TypeError: Index does not support mutable operations

    # Correct way to change index labels:
    # df.index = ['x', 'y'] # Assigns a new Index object
    # df = df.rename(index={'old_label': 'new_label'}) # Returns a new DataFrame
    ```

## Summary

- **Data/Values:** Mutable.
- **Shape (Number of Rows/Columns):** Mutable.
- **Axis Labels (Index/Columns objects themselves):** Immutable. You reassign the entire `df.index` or `df.columns` attribute to change them, or use methods like `rename` which return new DataFrames.

This distinction is important because the immutability of Index objects allows Pandas to perform efficient lookups and alignments, and enables safe sharing of Index objects between multiple DataFrames or Series. Operations that modify the data or shape often do so in-place or return new objects depending on the method and its parameters (like `inplace=True`).

---
**Source:** WS_Pandas_Main, Pandas Documentation