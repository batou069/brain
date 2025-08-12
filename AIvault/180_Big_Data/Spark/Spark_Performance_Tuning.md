---
tags:
  - spark
  - performance
  - optimization
  - tuning
  - partitioning
  - caching
  - shuffling
  - serialization
  - concept
aliases:
  - Spark Optimization
  - Tuning Spark Applications
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_Persistence_Caching|Spark Persistence and Caching]]"
  - "[[Spark_Data_Parallelism]]"
  - "[[Spark_explain_Plan|Understanding Query Plans (explain())]]"
  - "[[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]"
  - "[[Parquet_vs_CSV_Spark|Data Formats (Parquet)]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark Performance Tuning

Optimizing Apache Spark applications is crucial for efficiently processing large datasets and meeting performance goals. Tuning involves understanding Spark's architecture, execution model, and various configuration parameters.

## Key Areas for Performance Tuning

[list2tab|#Spark Tuning Areas]
- Data Serialization
    - **Issue:** Spark needs to serialize data when transferring it over the network (e.g., during shuffles) or when caching RDDs/DataFrames. Java's default serialization can be slow and produce large output.
    - **Tuning:**
        -   **Kryo Serialization (`spark.serializer`):** Often significantly faster and more compact than Java serialization. Configure Spark to use Kryo:
            ```python
            # In SparkSession builder
            # .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
            # .config("spark.kryo.registrationRequired", "false") # Or register classes
            ```
        -   **DataFrames/Datasets:** Use the DataFrame/Dataset API as much as possible. They use Spark's internal Tungsten execution engine with efficient Encoders and off-heap memory management, which often bypasses generic serialization issues for common operations.
- [[Spark_Shuffle_Operations|Shuffle Management]]
    - **Issue:** Shuffles are expensive (disk I/O, network I/O, serialization). Minimizing and optimizing shuffles is key.
    - **Tuning:**
        -   **Avoid Unnecessary Shuffles:**
            -   Use `reduceByKey` or `aggregateByKey` instead of `groupByKey().mapValues(...)` as they perform map-side aggregation.
            -   Utilize [[PySpark_Broadcast_Variables_Accumulators|broadcast joins]] for joining a large DataFrame with a small one.
        -   **Number of Shuffle Partitions (`spark.sql.shuffle.partitions`):**
            -   Default is 200. This controls the number of reduce tasks.
            -   Too few: Large partitions, potential memory issues, less parallelism.
            -   Too many: Overhead of managing many small tasks, potentially small files if writing output.
            -   Adjust based on data size, cluster resources, and stage characteristics. Often set to 2-4 times the number of cores in the cluster.
        -   **Reduce Data Before Shuffle:** Filter data as early as possible in the DAG.
        -   **Shuffle File Management:** Configure parameters like `spark.shuffle.file.buffer` (buffer size for writing shuffle files) and `spark.reducer.maxSizeInFlight` (limits size of shuffle blocks fetched by a reducer simultaneously).
- Partitioning
    - **Issue:** The number and nature of partitions affect parallelism and data skew.
    - **Tuning:**
        -   **Initial Partitioning:** When reading data, Spark tries to set a reasonable number of partitions (e.g., based on HDFS block size).
        -   **`repartition(numPartitions)`:** Performs a full shuffle to redistribute data into `numPartitions`. Use to increase parallelism or to partition by specific keys for subsequent joins (`df.repartition(col("key"))` or `df.repartition(N, col("key"))`).
            >[!question] What is the importance of `repartition`?
            >`repartition(numPartitions, *cols)` is important for:
            >1.  **Increasing Parallelism:** If you have too few partitions (e.g., after a filter that drastically reduces data, or reading many small files), `repartition` can increase the number of partitions to better utilize cluster cores.
            >2.  **Distributing Data Evenly / Mitigating Skew:** If data is skewed across existing partitions, `repartition` (without specific columns) will hash partition the data, which can lead to a more even distribution.
            >3.  **Co-locating Data for Joins:** Repartitioning multiple DataFrames by their join keys (`df1.repartition(N, col("join_key1"))`, `df2.repartition(N, col("join_key2"))`) before a join can sometimes improve join performance by ensuring data with the same keys ends up on the same partitions, potentially reducing shuffling during the join itself (though `repartition` itself is a shuffle).
            >4.  **Controlling Output File Count:** When writing data, the number of output files often corresponds to the number of partitions in the final RDD/DataFrame. `repartition` can be used to control this.
            >It's a full shuffle operation, so use it judiciously.
        -   **`coalesce(numPartitions)`:** Reduces the number of partitions. It tries to avoid a full shuffle by merging existing partitions on the same worker if possible. If you drastically reduce partitions, it might still trigger a shuffle internally for better balancing. Use when you have too many small partitions.
        -   **`partitionBy(*cols)` (DataFrameWriter):** When writing data (e.g., to Parquet), this partitions the output data into separate directories based on the distinct values of the specified columns. This is excellent for predicate pushdown when reading the data later.
- [[Spark_Persistence_Caching|Caching and Persistence]]
    - **Issue:** Recomputing RDDs/DataFrames multiple times in iterative algorithms or interactive sessions is inefficient.
    - **Tuning:**
        -   Use `rdd.cache()` (alias for `rdd.persist(StorageLevel.MEMORY_ONLY)`) or `df.cache()` to store the RDD/DataFrame in memory.
        -   Use `rdd.persist(storageLevel)` or `df.persist(storageLevel)` to choose different storage levels (e.g., `MEMORY_ONLY`, `MEMORY_AND_DISK`, `DISK_ONLY`, with options for serialization and replication).
        -   **When to cache:** Cache datasets that will be accessed multiple times, especially after expensive transformations or shuffles.
        -   **Don't over-cache:** Caching too much data can lead to memory pressure and eviction, potentially slowing down the application. Unpersist data when no longer needed (`rdd.unpersist()`).
- [[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]
    - **Issue:** Sending large read-only variables (e.g., lookup tables, machine learning models) to all executors repeatedly with each task can be inefficient.
    - **Tuning:**
        -   Use `SparkContext.broadcast(variable)` to send the variable to each executor only once. Tasks on that executor can then access the broadcasted variable from a local cache.
        -   Ideal for joining a large DataFrame with a small lookup table.
- Data Structures and APIs
    - **RDD vs. DataFrame/Dataset:** Prefer DataFrames/Datasets over RDDs where possible for structured data. The Catalyst optimizer and Tungsten execution engine provide significant performance benefits for DataFrames.
    - **Avoid User-Defined Functions (UDFs) if Possible:** Native Spark SQL functions and DataFrame operations are generally more optimized than Python/Scala UDFs. If UDFs are necessary, consider Pandas UDFs (Vectorized UDFs) for better performance with Python.
- [[Parquet_vs_CSV_Spark|Data Formats]]
    - **Issue:** The format of input/output data impacts read/write performance and storage.
    - **Tuning:**
        -   Use efficient columnar formats like **Apache Parquet** or ORC for analytical workloads. They offer good compression and enable column pruning and predicate pushdown.
        -   Avoid row-based formats like CSV or JSON for large-scale analytics if performance is critical.
- Code Optimization
    - **Filter Early, Project Early:** Reduce the amount of data processed as early as possible in your DAG.
    - **Avoid `collect()` on Large Data:** This brings all data to the driver and can cause OutOfMemoryErrors.
    - **Use Appropriate Join Strategies:** Understand when Spark might use Broadcast Hash Join, Sort Merge Join, etc. Provide hints or structure data if needed. See [[Spark_Join_Strategies]].
- Monitoring and [[Spark_explain_Plan|Understanding Query Plans]]
    - **Spark UI:** An invaluable tool for monitoring running applications, viewing DAGs, stages, tasks, shuffle read/write sizes, task duration, and identifying stragglers or bottlenecks.
    - **`DataFrame.explain()`:** Use this to understand the logical and physical plans Spark generates for your DataFrame operations. Helps identify if optimizations like predicate pushdown are occurring.

Effective Spark tuning often involves an iterative process of identifying bottlenecks using monitoring tools, understanding the execution plan, and then applying appropriate optimizations related to data representation, partitioning, shuffling, caching, and code structure.

---