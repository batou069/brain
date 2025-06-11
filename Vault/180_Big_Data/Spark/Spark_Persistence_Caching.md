---
tags:
  - spark
  - rdd
  - dataframe
  - persistence
  - caching
  - memory_management
  - performance
  - optimization
  - concept
aliases:
  - Spark Caching
  - RDD Persistence
  - DataFrame Caching
  - Spark Storage Levels
related:
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
  - "[[Spark_Lazy_vs_Eager_Execution|Spark Lazy vs. Eager Execution]]"
  - "[[Spark_Performance_Tuning]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark: Persistence (Caching)

Apache Spark's [[Spark_Lazy_vs_Eager_Execution|lazy evaluation]] model means that [[RDD_Resilient_Distributed_Dataset|RDDs]] and [[Spark_DataFrame_SQL|DataFrames]] are typically recomputed each time an [[Spark_Transformations_Actions|action]] is called on them (or on a derived RDD/DataFrame). For iterative algorithms or interactive use where a dataset is accessed multiple times, this recomputation can be very inefficient.

Spark provides a mechanism to **persist** or **cache** RDDs and DataFrames in memory across executors, on disk, or a combination. When a persisted RDD/DataFrame is accessed again, Spark will fetch it from the cache instead of recomputing its lineage, significantly speeding up subsequent operations.

## `persist()` and `cache()` Methods
-   **`rdd.persist(storageLevel)` / `dataframe.persist(storageLevel)`:**
    -   Marks the RDD or DataFrame to be persisted with a specified `StorageLevel`.
    -   This operation itself is **lazy**. The actual caching happens the first time an action is computed on this RDD/DataFrame (or one derived from it).
-   **`rdd.cache()` / `dataframe.cache()`:**
    -   A shorthand for `persist(StorageLevel.MEMORY_ONLY)` for RDDs and `persist(StorageLevel.MEMORY_AND_DISK)` for DataFrames by default (though DataFrame `cache()` is also just `MEMORY_AND_DISK`).

## Storage Levels (`pyspark.StorageLevel`)
Spark provides various storage levels to control how RDDs/DataFrames are cached:

[list2mdtable|#Storage Levels]
- Level Name
    - Python Constant
        - Description
- MEMORY_ONLY
    - `StorageLevel.MEMORY_ONLY`
        - Store RDD as deserialized Java objects in the JVM. If the RDD does not fit in memory, some partitions will not be cached and will be recomputed on the fly each time they're needed. (Default for RDD `cache()`)
- MEMORY_ONLY_SER
    - `StorageLevel.MEMORY_ONLY_SER`
        - Store RDD as serialized Java objects (one byte array per partition). Generally more space-efficient than deserialized objects, especially with fast serializers, but more CPU-intensive to read.
- MEMORY_AND_DISK
    - `StorageLevel.MEMORY_AND_DISK`
        - Store RDD as deserialized Java objects. If the RDD does not fit in memory, store the partitions that don't fit on disk, and read them from there when they're needed. (Default for DataFrame `cache()` and `persist()` without arguments)
- MEMORY_AND_DISK_SER
    - `StorageLevel.MEMORY_AND_DISK_SER`
        - Similar to `MEMORY_ONLY_SER`, but spill partitions that don't fit in memory to disk, rather than recomputing them on the fly each time they're needed.
- DISK_ONLY
    - `StorageLevel.DISK_ONLY`
        - Store the RDD partitions only on disk.
- MEMORY_ONLY_2, MEMORY_AND_DISK_2, etc.
    - `StorageLevel.MEMORY_ONLY_2`, etc.
        - Same as levels above, but replicate each partition on two cluster nodes for fault tolerance (if a node holding a cached partition fails, the data is not lost from cache).
- OFF_HEAP
    - `StorageLevel.OFF_HEAP`
        - Stores RDD data in off-heap memory (e.g., using Alluxio or Ignite). This requires off-heap memory to be enabled and configured. Reduces garbage collection overhead.

**Choosing a Storage Level:**
-   **Default (`MEMORY_ONLY` for RDDs, `MEMORY_AND_DISK` for DataFrames):** Often a good starting point.
-   **`_SER` versions:** Use if memory is tight and CPU cost of deserialization is acceptable. Can reduce memory footprint significantly. Kryo serialization (`spark.serializer`) helps here.
-   **`_DISK` versions:** Use if recomputing partitions is very expensive and they don't fit in memory. Disk access is slower than memory.
-   **Replicated versions (`_2`):** Increase fault tolerance for cached data but use twice the storage. Useful for critical, expensive-to-compute RDDs/DataFrames.
-   **DataFrames/Datasets with `cache()` or `persist()`:** Benefit from Tungsten's columnar Caching, which stores data in a more memory-efficient columnar format off-heap or on-heap, often more efficient than RDD caching.

## Example
```python
# from pyspark.sql import SparkSession
# from pyspark.storagelevel import StorageLevel

# spark = SparkSession.builder.appName("PersistenceDemo").getOrCreate()
# sc = spark.sparkContext

# Create an RDD or DataFrame from an expensive operation
# base_rdd = sc.textFile("path/to/large_log_file.txt") # Reading from disk
# processed_rdd = base_rdd.map(lambda line: line.split(",")) \
#                         .filter(lambda parts: len(parts) > 5) \
#                         .map(lambda parts: (parts, int(parts))) # Some transformations

# Persist the processed RDD in memory (deserialized)
# processed_rdd.persist(StorageLevel.MEMORY_ONLY)
# Or simply: processed_rdd.cache()

# First action triggers computation and caching
# count_of_records = processed_rdd.count()
# print(f"Number of processed records: {count_of_records}")

# Subsequent actions will use the cached RDD
# sum_of_values = processed_rdd.map(lambda x: x).sum()
# print(f"Sum of values: {sum_of_values}")

# top_records = processed_rdd.take(5)
# print(f"Top 5 records: {top_records}")

# Unpersist when no longer needed (optional, Spark evicts based on LRU if memory is full)
# processed_rdd.unpersist()

# spark.stop()
```

## When to Persist/Cache
-   When an RDD or DataFrame is used **multiple times** in your application (e.g., in iterative algorithms like K-Means or PageRank, or in interactive analysis).
-   After a particularly **expensive sequence of transformations** whose result will be reused.
-   To speed up access to frequently queried datasets.

## Important Considerations
-   **Lazy Operation:** `persist()` and `cache()` are themselves transformations and are lazy. The data is actually cached only when an action is first computed on the RDD/DataFrame.
-   **Memory Management:** Caching too much data can lead to memory pressure, causing Java OutOfMemoryErrors or excessive garbage collection, potentially slowing down the application. Monitor Spark UI for storage memory usage.
-   **Eviction Policy:** If there isn't enough memory to store all partitions of an RDD/DataFrame marked for caching, Spark will evict partitions based on a Least Recently Used (LRU) policy by default. These evicted partitions will be recomputed if needed, unless a storage level with disk spill is used.
-   **`unpersist()`:** It's good practice to explicitly unpersist an RDD/DataFrame using `rdd.unpersist()` or `df.unpersist()` when it's no longer needed, to free up memory.
-   **Lineage:** Even if a cached partition is lost (e.g., executor failure and no replication), Spark can recompute it using its lineage.

Caching is a key optimization technique in Spark for improving the performance of applications that reuse datasets.

---