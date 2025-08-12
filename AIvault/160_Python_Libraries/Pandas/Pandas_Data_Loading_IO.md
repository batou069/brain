---
tags:
  - pandas
  - python
  - file_io
  - data_loading
  - data_saving
  - concept
aliases:
  - Pandas I/O
  - Reading and Writing Data Pandas
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[CSV_Files]]"
  - "[[Excel_Files]]"
  - "[[SQL_Databases]]"
  - "[[JSON]]"
worksheet: [WS_Pandas_IO]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas Data Loading & Saving (I/O)

## Definition

[[Pandas]] provides a rich set of functions for reading data from various file formats into [[Pandas_DataFrame|DataFrames]] (and sometimes [[Pandas_Series|Series]]) and for writing DataFrames back to these formats. This I/O capability is crucial for any data analysis workflow.

## Key I/O Functions and Formats

[list2tab]

- CSV Files
	Comma-Separated Values (CSV) are a very common flat file format.

	**Reading from CSV:** `pd.read_csv()`
	```python
	import pandas as pd

	# Basic read
	df = pd.read_csv("my_data.csv")

	# Common parameters:
	df_custom = pd.read_csv(
	    "my_data.csv",
	    sep=',',           # Delimiter (default is comma)
	    header=0,          # Row number to use as column names (0 is first row)
	                       # None if no header
	    index_col=0,       # Column to use as row index
	    usecols=['colA', 'colB'], # List of column names to read
	    na_values=['NA', '?'], # Strings to recognize as NaN
	    skiprows=1,        # Skip N rows from the top
	    nrows=100          # Read only first N rows
	)
	print(df_custom.head())
	```
	> [!TIP] `read_csv` is highly configurable. Check documentation for many more options (encoding, date parsing, type inference, etc.).

	**Writing to CSV:** `DataFrame.to_csv()`
	```python
	# Assuming df is an existing DataFrame
	df.to_csv("output_data.csv", index=False) # index=False avoids writing row index to file

	# With custom separator and no header
	df.to_csv("output_tabbed.tsv", sep='\t', header=False, index=False)
	```
- Excel Files (.xls, .xlsx)
	Pandas can read from and write to Microsoft Excel files. Requires additional libraries like `openpyxl` (for `.xlsx`) or `xlrd` (for older `.xls`).
	`pip install openpyxl xlrd`

	**Reading from Excel:** `pd.read_excel()`
	```python
	import pandas as pd

	# Read from the first sheet
	df_excel = pd.read_excel("my_workbook.xlsx")

	# Read from a specific sheet name or index
	df_sheet2 = pd.read_excel("my_workbook.xlsx", sheet_name="Sheet2")
	df_sheet_idx = pd.read_excel("my_workbook.xlsx", sheet_name=1) # 0-indexed

	# Common parameters:
	header, index_col, usecols, skiprows (similar to read_csv)
	```

	**Writing to Excel:** `DataFrame.to_excel()`
	```python
	# Assuming df is an existing DataFrame
	df.to_excel("output_workbook.xlsx", sheet_name="MyData", index=False)

	# Writing multiple DataFrames to different sheets:
	with pd.ExcelWriter("multi_sheet_output.xlsx") as writer:
	    df1.to_excel(writer, sheet_name="Data1", index=False)
	    df2.to_excel(writer, sheet_name="Data2", index=False)
	```
- SQL Databases
	Pandas can interact with SQL databases. Requires a SQLAlchemy engine or a DB-API 2.0 compliant connection object.
	`pip install sqlalchemy psycopg2-binary` (for PostgreSQL, others for MySQL, SQLite, etc.)

	**Reading from SQL:** `pd.read_sql_query()` or `pd.read_sql_table()` or `pd.read_sql()`
	```python
	import pandas as pd
	from sqlalchemy import create_engine # Example

	# Example with SQLAlchemy engine (replace with your DB connection details)
	engine = create_engine("postgresql://user:password@host:port/database")
	
	query = "SELECT column1, column2 FROM my_table WHERE condition;"
	df_sql = pd.read_sql_query(query, engine)
	print(df_sql.head())

	# Read entire table
	df_table = pd.read_sql_table("my_table_name", engine, schema="my_schema")
	```

	**Writing to SQL:** `DataFrame.to_sql()`
	```python
	# Assuming df is an existing DataFrame and engine is configured
	df.to_sql(
	    name="new_table_name",
	    con=engine,
	    if_exists='replace', # 'fail', 'append'
	    index=False,         # Don't write DataFrame index as a column
	    # chunksize=1000     # For large DataFrames
	)
	```
- JSON Files
	JavaScript Object Notation ([[JSON]]) is a common data interchange format.

	**Reading from JSON:** `pd.read_json()`
	```python
	import pandas as pd

	# Assuming 'data.json' contains JSON data (e.g., array of objects)
	df_json = pd.read_json("data.json", orient='records') # 'orient' depends on JSON structure

	# Common 'orient' values:
	'split': dict like {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
	'records': list of dicts [{column -> value}, ... {column -> value}]
	'index': dict like {index -> {column -> value}}
	'columns': dict like {column -> {index -> value}}
	'values': just the values array
	'table': for table schema
	```

	**Writing to JSON:** `DataFrame.to_json()`
	```python
	# Assuming df is an existing DataFrame
	json_string = df.to_json(orient='records', indent=4) # indent for pretty printing
	with open("output.json", "w") as f:
	    f.write(json_string)

	# Or directly to file:
	df.to_json("output_direct.json", orient='records', indent=4)
	```
- Other Formats
	Pandas supports many other formats:
	- **HTML:** `pd.read_html()` (parses tables from HTML pages), `df.to_html()`
	- **Clipboard:** `pd.read_clipboard()`, `df.to_clipboard()`
	- **Pickle:** `pd.read_pickle()`, `df.to_pickle()` (Python-specific binary format)
	- **HDF5:** `pd.read_hdf()`, `df.to_hdf()` (Hierarchical Data Format, good for large datasets)
	- **Parquet:** `pd.read_parquet()`, `df.to_parquet()` (Columnar storage, efficient for analytics)
	- Feather, ORC, Stata, SAS, SPSS, Google BigQuery, etc.

## General Considerations

- **File Paths:** Can be local file paths, URLs, or file-like objects.
- **Performance:** For very large datasets, binary formats like HDF5, Parquet, or Feather are generally more efficient than text-based formats like CSV or JSON.
- **Dependencies:** Some formats (like Excel, SQL, Parquet) require installing additional Python libraries.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- Data Formats: [[CSV_Files]], [[Excel_Files]], [[SQL_Databases]], [[JSON]], HDF5, Parquet
- File Handling

---
**Source:** Pandas Documentation