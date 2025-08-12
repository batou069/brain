---
tags:
  - pandas
  - python
  - data_manipulation
  - transformation
  - groupby
  - function
  - concept
aliases:
  - df.transform
  - GroupBy.transform
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_groupby]]"
  - "[[Pandas_Apply_Map_Applymap]]" # .apply() is more general
  - "[[Data_Transformation]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `transform()` (on GroupBy Objects)

## Definition

The `transform()` method, when applied to a Pandas `GroupBy` object, is used to perform **group-wise computations** and then **broadcast the results back to the shape of the original DataFrame or Series**. This means the output of `transform()` will have the same index as the object it was called on.

It's particularly useful for operations like:
- Standardizing data within groups (e.g., calculating z-scores per group).
- Filling missing values within groups using group-specific statistics.
- Group-wise feature engineering where the result needs to align with the original data.

## `GroupBy.transform(func, *args, engine=None, engine_kwargs=None, **kwargs)`

- **`func`**: Function to apply to each group.
    - Can be a string name of a known aggregation function (e.g., `'mean'`, `'sum'`).
    - Can be a user-defined function (UDF) or a lambda function. This function will receive each group (as a Series or DataFrame, depending on what was grouped) and **must return a scalar, a Series, or a DataFrame that can be broadcast back to the group's original shape/index.**
        - If `func` returns a scalar, that scalar is broadcast to all members of the group.
        - If `func` returns a Series, its index must align with the group's index (or be broadcastable).
- **`*args`, `**kwargs`**: Positional and keyword arguments to pass to `func`.

## Key Differences from `apply()` and `agg()` on GroupBy

| Method         | Input to Function | Output Shape                                  | Typical Use Case                                  |
| :------------- | :---------------- | :-------------------------------------------- | :------------------------------------------------ |
| **`agg()`**    | Group (Series/DF) | Reduced (one value/row per group)             | Group-wise summary statistics                     |
| **`apply()`**  | Group (Series/DF) | Flexible (scalar, Series, DF - can change shape)| Complex group-wise operations, custom aggregation |
| **`transform()`**| Group (Series/DF) | **Same shape/index as original input group**  | Broadcast group result back to original shape     |

## AnyBlock Examples: `transform()`

[list2tab]
- Setup DataFrame
  ```python
  import pandas as pd
  import numpy as np

  data = {
      'Category': ['A', 'B', 'A', 'B', 'A', 'C'],
      'Value': ,
      'Score':
  }
  df = pd.DataFrame(data)
  print("Original DataFrame:\n", df)
  ```
  **Output:**
  ```
  Original DataFrame:
    Category  Value  Score
  0        A     10    100
  1        B     12    150
  2        A     11    110
  3        B     15    130
  4        A     13    120
  5        C     20    200
  ```

- Standardizing Data within Groups (Z-score)
  ```python
  # Calculate z-score for 'Score' within each 'Category'
  # z-score = (value - group_mean) / group_std
  df['Score_Z_Grouped'] = df.groupby('Category')['Score'].transform(
      lambda x: (x - x.mean()) / x.std()
  )
  print("\nDataFrame with Grouped Z-Scores for Score:\n", df)
  ```
  **Output (Conceptual for Score_Z_Grouped):**
  ```
  %% For Category A (mean=110, std=10):
  %% Row 0: (100-110)/10 = -1.0
  %% Row 2: (110-110)/10 =  0.0
  %% Row 4: (120-110)/10 =  1.0
  %% For Category B (mean=140, std=14.14...):
  %% Row 1: (150-140)/14.14 = ~0.707
  %% Row 3: (130-140)/14.14 = ~-0.707
  %% For Category C (mean=200, std=NaN as only one value):
  %% Row 5: NaN
  DataFrame with Grouped Z-Scores for Score:
    Category  Value  Score  Score_Z_Grouped
  0        A     10    100        -1.000000
  1        B     12    150         0.707107
  2        A     11    110         0.000000
  3        B     15    130        -0.707107
  4        A     13    120         1.000000
  5        C     20    200              NaN
  ```

- Filling Missing Values with Group Mean
  ```python
  df_with_nan = df.copy()
  df_with_nan.loc[1, 'Score'] = np.nan # Introduce a NaN
  print("\nDataFrame with NaN:\n", df_with_nan)

  # Fill NaN in 'Score' with the mean 'Score' of its 'Category'
  df_with_nan['Score_Filled'] = df_with_nan.groupby('Category')['Score'].transform(
      lambda x: x.fillna(x.mean())
  )
  print("\nDataFrame with NaNs filled by Group Mean:\n", df_with_nan)
  ```
  **Output (Conceptual for Score_Filled):**
  ```
  %% For Category B, original scores were [NaN, 130]. Mean of non-NaN is 130.
  %% So, NaN in row 1, Score_Filled becomes 130.
  DataFrame with NaNs filled by Group Mean:
    Category  Value  Score  Score_Z_Grouped  Score_Filled
  0        A     10  100.0        -1.000000         100.0
  1        B     12    NaN         0.707107         130.0
  2        A     11  110.0         0.000000         110.0
  3        B     15  130.0        -0.707107         130.0
  4        A     13  120.0         1.000000         120.0
  5        C     20  200.0              NaN         200.0
  ```
- Using a String Function Name
  ```python
  # Add the mean 'Value' of each 'Category' as a new column
  df['Category_Mean_Value'] = df.groupby('Category')['Value'].transform('mean')
  print("\nDataFrame with Category Mean Value:\n", df)
  ```
  **Output:**
  ```
  DataFrame with Category Mean Value:
    Category  Value  Score  Score_Z_Grouped  Category_Mean_Value
  0        A     10    100        -1.000000            11.333333
  1        B     12    150         0.707107            13.500000
  2        A     11    110         0.000000            11.333333
  3        B     15    130        -0.707107            13.500000
  4        A     13    120         1.000000            11.333333
  5        C     20    200              NaN            20.000000
  ```

## When to Use `transform()`

- When you need to compute a group-specific value and then use that value to transform each member of the group, aligning the result back to the original DataFrame's index.
- Common for creating new features based on group statistics (e.g., deviation from group mean, percentage of group total).

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]], [[Pandas_groupby]]
- [[Pandas_Aggregation_Functions]] (`.agg()` is for summary statistics per group)
- [[Pandas_Apply_Map_Applymap]] (`.apply()` on GroupBy is more general but can achieve similar results if it returns a correctly indexed Series/DataFrame)
- [[Data_Transformation]], Feature Engineering

---
**Source:** WS_Pandas_Main, Pandas Documentation