---
tags:
  - spark
  - sql
  - dataframe
  - join
  - optimization
  - performance
  - shuffle
  - broadcast_join
  - sort_merge_join
  - concept
aliases:
  - Spark Join Optimization
  - Spark Join Types
  - Broadcast Hash Join
  - Shuffle Hash Join
  - Sort Merge Join
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[PySpark_DataFrame_Operations]]"
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_explain_Plan|Understanding Query Plans (explain())]]"
  - "[[Spark_Performance_Tuning]]"
  - "[[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]"
worksheet:
  - WS_Spark_1
date_created: 2025-08-20
---
# Spark Join Strategies

When joining two [[Spark_DataFrame_SQL|DataFrames]] in Apache Spark, the Catalyst optimizer chooses a **join strategy** to execute the join operation efficiently. The choice of strategy significantly impacts performance, especially for large datasets, as some strategies involve more data movement ([[Spark_Shuffle_Operations|shuffling]]) than others.

Understanding these strategies helps in writing more performant Spark SQL queries and DataFrame operations, and in interpreting [[Spark_explain_Plan|query execution plans]].

## Common Join Strategies

[list2tab|#Join Strategies]
- Broadcast Hash Join (BHJ)
    -   **When Used:** Typically when one DataFrame is significantly smaller than the other (below a configurable threshold `spark.sql.autoBroadcastJoinThreshold`, default 10MB).
    -   **How it Works:**
        1.  The smaller DataFrame is **broadcasted** (sent in its entirety) to every executor node in the cluster.
        2.  Each executor builds an in-memory hash table from the broadcasted (smaller) DataFrame based on the join keys.
        3.  The larger DataFrame is streamed partition by partition. For each row in a partition of the larger DataFrame, it probes the hash table (built from the smaller DataFrame) using its join key to find matches.
    -   **Pros:**
        -   **Avoids Shuffle:** Completely avoids shuffling the larger DataFrame, which is a major performance win.
        -   Very fast if the smaller table fits comfortably in memory on each executor.
    -   **Cons:**
        -   Only suitable if one table is small enough to be broadcasted and fit in executor memory. Broadcasting very large tables can cause OutOfMemoryErrors on executors or driver.
        -   Requires an equijoin (join condition based on equality).
    -   **Hinting:** You can explicitly suggest a broadcast join using `broadcast(df_small)`:
        ```python
        # from pyspark.sql.functions import broadcast
        # joined_df = df_large.join(broadcast(df_small), "join_key_column")
        ```
- Shuffle Hash Join
    -   **When Used:** When tables are moderately sized, not small enough for broadcast, and an equijoin is performed. Often preferred if one side of the join is significantly smaller than the other (but still too large to broadcast) and can be built into a hash table on the reduce side.
    -   **How it Works:**
        1.  **Shuffle Phase:** Both DataFrames are shuffled (repartitioned) across the cluster based on their join keys, ensuring that rows with the same join key from both DataFrames end up on the same executor/partition.
        2.  **Build Phase (on Reducers):** On each reducer partition, a hash table is built from the (typically smaller) of the two shuffled DataFrames for that partition.
        3.  **Probe Phase (on Reducers):** The other (typically larger) shuffled DataFrame for that partition is streamed, and its rows probe the hash table to find matches.
    -   **Pros:**
        -   Can be more efficient than Sort Merge Join if one side (after shuffle) is small enough to build a hash table quickly.
        -   Good for equijoins.
    -   **Cons:**
        -   Involves a shuffle of both tables (or at least the parts needed for the join).
        -   Can be memory-intensive on reducers if the hash tables become very large.
        -   Sensitive to data skew in join keys (some reducers might get disproportionately large amounts of data).
- Sort Merge Join (SMJ)
    -   **When Used:** Often the default for large tables when broadcast join is not feasible, or when join keys are not equijoins (though primarily optimized for equijoins). Also used if data is already sorted on join keys.
    -   **How it Works:**
        1.  **Shuffle Phase (if not already sorted/partitioned correctly):** Both DataFrames are shuffled (repartitioned) based on their join keys.
        2.  **Sort Phase (within each partition):** Data within each partition (on the reducer side) is sorted by the join keys for both DataFrames.
        3.  **Merge Phase:** The sorted partitions from both DataFrames are merged together. Since they are sorted, matching rows can be found by iterating through both datasets simultaneously in a merge-like fashion.
    -   **Pros:**
        -   Robust and can handle large datasets.
        -   Less sensitive to data skew than Shuffle Hash Join in some cases because sorting helps distribute load (though severe skew is still an issue).
        -   Can handle non-equijoins more naturally, though still most efficient for equijoins.
    -   **Cons:**
        -   Involves shuffling (if not pre-partitioned/sorted).
        -   Sorting can be expensive.
- Cartesian Product (Cross Join)
    -   **When Used:** When an explicit `CROSS JOIN` is specified or if a join condition is missing or cannot be optimized into another type.
    -   **How it Works:** Produces every possible combination of rows from the two DataFrames.
    -   **Pros:** None in terms of performance for typical analytical joins.
    -   **Cons:**
        -   **Extremely Expensive:** The size of the result is (num_rows_df1 * num_rows_df2). This can lead to massive data generation and usually indicates a logical error in the join condition or an intentional but resource-intensive operation.
        -   Spark will often try to prevent or warn about accidental cross joins if `spark.sql.crossJoin.enabled` is false (default).
- Broadcast Nested Loop Join
    -   **When Used:** For non-equijoins or complex join conditions when one table is small enough to broadcast.
    -   **How it Works:** The smaller table is broadcasted. Then, for each row in the larger table, it iterates through all rows of the broadcasted smaller table to evaluate the join condition.
    -   **Pros:** Can handle arbitrary join conditions when one table is small.
    -   **Cons:** Can be very slow if the broadcasted table is not very small, as it involves a nested loop comparison ($O(N \cdot M)$ complexity per partition).

## Spark's Choice of Join Strategy
Spark's Catalyst optimizer automatically chooses a join strategy based on:
-   **Table Sizes:** Statistics about table sizes (if available, or estimated).
-   **Join Type:** Inner, left, right, full, cross, etc.
-   **Join Condition:** Equijoin vs. non-equijoin.
-   **Configuration Parameters:**
    -   `spark.sql.autoBroadcastJoinThreshold`: Maximum size (in bytes) of a table that will be broadcasted.
    -   `spark.sql.join.preferSortMergeJoin`: Can be set to `true` to hint Spark to prefer Sort Merge Join (though Catalyst often makes a good choice).
    -   Other cost-based optimization parameters.

## Viewing the Join Strategy
You can use `DataFrame.explain()` to see the physical plan, which will show the join strategy Spark has chosen.
```python
# Conceptual example
# large_df.join(small_df, "id").explain()
# Look for terms like "BroadcastHashJoin", "SortMergeJoin", "ShuffledHashJoin" in the physical plan.
```

Understanding and sometimes influencing join strategies (e.g., by ensuring accurate table statistics, using broadcast hints, or repartitioning data) is a key part of [[Spark_Performance_Tuning|Spark performance tuning]].

---

# same?

park Join Strategies

When joining two [[Spark_DataFrame_SQL|DataFrames]] in Apache Spark, the Catalyst optimizer automatically chooses a **join strategy** to execute the operation efficiently. The selected strategy significantly impacts performance, especially for large datasets, by influencing data movement ([[Spark_Shuffle_Operations|shuffling]]) and computational load.

Understanding these strategies helps in writing performant Spark SQL queries and DataFrame operations, and in interpreting [[Spark_explain_Plan|query execution plans]].

## Common Join Strategies in Spark

[list2tab|#Join Strategies Overview]
- Broadcast Hash Join (BHJ)
    -   **Also Known As:** Map-side Join (though technically the "map" side is the broadcast and hash table build, probe is on the other side).
    -   **When Used:** When one DataFrame is significantly smaller than the other and can fit comfortably in the memory of each executor. The size threshold is controlled by `spark.sql.autoBroadcastJoinThreshold` (default typically 10MB).
    -   **How it Works:**
        1.  **Broadcast:** The smaller DataFrame is collected to the driver and then broadcasted (sent in its entirety) to every executor node in the cluster.
        2.  **Hash Table Build:** Each executor builds an in-memory hash table from the broadcasted (smaller) DataFrame based on the join keys.
        3.  **Probe:** The larger DataFrame (which is not moved) is processed partition by partition. For each row in a partition of the larger DataFrame, its join key is used to probe the hash table (built from the smaller DataFrame) to find matches.
    -   **Pros:**
        -   **Avoids Shuffle of Larger Table:** Completely avoids shuffling the larger DataFrame, which is a major performance advantage. Only the small table is moved.
        -   Very fast if the broadcasted table is indeed small.
    -   **Cons:**
        -   Only suitable if one table is small enough. Broadcasting very large tables can cause OutOfMemoryErrors on the driver (during collect) or executors.
        -   Requires an equijoin (join condition based on equality of keys).
    -   **Hinting:** You can explicitly suggest a broadcast join using `broadcast()` function:
        ```python
        from pyspark.sql.functions import broadcast
        # joined_df = df_large.join(broadcast(df_small), "join_key_column")
        ```
- Shuffle Hash Join (SHJ)
    -   **When Used:** For equijoins when tables are moderately sized, neither is small enough for a broadcast, but one side (after shuffling) is small enough to build a hash table on each partition. Spark might choose this if it estimates building hash tables is feasible.
    -   **How it Works:**
        1.  **Shuffle Phase:** Both DataFrames are shuffled (repartitioned) across the cluster based on their join keys. Rows with the same join key from both DataFrames are guaranteed to land on the same executor/partition.
        2.  **Build Phase (on Reducers/Executors):** On each partition, a hash table is built from one of the DataFrames (typically the smaller one for that partition after shuffling).
        3.  **Probe Phase (on Reducers/Executors):** The other DataFrame's partition is streamed, and its rows probe the hash table to find matches.
    -   **Pros:**
        -   Can be more efficient than Sort Merge Join if the hash table build is fast and fits in memory.
        -   Good for equijoins.
    -   **Cons:**
        -   Involves a shuffle of both tables (or the parts being joined).
        -   Memory-intensive on executors if the hash tables become large.
        -   Sensitive to data skew in join keys, which can lead to some executors having very large hash tables to build/probe.
- Sort Merge Join (SMJ)
    -   **When Used:** Often the default for joining large tables when a broadcast join is not feasible. It's robust and can handle large data sizes. Also used if data is already sorted or partitioned on the join keys.
    -   **How it Works:**
        1.  **Shuffle Phase (if not already co-partitioned and sorted):** Both DataFrames are shuffled (repartitioned) based on their join keys so that rows with the same join keys are on the same partition.
        2.  **Sort Phase (within each partition):** Data within each partition is sorted by the join keys for both DataFrames.
        3.  **Merge Phase:** The sorted partitions from both DataFrames are "merged" together. Since they are sorted by the join key, matching rows can be found by iterating through both datasets simultaneously in a manner similar to the merge step of a merge sort algorithm.
    -   **Pros:**
        -   Robust and can handle very large datasets as it doesn't require holding large hash tables in memory (it streams and sorts).
        -   Less sensitive to data skew in terms of memory blowup compared to Shuffle Hash Join, though severe skew can still lead to long-running tasks.
        -   Can handle non-equijoins if the condition allows for sorting and merging (though primarily optimized for equijoins).
    -   **Cons:**
        -   Involves shuffling (if data is not already appropriately partitioned and sorted).
        -   The sorting step itself can be computationally expensive.
- Cartesian Product (Cross Join) / Broadcast Nested Loop Join (BNLJ)
    -   **Cartesian Product (`CROSS JOIN`):**
        -   **When Used:** When an explicit `CROSS JOIN` is specified, or if no join condition is provided, or if the join condition cannot be optimized by Spark into a more efficient join.
        -   **How it Works:** Produces every possible combination of rows from the two DataFrames. The size of the result is $N \times M$.
        -   **Cons:** Extremely expensive and usually indicates an error or a very specific (and often problematic) requirement. Spark often requires `spark.sql.crossJoin.enabled=true` to allow it.
    -   **Broadcast Nested Loop Join (BNLJ):**
        -   **When Used:** For non-equijoins or complex join conditions where one DataFrame is small enough to be broadcast. If no specific optimization for the join condition is available, Spark might fall back to this if one side is broadcastable.
        -   **How it Works:** The smaller DataFrame is broadcasted to all executors. Then, for each partition of the larger DataFrame, Spark iterates through its rows, and for each row, it iterates through all rows of the (broadcasted) smaller DataFrame to evaluate the join condition.
        -   **Pros:** Can handle arbitrary join conditions when one table is small.
        -   **Cons:** Very high computational complexity ($O(N \cdot M)$ per partition of the larger table) if the broadcasted table is not extremely small.

## Spark's Choice and Influencing Factors
Spark's Catalyst optimizer automatically chooses a join strategy. Key factors influencing this choice include:
-   **Table Size Statistics:** If available (e.g., from `ANALYZE TABLE`), Spark uses these to estimate costs.
-   **`spark.sql.autoBroadcastJoinThreshold`:** Configures the maximum size (in bytes) of a DataFrame that will be broadcasted.
-   **Join Type:** Inner, left, right, full, cross.
-   **Join Condition:** Equijoin (e.g., `df1.key == df2.key`) vs. non-equijoin (e.g., `df1.key > df2.key`, complex UDFs). Equijoins have more optimization possibilities.
-   **Data Skew:** Highly skewed join keys can degrade the performance of shuffle-based joins.
-   **Availability of Sorted/Partitioned Data:** If input DataFrames are already partitioned and/or sorted on the join keys in a compatible way, Spark might skip some shuffle/sort steps.

## Checking the Join Strategy
Use `DataFrame.explain()` to inspect the physical plan and see which join strategy Spark has chosen. Look for operators like `BroadcastHashJoin`, `ShuffledHashJoin`, `SortMergeJoin`, or `BroadcastNestedLoopJoin`.

```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import broadcast

# spark = SparkSession.builder.appName("JoinStrategyDemo").master("local[*]").getOrCreate()

# df_large = spark.createDataFrame([(i, f"val_large_{i}") for i in range(10000)], ["id", "value_large"])
# df_small = spark.createDataFrame([(i, f"val_small_{i}") for i in range(100)], ["id", "value_small"])

# # Example 1: Likely BroadcastHashJoin due to broadcast hint or small size of df_small
# joined_bhj = df_large.join(broadcast(df_small), "id")
# print("--- Plan for likely BroadcastHashJoin ---")
# joined_bhj.explain()

# # Example 2: Potentially SortMergeJoin or ShuffledHashJoin if df_small were larger
# # and broadcast threshold not met.
# # To force a sort-merge join (for illustration, not always recommended to force)
# # spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
# # spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1") # Disable auto-broadcast

# # df_large2 = spark.createDataFrame([(i, f"val_large2_{i}") for i in range(10000)], ["id", "value_large2"])
# # df_medium = spark.createDataFrame([(i, f"val_medium_{i}") for i in range(5000)], ["id", "value_medium"])
# # joined_smj_shj = df_large2.join(df_medium, "id")
# # print("\n--- Plan for likely SortMergeJoin or ShuffledHashJoin ---")
# # joined_smj_shj.explain()

# spark.stop()
```

Understanding these strategies is crucial for optimizing join performance in Spark, which is often a critical part of data processing pipelines.

---