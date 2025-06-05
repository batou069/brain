---
tags:
  - pandas
  - python
  - data_manipulation
  - selection
  - filtering
  - function
  - concept
aliases:
  - df.query
  - Pandas DataFrame Query
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Indexing_Selection]]"
  - "[[NumPy_Boolean_Indexing]]" # Alternative way to filter
  - "[[Python_eval]]" # Placeholder, query uses similar mechanisms
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `DataFrame.query()`

## Definition

The `DataFrame.query(expr, inplace=False, **kwargs)` method allows you to filter rows of a [[Pandas_DataFrame|DataFrame]] using a **boolean expression string**. This can often be a more readable and concise way to perform conditional selection compared to standard [[NumPy_Boolean_Indexing|boolean indexing]], especially for complex conditions.

## Syntax

```python
DataFrame.query(expr, inplace=False, **kwargs)
```

-   **`expr`**: A string representing the boolean expression to evaluate.
    -   Column names can be used directly as variables within the expression string.
    -   If column names have spaces or special characters, they must be enclosed in backticks (e.g., `` `Column Name with Spaces` ``).
    -   You can refer to variables in the local Python scope by prefixing them with `@` (e.g., `df.query('Age > @min_age')`).
    -   Supports standard comparison operators (`>`, `<`, ` == `, ` != `, ` >= `, ` <= `), logical operators (`and`, `or`, `not` or `&`, `|`, `~`), and `in`/`not in` operators.
    -   Function calls and arithmetic operations can also be part of the expression.
-   **`inplace`**: (Default `False`) If `True`, modifies the DataFrame in place and returns `None`. If `False`, returns a new filtered DataFrame.
-   **`**kwargs`**: Additional keyword arguments passed to the evaluation engine (e.g., `engine='python'` or `engine='numexpr'`). `numexpr` can offer performance benefits for large DataFrames and complex expressions.


## Advantages
- **Readability:** For complex conditions, query strings can be more natural to read than chained boolean indexing expressions with many parentheses.
- **Conciseness:** Often results in shorter code.
- **Performance (Potentially):** With the `numexpr` engine, `query()` can sometimes be faster than equivalent boolean indexing for large DataFrames, as `numexpr` can optimize numerical expressions and use multiple cores.

## Examples: `query()`

[list2tab]
- Setup
  ```python
  import pandas as pd
  data = {
      'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
      'Age':,
      'Score':,
      'City': ['NY', 'SF', 'LA', 'NY', 'SF'],
      'Years Experience': # Column with spaces
  }
  df = pd.DataFrame(data)
  print("Original DataFrame:\n", df)
  ```

- Basic Queries
  ```python
  # Select rows where Age > 25
  older_than_25 = df.query('Age > 25')
  print("\nAge > 25:\n", older_than_25)

  # Select rows where City is 'SF'
  sf_residents = df.query("City == 'SF'") # Note: string values need quotes inside the query string
  print("\nCity == 'SF':\n", sf_residents)
  ```

- Complex Queries
  ```python
  # Age > 25 AND City == 'NY'
  older_ny_residents = df.query('Age > 25 and City == "NY"')
  # Equivalent: df.query('Age > 25 & City == "NY"')
  print("\nAge > 25 AND City == 'NY':\n", older_ny_residents)

  # Age < 25 OR Score > 90
  young_or_high_score = df.query('Age < 25 or Score > 90')
  print("\nAge < 25 OR Score > 90:\n", young_or_high_score)
  ```

- Local Var (`@`)
  ```python
  min_age_threshold = 28
  min_score_threshold = 90

  # Referencing local variables with @
  filtered_by_vars = df.query('Age >= @min_age_threshold and Score < @min_score_threshold')
  print("\nAge >= min_age_threshold AND Score < min_score_threshold:\n", filtered_by_vars)
  ```

- `in` & `not in`
  ```python
  target_cities = ['NY', 'LA']
  # Rows where City is in the target_cities list
  in_target_cities = df.query('City in @target_cities')
  print("\nCity in ['NY', 'LA']:\n", in_target_cities)

  # Rows where City is NOT 'SF'
  not_sf = df.query("City != 'SF'") # or df.query("City not in ['SF']")
  print("\nCity != 'SF':\n", not_sf)
  ```

- Column Names with Spaces (Backticks)
  ```python
  # Select rows where 'Years Experience' > 4
  experienced = df.query("`Years Experience` > 4")
  print("\nYears Experience > 4:\n", experienced)
  ```

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Indexing_Selection]]
- [[NumPy_Boolean_Indexing]] (Alternative method for conditional selection)
- Query Languages (e.g., SQL `WHERE` clause - `query()` provides similar expressiveness)
- [[Python_eval]] (The underlying mechanism for evaluating the expression string is similar)

## Questions / Further Study
>[!question] What is the difference between querying and boolean indexing? (WS_Pandas_Main)
> Both `df.query('expression_string')` and standard boolean indexing (e.g., `df[ (df['colA'] > 5) & (df['colB'] == 'X') ]`) achieve conditional row selection.
> - **Syntax:**
>     - `query()`: Uses a **string expression** that is parsed and evaluated. Column names are treated like variables.
>     - Boolean Indexing: Uses **Python code** to construct a boolean Series directly, often involving standard Python comparison and logical operators (`&`, `|`, `~`) on Pandas Series.
> - **Readability:** For complex conditions, `query()` strings can sometimes be more readable and closer to natural language or SQL syntax. Boolean indexing with multiple conditions can become verbose with many parentheses.
> - **Performance:** For very large DataFrames and complex numerical expressions, `query()` *can* be faster if it utilizes the `numexpr` engine (which needs to be installed). For simpler conditions or smaller DataFrames, the performance difference might be negligible, and boolean indexing can sometimes be faster due to less overhead from string parsing.
> - **Variable Access:** `query()` allows easy access to local Python variables within the expression string using the `@` prefix (e.g., `df.query('Age > @min_age')`). Achieving this with boolean indexing requires directly inserting the variable into the boolean expression (e.g., `df[df['Age'] > min_age]`).
> - **Column Names:** `query()` handles column names with spaces or special characters by requiring backticks (`` `My Column` ``). Boolean indexing handles them directly as strings `df['My Column']`.
>
> **When to choose:**
> - **`query()`:** Good for complex conditions where string-based expression is more readable, or when performance with `numexpr` is a benefit. Convenient for using local variables in the condition.
> - **Boolean Indexing:** Standard, explicit, and often very clear for simple to moderately complex conditions. Always available and doesn't depend on an external engine like `numexpr`. Might be slightly more performant for very simple conditions due to no string parsing overhead.

---
**Source:** WS_Pandas_Main, Pandas Documentation