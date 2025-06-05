---
tags:
  - pandas
  - python
  - indexing
  - selection
  - filtering
  - concept
aliases:
  - DataFrame Boolean Indexing
  - Pandas Conditional Selection
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[NumPy_Boolean_Indexing]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[Pandas_query_Method]]"
worksheet:
  - WS_Pandas
date_created: 2025-05-27
---
# Pandas DataFrame: Boolean Indexing

## Definition

**Boolean Indexing** in Pandas DataFrames allows you to select subsets of rows (and potentially columns) based on a boolean condition or a boolean Series/array. Rows where the corresponding boolean value is `True` are selected. This is a powerful method for filtering data.

## How it Works

1.  **Create a Boolean Series/Mask:** Typically, you create a boolean Series by applying a comparison operator to a column of the DataFrame or by combining multiple conditions. This boolean Series acts as a "mask."
    ```python
    # Example: df['Age'] > 30 will produce a boolean Series
    # True for rows where Age is > 30, False otherwise.
    ```
2.  **Apply the Mask:** Use the boolean Series inside the square brackets `[]` of the DataFrame (or with `.loc[]`).
    ```python
    # df[boolean_mask]
    # df.loc[boolean_mask]
    # df.loc[boolean_mask, ['ColumnA', 'ColumnB']] # Select specific columns for filtered rows
    ```

## Key Aspects

- **Row Filtering:** Primarily used to filter rows that meet certain criteria.
- **Conditions on Columns:** Conditions are usually based on the values within one or more columns.
- **Logical Operators:** Combine multiple conditions using:
    - `&` for logical AND
    - `|` for logical OR
    - `~` for logical NOT
    - Parentheses `()` are crucial for correct precedence when combining conditions.
- **Result:** Returns a new DataFrame containing only the rows where the boolean mask was `True`.

## Examples

[list2card|addClass(ab-col2)]
- Setup
	```python
	import pandas as pd
	data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	        'Age': [25, 30, 22, 35, 28],
	        'Score': [88, 92, 77, 95, 85],
	        'City': ['NY', 'SF', 'LA', 'NY', 'SF']}
	df = pd.DataFrame(data)
	print("Original DataFrame:\n", df)
	```
- Single Condition
	```python
	# Select rows where Age > 28
	older_than_28 = df[df['Age'] > 28]
	print("\nAge > 28:\n", older_than_28)
	
	# Select rows where City is 'NY'
	in_ny = df[df['City'] == 'NY']
	print("\nCity is 'NY':\n", in_ny)
	```
- Multiple Conditions
	```python
	# Select rows where Age > 25 AND City is 'SF'
	age_gt_25_and_city_sf = df[(df['Age'] > 25) & (df['City'] == 'SF')]
	print("\nAge > 25 AND City == 'SF':\n", age_gt_25_and_city_sf)

	# Select rows where Score < 90 OR Age < 25
	score_lt_90_or_age_lt_25 = df[(df['Score'] < 90) | (df['Age'] < 25)]
	print("\nScore < 90 OR Age < 25:\n", score_lt_90_or_age_lt_25)
	```
- Using with `.loc`
	`.loc` can also accept a boolean array for row selection, and allows simultaneous column selection.
	```python
	# Select Name and Score for people older than 30
	result_loc = df.loc[df['Age'] > 30, ['Name', 'Score']]
	print("\n.loc with boolean (Age > 30), selected columns:\n", result_loc)
	```

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[NumPy_Boolean_Indexing]] (Pandas extends this concept)
- [[Pandas_Indexing_Selection]] (Boolean indexing is a key part)
- [[Pandas_query_Method]] (Alternative for conditional selection using string expressions)
- Filtering, Subsetting Data

## Questions / Further Study
>[!question] What is the difference between querying and boolean indexing? (WS_Pandas)
> - **[[Pandas_Boolean_Indexing_DataFrame|Boolean Indexing]]:** Uses boolean Series/arrays directly (e.g., `df[df['col'] > 5]`). Conditions are constructed using Python/NumPy comparison and logical operators (`>`, `==`, `&`, `|`, `~`). It's very explicit and powerful, especially for complex conditions involving multiple columns or external boolean arrays.
> - **[[Pandas_query_Method|`df.query(expr_string)`]]:** Allows filtering using a **string expression** that is evaluated (e.g., `df.query("col > 5 and another_col == 'value'")`).
>     - **Pros of `query()`:** Can be more readable for simple to moderately complex conditions, avoids verbose repetition of `df[]`, can directly reference column names as if they were variables within the string, and can reference local Python variables using `@variable_name`. May sometimes offer performance benefits with the `numexpr` engine for large DataFrames.
>     - **Cons of `query()`:** String-based, so less IDE support for error checking within the string. Might be less flexible for highly programmatic or dynamic condition building compared to constructing boolean arrays directly. Performance benefits are not guaranteed for all cases.
>
> **In summary:** Boolean indexing is fundamental and always works. `query()` is a convenient alternative for more readable expressions in many common cases.

---
**Source:** Pandas Documentation