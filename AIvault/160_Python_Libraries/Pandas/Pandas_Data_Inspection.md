---
tags:
  - pandas
  - python
  - data_analysis
  - data_exploration
  - function
  - concept
aliases:
  - Inspecting Pandas DataFrames
  - Pandas DataFrame Exploration
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[NumPy_Data_Types]]"
  - "[[Exploratory_Data_Analysis]]"
worksheet: [WS_Pandas_Exploration]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Data Inspection & Exploration

## Definition

Once data is loaded into a Pandas [[Pandas_DataFrame|DataFrame]] or [[Pandas_Series|Series]], the next step is often to inspect and explore it to understand its structure, content, quality, and basic statistical properties. Pandas provides a variety of attributes and methods for this purpose.

## Common Inspection Methods & Attributes

[list2tab]

- Initial Glimpse
	**`df.head(n=5)`**
	- Returns the first `n` rows of the DataFrame. Default is 5.
	- Useful for quickly seeing the structure and some sample data.
	```python
	print(df.head())
	```

	**`df.tail(n=5)`**
	- Returns the last `n` rows. Default is 5.
	```python
	print(df.tail(3))
	```

	**`df.sample(n=None, frac=None, replace=False, random_state=None)`**
	- Returns a random sample of `n` items or a fraction `frac` of items.
	- `replace`: Allow sampling with replacement.
	- `random_state`: Seed for reproducibility.
	```python
	print(df.sample(5)) # Sample 5 random rows
	print(df.sample(frac=0.1)) # Sample 10% of rows
	```
- Structure & Metadata
	**`df.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None)`**
	- Prints a concise summary of the DataFrame, including:
		- Index dtype and row count.
		- Column names.
		- Number of non-null values per column.
		- Data type ([[NumPy_Data_Types|dtype]]) of each column.
		- Memory usage.
	- Very useful for a quick overview of data types and missing values.
	```python
	# df.info()
	```

	**`df.shape`** (Attribute)
	- Returns a tuple representing the dimensionality: `(number_of_rows, number_of_columns)`.
	```python
	print(f"Shape: {df.shape}")
	```

	**`df.ndim`** (Attribute)
	- Returns the number of axes / array dimensions (always 2 for a DataFrame).
	```python
	print(f"Number of dimensions: {df.ndim}")
	```

	**`df.size`** (Attribute)
	- Returns the total number of elements (rows * columns).
	```python
	print(f"Total elements: {df.size}")
	```

	**`df.dtypes`** (Attribute)
	- Returns a Series with the data type of each column.
	```python
	print(f"Data types:\n{df.dtypes}")
	```

	**`df.columns`** (Attribute)
	- Returns the column labels (an `Index` object).
	```python
	print(f"Column labels: {df.columns}")
	for col in df.columns: print(col)
	```

	**`df.index`** (Attribute)
	- Returns the row labels (an `Index` object).
	```python
	print(f"Row labels: {df.index}")
	```
- Descriptive Statistics
	**`df.describe(percentiles=None, include=None, exclude=None)`**
	- Generates descriptive statistics of the DataFrame's columns.
	- For **numerical columns** (default): count, mean, std, min, 25th percentile (Q1), 50th percentile (median), 75th percentile (Q3), max.
	- For **object/categorical columns** (using `include='object'` or `include='all'`): count, unique, top (most frequent), freq (frequency of top).
	```python
	print("Numerical describe:\n", df.describe())
	print("\nObject describe:\n", df.describe(include='object'))
	print("\nAll describe:\n", df.describe(include='all'))
	```
- Value Counts & Uniqueness
	**`series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)`**
	- (Applied to a Series, e.g., `df['column_name'].value_counts()`)
	- Returns a Series containing counts of unique values, sorted by frequency by default.
	- `normalize=True`: Returns relative frequencies (proportions).
	```python
	print(df['City'].value_counts())
	```

	**`df.nunique(axis=0, dropna=True)`**
	- Returns a Series with the number of distinct elements in each column (if `axis=0`) or row (if `axis=1`).
	```python
	print("\nNumber of unique values per column:\n", df.nunique())
	```

	**`series.unique()`**
	- (Applied to a Series)
	- Returns an array of the unique values in the Series, in order of appearance.
	```python
	print(f"\nUnique cities: {df['City'].unique()}")
	```

## Purpose in Data Analysis Workflow

Data inspection is a critical first step in any data analysis project:
- **Understand Data Structure:** Get familiar with rows, columns, data types.
- **Identify Data Quality Issues:** Detect missing values, outliers, inconsistent data types, or unexpected values.
- **Formulate Hypotheses:** Initial exploration can lead to questions and hypotheses about the data.
- **Guide Preprocessing:** Information gathered informs data cleaning and transformation steps.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Exploratory_Data_Analysis]] (EDA) (Inspection is part of EDA)
- [[NumPy_Data_Types]] (dtypes shown by `.info()` and `.dtypes`)
- Descriptive Statistics
- Data Quality

---
**Source:** Pandas Documentation