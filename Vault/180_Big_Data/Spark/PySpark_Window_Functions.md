---
tags:
  - spark
  - pyspark
  - dataframe
  - window_functions
  - analytics
  - sql
  - concept
  - example
aliases:
  - Spark Window Functions
  - PySpark Window Ops
related:
  - "[[PySpark_DataFrame_Operations]]"
  - "[[PySpark_SQL_Functions]]"
  - "[[SQL_Window_Functions]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: Window Functions

Window functions in PySpark (and SQL in general) perform calculations across a set of table rows that are somehow related to the current row. This set of rows is called a **window** or **window frame**. Unlike regular aggregate functions which collapse rows into a single output row per group, window functions return a value for **each row** based on the group of rows in its window.

They are very powerful for tasks like calculating running totals, moving averages, ranking, or comparing a row's value to those in its partition.

## Key Concepts for Window Functions
1.  **Window Specification (`WindowSpec`):** Defines the window of rows over which the function operates. Created using `pyspark.sql.Window`.
    -   **`partitionBy(*cols)`:** Divides the rows of the DataFrame into partitions based on the distinct values of one or more columns. The window function is then applied independently within each partition.
    -   **`orderBy(*cols)`:** Orders the rows within each partition. This is crucial for functions that depend on order (e.g., `rank()`, `lag()`, `lead()`, running totals).
    -   **`rowsBetween(start, end)` / `rangeBetween(start, end)` (Frame Specification):** Defines the boundaries of the window frame relative to the current row within a partition.
        -   `start`, `end` can be:
            -   `Window.unboundedPreceding`, `Window.unboundedFollowing`
            -   `Window.currentRow`
            -   Offsets (e.g., `-1` for one row before, `1` for one row after in `rowsBetween`).
        -   `rowsBetween`: Defines frame based on row offsets.
        -   `rangeBetween`: Defines frame based on value offsets from current row's `orderBy` column (requires exactly one `orderBy` column).

2.  **Window Functions:** The functions that operate on these windows. They can be:
    -   **Ranking Functions:** `rank()`, `dense_rank()`, `percent_rank()`, `ntile(n)`, `row_number()`.
    -   **Analytic Functions:** `lag(col, offset, default)`, `lead(col, offset, default)`, `cume_dist()`.
    -   **Aggregate Functions used as Window Functions:** `sum()`, `avg()`, `min()`, `max()`, `count()` when used with an `OVER` clause (implicitly via `.over(windowSpec)` in PySpark).

## Syntax
In PySpark, you apply a window function to a column expression using the `.over(windowSpec)` method.

```python
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, rank, avg, lag, row_number

# spark = SparkSession.builder.appName("WindowFunctionsDemo").getOrCreate()

# Conceptual e-commerce sales data: product_id, category, sale_date, sale_amount
# sales_data = [
#     ("P101", "Electronics", "2023-01-05", 1200.00), ("P101", "Electronics", "2023-01-15", 1250.00),
#     ("P203", "Books", "2023-01-10", 29.95), ("P203", "Books", "2023-01-20", 35.00),
#     ("P101", "Electronics", "2023-02-01", 1100.00), ("P203", "Books", "2023-02-05", 32.50),
#     ("P305", "Apparel", "2023-01-07", 89.00), ("P305", "Apparel", "2023-02-10", 95.00),
# ]
# sales_df = spark.createDataFrame(sales_data, ["product_id", "category", "sale_date", "sale_amount"])
# sales_df = sales_df.withColumn("sale_date", col("sale_date").cast("date"))

# sales_df.show()
# +----------+-----------+----------+-----------+
# |product_id|   category| sale_date|sale_amount|
# +----------+-----------+----------+-----------+
# |      P101|Electronics|2023-01-05|     1200.0|
# |      P101|Electronics|2023-01-15|     1250.0|
# |      P203|      Books|2023-01-10|      29.95|
# |      P203|      Books|2023-01-20|       35.0|
# |      P101|Electronics|2023-02-01|     1100.0|
# |      P203|      Books|2023-02-05|      32.5|
# |      P305|    Apparel|2023-01-07|       89.0|
# |      P305|    Apparel|2023-02-10|       95.0|
# +----------+-----------+----------+-----------+

# --- Example 1: Rank products by sale_amount within each category ---
# window_spec_category_rank = Window.partitionBy("category").orderBy(col("sale_amount").desc())

# ranked_sales_df = sales_df.withColumn(
#     "rank_in_category",
#     rank().over(window_spec_category_rank)
# )
# print("--- Ranked Sales by Amount within Category ---")
# ranked_sales_df.show(truncate=False)

# --- Example 2: Calculate running total of sale_amount per category over time ---
# window_spec_running_total = Window.partitionBy("category") \
#                                   .orderBy("sale_date") \
#                                   .rowsBetween(Window.unboundedPreceding, Window.currentRow)
# This defines a frame from the start of the partition to the current row

# running_total_df = sales_df.withColumn(
#     "running_total_amount",
#     sum(col("sale_amount")).over(window_spec_running_total)
# )
# print("--- Running Total of Sales Amount within Category ---")
# running_total_df.orderBy("category", "sale_date").show(truncate=False)

# --- Example 3: Get previous sale_amount for each product (lag) ---
# window_spec_product_lag = Window.partitionBy("product_id").orderBy("sale_date")

# lag_df = sales_df.withColumn(
#     "previous_sale_amount",
#     lag("sale_amount", 1).over(window_spec_product_lag) # Offset 1, default value is None/NULL
# )
# print("--- Sales with Previous Sale Amount for Same Product ---")
# lag_df.orderBy("product_id", "sale_date").show(truncate=False)

# --- Example 4: Average sale amount for the category (for comparison with current row) ---
# window_spec_category_avg = Window.partitionBy("category") # No orderBy needed if avg over whole partition

# category_avg_df = sales_df.withColumn(
#     "avg_category_sale_amount",
#     avg(col("sale_amount")).over(window_spec_category_avg)
# )
# print("--- Sales with Average Category Sale Amount ---")
# category_avg_df.show(truncate=False)


# spark.stop()
```

## Common Use Cases
[list2card|addClass(ab-col2)|#Window Function Use Cases]
- **Ranking:**
    -   Top N products per category.
    -   Salesperson rankings within regions.
    -   `rank()`, `dense_rank()`, `row_number()`, `ntile()`.
- **Running Totals / Moving Averages:**
    -   Cumulative sales over time.
    -   30-day moving average of stock prices.
    -   `sum().over(...)`, `avg().over(...)` with appropriate `rowsBetween` or `rangeBetween`.
- **Period-over-Period Comparisons:**
    -   Comparing current month's sales to previous month's sales for the same product.
    -   `lag()`, `lead()`.
- **Calculating Percentages of Total within Group:**
    -   Each product's contribution to its category's total sales.
    -   `sum(col("sales")).over(Window.partitionBy("category"))` can be used as a denominator.
- **Sessionization:**
    -   Grouping user activity into sessions based on time gaps.
- **Filling Missing Time Series Data:**
    -   Using `lag` or `lead` to fill forward or backward within a series.

## Key Considerations
-   **Performance:** Window functions, especially those with large or complex window frames or many partitions, can be computationally intensive. The amount of data shuffled or held in memory per partition matters.
-   **`partitionBy` vs. `groupBy`:**
    -   `groupBy().agg(...)` reduces the number of rows; each group becomes one row in the output.
    -   Window functions with `partitionBy()... .over()` **do not reduce the number of rows**; they compute a value for each input row based on its window.
-   **Frame Specification (`rowsBetween` / `rangeBetween`):**
    -   `rowsBetween` is based on physical offsets from the current row.
    -   `rangeBetween` is based on value differences from the current row's `orderBy` column value. This requires the `orderBy` column to be numeric or date/timestamp and have a meaningful range. It can lead to a variable number of rows in the frame.
-   **Ordering (`orderBy`):** Crucial for ranking, `lag`/`lead`, and running calculations. If omitted for aggregate functions, the aggregate is computed over the entire partition.

Window functions are a very expressive feature of Spark SQL and the DataFrame API, enabling complex analytical queries that would be much harder to write using other transformations alone.

---