---
tags:
  - pandas
  - python
  - data_manipulation
  - combining_data
  - function
  - concept
aliases:
  - pd.concat
  - Pandas Concatenate DataFrames
  - Pandas Append DataFrames
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Join_vs_Merge]]"
  - "[[NumPy_concatenate]]"
worksheet:
  - WS_Pandas_Main
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `pd.concat()`

## Definition

`pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)` is a Pandas function used to **concatenate** (combine or "stack") Pandas objects (like [[Pandas_DataFrame|DataFrames]] or [[Pandas_Series|Series]]) along a particular axis.

## Key Parameters

-   **`objs`**: A sequence or mapping of Series or DataFrame objects to be concatenated.
-   **`axis`**: (Default `0`) The axis to concatenate along.
    -   `0` or `'index'`: Stack DataFrames/Series vertically (row-wise). Appends rows. Column labels are aligned.
    -   `1` or `'columns'`: Stack DataFrames/Series horizontally (column-wise). Appends columns. Row index labels are aligned.
-   **`join`**: (Default `'outer'`) How to handle indexes on other axis(es).
    -   `'outer'`: Take the union of them. Fills with `NaN` where labels don't align.
    -   `'inner'`: Take the intersection of them. Only keeps labels present in all objects along the other axis.
-   **`ignore_index`**: (Default `False`) If `True`, do not use the index values along the concatenation axis. The resulting axis will be labeled `0, ..., n-1`. Useful when concatenating objects where the original index is not meaningful.
-   **`keys`**: Sequence to associate with objects being concatenated. Creates a hierarchical index on the concatenation axis (a [[Pandas_MultiIndex|MultiIndex]]).
-   `verify_integrity`: (Default `False`) If `True`, check if the new concatenated axis contains duplicates. Will raise an exception if it does.
-   `sort`: (Default `False`) Sort non-concatenation axis if it is not already aligned when `join='outer'`.

## AnyBlock Examples: `pd.concat()`

[list2tab]
- Setup DataFrames
  ```python
  import pandas as pd
  df1 = pd.DataFrame({
      'A': ['A0', 'A1', 'A2'],
      'B': ['B0', 'B1', 'B2']
  }, index=)

  df2 = pd.DataFrame({
      'A': ['A3', 'A4'],
      'B': ['B3', 'B4'],
      'C': ['C3', 'C4'] # df2 has an extra column
  }, index=)

  df3 = pd.DataFrame({
      'D': ['D0', 'D1'],
      'E': ['E0', 'E1']
  }, index=) # df3 has same index as part of df1

  print("df1:\n", df1)
  print("\ndf2:\n", df2)
  print("\ndf3:\n", df3)
  ```

- Concatenating Rows (`axis=0`)
  ```python
  # Default: axis=0, join='outer'
  result_rows_outer = pd.concat([df1, df2])
  print("\nConcatenate rows (outer join for columns):\n", result_rows_outer)
  # Column C will have NaNs for rows from df1

  # Concatenate rows (inner join for columns)
  result_rows_inner = pd.concat([df1, df2], join='inner')
  print("\nConcatenate rows (inner join for columns - only A, B):\n", result_rows_inner)

  # Concatenate rows and ignore original index
  result_rows_ignore_idx = pd.concat([df1, df2], ignore_index=True)
  print("\nConcatenate rows (ignore_index=True):\n", result_rows_ignore_idx)

  # Concatenate with keys to create a hierarchical index
  result_rows_keys = pd.concat([df1, df2], keys=['source1', 'source2'])
  print("\nConcatenate rows with keys:\n", result_rows_keys)
  # print("\nAccessing source1 data:\n", result_rows_keys.loc['source1'])
  ```
  **Output (Conceptual for `result_rows_outer`):**
  ```
        A   B    C
  0    A0  B0  NaN
  1    A1  B1  NaN
  2    A2  B2  NaN
  3    A3  B3   C3
  4    A4  B4   C4
  ```

- Concatenating Columns (`axis=1`)
  ```python
  # Default: axis=1, join='outer'
  result_cols_outer = pd.concat([df1, df3], axis=1)
  print("\nConcatenate columns (outer join for rows):\n", result_cols_outer)
  # Rows 2 from df1 will have NaNs for D, E.
  # Rows in df3 not in df1's index would also get NaNs for A, B.

  # Concatenate columns (inner join for rows)
  result_cols_inner = pd.concat([df1, df3], axis=1, join='inner')
  print("\nConcatenate columns (inner join for rows - only index 0, 1):\n", result_cols_inner)
  ```
  **Output (Conceptual for `result_cols_outer`):**
  ```
        A    B    D    E
  0    A0   B0   D0   E0
  1    A1   B1   D1   E1
  2    A2   B2  NaN  NaN
  ```

## `DataFrame.append()` (Legacy)

- The `append()` method (e.g., `df1.append(df2)`) was a shortcut for `pd.concat([df1, df2], ignore_index=True if df1.index is default else False)` along `axis=0`.
- **`append()` is deprecated since Pandas 1.4.0 and removed in Pandas 2.0. Use `pd.concat()` instead.**

## `concat` vs. `merge`/`join`

- **`pd.concat()`:** Primarily for **stacking** DataFrames/Series along an axis (either vertically or horizontally). Alignment happens on the *other* axis. It's like gluing pieces together.
- **[[Pandas_Join_vs_Merge|`pd.merge()` / `df.join()`]]:** For **database-style joins** based on common keys or indices to combine columns from different DataFrames based on relationships in those keys.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Join_vs_Merge]] (For database-style combining)
- [[Pandas_MultiIndex]] (Can be created using `keys` parameter)
- Data Combining, Stacking, Appending

---
**Source:** WS_Pandas_Main, Pandas Documentation

[list2tab]
- Creation
	[list2tab]	
	- Empty df
		[list2mdtable]
		- Column 1:
			- Column 2:
				- Column 3:
					- Column 4:
		- np.arrange() is in col 1
			-  this is col2
	     	  ```python
	     	  import numpy as np
	     	   np.arange(10)
	     	   np.arange(2, 10, dtype=float)
	     	   np.arange(2, 3, 0.1)
	     	   ```   
		     this is another row in col2 
				  - col3 sub1
				    > col3 sub2
				    > 	- col4 row1
				    > 	- col4 row2

	- 1D arrays 
		[list2mdtable]
		- SQL:
			- Pandas:
				- Pure Numpy:
					- R:
		- Some header about sql expression
			```sql
			SELECT * FROM Table;*
			```
			- this is col2
	     	  ```python
	     	  import 
	     	   ```   
		     this is another row in col2 
				- col3 sub1
				  > col3 sub2
- Manipulation
	content


