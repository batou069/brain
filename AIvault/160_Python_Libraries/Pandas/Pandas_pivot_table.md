---
tags:
  - pandas
  - python
  - data_manipulation
  - reshaping
  - aggregation
  - function
  - concept
aliases:
  - pd.pivot_table
  - Pivot Table Pandas
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_groupby]]"
  - "[[Pandas_MultiIndex]]"
  - "[[Spreadsheet_Pivot_Table]]"
  - "[[Data_Reshaping]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `pivot_table()`

## Definition

`pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', ...)` is a Pandas function used to create a **spreadsheet-style pivot table** as a [[Pandas_DataFrame|DataFrame]]. It reshapes or summarizes data by aggregating values based on grouping keys for rows and columns.

## Key Parameters

-   **`data`**: Input `DataFrame`.
-   **`values`**: Column(s) to aggregate.
-   **`index`**: Column(s) to group by on rows.
-   **`columns`**: Column(s) to group by on columns.
-   **`aggfunc`**: Function for aggregation (e.g., `'mean'`, `'sum'`, `np.std`). Default is `'mean'`.
-   **`fill_value`**: Value to replace missing combinations.
-   **`margins`**: If `True`, add subtotals/grand total.

## How it Works (Conceptual)

1.  **Grouping:** Data grouped by unique combinations of `index` and `columns`.
2.  **Aggregation:** `aggfunc` applied to `values` for each group.
3.  **Reshaping:** Results arranged with `index` values as row index, `columns` values as column headers.

## AnyBlock Example: `pivot_table()`

[list2tab]
- Setup DataFrame
  ```python
  import pandas as pd
  import numpy as np

  data = {
      'Region': ['North', 'North', 'South', 'South', 'North', 'West', 'West', 'South'],
      'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A'],
      'Sales':,
      'Quantity':
  }
  df = pd.DataFrame(data)
  print("Original DataFrame:\n", df)
  ```
  **Output:**
  ```
  Original DataFrame:
    Region Product  Sales  Quantity
  0  North       A    100        10
  1  North       B    150        12
  2  South       A    200         8
  3  South       B    130        15
  4  North       A    120        11
  5   West       B    180        20
  6   West       A    110         9
  7  South       A    210        10
  ```

- Pivot Table: Mean Sales by Region (Rows) and Product (Columns)
  ```python
  pivot1 = pd.pivot_table(df, values='Sales', index='Region', columns='Product')
  print("\nPivot Table 1 (Mean Sales):\n", pivot1)
  ```
  **Output:**
  ```
  Pivot Table 1 (Mean Sales):
  Product      A      B
  Region
  North    110.0  150.0
  South    205.0  130.0
  West     110.0  180.0
  ```

- Pivot Table: Sum of Sales and Mean Quantity, with Margins
  ```python
  pivot2 = pd.pivot_table(df,
                          values=['Sales', 'Quantity'],
                          index='Region',
                          aggfunc={'Sales': np.sum, 'Quantity': 'mean'},
                          fill_value=0,
                          margins=True,
                          margins_name='GrandTotal')
  print("\nPivot Table 2 (Sum Sales, Mean Quantity, with Margins):\n", pivot2)
  ```
  **Output:**
  ```
  Pivot Table 2 (Sum Sales, Mean Quantity, with Margins):
                    Quantity         Sales
  Region
  North            11.000000   370
  South            11.000000   540
  West             14.500000   290
  GrandTotal       11.750000  1200
  ```

- Pivot Table: Multiple Index Levels
  ```python
  pivot3 = pd.pivot_table(df,
                          values='Sales',
                          index=['Region', 'Product'],
                          aggfunc=['sum', 'count'])
  print("\nPivot Table 3 (Sum and Count of Sales by Region & Product):\n", pivot3)
  ```
  **Output:**
  ```
  Pivot Table 3 (Sum and Count of Sales by Region & Product):
                       sum  count
                       Sales  Sales
  Region Product
  North  A           220      2
         B           150      1
  South  A           410      2
         B           130      1
  West   A           110      1
         B           180      1
  ```

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_groupby]]
- [[Pandas_MultiIndex]]
- [[Data_Reshaping]], Data Summarization
- [[Spreadsheet_Pivot_Table]]

---
**Source:** WS_Pandas_Main, Pandas Documentation