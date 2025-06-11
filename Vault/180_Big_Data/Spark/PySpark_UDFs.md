---
tags:
  - spark
  - pyspark
  - dataframe
  - udf
  - user_defined_function
  - performance
  - concept
  - example
aliases:
  - PySpark UDF
  - User Defined Functions PySpark
  - Pandas UDFs
related:
  - "[[PySpark_DataFrame_Operations]]"
  - "[[PySpark_SQL_Functions]]"
  - "[[Apache_Arrow]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: User-Defined Functions (UDFs)

**User-Defined Functions (UDFs)** in PySpark allow you to define custom column-based functions in Python that can be applied to [[Spark_DataFrame_SQL|Spark DataFrames]]. While Spark provides a rich set of built-in [[PySpark_SQL_Functions|`pyspark.sql.functions`]], UDFs are useful when you need to implement logic that is not available through these standard functions or is too complex to express with them.

There are primarily two types of UDFs in PySpark:
1.  **Regular Python UDFs:** Process data row by row.
2.  **Pandas UDFs (Vectorized UDFs):** Process data in batches using Pandas Series/DataFrames, offering significantly better performance.

## Regular Python UDFs
-   **Definition:** Defined as a standard Python function, then registered with Spark using `pyspark.sql.functions.udf()`.
-   **Execution:**
    -   Spark serializes the UDF and sends it to executors.
    -   Data is transferred between the Spark JVM (where DataFrame data resides) and Python worker processes on executors for each row. This involves **serialization and deserialization costs** (e.g., using Pickle).
    -   The Python function is executed row by row by a Python interpreter on the executor.
-   **Performance:** Can be slow due to serialization/deserialization overhead and row-at-a-time processing in Python. **Generally, avoid regular Python UDFs if the same logic can be achieved with built-in Spark SQL functions or Pandas UDFs.**
-   **Syntax:**
    ```python
    from pyspark.sql.functions import udf
    from pyspark.sql.types import StringType, IntegerType # For specifying return type

    # Define a Python function
    def categorize_price_py(price):
        if price is None:
            return "Unknown"
        if price < 50:
            return "Low"
        elif price < 200:
            return "Medium"
        else:
            return "High"

    # Register it as a UDF, specifying the return type
    categorize_price_udf = udf(categorize_price_py, StringType())
    ```

**Example (Using a regular Python UDF):**
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, udf
# from pyspark.sql.types import StringType

# spark = SparkSession.builder.appName("RegularUDFDemo").getOrCreate()

# product_data = [("Laptop", 1200.00), ("Mouse", 25.00), ("Keyboard", 75.00), (None, 150.00)]
# products_df = spark.createDataFrame(product_data, ["name", "price"])

# Define the Python function
# def get_price_category_simple(price):
#     if price is None: return "Unknown"
#     if price < 50: return "Budget"
#     if price < 200: return "Mid-Range"
#     return "Premium"

# Register the UDF
# get_price_category_udf = udf(get_price_category_simple, StringType())

# Apply the UDF
# products_with_category_df = products_df.withColumn(
#     "price_label", get_price_category_udf(col("price"))
# )
# products_with_category_df.show()
# # +--------+-------+------------+
# # |    name|  price| price_label|
# # +--------+-------+------------+
# # |  Laptop| 1200.0|     Premium|
# # |   Mouse|   25.0|      Budget|
# # |Keyboard|   75.0|   Mid-Range|
# # |    null|  150.0|   Mid-Range| # Example: If product name was null, price is still processed
# # +--------+-------+------------+

# spark.stop()
```

## Pandas UDFs (Vectorized UDFs)
-   **Definition:** Allow you to define UDFs that operate on Pandas Series or DataFrames within Spark.
-   **Execution:**
    -   Spark splits columns into batches.
    -   Each batch is converted to a Pandas Series/DataFrame.
    -   Your Python function (which takes and returns Pandas Series/DataFrames) is executed on these batches.
    -   The results (Pandas Series/DataFrames) are converted back to Spark DataFrame columns.
    -   Uses **[[Apache_Arrow]]** for efficient data transfer between JVM and Python processes, minimizing serialization overhead.
-   **Performance:** Significantly faster than regular Python UDFs for many operations because they process data in batches and leverage Pandas' optimized C implementations.
-   **Types (decorators used for registration):**
    -   **Scalar Pandas UDFs (`@pandas_udf(return_type, PandasUDFType.SCALAR)` or just `@pandas_udf(return_type)`):**
        -   Input: One or more `pandas.Series`.
        -   Output: A `pandas.Series` of the same length.
        -   Used like regular Spark SQL functions.
    -   **Grouped Map Pandas UDFs (`@pandas_udf(return_schema, PandasUDFType.GROUPED_MAP)`):**
        -   Used with `groupBy().applyInPandas()`.
        -   Splits a Spark DataFrame into groups, converts each group to a Pandas DataFrame, applies the function, and combines results.
        -   Input: A `pandas.DataFrame` (representing a group).
        -   Output: A `pandas.DataFrame` (with a specified schema).
    -   **Grouped Aggregate Pandas UDFs (`@pandas_udf(return_type, PandasUDFType.GROUPED_AGG)`):**
        -   Used with `groupBy().agg()`.
        -   Similar to Spark aggregate functions but defined in Python with Pandas.
        -   Input: One or more `pandas.Series` (representing columns of a group).
        -   Output: A single scalar value (the aggregate).
    -   *(Older Iterator UDFs also exist but Scalar and Grouped Map are most common).*

**Example (Scalar Pandas UDF for price categorization):**
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, pandas_udf
# from pyspark.sql.types import StringType
# import pandas as pd # Pandas UDFs operate on pandas Series/DataFrames

# spark = SparkSession.builder.appName("PandasUDFDemo").getOrCreate()

# product_data = [("Laptop", 1200.00), ("Mouse", 25.00), ("Keyboard", 75.00), (None, 150.00), ("Monitor", None)]
# products_df = spark.createDataFrame(product_data, ["name", "price"])

# Define the Python function that takes a pandas.Series and returns a pandas.Series
# @pandas_udf(StringType()) # Decorator specifies return type
# def categorize_price_pandas_udf(prices: pd.Series) -> pd.Series:
#     # Handle None/NaN within pandas Series if necessary
#     # prices = prices.fillna(-1) # Example: fill NaN to handle in conditions
#     conditions = [
#         (prices < 50),
#         (prices >= 50) & (prices < 200),
#         (prices >= 200)
#     ]
#     choices = ['Budget', 'Mid-Range', 'Premium']
#     # np.select is vectorized and efficient for conditional logic on pandas Series/numpy arrays
#     # It requires prices to be numeric and not have NaNs that break conditions,
#     # or handle NaNs explicitly before/within np.select.
#     # A simpler approach for this UDF if NaNs can exist and should be 'Unknown':
#     def categorize_single_price(p):
#         if pd.isna(p): return "Unknown"
#         if p < 50: return "Budget"
#         if p < 200: return "Mid-Range"
#         return "Premium"
#     return prices.apply(categorize_single_price)


# Apply the Pandas UDF
# products_with_category_pandas_df = products_df.withColumn(
#     "price_label_pandas", categorize_price_pandas_udf(col("price"))
# )
# products_with_category_pandas_df.show()
# # +--------+-------+--------------------+
# # |    name|  price|price_label_pandas|
# # +--------+-------+--------------------+
# # |  Laptop| 1200.0|             Premium|
# # |   Mouse|   25.0|              Budget|
# # |Keyboard|   75.0|           Mid-Range|
# # |    null|  150.0|           Mid-Range|
# # | Monitor|   null|             Unknown|
# # +--------+-------+--------------------+

# spark.stop()
```

## When to Use UDFs
-   When the required logic cannot be expressed using built-in Spark SQL functions.
-   When you need to integrate existing Python code or libraries that operate on Pandas Series/DataFrames (for Pandas UDFs).

## Best Practices for UDFs
1.  **Prefer Built-in Functions:** Always try to use built-in Spark SQL functions first, as they are highly optimized and operate directly on Spark's internal data representation within the JVM, avoiding Python overhead.
2.  **Use Pandas UDFs over Regular Python UDFs:** If a UDF is necessary, prefer Pandas UDFs for performance due to vectorized execution and efficient Arrow data transfer.
3.  **Minimize Data Transfer:** Be mindful of the data being passed to and from UDFs.
4.  **Specify Return Types:** Always define the return type for your UDFs. This helps Spark optimize and catch errors.
5.  **Handle Nulls:** Ensure your Python function correctly handles `None` or `NaN` values if they can occur in your input columns, as Spark SQL has its own null semantics.

UDFs provide extensibility but should be used judiciously, with a preference for built-in functions or Pandas UDFs when custom Python logic is unavoidable.

---