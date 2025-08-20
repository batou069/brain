---
tags:
  - spark
  - pyspark
  - dataframe
  - rdd
  - repartition
  - coalesce
  - partitioning
  - performance
  - shuffle
  - concept
aliases:
  - Spark Repartition
  - Spark Coalesce
  - Changing Partitions Spark
related:
  - "[[Spark_Performance_Tuning]]"
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_Data_Parallelism]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
worksheet:
  - WS_Spark_1
date_created: 2025-08-20
---
# Spark: `repartition()` vs. `coalesce()`

In Apache Spark, `repartition()` and `coalesce()` are transformations used to change the number of partitions of a [[RDD_Resilient_Distributed_Dataset|RDD]] or [[Spark_DataFrame_SQL|DataFrame]]. While both affect partitioning, they do so in different ways and have different performance implications, primarily concerning [[Spark_Shuffle_Operations|shuffle operations]].

>[!question] What is the importance of `repartition`? (and `coalesce`)

The importance of `repartition()` and `coalesce()` lies in their ability to control the level of [[Spark_Data_Parallelism|parallelism]] and manage data distribution, which are critical for [[Spark_Performance_Tuning|Spark performance tuning]].

-   **Controlling Parallelism:** The number of partitions often dictates the number of tasks Spark can run in parallel for subsequent stages. Adjusting partitions can help fully utilize cluster resources or prevent too many small tasks.
-   **Data Skew Mitigation:** `repartition()` (especially by key) can help redistribute skewed data more evenly.
-   **Optimizing Shuffles:** While `repartition()` itself is a shuffle, it can sometimes be used to set up data in a way that benefits subsequent shuffles (e.g., for joins).
-   **Controlling Output File Numbers:** When writing data to a file system, the number of output files typically corresponds to the number of partitions in the final RDD/DataFrame. `repartition()` or `coalesce()` can be used to control this.
-   **Reducing Overhead of Small Partitions:** `coalesce()` is particularly useful for reducing the number of partitions after filtering operations that might have created many small, inefficient partitions.

## `repartition(numPartitions, *cols)`
-   **Purpose:** Reshuffles the data in the RDD/DataFrame to create exactly `numPartitions`.
-   **Mechanism:** Always triggers a **full shuffle** of the data across the network. Data is redistributed based on a hash of the partitioning columns (if specified) or round-robin if no columns are specified.
-   **Use Cases:**
    1.  **Increasing the number of partitions:** If you have too few partitions and want to increase parallelism for subsequent operations. This is common after filtering data heavily or reading from a source that creates few partitions.
    2.  **Decreasing the number of partitions AND redistributing data:** If you want to reduce partitions and also ensure data is re-hashed and potentially more evenly distributed.
    3.  **Partitioning by specific columns (`df.repartition(N, col("key_col"))` or `rdd.repartitionAndSortWithinPartitions(...)` for RDDs):** This shuffles data such that all rows/elements with the same values in the specified columns end up in the same partition. This can be very beneficial for optimizing subsequent joins or aggregations on those keys.
-   **Performance:** Can be expensive due to the full shuffle. Use judiciously.
-   **Example (DataFrame):**
    ```python
    # from pyspark.sql import SparkSession
    # from pyspark.sql.functions import spark_partition_id

    # spark = SparkSession.builder.appName("RepartitionExample").master("local").getOrCreate()
    # data = [(i, "value_" + str(i % 3)) for i in range(100)]
    # df = spark.createDataFrame(data, ["id", "category"])
    # print(f"Original number of partitions: {df.rdd.getNumPartitions()}") # Might be default parallelism
    # df.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()

    # Repartition into 5 partitions (full shuffle)
    # df_repartitioned = df.repartition(5)
    # print(f"Number of partitions after repartition(5): {df_repartitioned.rdd.getNumPartitions()}")
    # df_repartitioned.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()

    # Repartition by 'category' column into 3 partitions (if possible, based on distinct categories)
    # df_repartitioned_by_cat = df.repartition(3, "category") # Data with same category goes to same partition
    # print(f"Number of partitions after repartition(3, 'category'): {df_repartitioned_by_cat.rdd.getNumPartitions()}")
    # df_repartitioned_by_cat.select("category", "id", spark_partition_id().alias("pid")).orderBy("pid", "category").show(30)

    # spark.stop()
    ```

## `coalesce(numPartitions)`
-   **Purpose:** Reduces the number of partitions in an RDD/DataFrame to `numPartitions`.
-   **Mechanism:** This operation tries to **avoid a full shuffle** when decreasing the number of partitions. It achieves this by merging existing partitions on the same worker nodes. Data from some partitions is moved to reside on fewer nodes.
    -   If you are *drastically* reducing the number of partitions (e.g., from 1000 to 10), or if data is very skewed, `coalesce` might still involve some data movement that resembles a partial shuffle to achieve better balance, but it aims to be less expensive than a full `repartition`.
    -   `coalesce` **cannot** be used to increase the number of partitions (it will have no effect or might error if `numPartitions` is greater than current). For increasing partitions, `repartition` is needed.
-   **Use Cases:**
    1.  **Decreasing the number of partitions efficiently:** This is its primary use case, especially after operations like `filter()` that might result in many small, sparse partitions. Reducing partitions can reduce task scheduling overhead and improve performance of subsequent operations or when writing output (fewer output files).
-   **Performance:** Generally more efficient than `repartition()` when *only decreasing* the number of partitions because it minimizes data movement.
-   **Example (DataFrame):**
    ```python
    # from pyspark.sql import SparkSession
    # from pyspark.sql.functions import spark_partition_id

    # spark = SparkSession.builder.appName("CoalesceExample").master("local").getOrCreate()
    # # Create a DataFrame with more partitions initially, e.g., by repartitioning
    # initial_df = spark.range(1000).repartition(10)
    # print(f"Number of partitions before coalesce: {initial_df.rdd.getNumPartitions()}")
    # initial_df.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()


    # Coalesce into 3 partitions
    # df_coalesced = initial_df.coalesce(3)
    # print(f"Number of partitions after coalesce(3): {df_coalesced.rdd.getNumPartitions()}")
    # df_coalesced.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()
    # Note: The distribution after coalesce might not be perfectly even if it avoids a full shuffle.

    # spark.stop()
    ```

## `repartitionByRange(*cols)` (DataFrame specific)
-   **Purpose:** Repartitions the DataFrame according to the ranges of the specified columns. Rows with column values within the same range will go to the same partition.
-   **Mechanism:** Involves a shuffle and sorting by the partitioning columns. Useful if you want data to be physically ordered by certain columns across partitions.

## Key Differences Summarized

[list2mdtable|#Repartition vs Coalesce]
- Feature
    - `repartition(numPartitions, *cols)`
        - `coalesce(numPartitions)`
- **Primary Use**
    - Increase or decrease partitions; redistribute data (optionally by key).
        - Decrease partitions efficiently.
- **Shuffle**
    - Always performs a full shuffle.
        - Avoids a full shuffle if possible (merges existing partitions). Can involve some data movement for balancing if reducing drastically.
- **Increasing Partitions**
    - Yes.
        - No (use `repartition` for this).
- **Performance Cost**
    - Generally more expensive due to full shuffle.
        - Generally less expensive when decreasing partitions.
- **Data Distribution**
    - Can lead to more even data distribution due to hashing/sorting in shuffle.
        - May result in less even data distribution if it simply merges existing partitions without rebalancing.

**When to Use Which:**
-   Use **`repartition()`**:
    -   When you need to **increase** the number of partitions.
    -   When you need to **decrease** the number of partitions AND ensure data is **re-shuffled and potentially more evenly distributed** (e.g., to mitigate skew before a join, or if partitioning by specific keys).
    -   Before writing data if you need a specific number of output files with potentially more even sizes.
-   Use **`coalesce()`**:
    -   When you need to **decrease** the number of partitions and want to **minimize data movement** (avoid a full shuffle). This is common after filtering operations that create many small partitions.
    -   Typically faster than `repartition()` for reducing partition count.

Choosing the right number of partitions and using `repartition` or `coalesce` appropriately is a common Spark optimization technique. Monitor the Spark UI to observe the number of tasks and stages to help guide these decisions.

---