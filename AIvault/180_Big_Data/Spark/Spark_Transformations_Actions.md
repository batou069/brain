---
tags:
  - spark
  - rdd
  - dataframe
  - transformations
  - actions
  - lazy_evaluation
  - execution_model
  - concept
aliases:
  - Spark Transformations
  - Spark Actions
  - RDD Operations
  - DataFrame Operations Spark
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
  - "[[Spark_Lazy_vs_Eager_Execution|Spark Lazy vs. Eager Execution]]"
  - "[[Spark_DAG_Scheduler|Spark DAG Scheduler]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark: Transformations and Actions

Apache Spark operations on its core data structures ([[RDD_Resilient_Distributed_Dataset|RDDs]] and [[Spark_DataFrame_SQL|DataFrames]]/Datasets) can be divided into two main types: **transformations** and **actions**. Understanding this distinction is crucial for comprehending Spark's execution model, particularly its [[Spark_Lazy_vs_Eager_Execution|lazy evaluation]] strategy.

## Transformations
**Transformations** are operations on RDDs or DataFrames that create a **new** RDD or DataFrame.
-   **[[Spark_Lazy_vs_Eager_Execution|Lazy Evaluation]]:** Transformations are *lazy*, meaning Spark does not execute them immediately. Instead, it builds up a lineage graph (a [[Spark_DAG_Scheduler|Directed Acyclic Graph - DAG]]) of these operations. The actual computation is deferred until an action is called.
-   **Return Type:** They return a new RDD or DataFrame representing the transformed dataset. The original RDD/DataFrame remains unchanged due to immutability.
-   **Purpose:** To define the sequence of computations to be performed on the data.

**Types of Transformations:**

1.  **Narrow Transformations:**
    -   Each partition of the parent RDD/DataFrame is used by at most one partition of the child RDD/DataFrame.
    -   Data from different partitions does not need to be shuffled across the network.
    -   Can often be pipelined together within a single stage by Spark.
    -   **Examples (RDD API):** `map()`, `flatMap()`, `filter()`, `sample()`, `union()`.
    -   **Examples (DataFrame API):** `select()`, `withColumn()`, `filter()` (where clause), `drop()`, `union()`.

2.  **Wide Transformations (Shuffle Transformations):**
    -   Data from multiple input partitions may be needed to compute a single output partition.
    -   These operations require a **[[Spark_Shuffle_Operations|shuffle]]**, which involves redistributing data across executors over the network. Shuffles are computationally expensive.
    -   Wide transformations mark stage boundaries in the Spark execution DAG.
    -   **Examples (RDD API):** `groupByKey()`, `reduceByKey()`, `sortByKey()`, `join()`, `distinct()`, `repartition()`, `coalesce()` (if increasing partitions or shuffling).
    -   **Examples (DataFrame API):** `groupBy().agg()`, `orderBy()`, `join()`, `distinct()`, `repartition()`, `coalesce()` (if shuffling).

## Actions
**Actions** are operations on RDDs or DataFrames that **trigger the execution** of all previously defined (lazy) transformations to compute a result.
-   **Eager Evaluation (Trigger):** When an action is called, Spark evaluates the DAG of transformations.
-   **Return Type:** Actions either:
    -   Return a non-RDD/non-DataFrame value to the driver program (e.g., a number, a list of data).
    -   Write data to an external storage system (e.g., HDFS, local file system).
-   **Purpose:** To get results from the computation or to materialize data.

**Common Actions:**

-   **Examples (RDD API):**
    -   `count()`: Returns the number of elements in the RDD.
    -   `collect()`: Returns all elements of the RDD as an array to the driver program. **Use with caution on large RDDs as it can cause driver OutOfMemoryErrors.**
    -   `take(n)`: Returns the first $n$ elements of the RDD.
    -   `first()`: Returns the first element of the RDD (equivalent to `take(1)[0]`).
    -   `reduce(func)`: Aggregates the elements of the RDD using a specified commutative and associative binary operator.
    -   `foreach(func)`: Applies a function to each element of the RDD (usually for side effects like writing to a database).
    -   `saveAsTextFile(path)`: Saves the RDD content as text files in a directory.
    -   `takeOrdered(n, [ordering])`: Returns the first $n$ elements as ordered by their natural order or a custom comparator.
-   **Examples (DataFrame API):**
    -   `count()`: Returns the number of rows.
    -   `collect()`: Returns all rows as a list of `Row` objects to the driver. **Same caution as RDD `collect()` applies.**
    -   `show(n, truncate)`: Displays the first $n$ rows in a tabular format (primarily for interactive use).
    -   `take(n)`: Returns the first $n$ rows as a list of `Row` objects.
    -   `first()`: Returns the first `Row`.
    -   `write.format(...).save(path)` (e.g., `write.parquet(path)`, `write.csv(path)`): Saves the DataFrame to an external storage system.
    -   `toPandas()`: Converts the Spark DataFrame to a Pandas DataFrame. **Use with extreme caution on large DataFrames as it collects all data to the driver's memory.**

>[!question]- What is the difference between a transformation and an action?
>The key differences are:
>
> | Feature | Transformation | Action |
> |---------|----------------|--------|
> | **Execution** | Lazy (does not compute immediately) | Eager (triggers computation of the DAG) |
> | **Return Value** | Returns a new RDD/DataFrame | Returns a non-RDD/non-DataFrame value to the driver OR writes to external storage (no RDD/DataFrame returned directly from the action itself for further Spark processing in the same chain) |
> | **Purpose** | Define a sequence of operations to create a new dataset from an existing one. Builds the computation plan (DAG). | Execute the planned computations to produce a result or side effect. |
> | **Example RDD methods** | `map`, `filter`, `flatMap`, `join`, `groupByKey` | `count`, `collect`, `take`, `saveAsTextFile`, `reduce` |
> | **Example DataFrame methods** | `select`, `filter`, `withColumn`, `join`, `groupBy` | `count`, `collect`, `show`, `take`, `write.save` |
>
>Understanding this distinction is fundamental to writing efficient and correct Spark applications. You build up a plan of transformations and then execute it with an action.

---