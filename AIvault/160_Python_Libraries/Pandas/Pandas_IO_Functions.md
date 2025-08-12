---
tags:
  - pandas
  - python
  - file_io
  - data_loading
  - data_saving
  - concept
aliases:
  - Pandas read_csv
  - Pandas to_csv
  - Pandas read_excel
  - Pandas to_excel
  - Pandas read_sql
  - Pandas to_sql
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Data_Loading_IO]]" # General overview
  - "[[CSV_Files]]"
  - "[[Excel_Files]]"
  - "[[SQL_Databases]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas I/O: CSV, Excel, SQL

This note details common Pandas I/O functions for CSV, Excel, and SQL databases, as listed in the worksheet keywords. For a broader overview, see [[Pandas_Data_Loading_IO]].

## CSV Files

[list2card|addClass(ab-col2)]
- **`pd.read_csv(filepath_or_buffer, sep=',', ...)`**
  - **Purpose:** Reads a comma-separated values (CSV) file into a [[Pandas_DataFrame]].
  - **Key Parameters:**
    - `filepath_or_buffer`: Path to file, URL, or file-like object.
    - `sep` (or `delimiter`): Delimiter to use (default is `,`).
    - `header`: Row number(s) to use as column names (e.g., `0` for first line, `None` if no header).
    - `index_col`: Column(s) to use as row index.
    - `usecols`: Subset of columns to read.
    - `dtype`: Data type for data or columns.
    - `na_values`: Additional strings to recognize as `NaN`.
    - `skiprows`: Number of lines to skip at the start.
    - `nrows`: Number of rows to read.
    - `parse_dates`: Columns to parse as dates.
    - `encoding`: File encoding (e.g., `'utf-8'`).
  - **Example:**
    ```python
    import pandas as pd
    # df = pd.read_csv('data.csv', index_col='ID', usecols=['ID', 'Name', 'Score'])
    ```
- **`DataFrame.to_csv(path_or_buf, sep=',', index=True, header=True, ...)`**
  - **Purpose:** Writes a DataFrame to a CSV file.
  - **Key Parameters:**
    - `path_or_buf`: File path or object.
    - `sep`: Field delimiter (default `,`).
    - `index`: Write row index (default `True`). Set to `False` to omit.
    - `header`: Write column names (default `True`).
    - `columns`: Subset of columns to write.
    - `mode`: `'w'` (write, default) or `'a'` (append).
    - `encoding`: File encoding.
    - `na_rep`: String representation for `NaN` values.
  - **Example:**
    ```python
    # Assuming df is a DataFrame
    # df.to_csv('output.csv', index=False)
    ```

## Excel Files (`.xls`, `.xlsx`)

Requires `openpyxl` (for `.xlsx`) or `xlrd` (for older `.xls`). Install with `pip install openpyxl xlrd`.

[list2card|addClass(ab-col2)]
- **`pd.read_excel(io, sheet_name=0, header=0, index_col=None, ...)`**
  - **Purpose:** Reads an Excel file into a DataFrame.
  - **Key Parameters:**
    - `io`: File path, URL, or ExcelFile object.
    - `sheet_name`: String name of sheet, integer position (0-indexed), list of names/positions (returns dict of DataFrames), or `None` (all sheets). Default is `0`.
    - `header`, `index_col`, `usecols`, `dtype`, `na_values`, `skiprows`.
  - **Example:**
    ```python
    import pandas as pd
    # df_sheet1 = pd.read_excel('workbook.xlsx', sheet_name='DataSheet1')
    # all_sheets_dict = pd.read_excel('workbook.xlsx', sheet_name=None)
    ```
- **`DataFrame.to_excel(excel_writer, sheet_name='Sheet1', index=True, header=True, ...)`**
  - **Purpose:** Writes a DataFrame to an Excel file.
  - **Key Parameters:**
    - `excel_writer`: File path or `ExcelWriter` object.
    - `sheet_name`: Name of the sheet to write to.
    - `index`, `header`, `columns`.
    - `startrow`, `startcol`: Top-left cell to write data to.
  - **Example (single sheet):**
    ```python
    # Assuming df is a DataFrame
    # df.to_excel('output_excel.xlsx', sheet_name='ReportData', index=False)
    ```
  - **Example (multiple sheets using `ExcelWriter`):**
    ```python
    # with pd.ExcelWriter('multiple_reports.xlsx') as writer:
    #     df_report1.to_excel(writer, sheet_name='Report1')
    #     df_report2.to_excel(writer, sheet_name='Report2')
    ```

## SQL Databases

Requires a database driver (e.g., `psycopg2` for PostgreSQL, `mysql.connector` for MySQL) and often SQLAlchemy (`pip install sqlalchemy`).

[list2card|addClass(ab-col2)]
- **`pd.read_sql(sql, con, index_col=None, params=None, ...)`**
  - **Purpose:** Reads data from a SQL database into a DataFrame.
  - **Key Parameters:**
    - `sql`: SQL query string to be executed or a table name.
    - `con`: SQLAlchemy engine, DBAPI2 connection, or sqlite3.Connection.
    - `index_col`: Column to set as DataFrame index.
    - `params`: List of parameters to pass to the SQL query.
  - **Note:** `pd.read_sql_query()` (for queries) and `pd.read_sql_table()` (for full tables, needs SQLAlchemy) are more specific alternatives.
  - **Example:**
    ```python
    import pandas as pd
    # from sqlalchemy import create_engine
    # engine = create_engine('sqlite:///my_database.db')
    # query = "SELECT * FROM users WHERE age > 30;"
    # df_users = pd.read_sql(query, engine)
    ```
- **`DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)`**
  - **Purpose:** Writes records stored in a DataFrame to a SQL database table.
  - **Key Parameters:**
    - `name`: Name of the SQL table.
    - `con`: SQLAlchemy engine or DBAPI2 connection.
    - `schema`: Specify schema (if database supports it).
    - `if_exists`: How to behave if table already exists: `'fail'` (raise error), `'replace'` (drop then create new), `'append'` (insert new values).
    - `index`: Write DataFrame index as a column (default `True`).
    - `index_label`: Column label(s) for index column(s).
    - `chunksize`: Number of rows to write at a time (for large DataFrames).
    - `dtype`: Dictionary mapping column names to SQLAlchemy types.
  - **Example:**
    ```python
    # Assuming df_new_users is a DataFrame and engine is configured
    # df_new_users.to_sql('users_table', engine, if_exists='append', index=False)
    ```

## Related Concepts
- [[Pandas_DataFrame]] (The primary object for I/O)
- [[Pandas_Data_Loading_IO]] (General overview)
- File formats: CSV, Excel, SQL, JSON, etc.
- Database connectivity (SQLAlchemy, DBAPI2)

---
**Source:** WS_Pandas_Main, Pandas Documentation