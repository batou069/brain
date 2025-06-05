---
tags:
  - pandas
  - python
  - data_manipulation
  - indexing
  - selection
  - concept
aliases:
  - Pandas Selecting Data
  - Pandas Slicing Data
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Index_Object]]"
  - "[[Label_Based_Indexing]]"
  - "[[Position_Based_Indexing]]"
  - "[[NumPy_Boolean_Indexing]]"
  - "[[NumPy_Indexing_Slicing]]"
worksheet: [WS_Pandas_Selection]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Indexing and Selection

## Definition

Pandas provides powerful and flexible mechanisms for **indexing** (accessing specific data elements) and **selection** (subsetting data) in [[Pandas_Series|Series]] and [[Pandas_DataFrame|DataFrames]]. These operations are fundamental for data analysis and manipulation.

## Primary Indexing Methods

Pandas offers three main access methods, along with direct `[]` indexing:

1.  **`[]` (Bracket Indexing / `__getitem__`)**:
    -   **For Series:** Accesses by label, position, boolean array, or list of labels/positions.
    -   **For DataFrame:**
        -   `df['col_name']`: Selects a single column.
        -   `df[['col1', 'col2']]`: Selects multiple columns.
        -   `df[boolean_series]`: Selects rows by boolean condition.
        -   `df[label_slice]` or `df[pos_slice]`: Slices rows.
    > [!WARNING]
    > Using `df[]` for row selection can be ambiguous with integer indexes. Prefer `.loc` or `.iloc`.

2.  **`.loc[]` (Label-based Indexing):**
    -   Accesses using **labels** of rows and columns.
    -   Syntax: `df.loc[row_label_selector, column_label_selector]`
    -   Selectors: single label, list of labels, slice of labels (inclusive), boolean array, callable.
    -   Raises `KeyError` if label not found.

3.  **`.iloc[]` (Integer Position-based Indexing):**
    -   Accesses using **integer positions** (0-indexed).
    -   Syntax: `df.iloc[row_integer_selector, column_integer_selector]`
    -   Selectors: single integer, list of integers, slice of integers (exclusive end), boolean array (positional), callable.
    -   Raises `IndexError` if position out of bounds.

## Examples: Indexing & Selection

[list2tab]

- Setup DataFrame
	```python
	import pandas as pd
	import numpy as np

	data = {
	    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	    'Age': [25, 30, 22, 35, 28],
	    'Score': [88, 92, 77, 95, 85],
	    'City': ['NY', 'SF', 'LA', 'NY', 'SF']
	}
	df = pd.DataFrame(data, index=['r1', 'r2', 'r3', 'r4', 'r5'])
	print("Original DataFrame:\n", df)
	```
	**Output:**
	```
	Original DataFrame:
	      Name  Age  Score City
	r1    Alice   25     88   NY
	r2      Bob   30     92   SF
	r3  Charlie   22     77   LA
	r4    David   35     95   NY
	r5      Eve   28     85   SF
	```
- Bracket Indexing `[]`
	```python
	# Select a single column (returns a Series)
	names = df['Name']
	print("\nColumn 'Name':\n", names)

	# Select multiple columns (returns a DataFrame)
	name_age = df[['Name', 'Age']]
	print("\nColumns 'Name' and 'Age':\n", name_age)

	# Select rows using boolean indexing
	high_scores = df[df['Score'] > 90]
	print("\nRows with Score > 90:\n", high_scores)

	# Slice rows by label (inclusive end)
	rows_r1_to_r3 = df['r1':'r3']
	print("\nRows 'r1' to 'r3' (label slice):\n", rows_r1_to_r3)
	```
- Label-based `.loc[]`
	```python
	# Select a single row by label (returns a Series)
	row_r2 = df.loc['r2']
	print("\nRow 'r2' using .loc:\n", row_r2)

	# Select multiple rows by label (returns a DataFrame)
	rows_r1_r4 = df.loc[['r1', 'r4']]
	print("\nRows 'r1', 'r4' using .loc:\n", rows_r1_r4)

	# Select rows and specific columns by label
	name_city_r1_r3 = df.loc[['r1', 'r3'], ['Name', 'City']]
	print("\nName & City for r1, r3 using .loc:\n", name_city_r1_r3)

	# Slice rows and columns by label (inclusive)
	slice_loc = df.loc['r2':'r4', 'Age':'Score']
	print("\nSlice 'r2':'r4', 'Age':'Score' using .loc:\n", slice_loc)

	# Boolean indexing with .loc (on row labels)
	bool_loc = df.loc[df['Age'] < 30] # Selects entire rows
	print("\nRows where Age < 30 using .loc:\n", bool_loc)
	```
- Position-based `.iloc[]`
	```python
	# Select a single row by integer position (returns a Series)
	row_pos0 = df.iloc[0]
	print("\nRow at position 0 using .iloc:\n", row_pos0)

	# Select multiple rows by integer position (returns a DataFrame)
	rows_pos_1_3 = df.iloc[[1, 3]] # Rows at index 1 and 3
	print("\nRows at positions 1, 3 using .iloc:\n", rows_pos_1_3)

	# Select rows and specific columns by integer position
	# Rows 0, 2 and Columns 0 (Name), 2 (Score)
	subset_iloc = df.iloc[[0, 2], [0, 2]]
	print("\nRows 0,2 & Cols 0,2 using .iloc:\n", subset_iloc)

	# Slice rows and columns by integer position (exclusive end)
	slice_iloc = df.iloc[1:4, 0:2] # Rows 1,2,3 and Columns 0,1
	print("\nSlice [1:4, 0:2] using .iloc:\n", slice_iloc)
	```
- Conditional Selection (Boolean Array)
	```python
	# Complex condition
	condition = (df['Age'] > 25) & (df['City'] == 'SF')
	print("\nCondition (Age > 25 & City == 'SF'):\n", condition)
	
	filtered_df = df[condition]
	print("\nFiltered DataFrame:\n", filtered_df)
	
	# Using .loc with a boolean array (generated from a condition on a column)
	# Select 'Name' and 'Score' for rows where Age > 30
	older_than_30 = df.loc[df['Age'] > 30, ['Name', 'Score']]
	print("\nName and Score for Age > 30:\n", older_than_30)
	```

## Other Selection Methods

- **`df.query(expr)`**: Selects rows using a boolean expression string.
  ```python
  young_sf = df.query("Age < 30 and City == 'SF'")
  ```
- **`df.at[]` / `df.iat[]`**: Fast scalar access for single values by label/integer position respectively. Optimized for single cell lookup/setting.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]], [[Pandas_Index_Object]]
- [[Label_Based_Indexing]] (`.loc`), [[Position_Based_Indexing]] (`.iloc`)
- [[NumPy_Boolean_Indexing]] (Principles apply here)
- Slicing (Python's `start:stop:step` notation)
- Data Subsetting, Filtering

---
**Source:** Pandas Documentation