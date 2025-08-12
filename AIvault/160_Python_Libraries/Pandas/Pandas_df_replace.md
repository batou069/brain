---
tags:
  - pandas
  - python
  - data_manipulation
  - data_cleaning
  - function
  - concept
aliases:
  - df.replace
  - Series.replace
  - Pandas Replace Values
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Handling_Missing_Data]]" # Can be used to replace specific missing value indicators
  - "[[Data_Cleaning]]"
  - "[[Regular_Expressions]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `replace()`

## Definition

The `replace()` method in Pandas (available for both [[Pandas_DataFrame|DataFrames]] and [[Pandas_Series|Series]]) is used to replace occurrences of specified values with other values. It's a versatile tool for data cleaning and transformation.

## `DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')`
## `Series.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')`

*(Parameters are largely the same for Series and DataFrame; `method` is more relevant for Series when `to_replace` is a scalar and `value` is None).*

- **`to_replace`**: The value(s) to be replaced. Can be:
    - Scalar (numeric, string, `None`, `np.nan`): Replaces all occurrences of this scalar.
    - List/Tuple: Replaces all occurrences of any value in the list/tuple.
        - If `value` is also a list/tuple, replacement is element-wise (e.g., `to_replace=[1,2]`, `value=['a','b']` replaces 1 with 'a', 2 with 'b').
    - Dictionary: `{value_to_replace: replacement_value, ...}`.
        - For DataFrame, can be nested: `{column_name: {value_to_replace: replacement_value}}` to replace only in specific columns.
    - Regular Expression (if `regex=True`): `to_replace` is a regex pattern, `value` is the replacement string (can include backreferences).
- **`value`**: The value(s) to replace with.
    - Scalar: Replaces all matches of `to_replace` with this scalar.
    - List/Tuple: Used for element-wise replacement when `to_replace` is also a list/tuple of the same length.
    - `None`: If `method` is specified (e.g., `'pad'`, `'ffill'`, `'bfill'`), this is used for filling with previous/next values (more common with `Series.replace` when `to_replace` is a specific value like `np.nan`).
- **`inplace`**: (Default `False`) If `True`, modifies the object in-place.
- **`limit`**: Maximum size of forward/backward fill if `method` is used.
- **`regex`**: (Default `False`) If `True`, `to_replace` is treated as a regular expression, and `value` can be a replacement string or a callable.

## Examples: `replace()`

[list2tab]
- Setup
  ```python
  import pandas as pd
  import numpy as np

  df = pd.DataFrame({
      'A': ['apple', 'banana', 'cherry', 'apple', 'date'],
      'B': [10, 20, np.nan, 10, 40],
      'C': ['X', 'Y', 'Z', 'X', 'W']
  })
  print("Original DataFrame:\n", df)

  s = pd.Series([100, 200, -99, 100, 500, -99])
  print("\nOriginal Series:\n", s)
  ```

- Basic Scalar Replacement
  ```python
  # Replace all occurrences of 'apple' with 'apricot' in df
  df_replaced_apple = df.replace(to_replace='apple', value='apricot')
  print("\nDataFrame with 'apple' replaced by 'apricot':\n", df_replaced_apple)

  # Replace all occurrences of 10 with 100 in df['B']
  df['B_replaced'] = df['B'].replace(10, 100)
  print("\nDataFrame with 10 in 'B' replaced by 100:\n", df)

  # Replace -99 with 0 in Series s
  s_replaced_neg99 = s.replace(-99, 0)
  print("\nSeries with -99 replaced by 0:\n", s_replaced_neg99)
  ```

- List Replacement
  ```python
  # Replace 'apple' with 'APPLE' and 'banana' with 'BANANA' in df['A']
  df['A_list_replaced'] = df['A'].replace(['apple', 'banana'], ['APPLE', 'BANANA'])
  print("\nDataFrame with list replacement in 'A':\n", df)

  # Replace multiple values with a single value
  s_multi_to_one = s.replace(, 0)
  print("\nSeries with 100 and 200 replaced by 0:\n", s_multi_to_one)
  ```

- Dictionary Replacement
  ```python
  # Replace specific values in the entire DataFrame
  df_dict_replaced = df.replace({'apple': 'fruit_apple', 10: 11, 'X': 'CategoryX'})
  print("\nDataFrame with dictionary replacement:\n", df_dict_replaced)

  # Replace specific values in specific columns
  df_col_specific_replace = df.replace({
      'A': {'cherry': 'sweet_cherry'},
      'B': {20: 22, np.nan: 0} # Replace NaN in column B with 0
  })
  print("\nDataFrame with column-specific dictionary replacement:\n", df_col_specific_replace)
  ```

- Regular Expression Replacement
  ```python
  # Replace strings starting with 'a' or 'b' with 'fruit_starts_ab' in column 'A'
  df_regex_replace = df.copy() # Work on a copy
  df_regex_replace['A'] = df_regex_replace['A'].replace(r'^[ab].*', 'fruit_starts_ab', regex=True)
  print("\nDataFrame with regex replacement in 'A':\n", df_regex_replace)

  # Replace all digits in Series s with 'N'
  s_digits_replaced = s.astype(str).replace(r'\d', 'N', regex=True) # Convert to str first for regex
  print("\nSeries with digits replaced by 'N':\n", s_digits_replaced)
  ```

## Key Considerations

- **Specificity:** Using dictionaries for `to_replace` (and `value` if needed) provides the most control, especially for column-specific replacements in DataFrames.
- **`NaN` Handling:** `replace()` can be used to replace specific values (e.g., sentinel values like -999, 9999) with `np.nan` to standardize missing data representation before using `fillna()` or `dropna()`.
  ```python
  # df.replace(-999, np.nan, inplace=True)
  ```
- **Regex Power:** `regex=True` enables powerful pattern-based replacements.
- **Chaining:** `replace()` can be chained for multiple replacements.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Data_Cleaning]], [[Data_Manipulation]]
- [[Pandas_Handling_Missing_Data]] (`fillna`)
- [[Regular_Expressions]] (When `regex=True`)
- [[NumPy_NaN]]

---
**Source:** WS_Pandas_Main, Pandas Documentation