---
tags:
  - spark
  - pyspark
  - python
  - api
  - big_data
  - distributed_computing
  - concept
aliases:
  - PySpark Introduction
  - Python Spark API
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[PySpark_SparkSession_SparkContext]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark Overview

**PySpark** is the **Python API for Apache Spark**. It allows Python developers to interface with the Spark framework, enabling them to write Spark applications using Python and leverage Spark's powerful distributed processing capabilities for [[Big_Data_Definition_Characteristics|Big Data]].

PySpark combines the simplicity and extensive libraries of Python with the performance and scalability of Apache Spark.

## Key Features of PySpark
-   **Pythonic API:** Provides an intuitive API that feels natural to Python programmers.
-   **Access to Spark Core Functionality:** Allows interaction with core Spark abstractions like [[RDD_Resilient_Distributed_Dataset|RDDs (Resilient Distributed Datasets)]].
-   **[[Spark_DataFrame_SQL|DataFrame API]]:** Offers a higher-level, structured data API similar to Pandas DataFrames but designed for distributed computation. This is the most commonly used API in modern PySpark.
-   **Spark SQL:** Enables running SQL queries on Spark DataFrames.
-   **[[Spark_MLlib|MLlib Integration]]:** Provides access to Spark's distributed machine learning library.
-   **[[Spark_Streaming_Structured_Streaming|Structured Streaming]]:** Supports scalable and fault-tolerant stream processing.
-   **[[Spark_GraphX_GraphFrames|GraphFrames (via a separate package)]]:** While GraphX is Scala/Java-based, GraphFrames provide a DataFrame-based API for graph processing in PySpark.
-   **Interoperability with Python Libraries:** Can easily integrate with other Python libraries like [[_NumPy_MOC|NumPy]], [[_Pandas_MOC|Pandas]], and [[160_Python_Libraries/Scikit_learn/_Scikit_learn_MOC|Scikit-learn]]. (e.g., converting Spark DataFrames to/from Pandas DataFrames, using Pandas UDFs).

## How PySpark Works
-   **Driver Program:** Your PySpark application runs in a Python interpreter (the driver program).
-   **[[PySpark_SparkSession_SparkContext|`SparkSession` / `SparkContext`]]:** The entry point to Spark functionality. The driver uses these objects to communicate with the cluster manager and coordinate execution.
-   **Py4J:** Internally, PySpark uses the Py4J library. This library allows Python programs running in the driver to call Java objects residing in the Spark JVM (Java Virtual Machine) on the driver and executors. Spark's core engine is written in Scala and runs on the JVM.
    -   When you call a PySpark RDD or DataFrame transformation, PySpark translates this into operations on Java RDD/DataFrame objects within the Spark JVMs.
-   **Data Serialization:** Data that needs to be transferred between Python processes (driver or Python UDFs on executors) and Spark JVMs is serialized (e.g., using Pickle by default for RDDs of Python objects, or more efficient internal formats for DataFrames).

## Main PySpark Components/APIs to Use

1.  **[[PySpark_SparkSession_SparkContext|`SparkSession`]]:**
    -   The main entry point for DataFrame and SQL functionality.
    -   Used to create DataFrames, register DataFrames as tables, execute SQL over tables, cache tables, and read Parquet/JSON/CSV files.
    -   An instance of `SparkSession` is typically created as `spark`.
    -   It internally creates a `SparkContext` (`spark.sparkContext`).

2.  **[[PySpark_SparkSession_SparkContext|`SparkContext` (`sc`)]]:**
    -   The main entry point for Spark RDD functionality.
    -   Used to create RDDs (e.g., `sc.parallelize()`, `sc.textFile()`), create broadcast variables, and accumulators.
    -   While still available, direct RDD usage is less common for structured data tasks compared to the DataFrame API in modern Spark.

3.  **[[Spark_DataFrame_SQL|DataFrames (`pyspark.sql.DataFrame`)]]:**
    -   A distributed collection of data organized into named columns. Conceptually equivalent to a table in a relational database or a Pandas DataFrame.
    -   Provides a rich set of transformations (`select`, `filter`, `groupBy`, `join`, `withColumn`, etc.) and actions (`show`, `count`, `collect`, `write`).
    -   Leverages the Catalyst optimizer for performance.

4.  **[[PySpark_SQL_Functions|SQL Functions (`pyspark.sql.functions`)]]:**
    -   A large collection of built-in functions for working with DataFrame columns (e.g., string manipulation, date/time functions, mathematical operations, aggregations).
    -   Typically imported as `import pyspark.sql.functions as F`.

5.  **[[PySpark_Window_Functions|Window Functions (`pyspark.sql.Window`)]]:**
    -   For performing calculations across a set of table rows that are somehow related to the current row (e.g., ranking, moving averages within partitions).

## Basic PySpark Application Structure (Conceptual)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count # Example functions

# 1. Create a SparkSession (entry point)
spark = SparkSession.builder \
    .appName("MyPySparkApp") \
    .master("local[*]") \  # Run locally using all available cores; for a cluster, use YARN, Mesos, etc.
    .getOrCreate()

# Access SparkContext if needed for RDDs
sc = spark.sparkContext

# 2. Load Data (e.g., into a DataFrame)
Assuming an e-commerce 'orders.csv' file: order_id, customer_id, product_id, quantity, price
orders_df = spark.read.csv("path/to/orders.csv", header=True, inferSchema=True)

# 3. Perform Transformations
Example: Calculate total revenue per customer
customer_revenue_df = orders_df \
    .withColumn("line_total", col("quantity") * col("price")) \
    .groupBy("customer_id") \
    .agg(
        sum("line_total").alias("total_revenue"),
        count("order_id").alias("num_orders")
    ) \
    .orderBy(col("total_revenue").desc())

# 4. Perform Actions
Show results
customer_revenue_df.show(10)

# Save results
customer_revenue_df.write.parquet("path/to/customer_revenue_output", mode="overwrite")

# 5. Stop the SparkSession
spark.stop()
```

PySpark makes Apache Spark's powerful distributed processing capabilities accessible to Python developers, enabling them to build scalable Big Data applications and analyses.

---