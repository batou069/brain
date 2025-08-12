---
tags:
  - pandas
  - python
  - data_manipulation
  - dataframe
  - series
  - function
aliases:
  - df.drop
  - pd.DataFrame.drop
  - pd.Series.drop
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[Pandas_Data_Cleaning]]"
worksheet:
  - WS_Pandas
date_created: 2025-05-27
---
# Pandas `drop()` Method

## Definition

The `drop()` method in Pandas is used to remove specified labels (rows or columns) from a [[Pandas_Series|Series]] or [[Pandas_DataFrame|DataFrame]].

## Syntax

**For DataFrame:**
```python
DataFrame.drop(
    labels=None,      # Single label or list-like of labels to drop
    axis=0,           # 0 or 'index' for rows, 1 or 'columns' for columns
    index=None,       # Alternative to labels for rows (axis=0)
    columns=None,     # Alternative to labels for columns (axis=1)
    level=None,       # For MultiIndex, level from which to drop labels
    inplace=False,    # If True, modifies DataFrame in place and returns None
    errors='raise'    # If 'ignore', suppress errors and only existing labels are dropped
)
```

**For Series:**
```python
Series.drop(
    labels=None,      # Single label or list-like
    axis=0,           # Must be 0 or 'index' for Series
    index=None,       # Alternative to labels
    level=None,
    inplace=False,
    errors='raise'
)
```

## Key Parameters

- **`labels`**: The row/column label(s) to drop.
- **`axis`**: `0` or `'index'` to drop rows (default); `1` or `'columns'` to drop columns. For a Series, `axis` is implicitly `0`.
- **`index`**: Single label or list-like. Alternative to specifying `axis=0` or `axis='index'`.
- **`columns`**: Single label or list-like. Alternative to specifying `axis=1` or `axis='columns'`.
- **`inplace`**: If `True`, the operation is done on the DataFrame/Series itself, and `None` is returned. If `False` (default), a new DataFrame/Series with the labels dropped is returned, and the original object is unchanged.
- **`errors`**: `'raise'` (default) will cause an error if any of the specified labels are not found. `'ignore'` will silently drop only the labels that exist.

## Examples

[list2tab]
- DataFrame Setup
	```python
	import pandas as pd
	import numpy as np

	data = {
	    'A': [1, 2, 3, 4],
	    'B': [5, 6, 7, 8],
	    'C': [9, 10, 11, 12],
	    'D': [13, 14, 15, 16]
	}
	df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'])
	print("Original DataFrame:\n", df)
	```
	```
	Original DataFrame:
	      A  B   C   D
	row1  1  5   9  13
	row2  2  6  10  14
	row3  3  7  11  15
	row4  4  8  12  16
	```
- Dropping Rows
	```python
	# Drop a single row by label
	df_drop_row1 = df.drop('row1') # axis=0 by default
	print("\nDropped 'row1':\n", df_drop_row1)

	# Drop multiple rows by label
	df_drop_rows = df.drop(['row2', 'row4'])
	print("\nDropped 'row2' and 'row4':\n", df_drop_rows)

	# Drop rows using the 'index' parameter
	df_drop_index_param = df.drop(index=['row1', 'row3'])
	print("\nDropped using index=['row1', 'row3']:\n", df_drop_index_param)
	```
- Dropping Columns
	```python
	# Drop a single column by label
	df_drop_col_B = df.drop('B', axis=1)
	print("\nDropped column 'B':\n", df_drop_col_B)

	# Drop multiple columns by label
	df_drop_cols = df.drop(['A', 'C'], axis='columns')
	print("\nDropped columns 'A' and 'C':\n", df_drop_cols)

	# Drop columns using the 'columns' parameter
	df_drop_columns_param = df.drop(columns=['B', 'D'])
	print("\nDropped using columns=['B', 'D']:\n", df_drop_columns_param)
	```
	- `inplace` and `errors`
	```python
	df_copy = df.copy()
	print("\nDataFrame df_copy (before inplace drop):\n", df_copy)
	df_copy.drop('row1', inplace=True)
	print("\nDataFrame df_copy (after inplace drop 'row1'):\n", df_copy) # df_copy is modified

	# Attempt to drop a non-existent label with errors='ignore'
	df_ignore_errors = df.drop('non_existent_row', errors='ignore')
	print("\nAttempted drop with errors='ignore' (df is unchanged if label not found):\n", df_ignore_errors)
	```- Series Drop
	```python
	s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
	print("\nOriginal Series:\n", s)
	s_dropped = s.drop(['a', 'd'])
	print("\nSeries after dropping 'a' and 'd':\n", s_dropped)
	```

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Indexing_Selection]] (Alternative ways to select data, `drop` is for removal)
- [[Data_Cleaning]], [[Data_Manipulation]]
- `del df['column_name']` (Another way to delete a column in-place)

---
**Source:** Pandas Documentation