---
tags:
  - spark
  - rdd
  - distributed_data
  - fault_tolerance
  - immutability
  - lazy_evaluation
  - concept
aliases:
  - Resilient Distributed Dataset
  - Spark RDD
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_Transformations_Actions|Spark Transformations and Actions]]"
  - "[[Spark_Lazy_vs_Eager_Execution|Spark Lazy Execution]]"
  - "[[Spark_Persistence_Caching|Spark Persistence and Caching]]"
  - "[[Spark_Data_Parallelism]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# RDD (Resilient Distributed Dataset)

## Definition
A **Resilient Distributed Dataset (RDD)** is the fundamental data structure and abstraction in Apache Spark before the introduction of [[Spark_DataFrame_SQL|DataFrames and Datasets]]. An RDD represents an **immutable, partitioned collection of elements** that can be operated on in parallel across a cluster of machines.

## Key Characteristics of RDDs

[list2tab|#RDD Characteristics]
- Resilient (Fault-Tolerant)
    -   RDDs track the lineage of transformations used to build them (a [[Spark_DAG_Scheduler|Directed Acyclic Graph - DAG]]).
    -   If a partition of an RDD is lost due.g., a worker node failure), Spark can automatically recompute that partition using the lineage information from the original data source and transformations. This provides fault tolerance without needing to replicate the data itself in the same way HDFS does for its blocks (though RDDs often originate from HDFS data which *is* replicated).
- Distributed
    -   The data in an RDD is partitioned and distributed across multiple nodes in the Spark cluster.
    -   This allows for [[Spark_Data_Parallelism|parallel operations]] on the data.
- Dataset
    -   Represents a collection of data items (e.g., lines of a text file, objects, key-value pairs).
    -   RDDs can hold objects of any Python, Java, or Scala type.
- Immutable (Read-Only)
    -   Once an RDD is created, it cannot be changed. Applying a [[Spark_Transformations_Actions|transformation]] to an RDD creates a *new* RDD.
    -   Immutability simplifies fault tolerance (easier to recompute) and consistency.
- Lazily Evaluated
	[[Spark_Lazy_vs_Eager_Execution|Lazily Evaluated]]
    -   [[Spark_Transformations_Actions|Transformations]] on RDDs (e.g., `map`, `filter`) are not executed immediately. Instead, Spark builds up a DAG of operations.
    -   The computations are only triggered when an [[Spark_Transformations_Actions|action]] (e.g., `count`, `collect`, `saveAsTextFile`) is called.
- Cached
	[[Spark_Persistence_Caching|Optionally Persisted (Cached)]]
    -   Users can explicitly persist (cache) an RDD in memory across executors, on disk, or a combination.
    -   This is very useful for iterative algorithms or interactive queries where the same RDD is accessed multiple times, as it avoids recomputing the RDD from its lineage each time.
- Partitioned
    -   Each RDD is divided into multiple partitions. Each partition is a logical chunk of the data that can be processed by a single task on an executor.
    -   The number of partitions can influence the degree of parallelism.

## Creating RDDs
RDDs can be created in two main ways using the [[PySpark_SparkSession_SparkContext|`SparkContext` (`sc`)]]:
1.  **Parallelizing an existing collection in your driver program:**
    ```python
    # from pyspark.sql import SparkSession
    # spark = SparkSession.builder.appName("RDDCreateDemo").getOrCreate()
    # sc = spark.sparkContext

    data_list = 
    rdd_from_list = sc.parallelize(data_list, numSlices=4) # numSlices suggests number of partitions
    # print(f"Number of partitions: {rdd_from_list.getNumPartitions()}")
    # spark.stop()
    ```
2.  **Referencing a dataset in an external storage system:**
    -   Supported by Hadoop, such as HDFS, HBase, or any data source offering a Hadoop InputFormat.
    -   Local file systems.
    ```python
    # from pyspark.sql import SparkSession
    # spark = SparkSession.builder.appName("RDDFromFileDemo").getOrCreate()
    # sc = spark.sparkContext

    # Assuming 'product_reviews.txt' is in HDFS or accessible path
    # file_path = "hdfs:///user/data/product_reviews.txt" # or "file:///path/to/local/file.txt"
    # try:
    #     rdd_from_file = sc.textFile(file_path, minPartitions=2)
    #     # print(f"First few lines from file RDD: {rdd_from_file.take(3)}")
    # except Exception as e:
    #     print(f"Error creating RDD from file (ensure file exists and Spark is configured): {e}")
    
    # spark.stop()
    ```

## Operations on RDDs
RDDs support two types of operations:
1.  **[[Spark_Transformations_Actions|Transformations]]:** Create a new RDD from an existing one (e.g., `map`, `filter`, `flatMap`, `union`, `groupByKey`, `reduceByKey`, `sortByKey`). Transformations are lazily evaluated.
2.  **[[Spark_Transformations_Actions|Actions]]:** Compute a result based on an RDD and either return it to the driver program or save it to an external storage system (e.g., `count`, `collect`, `take`, `first`, `reduce`, `saveAsTextFile`). Actions trigger the execution of the DAG.

## Example RDD Workflow (Word Count)
```python
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("RDDWordCount").getOrCreate()
# sc = spark.sparkContext

# 1. Create an RDD from a text file (or parallelized list)
# Assuming 'reviews.txt' contains product review text
# lines_rdd = sc.textFile("path/to/reviews.txt") # Replace with actual path or use parallelize
# conceptual_lines = ["great product love it", "product okay but service bad", "love love love this product"]
# lines_rdd = sc.parallelize(conceptual_lines)

# 2. Transformations
# Split each line into words (flatMap)
# words_rdd = lines_rdd.flatMap(lambda line: line.lower().split(" "))

# Filter out empty strings if any
# words_rdd_filtered = words_rdd.filter(lambda word: len(word) > 0)

# Map each word to a (word, 1) pair
# word_pairs_rdd = words_rdd_filtered.map(lambda word: (word, 1))

# Reduce by key to sum counts for each word
# word_counts_rdd = word_pairs_rdd.reduceByKey(lambda a, b: a + b)

# 3. Action: Collect and print results
# results = word_counts_rdd.collect()
# for word, count in results:
#     print(f"{word}: {count}")

# spark.stop()
```

## RDDs vs. DataFrames/Datasets
While RDDs were the original core abstraction, Spark has since introduced higher-level APIs:
-   **[[Spark_DataFrame_SQL|DataFrames]]:** A distributed collection of data organized into named columns, conceptually similar to a table in a relational database or a Pandas DataFrame. Provides schema and optimizations via the Catalyst optimizer.
-   **Datasets (Scala/Java):** An extension of DataFrames that provides type safety and object-oriented programming benefits. (In PySpark, DataFrame is the primary structured API, and its rows are `Row` objects, not typed like Scala/Java Datasets).

**Advantages of DataFrames/Datasets over RDDs:**
-   **Optimization:** The Catalyst optimizer can significantly optimize queries and operations on DataFrames/Datasets.
-   **Schema:** Enforced schema provides better structure and error checking.
-   **Ease of Use:** More concise and often more intuitive for structured data operations, especially with SQL-like queries.
-   **Performance:** Tungsten execution engine provides efficient in-memory columnar storage and code generation.

**When to use RDDs:**
-   When you need low-level control over data partitioning and physical execution.
-   When working with unstructured or semi-structured data that doesn't fit well into a tabular schema.
-   For certain advanced algorithms that are easier to express with RDD transformations.
-   When interfacing with older Spark libraries or codebases primarily using RDDs.

Modern Spark development heavily favors the DataFrame/Dataset API for most tasks due to its optimizations and ease of use, but understanding RDDs is still important as they are the underlying foundation.

---