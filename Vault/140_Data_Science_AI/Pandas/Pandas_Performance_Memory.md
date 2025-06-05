---
tags:
  - pandas
  - dataframe
  - performance
  - memory
  - categorical_dtype
  - optimization
  - concept
aliases:
  - Pandas Optimization
  - Memory Usage Pandas
  - Categorical Data Type
  - Efficient Chaining
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[NumPy_Data_Types]]"
worksheet:
  - WS_Pandas_Further_Topics_1
date_created: 2025-05-30
---
# Pandas Performance & Memory Optimization

Working with large datasets in Pandas requires attention to performance and memory usage. Pandas provides tools and techniques to optimize both.

[list2tab|#Performance & Memory Techniques]
- Using `Categorical` dtype
    - **Purpose:** The `category` dtype is a Pandas data type corresponding to categorical variables in statistics. A categorical variable takes on a limited, and usually fixed, number of possible values (categories; levels in R). Examples are gender, social class, blood type, country affiliation, observation time or rating via Likert scales.
    - **Benefits:**
        - **Memory Saving:** If a string column has low cardinality (few unique values relative to its length), converting it to `category` dtype can significantly reduce memory usage. Pandas stores unique categories and then uses integer codes to represent the values in the Series.
        - **Performance:** Operations on `category` dtype columns can be faster than on `object` (string) columns, especially for `groupby` operations.
    - **How to Use:**
        - `df['col'] = df['col'].astype('category')`
        - `df['col'] = pd.Categorical(df['col'], categories=['val1', 'val2'], ordered=True)` (for specific order or categories)
        - Specify `dtype='category'` when reading data (e.g., `pd.read_csv(..., dtype={'col_name': 'category'})`).
    - **Example:**
      ```python
      import pandas as pd
      import numpy as np

      # Create a DataFrame with a low-cardinality string column
      n_rows = 10**5
      data = {'ID': np.arange(n_rows),
              'Status': np.random.choice(['Open', 'Closed', 'Pending', 'Resolved'], size=n_rows)}
      df = pd.DataFrame(data)
      print(f"Memory usage (Status as object):\n{df.memory_usage(deep=True)}")

      # Convert 'Status' to category
      df['Status_Cat'] = df['Status'].astype('category')
      print(f"\nMemory usage (Status as category):\n{df.memory_usage(deep=True)}")
      
      # Compare memory for the columns directly
      mem_object = df['Status'].memory_usage(deep=True)
      mem_category = df['Status_Cat'].memory_usage(deep=True)
      print(f"\nMemory for 'Status' (object): {mem_object} bytes")
      print(f"Memory for 'Status_Cat' (category): {mem_category} bytes")
      print(f"Reduction: {((mem_object - mem_category) / mem_object * 100):.2f}%")
      ```
    - >[!tip] Use `category` dtype for columns with a small number of unique string values relative to the total number of rows. It's one of the most effective ways to reduce memory footprint and speed up some computations.

- `df.memory_usage(deep=True)`
    - **Purpose:** Returns the memory usage of each column in bytes.
    - **Key Parameters:**
        - `index`: `bool`, default `True`. Specifies whether to include the memory usage of the DataFrame’s index in the returned Series.
        - `deep`: `bool`, default `False`. If `True`, introspect the data deeply by interrogating `object` dtypes for system-level memory consumption, and include it in the returned values.
    - **Returns:** `Series` whose index is the original column names and whose values is the memory usage of each column in bytes.
    - **Example:**
      ```python
      import pandas as pd
      data = {'col_int': [1, 2, 3, 4, 5],
              'col_float': [1.0, 2.5, 3.1, 4.7, 5.0],
              'col_object': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
              'col_cat': pd.Series(['A', 'B', 'A', 'C', 'B']).astype('category')}
      df = pd.DataFrame(data)

      # Memory usage (shallow - doesn't accurately reflect object memory)
      mem_shallow = df.memory_usage()
      print("Shallow memory usage (bytes):\n", mem_shallow)
      print(f"Total shallow: {mem_shallow.sum()} bytes")

      # Memory usage (deep - accurate for objects)
      mem_deep = df.memory_usage(deep=True)
      print("\nDeep memory usage (bytes):\n", mem_deep)
      print(f"Total deep: {mem_deep.sum()} bytes")
      ```
    - >[!note] Always use `deep=True` when assessing memory usage of DataFrames containing `object` (string) columns to get an accurate picture. The default `deep=False` can be misleading for such columns.

- Efficiently Chaining Operations
    - **Purpose:** Avoid creating unnecessary intermediate [[Pandas_DataFrame]] objects, which can consume extra memory and time.
    - **Technique:** Chain Pandas methods together where possible, especially those that can operate in-place (though use `inplace=True` with caution as it modifies the original DataFrame and returns `None`). More commonly, assign the result of a chain of operations back to a variable.
    - **Example (Less Efficient - Intermediate DataFrames):**
      ```python
      import pandas as pd
      df = pd.DataFrame({
          'A': range(100000),
          'B': range(100000, 200000),
          'C': ['X', 'Y'] * 50000
      })
      
      # Less efficient: creates df_filtered, then df_transformed
      # df_filtered = df[df['A'] > 50000]
      # df_transformed = df_filtered.copy() # Explicit copy to avoid SettingWithCopyWarning
      # df_transformed['B_plus_10'] = df_transformed['B'] + 10
      # result = df_transformed[df_transformed['C'] == 'X']
      # print("\nLess efficient result (example):\n", result.head())
      ```
    - **Example (More Efficient - Chaining):**
      ```python
      import pandas as pd
      df = pd.DataFrame({
          'A': range(100000),
          'B': range(100000, 200000),
          'C': ['X', 'Y'] * 50000
      })
      # More efficient: operations are chained
      result_chained = (df[df['A'] > 50000]
                        .assign(B_plus_10 = lambda x: x['B'] + 10) # .assign creates a new df
                        .query("C == 'X'") # .query is often efficient
                       )
      print("\nChained result (example):\n", result_chained.head())

      # Alternative using .loc for selection and assignment
      # This modifies a slice, so be mindful of SettingWithCopyWarning if not careful
      # result_loc = df.loc[df['A'] > 50000].copy() # Start with a copy of the filtered data
      # result_loc['B_plus_10'] = result_loc['B'] + 10
      # result_loc = result_loc[result_loc['C'] == 'X']
      # print("\n.loc based result (example):\n", result_loc.head())
      ```
    - **Using `pipe()`:** For complex chains, `df.pipe()` can improve readability.
      ```python
      def add_value(df, col_name, value):
          df_copy = df.copy()
          df_copy[col_name] = df_copy[col_name] + value
          return df_copy

      def filter_col(df, col_name, filter_value):
          return df[df[col_name] == filter_value]

      result_pipe = (df[df['A'] > 50000]
                     .pipe(add_value, col_name='B', value=10)
                     .pipe(filter_col, col_name='C', filter_value='X')
                    )
      print("\nPipe result (example):\n", result_pipe.head())
      ```
    - >[!warning] While chaining is generally good, excessively long chains can become hard to read and debug. Use intermediate variables for clarity if a chain becomes too complex. Be mindful of methods that return copies vs. views (see [[NumPy_Views_vs_Copies]] which has relevance here too). `.assign()` always returns a new DataFrame (a copy).

- **Other Tips:**
    - **Downcasting Numeric Types:** If your numeric columns (e.g., `int64`, `float64`) don't need the full range or precision, downcast them to smaller types (e.g., `int32`, `float32`, `int16`) using `pd.to_numeric()` or `astype()`.
      ```python
      # df['int_col_small'] = pd.to_numeric(df['int_col_large'], downcast='integer')
      # df['float_col_small'] = pd.to_numeric(df['float_col_large'], downcast='float')
      ```
    - **Reading Data in Chunks:** When dealing with very large files that don't fit in memory, use the `chunksize` parameter in `pd.read_csv()` (and similar read functions) to process the file in pieces.
    - **Efficient String Operations:** Use vectorized `.str` methods instead of applying Python string methods row-by-row using `.apply()`.
    - **Avoid Loops:** Prefer vectorized operations (NumPy/Pandas built-in functions) over explicit Python loops whenever possible.
    - **Use `query()` for Filtering:** For boolean indexing based on column values, `df.query('A > B and C == "X"')` can sometimes be faster and more memory-efficient (and more readable) than standard boolean indexing `df[(df['A'] > df['B']) & (df['C'] == "X")]`, especially with large DataFrames, because it can use the `numexpr` library in the background.

---