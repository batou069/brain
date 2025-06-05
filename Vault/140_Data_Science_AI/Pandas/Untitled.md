---
tags:
  - pandas
  - python
  - cheatsheet
  - data_manipulation
  - data_analysis
  - reference
aliases:
  - Pandas Cheatsheet
  - Pandas Operations Guide
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[_Pandas_MOC]]"
worksheet: [WS_Pandas_Main_Combined]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Operations Cheatsheet

This document provides a structured overview of common Pandas operations using nested AnyBlocks for easy navigation.

[list2tab]
- **Data I/O & Inspection**
  [list2tab]
  - `pd.read_csv` / `df.to_csv`
    [list2mdtable]
    - **Definition**
      - `pd.read_csv()`: Reads a comma-separated values (CSV) file into a DataFrame.
      - `df.to_csv()`: Writes a DataFrame to a CSV file.
    - **Distinction**
      - Core functions for handling the most common flat file format. `read_csv` is highly configurable for various CSV dialects.
    - **Examples**
      ```python
      # df_new = pd.read_csv('input.csv', sep=';', header=0, index_col='ID')
      # df.to_csv('output.csv', index=False, columns=['Name', 'Score'])
      ```
  - `pd.read_excel` / `df.to_excel`
    [list2mdtable]
    - **Definition**
      - `pd.read_excel()`: Reads data from a Microsoft Excel file (`.xls` or `.xlsx`) into a DataFrame.
      - `df.to_excel()`: Writes a DataFrame to an Excel file.
    - **Distinction**
      - Requires `openpyxl` or `xlrd`. Can handle multiple sheets.
    - **Examples**
      ```python
      # df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1', usecols="A:C")
      # df.to_excel('report.xlsx', sheet_name='Summary', index=False)
      ```
  - `pd.read_sql` / `df.to_sql`
    [list2mdtable]
    - **Definition**
      - `pd.read_sql()`: Reads data from a SQL database table or query into a DataFrame.
      - `df.to_sql()`: Writes records from a DataFrame to a SQL database table.
    - **Distinction**
      - Requires a database connection object (e.g., SQLAlchemy engine). `if_exists` parameter in `to_sql` is important.
    - **Examples**
      ```python
      # from sqlalchemy import create_engine
      # engine = create_engine('sqlite:///mydb.db')
      # df_sql = pd.read_sql("SELECT Name, Age FROM users WHERE Age > 30", engine)
      # df.to_sql('processed_users', engine, if_exists='replace', index_label='id')
      ```
  - `df.head()` / `df.tail()` / `df.sample()`
    [list2mdtable]
    - **Definition**
      - `head(n=5)`: Returns first `n` rows.
      - `tail(n=5)`: Returns last `n` rows.
      - `sample(n=1, frac=None)`: Returns a random sample of rows.
    - **Distinction**
      - Essential for quick glimpses into the DataFrame's content.
    - **Examples**
      ```python
      # first_3_rows = df.head(3)
      # random_row = df.sample()
      ```
  - `df.info()` / `df.describe()`
    [list2mdtable]
    - **Definition**
      - `info()`: Prints a concise summary (index/column dtypes, non-null counts, memory usage).
      - `describe()`: Generates descriptive statistics (count, mean, std, min/max, quartiles for numerical; count, unique, top, freq for object).
    - **Distinction**
      - `info()` for structure and nulls, `describe()` for statistical summary.
    - **Examples**
      ```python
      # df.info()
      # summary_stats = df.describe(include='all')
      ```
  - `df.shape` / `df.index` / `df.columns` / `df.dtypes` / `df.count()`
    [list2mdtable]
    - **Definition**
      - `shape`: Tuple of (rows, cols).
      - `index`: The row index labels.
      - `columns`: The column index labels.
      - `dtypes`: Series of data types for each column.
      - `count()`: Number of non-NA/null observations per column/row.
    - **Distinction**
      - Attributes (`shape`, `index`, `columns`, `dtypes`) provide metadata. `count()` is an aggregation.
    - **Examples**
      ```python
      # num_rows, num_cols = df.shape
      # column_names = df.columns.tolist()
      # non_null_counts = df.count() # Counts per column
      ```

- **Indexing & Selection**
  [list2tab]
  - `df.loc[]` / `df.iloc[]`
    [list2mdtable]
    - **Definition**
      - `.loc[]`: Access a group of rows and columns by **label(s)** or a boolean array.
      - `.iloc[]`: Access a group of rows and columns by **integer position(s)** (0-indexed).
    - **Distinction**
      - `.loc` is label-based (inclusive for label slices). `.iloc` is position-based (exclusive for integer slices). See [[Pandas_loc_vs_iloc]].
    - **Examples**
      ```python
      # alice_data_loc = df.loc['r1'] # Row with index label 'r1'
      # first_row_iloc = df.iloc   # First row by position
      # subset_loc = df.loc[['r1', 'r3'], ['Name', 'Score']]
      # subset_iloc = df.iloc[0:2,] # First 2 rows, columns at pos 0 and 2
      ```
  - `df.at[]` / `df.iat[]`
    [list2mdtable]
    - **Definition**
      - `.at[]`: Fast access to a single scalar value using **labels**.
      - `.iat[]`: Fast access to a single scalar value using **integer positions**.
    - **Distinction**
      - Optimized for single value get/set. Faster than `.loc`/`.iloc` for this specific task. See [[Pandas_at_iat]].
    - **Examples**
      ```python
      # score_alice = df.at['r1', 'Score']
      # age_bob_pos = df.iat # Age of Bob (row pos 1, col pos 1)
      # df.at['r3', 'City'] = 'SF' # Set value
      ```
  - Boolean Indexing
    [list2mdtable]
    - **Definition**
      - Selecting subsets of a DataFrame or Series using a boolean array/Series of the same length. Rows where the boolean is `True` are selected.
    - **Distinction**
      - Powerful for conditional selection. Can be used with `[]`, `.loc[]`, or `.iloc[]`. See [[NumPy_Boolean_Indexing]] (principles apply).
    - **Examples**
      ```python
      # young_folks = df[df['Age'] < 30]
      # high_scorers_in_NY = df.loc[(df['Score'] > 90) & (df['City'] == 'NY')]
      ```
  - `df.query()`
    [list2mdtable]
    - **Definition**
      - Filters rows using a boolean expression provided as a string.
    - **Distinction**
      - Can be more readable for complex conditions. Allows referencing local variables with `@`. See [[Pandas_df_query]].
    - **Examples**
      ```python
      # min_age = 25
      # result = df.query('Age > @min_age and City == "SF"')
      ```

- **Data Cleaning & Transformation**
  [list2tab]
  - `df.isnull()` / `df.fillna()` / `df.dropna()`
    [list2mdtable]
    - **Definition**
      - `isnull()`: Detect missing values (returns boolean DataFrame).
      - `fillna(value)`: Fill NA/NaN values using a specified method or value.
      - `dropna()`: Remove missing values (rows or columns).
    - **Distinction**
      - Core tools for handling missing data. See [[Pandas_Handling_Missing_Data]].
    - **Examples**
      ```python
      # missing_count = df.isnull().sum()
      # df_filled = df.fillna({'Score': df['Score'].mean()})
      # df_no_na_rows = df.dropna(subset=['Score'])
      ```
  - `df.duplicated()` / `df.drop_duplicates()`
    [list2mdtable]
    - **Definition**
      - `duplicated()`: Returns boolean Series indicating duplicate rows.
      - `drop_duplicates()`: Removes duplicate rows.
    - **Distinction**
      - Parameters `subset` and `keep` control how duplicates are identified and which ones are dropped. See [[Pandas_Dealing_with_Duplicates]].
    - **Examples**
      ```python
      # duplicate_rows = df[df.duplicated(subset=['Name', 'City'], keep=False)]
      # df_unique = df.drop_duplicates(subset=['Name'], keep='first')
      ```
  - `df.astype()` / `pd.to_numeric()` / `pd.to_datetime()`
    [list2mdtable]
    - **Definition**
      - `astype(dtype)`: Casts a pandas object to a specified dtype.
      - `to_numeric()`: Converts argument to a numeric type (handles errors).
      - `to_datetime()`: Converts argument to datetime objects.
    - **Distinction**
      - `astype` is general. `to_numeric`/`to_datetime` are specialized with better error handling for their types. See [[Pandas_Data_Type_Conversion]].
    - **Examples**
      ```python
      # df['Age'] = df['Age'].astype(float)
      # df['Score_Numeric'] = pd.to_numeric(df['Score'], errors='coerce')
      # df['Date_dt'] = pd.to_datetime(df['Date'])
      ```
  - `Series.str` Accessor
    [list2mdtable]
    - **Definition**
      - Provides vectorized string methods for Series with string-like data.
    - **Distinction**
      - Allows applying Python string methods (lower, upper, contains, split, replace, etc.) element-wise on a Series. See [[Pandas_String_Operations]].
    - **Examples**
      ```python
      # df['Name_Lower'] = df['Name'].str.lower()
      # df['City_Initial'] = df['City'].str[] # First character
      # df_ny_people = df[df['City'].str.startswith('N')]
      ```
  - `df.apply()` / `Series.map()` / `df.applymap()` / `df.transform()`
    [list2mdtable]
    - **Definition**
      - `apply()`: Applies a function along an axis of a DataFrame (row or column-wise).
      - `Series.map()`: Element-wise mapping/substitution for a Series.
      - `df.applymap()` (deprecated, use `df.map()`): Element-wise on DataFrame.
      - `df.groupby().transform()`: Group-wise transformation broadcast to original shape.
    - **Distinction**
      - Different scopes of application: element-wise, row/column-wise, group-wise. See [[Pandas_Apply_Map_Applymap]] and [[Pandas_transform]].
    - **Examples**
      ```python
      # df['Score_Normalized'] = df['Score'].apply(lambda x: (x - df['Score'].min()) / (df['Score'].max() - df['Score'].min()))
      # df['Age_Group'] = df['Age'].map(lambda x: 'Young' if x < 30 else 'Old')
      # df['City_Category_Mean_Score'] = df.groupby('City')['Score'].transform('mean')
      ```
  - `df.replace()`
    [list2mdtable]
    - **Definition**
      - Replaces occurrences of specified values with other values.
    - **Distinction**
      - Can replace scalars, lists, dicts, or use regex. See [[Pandas_df_replace]].
    - **Examples**
      ```python
      # df_replaced = df.replace({'NY': 'New York', 999: np.nan})
      # df['Score'] = df['Score'].replace(-1, 0)
      ```
  - `df.rename()`
    [list2mdtable]
    - **Definition**
      - Alters axis labels (row index or column names).
    - **Distinction**
      - Uses a mapper (dict or function). See [[Pandas_df_rename]].
    - **Examples**
      ```python
      # df_renamed = df.rename(columns={'Score': 'Total Score', 'City': 'Location'},
      #                        index={'r1': 'Record1'})
      ```

- **Combining & Reshaping Data**
  [list2tab]
  - `df.join()` / `pd.merge()`
    [list2mdtable]
    - **Definition**
      - `join()`: Combines DataFrames primarily on index or on calling df's column and other's index. Defaults to left join.
      - `merge()`: More flexible database-style join on columns or indices. Defaults to inner join.
    - **Distinction**
      - `merge` is more versatile for column-based joins and different join types. `join` is convenient for index-based joins. See [[Pandas_Join_vs_Merge]].
    - **Examples**
      ```python
      # df_other = pd.DataFrame({'Grade': ['A', 'B']}, index=['r1', 'r3'])
      # df_joined = df.join(df_other)

      # df_info = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Department': ['HR', 'IT']})
      # df_merged = pd.merge(df, df_info, on='Name', how='left')
      ```
  - `pd.concat()`
    [list2mdtable]
    - **Definition**
      - Concatenates (stacks) Pandas objects along a particular axis (rows or columns).
    - **Distinction**
      - For appending rows or columns. Alignment based on the *other* axis. See [[Pandas_concat]].
    - **Examples**
      ```python
      # df_part1 = df.iloc[:2]
      # df_part2 = df.iloc[2:]
      # df_recombined = pd.concat([df_part1, df_part2]) # axis=0 by default
      ```
  - `df.groupby()`
    [list2mdtable]
    - **Definition**
      - Groups DataFrame using a mapper or by a Series of columns, then applies a function (aggregate, transform, filter) to each group.
    - **Distinction**
      - Core of "split-apply-combine" strategy. See [[Pandas_groupby]].
    - **Examples**
      ```python
      # city_mean_scores = df.groupby('City')['Score'].mean()
      # city_stats = df.groupby('City').agg({'Score': ['mean', 'std'], 'Age': 'max'})
      ```
  - `pd.pivot_table()`
    [list2mdtable]
    - **Definition**
      - Creates a spreadsheet-style pivot table as a DataFrame. Aggregates data based on specified index, columns, and values.
    - **Distinction**
      - Reshapes data by moving unique values from one or more columns into new column headers, and unique values from other columns into new row indexes, with aggregation in cells. See [[Pandas_pivot_table]].
    - **Examples**
      ```python
      # pivot = pd.pivot_table(df, values='Score', index='City', columns='Name', aggfunc='mean')
      ```
  - `MultiIndex`
    [list2mdtable]
    - **Definition**
      - Hierarchical indexing on an axis, allowing multiple levels of labels for rows or columns.
    - **Distinction**
      - Enables representation of higher-dimensional data in 2D. Often results from `groupby()` with multiple keys or `pivot_table()`. See [[Pandas_MultiIndex]].
    - **Examples**
      ```python
      # df_multi = df.set_index(['City', 'Name'])
      # score_ny_alice = df_multi.loc[('NY', 'Alice'), 'Score']
      ```

- **Iteration & Plotting**
  [list2tab]
  - `df.iterrows()`
    [list2mdtable]
    - **Definition**
      - Iterates over DataFrame rows as (index, Series) pairs.
    - **Distinction**
      - Generally **inefficient** due to Series creation per row. Prefer vectorized operations, `apply()`, or `itertuples()`. See [[Pandas_df_iterrows]].
    - **Examples**
      ```python
      # for index, row_series in df.iterrows():
      #     print(f"Index: {index}, Name: {row_series['Name']}")
      ```
  - `df.plot()` / `df.hist()`
    [list2mdtable]
    - **Definition**
      - Convenience wrappers around Matplotlib to quickly generate plots from DataFrame or Series data.
      - `plot()` supports various kinds (line, bar, scatter, etc.). `hist()` is specific for histograms.
    - **Distinction**
      - Simplifies basic plotting. For complex plots, direct Matplotlib usage is more flexible. See [[140_Data_Science_AI/Pandas/Pandas_Plotting]].
    - **Examples**
      ```python
      # import matplotlib.pyplot as plt
      # df['Score'].plot(kind='hist', bins=5, title='Score Distribution')
      # plt.show()
      # df.plot(x='Age', y='Score', kind='scatter', title='Age vs Score')
      # plt.show()
      ```

---