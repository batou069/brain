---
tags: [comparison, sql, r, numpy, pandas, data_manipulation, syntax, concept]
aliases: [Data Tool Syntax Comparison, Pandas vs SQL, R vs SQL, NumPy vs Pandas]
related:
  - "[[SQL_MOC]]"
  - "[[R_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[_Pandas_MOC]]"
worksheet: [WS_Tool_Comparison_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---

# SQL vs. R vs. NumPy vs. Pandas: Syntax Comparison

This note provides a comparative overview of common data manipulation tasks and how they are performed using SQL, R (with `dplyr`), Pandas, and pure NumPy.

> [!note] Assumptions
> - **SQL:** Standard SQL syntax is used. Minor variations may exist across different RDBMS.
> - **R:** Examples primarily use base R and the `dplyr` package. Assumes `dplyr` is loaded (`library(dplyr)`).
> - **Python (Pandas/NumPy):** Assumes `import pandas as pd` and `import numpy as np`.
> - **Data:** Examples refer to a conceptual `employees` table/DataFrame (cols: `id`, `name`, `department`, `salary`, `hire_date`, `manager_id`) and a `departments` table/DataFrame (cols: `dept_id`, `dept_name`).

[list2tab|#Data Operations]
- Data Loading
    [list2tab|#Load Tasks]
    - Load CSV File
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Example for PostgreSQL:
                COPY employees FROM '/path/to/employees.csv' DELIMITER ',' CSV HEADER;

                -- Example for MySQL:
                LOAD DATA INFILE '/path/to/employees.csv'
                INTO TABLE employees
                FIELDS TERMINATED BY ','
                LINES TERMINATED BY '\n'
                IGNORE 1 ROWS;
	            ```
	            - SQL loads data into pre-existing tables. Syntax varies significantly by RDBMS. This is a bulk load operation, not typically for ad-hoc analysis of a single file without a database.
        - Pandas
            -
                ```python
                import pandas as pd
                employees_df = pd.read_csv('employees.csv')
                ```
	            - `pd.read_csv()` is the standard function. It infers data types and can handle many options.
        - NumPy
            -
                ```python
                import numpy as np
                # For purely numerical CSVs, skipping header
                data_array = np.loadtxt('numerical_data.csv', delimiter=',', skiprows=1)

                # For CSVs with mixed types (more complex, often less ideal than Pandas)
                # Assumes first row is header, attempts to infer dtypes.
                employees_array = np.genfromtxt('employees.csv', delimiter=',', names=True, dtype=None, encoding='utf-8-sig')
                ```
	            - `np.loadtxt()` is for simple numerical data. `np.genfromtxt()` is more flexible for mixed types and missing values but returns a structured array. Pandas is generally preferred for tabular CSVs.
        - R
            -
                ```R
                employees_df <- read.csv("employees.csv")
                # For other delimiters, use read.table() or read.delim()
                 employees_df_tsv <- read.delim("employees.tsv")
                ```
	            - `read.csv()` is the base R function for CSVs. `read.table()` is more general. `data.table::fread()` or `readr::read_csv()` offer faster alternatives.
    - Load Excel File
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- No direct SQL command. Usually done via:
                -- 1. Database import tools (GUI).
                -- 2. Intermediate conversion to CSV then load.
                -- 3. Linked servers or external table features (advanced, RDBMS-specific).
                ```
	            - SQL databases typically require data to be in a more structured format like CSV or directly inserted. Excel import is usually an external process.
        - Pandas
            -
                ```python
                import pandas as pd
                # Read the first sheet
                employees_df = pd.read_excel('employees.xlsx')
                # Read a specific sheet
                employees_df_sheet2 = pd.read_excel('employees.xlsx', sheet_name='Sheet2')
                ```
	            - `pd.read_excel()` handles `.xls` and `.xlsx` files. Requires `openpyxl` or `xlrd` engine.
        - NumPy
            -
                ```python
                import numpy as np
                # NumPy does not have a built-in function to directly read Excel files.
                # Typically, one would use Pandas to read Excel then convert to NumPy array if needed:
                # import pandas as pd
                excel_data_df = pd.read_excel('data.xlsx')
                data_array = excel_data_df.to_numpy()
                ```
	            - Direct Excel reading is outside NumPy's core scope. Pandas is the go-to Python tool for this.
        - R
            -
                ```R
                # Using the 'readxl' package (recommended)
                install.packages("readxl") # If not already installed
                library(readxl)
                employees_df <- read_excel("employees.xlsx")
                # Read a specific sheet
                employees_df_sheet2 <- read_excel("employees.xlsx", sheet = "Sheet2")
                ```
	            - The `readxl` package is commonly used for reading Excel files. Older packages like `xlsx` exist but may have Java dependencies.
- Data Inspection
    [list2tab|#Inspect Tasks]
    - View First N Rows
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT * FROM employees LIMIT 5;
                -- SQL Server: SELECT TOP 5 * FROM employees;
                -- Oracle: SELECT * FROM employees WHERE ROWNUM <= 5;
                ```
	            - `LIMIT` clause is common. Syntax varies slightly.
        - Pandas
            -
                ```python
                import pandas as pd
                # Assuming employees_df is loaded
                print(employees_df.head(5))
                ```
	            - `.head(n)` method displays the first `n` rows. Default is 5.
        - NumPy
            -
                ```python
                import numpy as np
                # Assuming employees_array is loaded (e.g., structured array)
                print(employees_array[:5])
                # For a 2D homogeneous array:
                print(data_2d_array[:5, :]) # First 5 rows, all columns
                ```
	            - Array slicing is used. For structured arrays, this shows the first 5 records.
        - R
            -
                ```R
                # Assuming employees_df is loaded
                print(head(employees_df, n = 5))
                ```
	            - `head(df, n)` function displays the first `n` rows. Default for `n` is 6.
    - View Last N Rows
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- No standard SQL command for "last N" without an ordering column.
                -- Often requires ordering in descending order then LIMIT.
                SELECT * FROM employees ORDER BY id DESC LIMIT 5; -- Assuming 'id' defines order
                ```
	            - SQL requires an explicit ordering to define "last".
        - Pandas
            -
                ```python
                import pandas as pd
                print(employees_df.tail(5))
                ```
	            - `.tail(n)` method displays the last `n` rows. Default is 5.
        - NumPy
            -
                ```python
                import numpy as np
                # print(employees_array[-5:])
                # For a 2D homogeneous array:
                print(data_2d_array[-5:, :]) # Last 5 rows, all columns
                ```
	            - Negative indexing is used for slicing from the end.
        - R
            -
                ```R
                print(tail(employees_df, n = 5))
                ```
	            - `tail(df, n)` function displays the last `n` rows. Default for `n` is 6.
    - Get Dimensions
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Number of rows
                SELECT COUNT(*) AS num_rows FROM employees;
                -- Number of columns (RDBMS specific)
                -- PostgreSQL:
                -- SELECT COUNT(*) AS num_cols FROM information_schema.columns WHERE table_name = 'employees';
                ```
	            - Row count is standard. Column count often queries system catalogs.
        - Pandas
            -
                ```python
                import pandas as pd
                print(employees_df.shape) # Returns (number_of_rows, number_of_columns)
                ```
	            - `.shape` attribute returns a tuple `(rows, cols)`.
        - NumPy
            -
                ```python
                import numpy as np
                print(employees_array.shape) # For structured or homogeneous arrays
                # For structured arrays, len() gives rows, len(dtype.names) gives columns
                print(f"Rows: {len(employees_array)}, Cols: {len(employees_array.dtype.names)}")
                ```
	            - `.shape` attribute. For 1D structured arrays (like from `genfromtxt`), `len()` is rows, `len(dtype.names)` is columns.
        - R
            -
                ```R
                print(dim(employees_df))      # Returns c(number_of_rows, number_of_columns)
                print(nrow(employees_df))   # Number of rows
                print(ncol(employees_df))   # Number of columns
                ```
	            - `dim()` returns a vector. `nrow()` and `ncol()` give specific dimensions.
    - Column Data Types
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- RDBMS specific
                -- PostgreSQL: \d employees
                -- MySQL: DESCRIBE employees;
                -- SQL Server: EXEC sp_help 'employees';
                -- Standard:
                SELECT column_name, data_type FROM information_schema.columns
                WHERE table_name = 'employees';
                ```
	            - Relies on database-specific commands or `information_schema`.
        - Pandas
            -
                ```python
                import pandas as pd
                print(employees_df.dtypes)
                # For more detailed info including non-null counts and memory:
                employees_df.info()
                ```
	            - `.dtypes` attribute shows data type of each column. `.info()` is more comprehensive.
        - NumPy
            -
                ```python
                import numpy as np
                print(employees_array.dtype) # For structured arrays, shows field names and their types
                # For homogeneous arrays, shows the single data type of all elements.
                print(data_2d_array.dtype)
                ```
	            - `.dtype` attribute. For structured arrays, it's a compound dtype object.
        - R
            -
                ```R
                print(sapply(employees_df, class))
                # For a more detailed structure view:
                str(employees_df)
                ```
	            - `sapply(df, class)` iterates `class()` over columns. `str()` gives a detailed summary.
    - Summary Stats
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT
                    COUNT(salary) as count_salary,
                    AVG(salary) as mean_salary,
                    STDDEV(salary) as std_salary, -- or STDEV()
                    MIN(salary) as min_salary,
                    MAX(salary) as max_salary
                FROM employees;
                -- For multiple columns, repeat or use subqueries/CTEs.
                ```
	            - Aggregate functions compute statistics for specified columns.
        - Pandas
            -
                ```python
                import pandas as pd
                # For numerical columns
                print(employees_df.describe())
                # For all columns (including categorical)
                print(employees_df.describe(include='all'))
                ```
	            - `.describe()` provides count, mean, std, min, quartiles, max for numerical columns. `include='all'` adds stats for object/categorical columns.
        - NumPy
            -
                ```python
                import numpy as np
                # Assuming 'salary' is a field in a structured array or a separate 1D array
                salary_col = employees_array['salary'].astype(float) # Ensure numeric for stats
                print(f"Mean: {np.mean(salary_col)}, Std: {np.std(salary_col)}")
                print(f"Min: {np.min(salary_col)}, Max: {np.max(salary_col)}")
                print(f"Percentiles (25,50,75): {np.percentile(salary_col, [25, 50, 75])}")
                ```
	            - NumPy functions like `np.mean`, `np.std`, `np.min`, `np.max`, `np.percentile` operate on arrays. Requires extraction of numerical columns.
        - R
            -
                ```R
                # For the entire data frame (provides min, 1Q, median, mean, 3Q, max for numeric)
                print(summary(employees_df))
                # For specific column, e.g., salary:
                summary(employees_df$salary)
                # For individual stats:
                mean(employees_df$salary, na.rm = TRUE)
                sd(employees_df$salary, na.rm = TRUE)
                ```
	            - `summary()` function gives a quick overview. Individual functions for specific stats. `na.rm = TRUE` is important for calculations if NAs are present.
- Select & Filter
    [list2tab|#Select/Filter]
    - Select Columns
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT name, department, salary
                FROM employees;
                ```
	            - List desired column names in the `SELECT` statement.
        - Pandas
            -
                ```python
                import pandas as pd
                # Method 1: List of column names
                selected_df = employees_df[['name', 'department', 'salary']]
                # Method 2: Using .loc for label-based selection
                selected_loc_df = employees_df.loc[:, ['name', 'department', 'salary']]
                # Select a single column as a Series
                salary_series = employees_df['salary']
                ```
	            - `df[['col1', 'col2']]` or `df.loc[:, ['col1', 'col2']]`. Single bracket `df['col']` returns a Series.
        - NumPy
            -
                ```python
                import numpy as np
                # For structured arrays (by field name)
                # selected_fields = employees_array[['name', 'department', 'salary']]
                # For 2D homogeneous arrays (by column index)
                # Assuming name=idx 0, department=idx 1, salary=idx 2
                selected_cols_np = data_2d_array[:, [0, 1, 2]]
                ```
	            - For structured arrays, use a list of field names. For homogeneous arrays, use integer slicing for columns.
        - R
            -
                ```R
                # Method 1: Base R with c() for column names
                selected_df_base <- employees_df[, c("name", "department", "salary")]
                # Method 2: Base R with $ for single column (returns vector)
                salary_vector <- employees_df$salary
                # Method 3: dplyr::select()
                library(dplyr)
                selected_df_dplyr <- employees_df %>% select(name, department, salary)
                ```
	            - Base R uses `df[, c(...)]`. `dplyr::select()` is a common tidyverse approach.
    - Filter Rows
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT *
                FROM employees
                WHERE department = 'Sales' AND salary > 60000;
                ```
	            - Use the `WHERE` clause with conditions.
        - Pandas
            -
                ```python
                import pandas as pd
                # Method 1: Boolean indexing
                filtered_df = employees_df[(employees_df['department'] == 'Sales') & (employees_df['salary'] > 60000)]
                # Method 2: .query() method
                filtered_query_df = employees_df.query("department == 'Sales' and salary > 60000")
                ```
	            - Boolean indexing is powerful. `.query()` offers a string-based alternative.
        - NumPy
            -
                ```python
                import numpy as np
                # For structured arrays
                # Ensure correct data types for comparison, e.g. department might be bytes
                # Assuming department is string and salary is float/int
                condition = (employees_array['department'] == 'Sales') & (employees_array['salary'] > 60000)
                filtered_np_array = employees_array[condition]

                # For 2D homogeneous arrays (more complex, assumes column indices)
                dept_idx = 1; salary_idx = 2; # Example indices
                condition_2d = (data_2d_array[:, dept_idx] == 'Sales') & (data_2d_array[:, salary_idx].astype(float) > 60000)
                filtered_2d_np_array = data_2d_array[condition_2d]
                ```
	            - Boolean indexing on arrays. Requires careful handling of data types, especially for string comparisons in structured arrays (might be bytes).
        - R
            -
                ```R
                # Method 1: Base R subsetting
                filtered_df_base <- employees_df[employees_df$department == "Sales" & employees_df$salary > 60000, ]
                # Method 2: dplyr::filter()
                library(dplyr)
                filtered_df_dplyr <- employees_df %>% filter(department == "Sales", salary > 60000)
                ```
	            - Base R uses logical vectors for row subsetting. `dplyr::filter()` is a common tidyverse approach.
    - Distinct Values
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT DISTINCT department
                FROM employees;
                ```
	            - `DISTINCT` keyword applied to one or more columns.
        - Pandas
            -
                ```python
                import pandas as pd
                # Get unique values from a single column (returns NumPy array)
                unique_departments = employees_df['department'].unique()
                # Get DataFrame of unique rows based on a subset of columns
                unique_dept_salary_combos = employees_df[['department', 'salary']].drop_duplicates()
                ```
	            - `.unique()` on a Series. `.drop_duplicates()` on a DataFrame (can specify `subset`).
        - NumPy
            -
                ```python
                import numpy as np
                # For a single field in a structured array or a 1D array
                unique_np_departments = np.unique(employees_array['department'])
                # For unique rows in a 2D array (more complex, often easier via Pandas)
                unique_rows_np, indices = np.unique(data_2d_array, axis=0, return_index=True)
                data_2d_array_unique_rows = data_2d_array[np.sort(indices)]
                ```
	            - `np.unique()` works well on 1D arrays or fields. For unique rows in 2D arrays, `axis=0` can be used, but preserving order might need `return_index`.
        - R
            -
                ```R
                # Base R: Get unique values from a single column (returns vector)
                unique_departments_base <- unique(employees_df$department)
                # Base R: Get unique rows from a data frame
                unique_rows_df_base <- unique(employees_df) # Considers all columns
                dplyr::distinct()
                library(dplyr)
                # Get distinct values of 'department' column
                distinct_departments_dplyr <- employees_df %>% distinct(department)
                # Get distinct rows based on all columns or specified columns
                distinct_rows_dplyr <- employees_df %>% distinct()
                distinct_dept_salary_dplyr <- employees_df %>% distinct(department, salary)
                ```
	            - `unique()` for vectors. `dplyr::distinct()` is flexible for data frames.
- Data Manipulation
    [list2tab|#Manipulate Tasks]
    - Add New Column
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Derived column in a query
                SELECT
                    name,
                    salary,
                    salary * 0.10 AS bonus_amount
                FROM employees;

                -- Adding a persistent column (syntax varies)
                -- ALTER TABLE employees ADD COLUMN bonus_percentage DECIMAL(5,2);
                -- UPDATE employees SET bonus_percentage = 0.10;
                ```
	            -   Derived columns are common in `SELECT`. Adding persistent columns is a DDL operation (`ALTER TABLE`).
        - Pandas
            -
                ```python
                import pandas as pd
                # Assuming employees_df exists
                employees_df['bonus_amount'] = employees_df['salary'] * 0.10
                # Using .assign() for a new DataFrame (immutable style)
                employees_df_with_bonus = employees_df.assign(bonus_amount = employees_df['salary'] * 0.10)
                ```
	            -   Direct assignment creates/updates a column. `.assign()` returns a new DataFrame.
        - NumPy
            -
                ```python
                import numpy as np
                # Assuming employees_array is a structured array with 'salary' field
                # This is complex for structured arrays; typically involves creating a new array
                # with an expanded dtype. For simplicity, let's show for a conceptual 2D array
                # where salary is, say, column index 3.
                salaries = data_2d_array[:, 3].astype(float)
                bonus_column = salaries * 0.10
                data_2d_array_with_bonus = np.column_stack((data_2d_array, bonus_column))

                # For structured arrays, it's often easier to convert to Pandas, add column, then back to NumPy if needed.
                # Or, create a new structured array:
                if 'salary' in employees_array.dtype.names:
                    bonus_values = employees_array['salary'] * 0.10
                    new_dtype = employees_array.dtype.descr + [('bonus_amount', bonus_values.dtype)]
                    employees_with_bonus_array = np.empty(employees_array.shape, dtype=new_dtype)
                    for name in employees_array.dtype.names:
                        employees_with_bonus_array[name] = employees_array[name]
                    employees_with_bonus_array['bonus_amount'] = bonus_values
                ```
	            -   Adding columns to NumPy arrays (especially structured ones) is less direct than Pandas. Homogeneous arrays can use `np.column_stack` or `np.hstack`.
        - R
            -
                ```R
                # Base R
                employees_df$bonus_amount <- employees_df$salary * 0.10
                # Using dplyr::mutate()
                library(dplyr)
                employees_df <- employees_df %>%
                  mutate(bonus_amount = salary * 0.10)
                ```
	            -   Direct assignment with `$` or `dplyr::mutate()` are common.
    - Rename Columns
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Alias in a query
                SELECT name AS employee_name, hire_date AS start_date
                FROM employees;

                -- Renaming a persistent column (DDL, syntax varies)
                ALTER TABLE employees RENAME COLUMN salary TO annual_income;
                ```
	            -   `AS` keyword for aliases in `SELECT`. `ALTER TABLE` for persistent changes.
        - Pandas
            -
                ```python
                import pandas as pd
                # Rename specific columns, returns a new DataFrame by default
                renamed_df = employees_df.rename(columns={'name': 'employee_name', 'hire_date': 'start_date'})
                # To rename in-place
                employees_df.rename(columns={'name': 'employee_name'}, inplace=True)
                ```
	            -   `.rename(columns=...)` method is flexible. `inplace=True` modifies original.
        - NumPy
            -
                ```python
                import numpy as np
                # Homogeneous arrays don't have column names, only indices.
                # For structured arrays, renaming fields is not direct.
                # It usually involves creating a new structured array with the new field names
                # and copying the data, which is cumbersome.
                # Example: if employees_array.dtype.names was ('id', 'name', 'salary')
                new_dtype = [('emp_id', 'i4'), ('full_name', 'U30'), ('annual_salary', 'f8')]
                new_array = np.empty(employees_array.shape, dtype=new_dtype)
                new_array['emp_id'] = employees_array['id']
                new_array['full_name'] = employees_array['name']
                new_array['annual_salary'] = employees_array['salary']
                ```
	            -   No direct renaming for homogeneous arrays. Structured arrays require creating a new array with a new dtype.
        - R
            -
                ```R
                # Using base R `names()` or `colnames()`
                current_names <- names(employees_df)
                current_names[current_names == "name"] <- "employee_name"
                current_names[current_names == "hire_date"] <- "start_date"
                names(employees_df) <- current_names

                # Using dplyr::rename()
                library(dplyr)
                employees_df_renamed <- employees_df %>%
                  rename(employee_name = name, start_date = hire_date)
                ```
	            -   Modifying `names()` or `colnames()` vector. `dplyr::rename()` is common.
    - Delete Columns
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- "Delete" by not selecting in a query
                SELECT id, name, salary -- hire_date is excluded
                FROM employees;

                -- Deleting a persistent column (DDL, syntax varies)
                -- ALTER TABLE employees DROP COLUMN manager_id;
                ```
	            -   Excluding from `SELECT` or `ALTER TABLE DROP COLUMN`.
        - Pandas
            -
                ```python
                import pandas as pd
                # Using .drop(), returns a new DataFrame by default
                df_dropped_cols = employees_df.drop(columns=['manager_id', 'hire_date'])
                # To drop in-place
                employees_df.drop(columns=['manager_id'], inplace=True)
                # Using del keyword (in-place)
                del employees_df['manager_id']
                ```
	            -   `.drop(columns=...)` is preferred. `del` also works.
        - NumPy
            -
                ```python
                import numpy as np
                # For structured arrays: select fields to keep
                fields_to_keep = [name for name in employees_array.dtype.names if name not in ['manager_id', 'hire_date']]
                array_dropped_fields = employees_array[fields_to_keep]

                # For 2D homogeneous arrays: delete by column index
                # Assuming manager_id is at index 4
                data_2d_dropped_col = np.delete(data_2d_array, 4, axis=1)
                ```
	            -   For structured arrays, create a new view/copy with desired fields. For homogeneous, `np.delete()` along `axis=1`.
        - R
            -
                ```R
                # Base R: setting column to NULL
                employees_df$manager_id <- NULL
                # Base R: subsetting by column names to keep
                cols_to_keep <- setdiff(names(employees_df), c("manager_id", "hire_date"))
                employees_df_dropped <- employees_df[, cols_to_keep]

                # Using dplyr::select() with negation
                library(dplyr)
                employees_df_dropped_dplyr <- employees_df %>%
                  select(-manager_id, -hire_date)
                ```
	            -   Assigning `NULL`, subsetting, or `dplyr::select(-col_name)`.
    - Sort Data
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT *
                FROM employees
                ORDER BY department ASC, salary DESC;
                ```
	            -   `ORDER BY` clause with `ASC` (default) or `DESC`.
        - Pandas
            -
                ```python
                import pandas as pd
                sorted_df = employees_df.sort_values(by=['department', 'salary'], ascending=[True, False])
                ```
	            -   `.sort_values()` method, `ascending` list matches `by` list.
        - NumPy
            -
                ```python
                import numpy as np
                # For structured arrays
                # Sorts in-place by default if assigned back, or use np.sort for a copy
                # For mixed ascending/descending, it's complex. Typically sort one by one or use Pandas.
                # Simple sort by department, then by salary (both ascending):
                sorted_employees_array = np.sort(employees_array, order=['department', 'salary'])

                # For 2D homogeneous arrays (sorts rows based on a column's values)
                # Assuming salary is at index 3
                sort_indices = np.argsort(data_2d_array[:, 3]) # Ascending
                sorted_data_2d = data_2d_array[sort_indices]
                # For descending:
                sorted_data_2d_desc = data_2d_array[sort_indices[::-1]]
                ```
	            -   `np.sort(order=...)` for structured arrays. `np.argsort()` for homogeneous arrays to get indices for sorting.
        - R
            -
                ```R
                # Base R using order()
                # For salary descending, use a negative sign if numeric
                sorted_df_base <- employees_df[order(employees_df$department, -employees_df$salary), ]

                # Using dplyr::arrange()
                library(dplyr)
                sorted_df_dplyr <- employees_df %>%
                  arrange(department, desc(salary))
                ```
	            -   `order()` with indexing. `dplyr::arrange()` with `desc()` for descending.
    - Apply Function
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Using built-in functions or user-defined functions (UDFs)
                SELECT
                    name,
                    salary,
                    UPPER(department) AS department_upper,
                    salary * 1.10 AS increased_salary -- Simple arithmetic
                FROM employees;
                -- More complex logic might require CASE statements or UDFs
                ```
	            -   SQL relies on built-in functions (e.g., `UPPER`, `ROUND`) or database-specific UDFs for complex transformations.
        - Pandas
            -
                ```python
                import pandas as pd
                def custom_function(row):
                    if row['salary'] > 70000:
                        return 'High'
                    elif row['salary'] > 50000:
                        return 'Medium'
                    else:
                        return 'Low'
                # Apply to a column (Series)
                employees_df['department_upper'] = employees_df['department'].str.upper()
                # Apply a function row-wise (can be slower)
                employees_df['salary_category'] = employees_df.apply(custom_function, axis=1)
                # Apply to a column using .map (for Series) or .applymap (for DataFrame element-wise)
                employees_df['salary_plus_1k'] = employees_df['salary'].map(lambda x: x + 1000)
                ```
	            -   `.apply()` (row/column-wise), `.map()` (Series element-wise), `.applymap()` (DataFrame element-wise), vectorized string methods (`.str`), direct arithmetic.
        - NumPy
            -
                ```python
                import numpy as np
                # NumPy excels at vectorized operations on homogeneous arrays.
                salaries_np = employees_array['salary'].astype(float)
                increased_salaries_np = salaries_np * 1.10 # Vectorized
                department_np = employees_array['department']
                department_upper_np = np.char.upper(department_np) # Vectorized string op

                # Applying arbitrary Python functions element-wise can be done with np.vectorize
                # (though it's often a loop internally, not as fast as true ufuncs)
                def categorize_salary_np(s):
                    if s > 70000: return 'High'
                    elif s > 50000: return 'Medium'
                    else: return 'Low'
                vectorized_categorize = np.vectorize(categorize_salary_np)
                salary_categories_np = vectorized_categorize(salaries_np)
                ```
	            -   Favors vectorized operations (ufuncs). `np.vectorize` for convenience with non-ufuncs. String operations via `np.char`.
        - R
            -
                ```R
                # Base R using apply family (e.g., sapply, lapply) or direct vectorization
                employees_df$department_upper <- toupper(employees_df$department)
                employees_df$increased_salary <- employees_df$salary * 1.10

                # Custom function (example for salary category)
                categorize_salary_r <- function(s) {
                  if (is.na(s)) return(NA)
                  if (s > 70000) return("High")
                  else if (s > 50000) return("Medium")
                  else return("Low")
                }
                employees_df$salary_category <- sapply(employees_df$salary, categorize_salary_r)

                # Using dplyr::mutate() with functions
                library(dplyr)
                employees_df <- employees_df %>%
                  mutate(
                    department_upper = toupper(department),
                    salary_category = case_when(
                      salary > 70000 ~ "High",
                      salary > 50000 ~ "Medium",
                      TRUE ~ "Low" # Default case
                    )
                  )
                ```
	            -   R is naturally vectorized for many operations. `sapply`/`lapply` for element/list-wise application. `dplyr::mutate()` with `case_when()` is powerful.
- Joining Data (More)
    [list2tab|#Join Tasks]
    - Right Join
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT e.name, d.dept_name, e.salary
                FROM employees e
                RIGHT JOIN departments d ON e.dept_id = d.dept_id;
                ```
	            -   Returns all rows from the right table (`departments`), and matched rows from the left (`employees`). Unmatched left rows get NULLs.
        - Pandas
            -
                ```python
                import pandas as pd
                # Assuming employees_df and departments_df exist
                right_join_df = pd.merge(employees_df, departments_df,
                                         left_on='dept_id', right_on='dept_id', # Assuming common key is 'dept_id' in both
                                         how='right')
                ```
	            -   `pd.merge(..., how='right')`.
        - NumPy
            -
                ```python
                # Not a native high-level operation in NumPy.
                # Would require complex manual logic similar to inner join, but keeping all of the 'right' array.
                # Generally, convert to Pandas for joins.
                ```
	            -   Joins are best handled by Pandas or database systems.
        - R
            -
                ```R
                # Base R merge()
                # right_join_df_base <- merge(employees_df, departments_df, by = "dept_id", all.y = TRUE)

                 dplyr::right_join()
                library(dplyr)
                right_join_df_dplyr <- employees_df %>%
                  right_join(departments_df, by = "dept_id")
                ```
	            -   Base R `merge(all.y = TRUE)`. `dplyr::right_join()`.
    - Full Outer Join
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT e.name, d.dept_name, e.salary
                FROM employees e
                FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;
                ```
	            -   Returns all rows from both tables. Unmatched rows from either side get NULLs for columns from the other table.
        - Pandas
            -
                ```python
                import pandas as pd
                full_outer_join_df = pd.merge(employees_df, departments_df,
                                              left_on='dept_id', right_on='dept_id',
                                              how='outer')
                ```
	            -   `pd.merge(..., how='outer')`.
        - NumPy
            -
                ```python
                # Not a native high-level operation in NumPy.
                ```
	            -   Joins are best handled by Pandas or database systems.
        - R
            -
                ```R
                # Base R merge()
                full_outer_join_df_base <- merge(employees_df, departments_df, by = "dept_id", all = TRUE)

                dplyr::full_join()
                library(dplyr)
                full_outer_join_df_dplyr <- employees_df %>%
                  full_join(departments_df, by = "dept_id")
                ```
	            -   Base R `merge(all = TRUE)`. `dplyr::full_join()`.
    - Self Join
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Find employees and their managers (assuming manager_id refers to another employee's id)
                SELECT
                    e.name AS employee_name,
                    m.name AS manager_name
                FROM employees e
                LEFT JOIN employees m ON e.manager_id = m.id;
                ```
	            -   Joining a table to itself. Requires table aliases to distinguish instances.
        - Pandas
            -
                ```python
                import pandas as pd
                # Merge employees_df with itself
                self_join_df = pd.merge(employees_df, employees_df,
                                        left_on='manager_id', right_on='id',
                                        how='left', suffixes=('_emp', '_mgr'))
                # Select and rename columns for clarity
                result = self_join_df[['name_emp', 'name_mgr']].rename(columns={'name_emp':'employee_name', 'name_mgr':'manager_name'})
                ```
	            -   `pd.merge()` can join a DataFrame with itself. `suffixes` is important to differentiate columns with same names.
        - NumPy
            -
                ```python
                # Not a native high-level operation. Requires manual iteration and matching.
                ```
	            -   Best handled by Pandas or database systems.
        - R
            -
                ```R
                # Base R merge() - can be done but might need careful column renaming first or after
                managers_df <- employees_df # Create a copy for managers
                names(managers_df)[names(managers_df) == "id"] <- "manager_actual_id"
                names(managers_df)[names(managers_df) == "name"] <- "manager_name"
                self_join_df_base <- merge(employees_df, managers_df[, c("manager_actual_id", "manager_name")],
                                           by.x = "manager_id", by.y = "manager_actual_id", all.x = TRUE)

                # dplyr - more straightforward with joins and select/rename
                library(dplyr)
                self_join_df_dplyr <- employees_df %>%
                  left_join(employees_df %>% select(id, manager_name = name),
                            by = c("manager_id" = "id")) %>%
                  select(employee_name = name, manager_name)
                ```
	            -   Base R requires more steps. `dplyr` allows for cleaner self-joins.
- GroupBy & Aggregation (More)
    [list2tab|#GroupBy Advanced]
    - Multiple Aggregations
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT
                    department,
                    COUNT(id) AS num_employees,
                    AVG(salary) AS avg_salary,
                    MIN(salary) AS min_salary,
                    MAX(salary) AS max_salary,
                    SUM(salary) AS total_salary_paid
                FROM employees
                GROUP BY department;
                ```
	            -   List multiple aggregate functions in the `SELECT` statement with the `GROUP BY` clause.
        - Pandas
            -
                ```python
                import pandas as pd
                agg_summary_df = employees_df.groupby('department')['salary'].agg(
                    num_employees='count', # Note: this counts non-NA salaries. For total employees, use a column like 'id'
                    avg_salary='mean',
                    min_salary='min',
                    max_salary='max',
                    total_salary_paid='sum'
                ).reset_index()

                # To count total employees per department:
                agg_summary_df_emp_count = employees_df.groupby('department').agg(
                   num_employees=('id', 'size'), # 'size' counts all rows in group
                   avg_salary=('salary', 'mean')
                ).reset_index()
                ```
	            -   Use `.groupby().agg()` with a dictionary specifying new column names and aggregation functions.
        - NumPy
            -
                ```python
                # Requires manual looping through groups after identifying them,
                # then applying multiple np aggregate functions to slices.
                # Example conceptual outline for one group 'Sales':
                sales_salaries = employees_array[employees_array['department'] == 'Sales']['salary'].astype(float)
                num_employees_sales = len(sales_salaries)
                avg_salary_sales = np.mean(sales_salaries)
                min_salary_sales = np.min(sales_salaries)
                # ... and so on for each department. Very verbose.
                ```
	            -   Not straightforward. Requires significant manual coding or external libraries.
        - R
            -
                ```R
                library(dplyr)
                agg_summary_df_dplyr <- employees_df %>%
                  group_by(department) %>%
                  summarise(
                    num_employees = n(), # n() gives count of rows in group
                    avg_salary = mean(salary, na.rm = TRUE),
                    min_salary = min(salary, na.rm = TRUE),
                    max_salary = max(salary, na.rm = TRUE),
                    total_salary_paid = sum(salary, na.rm = TRUE)
                  )
                ```
	            -   `dplyr::group_by()` followed by `summarise()` with multiple aggregation functions.
    - Group by Multiple Cols
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Assume an additional column 'job_level'
                SELECT
                    department,
                    job_level,
                    AVG(salary) AS avg_salary_by_level
                FROM employees
                GROUP BY department, job_level
                ORDER BY department, job_level;
                ```
	            -   List multiple columns in the `GROUP BY` clause.
        - Pandas
            -
                ```python
                import pandas as pd
                # Assume 'job_level' column exists
                multi_group_df = employees_df.groupby(['department', 'job_level'])['salary'].mean().reset_index()
                # To rename the aggregated column:
                multi_group_df = employees_df.groupby(['department', 'job_level']).agg(
                   avg_salary_by_level=('salary', 'mean')
                ).reset_index()
                ```
	            -   Pass a list of column names to `.groupby()`.
        - NumPy
            -
                ```python
                # Even more complex manually than single column groupby.
                # Would involve sorting by multiple fields, then iterating through complex group boundaries.
                # Pandas is strongly recommended.
                ```
	            -   Highly impractical to do efficiently with pure NumPy for general cases.
        - R
            -
                ```R
                library(dplyr)
                # Assume 'job_level' column exists
                multi_group_df_dplyr <- employees_df %>%
                  group_by(department, job_level) %>%
                  summarise(
                    avg_salary_by_level = mean(salary, na.rm = TRUE)
                  ) %>%
                  ungroup() # Good practice to ungroup after summarise
                ```
	            -   Pass multiple column names to `dplyr::group_by()`.
- Advanced Operations / Workflows
    [list2tab|#Advanced Tasks]
    - Binning Numerical Data
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT
                    name,
                    salary,
                    CASE
                        WHEN salary < 50000 THEN 'Low'
                        WHEN salary >= 50000 AND salary < 80000 THEN 'Medium'
                        WHEN salary >= 80000 THEN 'High'
                        ELSE 'Unknown' -- Handles NULLs if not filtered
                    END AS salary_bin
                FROM employees;
                ```
	            -   Use `CASE` statements to define bins. Some databases might have specific functions for ranges or percentiles.
        - Pandas
            -
                ```python
                import pandas as pd
                bins = [0, 49999, 79999, float('inf')] # Define bin edges
                labels = ['Low', 'Medium', 'High']
                employees_df['salary_bin'] = pd.cut(employees_df['salary'], bins=bins, labels=labels, right=True)
                # right=True means bins include the right edge (e.g., 49999 is Low)
                # For quantile-based bins:
                employees_df['salary_quantile_bin'] = pd.qcut(employees_df['salary'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
                ```
	            -   `pd.cut()` for fixed bins, `pd.qcut()` for quantile-based bins.
        - NumPy
            -
                ```python
                import numpy as np
                salaries_np = employees_array['salary'].astype(float)
                bins = np.array([0, 49999, 79999, np.inf])
                labels_np = np.array(['Low', 'Medium', 'High']) # For display, actual result of digitize is int
                # # np.digitize returns the indices of the bins to which each value belongs
                bin_indices = np.digitize(salaries_np, bins[1:], right=True) # Exclude first bin edge for right=True logic
                salary_bins_np = labels_np[bin_indices] # Map indices to labels

                # A more direct way to get integer bins:
                bin_assignment = np.digitize(salaries_np, bins=bins)
                # This assigns 1 for first bin, 2 for second, etc. based on where value falls
                ```
	            -   `np.digitize()` can assign values to bins based on edges, returning integer indices of bins.
        - R
            -
                ```R
                # Base R using cut()
                bins <- c(0, 49999, 79999, Inf)
                labels <- c("Low", "Medium", "High")
                employees_df$salary_bin_base <- cut(employees_df$salary, breaks = bins, labels = labels, right = TRUE, include.lowest = TRUE)

                # dplyr using case_when() or cut() within mutate()
                library(dplyr)
                employees_df <- employees_df %>%
                  mutate(
                    salary_bin_dplyr = case_when(
                      salary < 50000 ~ "Low",
                      salary >= 50000 & salary < 80000 ~ "Medium",
                      salary >= 80000 ~ "High",
                      TRUE ~ NA_character_ # Handle NAs or other cases
                    ),
                    salary_bin_cut_dplyr = cut(salary, breaks = bins, labels = labels, right = TRUE, include.lowest = TRUE)
                  )
                ```
	            -   Base R `cut()` is powerful. `dplyr::case_when()` or `cut()` within `mutate()` are also common.
    - Generate Full Range
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Generate a series of prices (e.g., 0 to 1000) and LEFT JOIN actual data
                -- Syntax for generating series varies greatly by RDBMS
                -- PostgreSQL example:
                WITH all_prices AS (
                    SELECT generate_series(0, 1000) AS price_point
                ),
                product_sales AS (
                    -- Conceptual table with sales data
                    SELECT price, SUM(units_sold) as total_units, COUNT(*) as transactions
                    FROM sales_data
                    GROUP BY price
                )
                SELECT
                    ap.price_point,
                    COALESCE(ps.total_units, 0) AS total_units_sold,
                    COALESCE(ps.transactions, 0) AS num_transactions
                FROM all_prices ap
                LEFT JOIN product_sales ps ON ap.price_point = ps.price
                ORDER BY ap.price_point;
                ```
	            -   Requires a way to generate a series of numbers (e.g., `generate_series` in PostgreSQL, recursive CTEs in others). Then `LEFT JOIN` your actual data to this complete range.
        - Pandas
            -
                ```python
                import pandas as pd
                import numpy as np
                # Assume sales_data_df has 'price' and 'units_sold'
                sales_summary = sales_data_df.groupby('price')['units_sold'].agg(['sum', 'count']).reset_index()
                sales_summary.columns = ['price', 'total_units_sold', 'num_transactions']

                # Create a DataFrame with all desired prices
                min_price = 0
                max_price = 1000 # Or sales_data_df['price'].max() if dynamic
                all_prices_df = pd.DataFrame({'price_point': np.arange(min_price, max_price + 1)})

                # Merge to get the full range, filling missing sales with 0
                complete_sales_df = pd.merge(all_prices_df, sales_summary,
                                             left_on='price_point', right_on='price',
                                             how='left').drop(columns=['price']).fillna(0)
                complete_sales_df.rename(columns={'price_point': 'price'}, inplace=True)
                ```
	            -   Create a DataFrame/Series with the full desired range (e.g., using `np.arange` or `pd.RangeIndex`). Then `pd.merge` (left join) your aggregated actual data to it, and `fillna()` for points with no sales.
        - NumPy
            -
                ```python
                import numpy as np
                # Assume sales_prices_np (1D array of prices from sales) and units_sold_np (1D array)
                # This is much more manual with NumPy.
                # 1. Aggregate actual sales by price (e.g., using np.unique and np.bincount or loops)
                unique_sale_prices, counts = np.unique(sales_prices_np, return_counts=True)
                summed_units = np.array([np.sum(units_sold_np[sales_prices_np == p]) for p in unique_sale_prices])

                # 2. Create the full price range
                full_price_range_np = np.arange(0, 1001)

                # 3. Map aggregated sales to the full range (manual lookup and fill)
                units_on_full_range = np.zeros_like(full_price_range_np, dtype=float)
                transactions_on_full_range = np.zeros_like(full_price_range_np, dtype=int)
                for i, p_val in enumerate(unique_sale_prices):
                    if 0 <= p_val <= 1000: # Check if within desired range
                        idx_in_full_range = np.where(full_price_range_np == p_val)
                        if idx_in_full_range.size > 0:
                            units_on_full_range[idx_in_full_range] = summed_units[i]
                            transactions_on_full_range[idx_in_full_range] = counts[i]
                ```
	            -   Very manual. Involves creating the full range, aggregating actual data, and then carefully mapping/merging, often with loops or complex indexing. Pandas is far superior for this.
        - R
            -
                ```R
                library(dplyr)
                # Assume sales_data_df has 'price' and 'units_sold'
                sales_summary <- sales_data_df %>%
                  group_by(price) %>%
                  summarise(total_units_sold = sum(units_sold, na.rm = TRUE),
                            num_transactions = n(), .groups = 'drop')

                # Create a data frame with all desired prices
                all_prices_df <- data.frame(price_point = seq(0, 1000))

                Left join and replace NAs with 0
                complete_sales_df_r <- all_prices_df %>%
                  left_join(sales_summary, by = c("price_point" = "price")) %>%
                  mutate(
                    total_units_sold = ifelse(is.na(total_units_sold), 0, total_units_sold),
                    num_transactions = ifelse(is.na(num_transactions), 0, num_transactions)
                  ) %>%
                 rename(price = price_point)
                
                # Alternative using tidyr::complete for expanding grid
                library(tidyr)
                complete_sales_df_tidyr <- sales_data_df %>%
                  group_by(price) %>%
                  summarise(total_units_sold = sum(units_sold, na.rm = TRUE),
                            num_transactions = n(), .groups = 'drop') %>%
                  complete(price = seq(0, 1000), fill = list(total_units_sold = 0, num_transactions = 0))
                ```
		            -   Create a data frame with the full range. Use `dplyr::left_join` and then handle NAs, or `tidyr::complete` provides a more direct way to expand a data frame to include all combinations of specified variables, filling in missing values.
- Missing Values
    [list2tab|#Missing Data Ops]
    - Find Missing
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Find rows where 'salary' is missing
                SELECT * FROM employees WHERE salary IS NULL;

                -- Count missing salaries per department
                SELECT
                    department,
                    SUM(CASE WHEN salary IS NULL THEN 1 ELSE 0 END) AS missing_salary_count
                FROM employees
                GROUP BY department;
                ```
            -   Use `IS NULL` to identify missing values. Aggregations often require `CASE` statements or `COUNT(column)` vs `COUNT(*)` logic.
        - Pandas
            -
                ```python
                import pandas as pd
                import numpy as np # For creating example data with NaNs

                # Example DataFrame
                data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
                        'department': ['HR', 'Engineering', 'HR', np.nan],
                        'salary': [70000, 80000, np.nan, 90000]}
                employees_df = pd.DataFrame(data)

                # Boolean DataFrame indicating NaNs
                is_missing_df = employees_df.isnull()
                # print("Is Missing DF:\n", is_missing_df)

                # Count missing values per column
                missing_counts = employees_df.isnull().sum()
                # print("\nMissing counts per column:\n", missing_counts)

                # Filter rows where 'salary' is NaN
                missing_salary_rows = employees_df[employees_df['salary'].isnull()]
                # print("\nRows with missing salary:\n", missing_salary_rows)
                ```
            -   `.isnull()` or `.isna()` creates a boolean mask. `.sum()` on this mask counts `True` values (missing).
        - NumPy
            -
                ```python
                import numpy as np

                # Example structured array with potential NaNs (if float) or other sentinels
                # For floats, NaN is standard. For other types, it's more complex.
                salary_data = np.array([70000.0, 80000.0, np.nan, 90000.0])
                department_data = np.array(['HR', 'Engineering', 'HR', None], dtype=object) # Using None for object arrays

                # Finding NaNs in a float array
                is_salary_nan = np.isnan(salary_data)
                # print("Salary NaN mask:", is_salary_nan)
                # print("Count of NaN salaries:", np.sum(is_salary_nan))

                # Finding None in an object array (or specific sentinels)
                is_department_none = (department_data == None)
                # print("\nDepartment None mask:", is_department_none)
                # print("Count of None departments:", np.sum(is_department_none))
                ```
            -   `np.isnan()` for float arrays. For object arrays, check against `None` or other sentinels. No single function for all missing types across structured arrays.
        - R
            -
                ```R
                # Example data frame
                employees_df_r <- data.frame(
                  name = c("Alice", "Bob", "Charlie", "David"),
                  department = c("HR", "Engineering", "HR", NA_character_),
                  salary = c(70000, 80000, NA_real_, 90000)
                )

                # Boolean data frame indicating NAs
                is_na_df <- is.na(employees_df_r)
                # print("Is NA DF:")
                # print(is_na_df)

                # Count missing values per column
                missing_counts_r <- colSums(is.na(employees_df_r))
                # print("Missing counts per column:")
                # print(missing_counts_r)

                # Filter rows where 'salary' is NA
                missing_salary_rows_r <- employees_df_r[is.na(employees_df_r$salary), ]
                # print("Rows with missing salary:")
                # print(missing_salary_rows_r)
                ```
            -   `is.na()` creates a logical mask. `colSums()` on this mask counts `TRUE` values (missing).
    - Fill Missing
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Fill missing 'salary' with 0 in a query
                SELECT name, COALESCE(salary, 0) AS filled_salary
                FROM employees;

                -- Update missing 'salary' to department average (example, can be complex)
                -- UPDATE employees e
                -- SET salary = (SELECT AVG(s.salary) FROM employees s WHERE s.department = e.department AND s.salary IS NOT NULL)
                -- WHERE e.salary IS NULL;
                ```
            -   `COALESCE(column, value_if_null)` is standard. Updates require more complex subqueries or procedural logic.
        - Pandas
            -
                ```python
                import pandas as pd
                import numpy as np
                data = {'salary': [70000, 80000, np.nan, 90000], 'department': ['HR', 'Eng', 'HR', 'Eng']}
                employees_df = pd.DataFrame(data)

                # Fill all NaNs with a specific value
                df_filled_zero = employees_df.fillna(value=0)
                # print("Filled with 0:\n", df_filled_zero)

                # Fill 'salary' NaNs with the mean salary
                mean_salary = employees_df['salary'].mean()
                employees_df['salary_filled_mean'] = employees_df['salary'].fillna(mean_salary)
                # print("\nSalary filled with mean:\n", employees_df)

                # Forward fill
                # employees_df['salary_ffill'] = employees_df['salary'].fillna(method='ffill')
                # Backward fill
                # employees_df['salary_bfill'] = employees_df['salary'].fillna(method='bfill')
                ```
            -   `.fillna()` is versatile: can fill with a scalar, a Series/dict (for different values per column), or using methods like `ffill` or `bfill`.
        - NumPy
            -
                ```python
                import numpy as np
                salary_data = np.array([70000.0, 80000.0, np.nan, 90000.0])

                # Fill NaNs with a specific value (e.g., 0)
                salary_filled_zero_np = np.nan_to_num(salary_data, nan=0.0)
                # print("NaNs filled with 0:", salary_filled_zero_np)

                # Fill NaNs with the mean (ignoring NaNs in mean calculation)
                mean_val = np.nanmean(salary_data)
                salary_filled_mean_np = np.where(np.isnan(salary_data), mean_val, salary_data)
                # Or: salary_filled_mean_np = np.nan_to_num(salary_data, nan=mean_val)
                # print("NaNs filled with mean:", salary_filled_mean_np)
                ```
            -   `np.nan_to_num()` or boolean indexing with `np.isnan()` and assignment. `np.nanmean()` calculates mean ignoring NaNs.
        - R
            -
                ```R
                employees_df_r <- data.frame(salary = c(70000, 80000, NA, 90000))

                # Fill NAs in 'salary' with 0
                employees_df_r_filled_zero <- employees_df_r
                employees_df_r_filled_zero$salary[is.na(employees_df_r_filled_zero$salary)] <- 0
                # print(employees_df_r_filled_zero)

                # Fill NAs in 'salary' with mean salary
                mean_salary_r <- mean(employees_df_r$salary, na.rm = TRUE)
                employees_df_r_filled_mean <- employees_df_r
                employees_df_r_filled_mean$salary[is.na(employees_df_r_filled_mean$salary)] <- mean_salary_r
                # print(employees_df_r_filled_mean)

                # Using dplyr::mutate and coalesce or tidyr::replace_na
                library(dplyr)
                library(tidyr) # For replace_na
                # employees_df_r_dplyr_fill <- employees_df_r %>%
                #   mutate(salary = coalesce(salary, mean(salary, na.rm = TRUE)))
                # OR
                # employees_df_r_tidyr_fill <- employees_df_r %>%
                #   replace_na(list(salary = 0))
                ```
            -   Base R uses indexing with `is.na()`. `dplyr::coalesce` or `tidyr::replace_na` provide convenient alternatives.
    - Drop Missing Rows
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Select rows where 'salary' AND 'department' are not NULL
                SELECT *
                FROM employees
                WHERE salary IS NOT NULL AND department IS NOT NULL;

                -- Delete rows where 'salary' is NULL (DML)
                -- DELETE FROM employees WHERE salary IS NULL;
                ```
            -   Filter with `IS NOT NULL`. `DELETE` statement for persistent removal.
        - Pandas
            -
                ```python
                import pandas as pd
                import numpy as np
                data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                        'department': ['HR', 'Engineering', np.nan, 'HR', 'Sales'],
                        'salary': [70000, 80000, 60000, np.nan, 90000]}
                employees_df = pd.DataFrame(data)

                # Drop rows if ANY column has a NaN
                df_dropped_any = employees_df.dropna()
                # print("Dropped if any NaN:\n", df_dropped_any)

                # Drop rows if ALL columns have NaN (less common)
                df_dropped_all = employees_df.dropna(how='all')

                # Drop rows if NaN appears in a SUBSET of columns
                df_dropped_subset = employees_df.dropna(subset=['salary', 'department'])
                # print("\nDropped if NaN in salary or department:\n", df_dropped_subset)
                ```
            -   `.dropna()` method with `how` ('any' or 'all') and `subset` parameters.
        - NumPy
            -
                ```python
                import numpy as np
                # Example: 2D float array where rows with any NaN should be dropped
                data_float_array = np.array([[1.0, 2.0, 3.0],
                                             [4.0, np.nan, 6.0],
                                             [7.0, 8.0, 9.0],
                                             [np.nan, np.nan, np.nan]])

                # Keep rows where ALL elements are not NaN
                data_dropped_np = data_float_array[~np.isnan(data_float_array).any(axis=1)]
                # print("Rows without any NaNs:\n", data_dropped_np)

                # Keep rows where ALL elements are finite (not NaN, not Inf)
                data_finite_rows = data_float_array[np.isfinite(data_float_array).all(axis=1)]
                ```
            -   Boolean indexing using `~np.isnan().any(axis=1)` (to drop if any NaN in row) or `np.isfinite().all(axis=1)`. More complex for structured arrays with mixed types.
        - R
            -
                ```R
                employees_df_r <- data.frame(
                  name = c("Alice", "Bob", "Charlie", "David", "Eve"),
                  department = c("HR", "Engineering", NA, "HR", "Sales"),
                  salary = c(70000, 80000, 60000, NA, 90000)
                )

                # Base R: na.omit() removes rows with any NA
                df_dropped_base <- na.omit(employees_df_r)
                # print("Dropped rows with any NA (base R):\n")
                # print(df_dropped_base)

                dplyr::filter() with !is.na() or drop_na() from tidyr
                library(dplyr)
                library(tidyr)
                # Drop if 'salary' is NA
                df_dropped_dplyr_salary <- employees_df_r %>% filter(!is.na(salary))
                # Drop if 'salary' OR 'department' is NA using tidyr
                df_dropped_tidyr_subset <- employees_df_r %>% drop_na(salary, department)
                # print("\nDropped if NA in salary or department (tidyr):\n")
                # print(df_dropped_tidyr_subset)
                ```
            -   `na.omit()` is a common base R function. `tidyr::drop_na()` or `dplyr::filter(!is.na(col))` provide more control.
- Window Functions
    [list2tab|#Window Ops]
    - Moving Average
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                -- Calculate 3-period moving average of salary, partitioned by department
                SELECT
                    name,
                    department,
                    salary,
                    hire_date,
                    AVG(salary) OVER (PARTITION BY department ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_salary
                FROM employees
                ORDER BY department, hire_date;
                ```
            -   SQL window functions (`OVER (PARTITION BY ... ORDER BY ... ROWS/RANGE BETWEEN ...)`). Powerful for calculations over a "window" of rows related to the current row.
        - Pandas
            -
                ```python
                import pandas as pd
                data = {'department': ['Sales', 'Sales', 'Sales', 'Sales', 'HR', 'HR', 'HR'],
                        'salary':,
                        'hire_date': pd.to_datetime(['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01',
                                                  '2020-01-15', '2020-02-15', '2020-03-15'])}
                employees_df = pd.DataFrame(data).sort_values(by=['department', 'hire_date'])

                # Calculate 3-period rolling mean of salary within each department
                employees_df['moving_avg_salary'] = employees_df.groupby('department')['salary'] \
                                                              .rolling(window=3, min_periods=1) \
                                                              .mean() \
                                                              .reset_index(level=0, drop=True)
                # print(employees_df)
                ```
            -   `.groupby().rolling(window=...).mean()`. `min_periods=1` allows calculation for first few rows. `reset_index` is needed to align back.
        - NumPy
            -
                ```python
                import numpy as np
                # Manually implementing rolling window averages in NumPy is complex,
                # especially with groups. It involves striding tricks or explicit looping.
                # Example for a single 1D array (no grouping):
                 def rolling_mean_np(arr, window):
                     if window == 0: return arr
                     cumsum = np.cumsum(np.insert(arr, 0, 0)) # Cumulative sum
                     return (cumsum[window:] - cumsum[:-window]) / float(window)

                salaries = np.array()
                moving_avg_salaries = rolling_mean_np(salaries, 3)
                # print(moving_avg_salaries) # Note: length is len(salaries) - window + 1
                # Handling groups and aligning would require much more code.
                ```
            -   No direct built-in for grouped rolling operations. Possible for 1D arrays with `np.convolve` or manual cumsum methods, but complex for grouped data.
        - R
            -
                ```R
                library(dplyr)
                library(zoo) # For rollmean

                employees_df_r <- data.frame(
                  department = rep(c("Sales", "HR"), each = 4),
                  salary = c(50, 55, 60, 58, 70, 75, 72, 78),
                  hire_date = as.Date(c('2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01',
                                      '2020-01-15', '2020-02-15', '2020-03-15', '2020-04-15'))
                ) %>% arrange(department, hire_date)

                employees_df_r <- employees_df_r %>%
                  group_by(department) %>%
                  mutate(moving_avg_salary = zoo::rollmean(salary, k = 3, fill = NA, align = "right")) %>%
                  ungroup()
                # print(employees_df_r)
                # fill=NA and align="right" makes it similar to pandas default for first few values.
                # min_periods=1 equivalent in R's rollmean is often handled by partial=TRUE or careful fill.
                ```
            -   Packages like `zoo` or `RcppRoll` provide `rollmean`, `rollapply` etc. `dplyr::mutate` within groups is used. `slider` package is another modern option.
    - Rank Within Group
        [list2mdtable]
        - Language:
            - Code:
                - Comment:
        - SQL
            -
                ```sql
                SELECT
                    name,
                    department,
                    salary,
                    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank_in_dept
                FROM employees;
                ```
            -   `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()` are common window functions for ranking.
        - Pandas
            -
                ```python
                import pandas as pd
                data = {'name': ['A','B','C','D','E','F'],
                        'department': ['Sales','Sales','HR','HR','Sales','HR'],
                        'salary':}
                employees_df = pd.DataFrame(data)

                employees_df['salary_rank_in_dept'] = employees_df.groupby('department')['salary'] \
                                                                  .rank(method='dense', ascending=False)
                # print(employees_df.sort_values(by=['department', 'salary_rank_in_dept']))
                # method='dense': 1,2,2,3. 'min': 1,2,2,4. 'first': unique ranks based on order.
                ```
            -   `.groupby().rank()`. `method` controls tie-breaking. `ascending=False` for higher salary = higher rank.
        - NumPy
            -
                ```python
                # Very complex to do efficiently with pure NumPy for grouped ranking.
                # Would involve sorting within groups and then assigning ranks.
                # Pandas is the appropriate tool here.
                ```
            -   Not a standard NumPy operation. Requires extensive manual logic.
        - R
            -
                ```R
                library(dplyr)
                employees_df_r <- data.frame(
                  name = c("A","B","C","D","E","F"),
                  department = c("Sales","Sales","HR","HR","Sales","HR"),
                  salary = c(70, 80, 60, 75, 70, 65)
                )

                employees_df_r_ranked <- employees_df_r %>%
                  group_by(department) %>%
                  mutate(salary_rank_in_dept = dense_rank(desc(salary))) %>%
                  # For other rank types: rank(desc(salary), ties.method = "min" / "average" / "first")
                  ungroup() %>%
                  arrange(department, salary_rank_in_dept)
                # print(employees_df_r_ranked)
                ```
            -   `dplyr::group_by()` then `mutate()` with `rank()`, `dense_rank()`, `min_rank()`, etc. `desc()` for descending order ranking.

---
