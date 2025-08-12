---
tags:
  - pandas
  - python
  - data_analysis
  - statistics
  - dataframe
  - series
  - function
aliases:
  - df.sum
  - df.min
  - df.max
  - df.describe Pandas
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Data_Inspection]]"
  - "[[NumPy_Aggregation_Functions]]"
  - "[[Descriptive_Statistics]]"
worksheet:
  - WS_Pandas
date_created: 2025-05-27
---
# Pandas: `sum()`, `min()`, `max()`, `describe()`

## Definition

Pandas DataFrames and Series provide several methods for calculating common descriptive statistics and aggregations. `sum()`, `min()`, `max()`, and `describe()` are among the most frequently used.

## Common Aggregation/Descriptive Methods

[list2tab]
- Setup DataFrame
	```python
	import pandas as pd
	import numpy as np
	data = {'A': [1, 2, 3, 4, 5],
	        'B': [10, 20, np.nan, 40, 50],
	        'C': [100, 200, 300, 400, 500],
	        'D': ['x', 'y', 'x', 'z', 'y']}
	df = pd.DataFrame(data)
	print("Original DataFrame:\n", df)
	```
	```
	Original DataFrame:
	   A     B    C  D
	0  1  10.0  100  x
	1  2  20.0  200  y
	2  3   NaN  300  x
	3  4  40.0  400  z
	4  5  50.0  500  y
	```
- `df.sum(axis=None, skipna=True, numeric_only=False, min_count=0, **kwargs)`
	Returns the sum of values over the requested axis.
	- **`axis`**: `0` or `'index'` (default) to sum down columns; `1` or `'columns'` to sum across rows.
	- **`skipna`**: (Default `True`) Exclude NA/null values. If `False`, `NaN` in a sum results in `NaN`.
	- **`numeric_only`**: (Default `False`, but behavior can change. Explicitly set to `True` for summing only numeric columns if desired). If `True`, only `float`, `int`, `boolean` columns are included.
	```python
	print("\nSum of each column (df.sum()):\n", df.sum(numeric_only=True))
	# A     15.0
	# B    120.0
	# C   1500.0
	# dtype: float64

	print("\nSum of each row (df.sum(axis=1, numeric_only=True)):\n", df.sum(axis=1, numeric_only=True))
	# 0    111.0
	# 1    222.0
	# 2    303.0 # NaN in B is skipped
	# 3    444.0
	# 4    555.0
	# dtype: float64
	```
- `df.min(axis=None, skipna=True, numeric_only=False, **kwargs)`
	Returns the minimum of values over the requested axis.
	- String columns are compared lexicographically.
	```python
	print("\nMin of each column (df.min()):\n", df.min(numeric_only=True)) # Excludes column 'D'
	# A      1.0
	# B     10.0
	# C    100.0
	# dtype: float64
	print("\nMin of column D (object type):\n", df['D'].min()) # Output: x

	print("\nMin of each row (df.min(axis=1, numeric_only=True)):\n", df.min(axis=1, numeric_only=True))
	# 0      1.0
	# 1      2.0
	# 2      3.0 # NaN in B is skipped
	# 3      4.0
	# 4      5.0
	# dtype: float64
	```
- `df.max(axis=None, skipna=True, numeric_only=False, **kwargs)`
	Returns the maximum of values over the requested axis.
	- String columns are compared lexicographically.
	```python
	print("\nMax of each column (df.max()):\n", df.max(numeric_only=True)) # Excludes column 'D'
	# A      5.0
	# B     50.0
	# C    500.0
	# dtype: float64
	print("\nMax of column D (object type):\n", df['D'].max()) # Output: z

	print("\nMax of each row (df.max(axis=1, numeric_only=True)):\n", df.max(axis=1, numeric_only=True))
	# 0    100.0
	# 1    200.0
	# 2    300.0 # NaN in B is skipped
	# 3    400.0
	# 4    500.0
	# dtype: float64
	```
- `df.describe(percentiles=None, include=None, exclude=None)`
	Generates descriptive statistics.
	- **For numerical data:** count, mean, std, min, 25th (Q1), 50th (median), 75th (Q3) percentiles, max.
	- **For object/categorical data (if `include='object'` or `include='all'`):** count, unique, top (most frequent value), freq (frequency of top value).
	```python
	print("\nDescriptive statistics for numerical columns (df.describe()):\n", df.describe())

	print("\nDescriptive statistics for object columns (df.describe(include=['object'])):\n",
	      df.describe(include=['object']))

	print("\nDescriptive statistics for all columns (df.describe(include='all')):\n",
	      df.describe(include='all'))
	```
	(Output for `describe` is extensive, showing a table of statistics for each applicable column).

## Notes

- Many of these functions (`sum`, `min`, `max`, `mean`, `std`, `median`, etc.) can also be applied directly to a Pandas Series: `df['column_name'].sum()`.
- The behavior with `NaN` values is generally to skip them by default (`skipna=True`).
- `numeric_only=True` is often useful when applying these to a DataFrame with mixed types to avoid errors or unintended results (like string concatenation with `sum()`).

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Data_Inspection]]
- [[NumPy_Aggregation_Functions]] (Pandas methods often use NumPy's optimized functions internally)
- [[Descriptive_Statistics]]
- [[NumPy_NaN]] (Handling of missing values)

---
**Source:** Pandas Documentation