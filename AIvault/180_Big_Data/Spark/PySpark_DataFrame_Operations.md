---
tags:
  - spark
  - pyspark
  - dataframe
  - sql
  - transformations
  - actions
  - withcolumn
  - select
  - filter
  - groupby
  - concept
  - example
aliases:
  - PySpark DataFrame API
  - Spark SQL DataFrames
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[PySpark_SparkSession_SparkContext]]"
  - "[[Spark_Transformations_Actions]]"
  - "[[PySpark_SQL_Functions]]"
  - "[[PySpark_Window_Functions]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: DataFrame Operations

The [[Spark_DataFrame_SQL|DataFrame API]] in PySpark provides a higher-level, structured way to work with distributed data. DataFrames are conceptually similar to tables in a relational database or Pandas DataFrames, but they are distributed and leverage Spark's Catalyst optimizer and Tungsten execution engine for performance.

Operations on DataFrames are also categorized into [[Spark_Transformations_Actions|transformations (lazy)]] and [[Spark_Transformations_Actions|actions (trigger execution)]].

## Creating DataFrames
DataFrames are typically created using a `SparkSession` (usually named `spark`):
-   From existing RDDs: `spark.createDataFrame(rdd, schema)`
-   From Python lists/Pandas DataFrames: `spark.createDataFrame(data, schema)`
-   From external data sources: `spark.read.format(...).load(path)` (e.g., `spark.read.csv()`, `spark.read.parquet()`, `spark.read.json()`, `spark.read.jdbc()`). See [[PySpark_Data_Sources]].

```python
# from pyspark.sql import SparkSession
# from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# spark = SparkSession.builder.appName("DataFrameOpsDemo").getOrCreate()

# Conceptual e-commerce product data
# product_data = [
#     (1, "Laptop X200", "Electronics", 1200.00, 4.5),
#     (2, "Coffee Maker Pro", "Appliances", 79.99, 4.2),
#     (3, "Python for All", "Books", 29.95, 4.8),
#     (4, "Running Shoes Z", "Apparel", 89.50, 4.0),
#     (5, "Laptop X200", "Electronics", 1150.00, 4.3) # Another instance for aggregation
# ]
# schema = StructType([
#     StructField("product_id", IntegerType(), True),
#     StructField("name", StringType(), True),
#     StructField("category", StringType(), True),
#     StructField("price", DoubleType(), True),
#     StructField("rating", DoubleType(), True)
# ])
# products_df = spark.createDataFrame(product_data, schema=schema)
# products_df.printSchema()
# products_df.show(3, truncate=False)

# spark.stop()
```

## Common DataFrame Transformations (Lazy)

[list2tab|#DataFrame Transformations]
- `select(*cols)`
    -   Selects a set of columns. Can use string names, `col()` objects, or expressions.
    -   **Example (Select product name and price):**
        ```python
        # from pyspark.sql.functions import col
        # selected_df = products_df.select("name", "price")
        # selected_df_alt = products_df.select(col("name"), (col("price") * 0.9).alias("discounted_price"))
        # selected_df_alt.show(2)
        ```
- `filter(condition)` or `where(condition)`
    -   Filters rows based on a given condition (SQL-like string or column expression).
    -   **Example (Filter for electronics products with price > 1000):**
        ```python
        # from pyspark.sql.functions import col
        # filtered_df = products_df.filter((col("category") == "Electronics") & (col("price") > 1000))
        # filtered_df_sql_style = products_df.where("category = 'Electronics' AND price > 1000")
        # filtered_df.show(2)
        ```
- `withColumn(colName, col)`
    -   Adds a new column or replaces an existing column with the same name.
    -   `colName`: String, name of the new/updated column.
    -   `col`: A `Column` expression for the new column's values.
    -   **Example (Add a 'price_eur' column assuming an exchange rate):**
        ```python
        # from pyspark.sql.functions import col, lit
        # exchange_rate = 0.92
        # products_with_eur_df = products_df.withColumn("price_eur", col("price") * lit(exchange_rate))
        # products_with_eur_df.show(2)
        ```
- `drop(*cols)`
    -   Returns a new DataFrame with specified column(s) dropped.
    -   **Example (Drop the 'rating' column):**
        ```python
        # products_no_rating_df = products_df.drop("rating")
        # products_no_rating_df.show(2)
        ```
- `groupBy(*cols)`
    -   Groups the DataFrame using the specified columns, so we can run aggregation on them. Returns a `GroupedData` object.
    -   Followed by aggregation functions like `agg()`, `count()`, `mean()`, `sum()`, `max()`, `min()`.
    -   **Example (Average price and count per category):**
        ```python
        # from pyspark.sql.functions import avg, count, min, max
        # category_summary_df = products_df.groupBy("category").agg(
        #     count("product_id").alias("num_products"),
        #     avg("price").alias("avg_price"),
        #     min("rating").alias("min_rating"),
        #     max("rating").alias("max_rating")
        # )
        # category_summary_df.show()
        ```
- `orderBy(*cols, ascending=True/False or list)` or `sort(*cols, ...)`
    -   Sorts the DataFrame by the specified column(s).
    -   **Example (Sort products by price descending):**
        ```python
        # from pyspark.sql.functions import desc, asc
        # sorted_products_df = products_df.orderBy(desc("price"), asc("name")) # or col("price").desc()
        # sorted_products_df.show(3)
        ```
- `join(otherDF, on=None, how=None)`
    -   Joins with another DataFrame.
    -   `on`: A string for the join column name (if same in both DFs), a list of names, a join expression (Column object), or not specified if using a `USING` clause in SQL.
    -   `how`: Join type string: `'inner'`, `'cross'`, `'outer'`, `'full'`, `'full_outer'`, `'left'`, `'left_outer'`, `'right'`, `'right_outer'`, `'left_semi'`, `'left_anti'`. Default is `'inner'`.
    -   **Example (Join products with a conceptual `inventory_df`):**
        ```python
        # inventory_data = [(1, 100), (2, 50), (3, 0), (6, 200)] # product_id, stock_quantity
        # inventory_schema = StructType([StructField("p_id", IntegerType()), StructField("stock", IntegerType())])
        # inventory_df = spark.createDataFrame(inventory_data, schema=inventory_schema)

        # product_inventory_df = products_df.join(
        #     inventory_df,
        #     products_df["product_id"] == inventory_df["p_id"], # Join condition
        #     "left_outer"
        # ).select(products_df["name"], products_df["price"], inventory_df["stock"])
        # product_inventory_df.show()
        ```- `distinct()`
    -   Returns a new DataFrame with duplicate rows removed.
- `union(otherDF)` / `unionByName(otherDF, allowMissingColumns=False)`
    -   Returns a new DataFrame containing rows from this DataFrame and another DataFrame. `union` requires same number of columns and matching types by position. `unionByName` matches by column name and can fill missing columns with nulls if `allowMissingColumns=True`.
- `withColumnRenamed(existingName, newName)`
    -   Renames an existing column.
- `na.fill(value, subset=None)` / `na.drop(how='any', thresh=None, subset=None)`
    -   Handles missing values (NaN, None, Null). `na.fill` fills them, `na.drop` removes rows with them.

## Common DataFrame Actions (Trigger Execution)

[list2tab|#DataFrame Actions]
- `show(n=20, truncate=True, vertical=False)`
    -   Displays the first $n$ rows of the DataFrame in a tabular format.
    -   `truncate`: If `True` (default), strings longer than 20 characters are truncated. Set to `False` or an int for more.
- `count()`
    -   Returns the total number of rows in the DataFrame.
- `collect()`
    -   Returns all rows of the DataFrame as a list of `Row` objects to the driver program. **Use with extreme caution on large DataFrames.**
- `take(n)`
    -   Returns the first $n$ rows as a list of `Row` objects.
- `first()`
    -   Returns the first row as a `Row` object.
- `describe(*cols)`
    -   Computes basic summary statistics (count, mean, stddev, min, max) for numerical columns (or specified columns).
- `summary(*statistics)`
    -   Computes specified aggregate statistics for numeric and string columns. Can include approx percentiles.
- `write.format(...).save(path)` / `write.saveAsTable(tableName)`
    -   Saves the DataFrame to an external storage system or as a table in the metastore.
    -   Examples: `df.write.parquet("path")`, `df.write.mode("overwrite").csv("path")`, `df.write.saveAsTable("my_table")`.
- `toPandas()`
    -   Converts the Spark DataFrame to a Pandas DataFrame. **Use with extreme caution on large DataFrames as all data is collected to the driver's memory.**

## Using SQL with DataFrames
You can register a DataFrame as a temporary view or table and then query it using Spark SQL.
```python
# (Assuming 'products_df' and 'spark' session exist)
# products_df.createOrReplaceTempView("products_view")

# Query using Spark SQL
# electronics_high_rating_df = spark.sql("""
#     SELECT name, price, rating
#     FROM products_view
#     WHERE category = 'Electronics' AND rating > 4.0
#     ORDER BY price DESC
# """)
# electronics_high_rating_df.show()
```

The DataFrame API provides a rich, expressive, and optimized way to perform distributed data processing in PySpark, often being more performant and easier to use for structured data than raw RDD operations.

---