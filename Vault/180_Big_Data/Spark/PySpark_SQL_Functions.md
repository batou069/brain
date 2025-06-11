---
tags:
  - spark
  - pyspark
  - dataframe
  - sql_functions
  - column_operations
  - data_manipulation
  - concept
  - example
aliases:
  - pyspark.sql.functions
  - Spark SQL Built-in Functions
  - F module PySpark
related:
  - "[[PySpark_DataFrame_Operations]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: `pyspark.sql.functions`

The `pyspark.sql.functions` module in PySpark provides a rich collection of built-in functions for manipulating [[Spark_DataFrame_SQL|DataFrame]] columns. These functions operate on `Column` objects and are essential for performing data transformations, aggregations, and feature engineering within the DataFrame API.

It is common practice to import this module with an alias, typically `F`:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, avg, count, upper, lower, trim, to_date, year, month, dayofmonth, expr, array, struct, explode, collect_list, concat_ws
# import pyspark.sql.functions as F # Alternative common import
```

## Categories of Functions
The functions can be broadly categorized:

[list2tab|#SQL Function Categories]
- String Functions
    -   Manipulating string columns.
    -   Examples: `upper()`, `lower()`, `trim()`, `ltrim()`, `rtrim()`, `concat()`, `concat_ws()`, `substring()`, `length()`, `regexp_replace()`, `split()`, `initcap()`.
    -   **Usage Example (Cleaning product names):**
        ```python
        # spark = SparkSession.builder.appName("StringFuncDemo").getOrCreate()
        # data = [("  Laptop X200  ",), (" coffee maker pro ",), ("python for all",)]
        # df = spark.createDataFrame(data, ["raw_name"])
        # cleaned_df = df.withColumn("name_trimmed", trim(col("raw_name"))) \
        #                .withColumn("name_upper", upper(col("name_trimmed"))) \
        #                .withColumn("name_title", initcap(col("name_trimmed")))
        # cleaned_df.show(truncate=False)
        # spark.stop()
        ```
- Date and Timestamp Functions
    -   Working with date and time data.
    -   Examples: `to_date()`, `to_timestamp()`, `current_date()`, `current_timestamp()`, `year()`, `month()`, `dayofmonth()`, `hour()`, `minute()`, `second()`, `date_format()`, `datediff()`, `add_months()`, `date_add()`, `date_sub()`.
    -   **Usage Example (Extracting year from order date):**
        ```python
        # spark = SparkSession.builder.appName("DateFuncDemo").getOrCreate()
        # data = [("2023-01-15",), ("2022-11-20",), ("2023-05-05",)]
        # df = spark.createDataFrame(data, ["order_date_str"])
        # date_df = df.withColumn("order_date", to_date(col("order_date_str"), "yyyy-MM-dd")) \
        #             .withColumn("order_year", year(col("order_date"))) \
        #             .withColumn("days_since_order", datediff(current_date(), col("order_date")))
        # date_df.show()
        # spark.stop()
        ```
- Mathematical Functions
    -   Performing numerical calculations.
    -   Examples: `abs()`, `round()`, `ceil()`, `floor()`, `sqrt()`, `exp()`, `log()`, `log10()`, `pow()`, `sin()`, `cos()`, `rand()`, `randn()`.
    -   **Usage Example (Calculating discounted price):**
        ```python
        # spark = SparkSession.builder.appName("MathFuncDemo").getOrCreate()
        # data = [(100.00, 0.1), (75.50, 0.05), (199.99, 0.15)]
        # df = spark.createDataFrame(data, ["price", "discount_rate"])
        # math_df = df.withColumn("discount_amount", round(col("price") * col("discount_rate"), 2)) \
        #              .withColumn("final_price", col("price") - col("discount_amount"))
        # math_df.show()
        # spark.stop()
        ```
- Aggregate Functions
    -   Used with `groupBy()` or `agg()` to compute summary statistics.
    -   Examples: `count()`, `countDistinct()`, `sum()`, `avg()` (or `mean()`), `min()`, `max()`, `stddev()` (or `stddev_samp()`), `variance()` (or `var_samp()`), `collect_list()`, `collect_set()`, `first()`, `last()`.
    -   **Usage Example (See [[PySpark_DataFrame_Operations|DataFrame Operations]] `groupBy` example).**
- Collection Functions (Array and Map)
    -   Operating on array or map type columns.
    -   Examples: `array()` (create array), `array_contains()`, `size()` (of array/map), `explode()` (array/map to rows), `element_at()`, `map_keys()`, `map_values()`, `struct()` (create struct).
    -   **Usage Example (Exploding product tags):**
        ```python
        # spark = SparkSession.builder.appName("CollectionFuncDemo").getOrCreate()
        # data = [("Laptop", ["tech", "electronics", "computer"]),
        #         ("Coffee Beans", ["food", "beverage", "coffee"])]
        # df = spark.createDataFrame(data, ["product_name", "tags_array"])
        # exploded_df = df.withColumn("tag", explode(col("tags_array")))
        # exploded_df.show(truncate=False)
        # # Output:
        # # +------------+------------------------------+-----------+
        # # |product_name|tags_array                    |tag        |
        # # +------------+------------------------------+-----------+
        # # |Laptop      |[tech, electronics, computer] |tech       |
        # # |Laptop      |[tech, electronics, computer] |electronics|
        # # |Laptop      |[tech, electronics, computer] |computer   |
        # # |Coffee Beans|[food, beverage, coffee]      |food       |
        # # |Coffee Beans|[food, beverage, coffee]      |beverage   |
        # # |Coffee Beans|[food, beverage, coffee]      |coffee     |
        # # +------------+------------------------------+-----------+
        # spark.stop()
        ```
- Conditional Functions
    -   Applying logic based on conditions.
    -   Examples: `when(condition, valueIfTrue).otherwise(valueIfFalse)`, `expr()` (execute SQL expression string).
    -   **Usage Example (Categorizing product price):**
        ```python
        # spark = SparkSession.builder.appName("ConditionalFuncDemo").getOrCreate()
        # data = [(1200.00,), (79.99,), (29.95,)]
        # df = spark.createDataFrame(data, ["price"])
        # conditional_df = df.withColumn("price_category",
        #     when(col("price") >= 1000, "High")
        #     .when((col("price") >= 100) & (col("price") < 1000), "Medium")
        #     .otherwise("Low")
        # )
        # conditional_df.show()
        # spark.stop()
        ```
- Utility Functions
    -   Various helper functions.
    -   Examples: `lit(literalValue)` (create a literal column), `col(colName)` (return a Column based on name), `isnull()`, `isnotnull()`, `monotonically_increasing_id()`.
    -   >[!question] Why and when are `lit` and `col` useful?
    >    -   **`col(columnName)` or `df[columnName]` or `$"columnName"` (Scala/shortcut):**
    >        -   **Why:** Used to refer to an existing column in a DataFrame to apply transformations or use it in expressions. It returns a `Column` object.
    >        -   **When:** Almost always when you need to perform an operation on a column (e.g., `col("price") * 0.9`, `filter(col("age") > 18)`).
    >    -   **`lit(literalValue)`:**
    >        -   **Why:** Used to create a `Column` object from a literal value (a constant like a number, string, boolean). This is necessary when you want to use a constant value in operations where a `Column` object is expected, such as in `withColumn()`, `select()`, or in conditional expressions with `when()`. Spark needs to treat literals as columns in these contexts to build the expression tree correctly.
    >        -   **When:**
    >            -   Adding a new column with a constant value: `df.withColumn("status", lit("active"))`
    >            -   Comparing a column with a constant: `df.filter(col("age") > lit(18))` (though Spark often infers `lit` here, explicit use is clearer for complex types or to avoid ambiguity).
    >            -   Using constants in `when().otherwise()`: `when(col("stock") > 0, lit("In Stock")).otherwise(lit("Out of Stock"))`
    >            -   Passing constant arguments to UDFs or SQL functions that expect Column types.
    >    Essentially, `col` refers to existing data columns, while `lit` injects constant values into DataFrame operations as if they were columns.
- Window Functions
    -   Used with `Window` specifications to perform calculations across a set of rows related to the current row.
    -   Examples: `rank()`, `dense_rank()`, `row_number()`, `lag()`, `lead()`, aggregate functions used with an `OVER` clause (e.g., `avg("salary").over(windowSpec)`).
    -   See [[PySpark_Window_Functions]].

## Using `expr()`
The `expr(expression_string)` function allows you to use SQL-like expression strings directly within DataFrame transformations. This can be very convenient for complex expressions or when you are more familiar with SQL syntax.

```python
# spark = SparkSession.builder.appName("ExprDemo").getOrCreate()
# data = [("Alice", 70000, "HR"), ("Bob", 85000, "Engineering")]
# df = spark.createDataFrame(data, ["name", "salary", "department"])

# Using expr to create new columns and filter
# expr_df = df.withColumn("bonus", expr("salary * 0.1")) \
#             .withColumn("salary_plus_bonus", expr("salary + bonus")) \
#             .filter(expr("department = 'Engineering' OR salary_plus_bonus > 75000"))
# expr_df.show()
# spark.stop()
```

The `pyspark.sql.functions` module is extremely powerful and provides the building blocks for most data manipulation and feature engineering tasks in PySpark DataFrames. It's highly recommended to explore its documentation for the full list of available functions.

---