---
tags:
  - pandas
  - python
  - iteration
  - dataframe
  - function
  - concept
  - performance
aliases:
  - df.iterrows
  - Iterate DataFrame Rows
related:
  - "[[Pandas_DataFrame]]"
  - "[[Pandas_Series]]"
  - "[[Pandas_Iteration_Efficiency]]" # Placeholder
  - "[[Pandas_df_itertuples]]" # Placeholder (more efficient alternative)
  - "[[Pandas_Apply_Map_Applymap]]" # Vectorized alternatives
  - "[[Python_Loops]]"
worksheet: [WS_Pandas_Main]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pandas `DataFrame.iterrows()`

## Definition

`DataFrame.iterrows()` is a method that iterates over the rows of a Pandas [[Pandas_DataFrame|DataFrame]] as **(index, Series) pairs**. For each row, it yields a tuple where the first element is the row's index label and the second element is a [[Pandas_Series|Pandas Series]] containing the data for that row (with column names as the Series's index).

## Syntax

```python
DataFrame.iterrows()
```
- Takes no arguments.

## Return Value

- An iterator yielding `(index, Series)` pairs for each row.

## Usage Example

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age':,
        'City': ['NY', 'SF', 'LA']}
df = pd.DataFrame(data, index=['p1', 'p2', 'p3'])
print("DataFrame:\n", df)

print("\nIterating with iterrows():")
for index_label, row_series in df.iterrows():
    print(f"\nIndex Label: {index_label}")
    print("Row Data (as Series):")
    print(row_series)
    print(f"  Name: {row_series['Name']}, Age: {row_series['Age']}")
```
**Output:**
```
DataFrame:
       Name  Age City
p1    Alice   25   NY
p2      Bob   30   SF
p3  Charlie   22   LA

Iterating with iterrows():

Index Label: p1
Row Data (as Series):
Name     Alice
Age         25
City        NY
Name: p1, dtype: object
  Name: Alice, Age: 25

Index Label: p2
Row Data (as Series):
Name     Bob
Age       30
City      SF
Name: p2, dtype: object
  Name: Bob, Age: 30

Index Label: p3
Row Data (as Series):
Name     Charlie
Age           22
City          LA
Name: p3, dtype: object
  Name: Charlie, Age: 22
```

## Performance Considerations & Alternatives 

>[!warning] Performance Warning
> **`iterrows()` is generally inefficient and should be avoided for large DataFrames or performance-critical operations.**
> - **Row-by-Row Series Creation:** It creates a new Pandas Series object for *every row* during iteration, which has significant overhead.
> - **Data Type Preservation:** Does not preserve dtypes across rows if columns have different dtypes. Each row Series will have an `object` dtype if its elements are of mixed types, or it will upcast to a common type.

**What is the most efficient way to iterate over rows of a pandas DataFrame? How about columns?** (WS_Pandas_Main Question 2)

- **Iterating Rows (Generally Avoid if Possible):**
    1.  **Vectorized Operations (Best):** The most efficient approach is to **avoid explicit iteration** altogether and use Pandas/NumPy vectorized operations (e.g., `df['NewCol'] = df['ColA'] + df['ColB']`, boolean indexing, `df.apply()` with optimized functions). See [[NumPy_Vectorization]].
    2.  **`df.apply(func, axis=1)`:** Applies `func` to each row (passed as a Series). Can be more concise than `iterrows()` but still involves iteration and Series creation per row, so not as fast as pure vectorization. See [[Pandas_Apply_Map_Applymap]].
    3.  **`df.itertuples(index=True, name='Pandas')`:** Yields namedtuples (or simple tuples if `name=None`) for each row. **Significantly faster than `iterrows()`** because it doesn't create a Series object for each row. Access elements by attribute (e.g., `row.ColumnName`) or index.
        ```python
        # for row_namedtuple in df.itertuples(name='User'):
        #     print(f"Name: {row_namedtuple.Name}, Age: {row_namedtuple.Age}")
        ```
    4.  **List Comprehensions / Generator Expressions with `zip` (on columns):** If you need to process multiple columns together.
        ```python
        # for name, age in zip(df['Name'], df['Age']):
        #     print(f"{name} is {age}")
        ```
    5.  **Accessing NumPy Array (`df.values`):** If all data is numeric and you only need the values, iterating over `df.values` (a NumPy array) can be faster, but you lose index/column labels.

- **Iterating Columns:**
    1.  **Direct Iteration over `df`:** Iterating directly over a DataFrame iterates over its **column names**.
        ```python
        # for col_name in df:
        #     print(f"Column: {col_name}")
        #     print(df[col_name]) # Accesses the column Series
        ```
    2.  **`df.items()` (or `df.iteritems()` - older):** Iterates over `(column_name, Series)` pairs.
        ```python
        # for col_name, col_series in df.items():
        #     print(f"\nColumn: {col_name}")
        #     print(col_series)
        ```
    These are generally efficient as they operate on whole Series (columns) at a time.

## When `iterrows()` Might Be Acceptable

- For very small DataFrames where performance is not a concern.
- When the logic for each row is complex and cannot be easily vectorized, and creating a Series per row is convenient for accessing elements by name within the loop.
- For quick, one-off explorations.

## Related Concepts
- [[Pandas_DataFrame]], [[Pandas_Series]]
- [[Pandas_Iteration_Efficiency]]
- [[Pandas_df_itertuples]] (More efficient row iteration)
- [[Pandas_Apply_Map_Applymap]] (Vectorized alternatives)
- [[Python_Loops]] (What `iterrows` emulates, but with overhead)

---
