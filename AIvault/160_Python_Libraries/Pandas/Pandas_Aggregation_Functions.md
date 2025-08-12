---
tags:
  - pandas
  - python
  - data_analysis
  - aggregation
  - statistics
  - function
  - concept
aliases:
  - Pandas Aggregation
  - df.sum
  - df.min
  - df.max
  - df.mean
  - df.median
  - df.std
  - df.var
  - df.count (aggregation)
  - df.describe
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Data_Inspection]]" # .describe is also an inspection tool
  - "[[Pandas_groupby]]" # Aggregations are often used with groupby
  - "[[NumPy_Aggregation_Functions]]" # Pandas often uses NumPy's implementations
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
---
tags:
  - pandas
  - python
  - data_analysis
  - aggregation
  - statistics
  - function
  - concept
aliases:
  - Pandas Aggregation
  - df.sum
  - df.min
  - df.max
  - df.mean
  - df.median
  - df.std
  - df.var
  - df.count (aggregation)
  - df.describe
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Data_Inspection]]" # .describe is also an inspection tool
  - "[[Pandas_groupby]]" # Aggregations are often used with groupby
  - "[[NumPy_Aggregation_Functions]]" # Pandas often uses NumPy's implementations
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Aggregation Functions

## Definition

**Aggregation** in Pandas involves computing a summary statistic (like sum, mean, min, max, count) over a set of data, typically along an axis of a [[Pandas_DataFrame|DataFrame]] or for a [[Pandas_Series|Series]]. Pandas provides a rich set of built-in aggregation functions.

## Common Aggregation Functions

These functions can be applied to DataFrames (often column-wise by default) or Series.

[list2card|addClass(ab-col3)]
- **`df.sum(axis=0, skipna=True, numeric_only=False, ...)`**
  - Returns the sum of values over the requested axis.
  - `axis=0` (default): Sums down each column.
  - `axis=1`: Sums across each row.
  - `skipna=True` (default): Excludes `NaN` values.
- **`df.mean(axis=0, skipna=True, numeric_only=False, ...)`**
  - Returns the mean (average) of values.
- **`df.median(axis=0, skipna=True, numeric_only=False, ...)`**
  - Returns the median (middle value).
- **`df.min(axis=0, skipna=True, numeric_only=False, ...)`**
  - Returns the minimum value.
- **`df.max(axis=0, skipna=True, numeric_only=False, ...)`**
  - Returns the maximum value.
- **`df.std(axis=0, skipna=True, ddof=1, numeric_only=False, ...)`**
  - Returns the standard deviation. `ddof=1` for sample standard deviation (default).
- **`df.var(axis=0, skipna=True, ddof=1, numeric_only=False, ...)`**
  - Returns the variance.
- **`df.count(axis=0, numeric_only=False)`**
  - Returns the number of non-NA/null observations.
- **`df.nunique(axis=0, dropna=True)`**
  - Returns the number of unique values.
- **`df.idxmin(axis=0, skipna=True)` / `df.idxmax(axis=0, skipna=True)`**
  - Returns the index label of the first occurrence of the minimum/maximum value.
- **`df.quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear')`**
  - Returns value at the given quantile (e.g., `q=0.5` for median, `q=[0.25, 0.75]` for Q1 and Q3).
- **`df.describe(percentiles=None, include=None, exclude=None)`**
  - Generates descriptive statistics. For numerical data, includes count, mean, std, min, max, and percentiles. For object data, includes count, unique, top, and frequency. (Also covered in [[Pandas_Data_Inspection]]).

## Example: Aggregations on DataFrame

```python
import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Score1':,
    'Score2': [20, 25, 22, np.nan, 21],
    'Count':
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Sum of each numeric column
print("\nColumn Sums (df.sum()):\n", df.sum(numeric_only=True))
# Score1    66
# Score2    88.0 (NaNs are skipped by default)
# Count     660

# Mean of each numeric column
print("\nColumn Means (df.mean()):\n", df.mean(numeric_only=True))
# Score1    13.2
# Score2    22.0
# Count     132.0

# Sum across rows for numeric columns
df['RowSum'] = df.sum(axis=1, numeric_only=True)
print("\nDataFrame with RowSum:\n", df)

# Min and Max of Score1
print(f"\nMin Score1: {df['Score1'].min()}") # 10
print(f"Max Score1: {df['Score1'].max()}") # 18

# Count of non-NA values per column
print("\nNon-NA Counts (df.count()):\n", df.count())
# Category    5
# Score1      5
# Score2      4 (one NaN)
# Count       5
# RowSum      5

# Descriptive statistics
print("\nDescriptive Statistics (df.describe()):\n", df.describe())
```

## Aggregation with `groupby()`

Aggregation functions are extremely powerful when combined with [[Pandas_groupby|`df.groupby()`]] to compute statistics for different groups within the data.

```python
# Group by 'Category' and calculate mean scores
grouped_means = df.groupby('Category')[['Score1', 'Score2']].mean()
print("\nMean scores by Category:\n", grouped_means)
# Output:
#           Score1  Score2
# Category                
# A           11.0    21.5
# B           16.5    25.0
```

## `agg()` and `aggregate()` Methods

For more complex aggregations or applying multiple aggregation functions at once:
- **`df.agg(func, axis=0, *args, **kwargs)`**
- **`GroupBy.agg(func, *args, **kwargs)`**

`func` can be:
- A single function name (string): `'sum'`, `'mean'`
- A list of function names: `['sum', 'mean']`
- A dictionary mapping column names to functions or lists of functions: `{'Score1': 'mean', 'Score2': ['min', 'max']}`

```python
# Multiple aggregations on grouped data
agg_results = df.groupby('Category').agg(
    min_score1=('Score1', 'min'),
    max_score1=('Score1', 'max'),
    avg_score2=('Score2', 'mean'),
    total_count=('Count', 'sum')
)
print("\nCustom aggregations by Category:\n", agg_results)
```

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Data_Inspection]] (`.describe()` overlaps)
- [[Pandas_groupby]] (Key for grouped aggregations)
- [[NumPy_Aggregation_Functions]] (Pandas often wraps or uses these)
- Descriptive Statistics, Summary Statistics

---
**Source:** WS_Pandas_Main, Pandas Documentation