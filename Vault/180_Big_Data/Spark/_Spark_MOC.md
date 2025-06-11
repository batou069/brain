---
tags:
  - spark
  - big_data
  - distributed_computing
  - in_memory_processing
  - rdd
  - dataframe
  - streaming
  - mllib
  - moc
  - concept
aliases:
  - Apache Spark MOC
  - Spark Ecosystem MOC
  - PySpark MOC
related:
  - "[[_Big_Data_MOC]]"
  - "[[180_Big_Data/Hadoop/_Hadoop_MOC|Hadoop Ecosystem MOC]]"
  - "[[Spark_vs_Hadoop_MapReduce]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD (Resilient Distributed Dataset)]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_Transformations_Actions|Spark Transformations and Actions]]"
  - "[[Spark_Lazy_vs_Eager_Execution|Spark Lazy vs. Eager Execution]]"
  - "[[Spark_DAG_Scheduler|Spark DAG Scheduler]]"
  - "[[Spark_Cluster_Architecture|Spark Cluster Architecture]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Apache Spark MOC ⚡️🚀

**Apache Spark** is a fast, general-purpose, open-source cluster-computing framework for [[Big_Data_Definition_Characteristics|Big Data]] processing. It provides high-level APIs in Java, Scala, Python (PySpark), and R, and an optimized engine that supports general execution graphs. Spark is known for its speed, largely due to its ability to perform in-memory computations, and its versatility in handling various workloads like batch processing, interactive queries (SQL), real-time streaming, machine learning, and graph processing.

## Core Concepts
-   [[Spark_vs_Hadoop_MapReduce|Spark vs. Hadoop MapReduce]]
-   [[Why_Spark_Needed|Why Spark is Needed]]
-   [[Spark_Cluster_Architecture|Spark Cluster Architecture]]
    -   [[Spark_Cluster_Manager|Cluster Manager (Standalone, YARN, Mesos, Kubernetes)]]
    -   Driver Program, Executors, Workers
-   [[RDD_Resilient_Distributed_Dataset|Resilient Distributed Datasets (RDDs)]]
    -   The fundamental data abstraction in Spark.
-   [[Spark_DataFrame_SQL|DataFrames and Datasets API]]
    -   Higher-level, structured data abstractions providing optimizations via Catalyst optimizer and Tungsten execution engine.
-   [[Spark_Transformations_Actions|Transformations (Narrow & Wide) and Actions]]
-   [[Spark_Lazy_vs_Eager_Execution|Lazy Execution and Eager Execution]]
-   [[Spark_DAG_Scheduler|Directed Acyclic Graph (DAG) of Operations]]
-   [[Spark_Data_Parallelism|Data Parallelism in Spark]]
-   [[Spark_Shuffle_Operations|Shuffle Operations]]
-   [[Spark_Persistence_Caching|Persistence and Caching]]
-   [[Spark_Join_Strategies|Join Strategies in Spark SQL]]

## PySpark (Python API for Spark)
-   [[PySpark_Overview|Introduction to PySpark]]
-   [[PySpark_SparkSession_SparkContext|`SparkSession` and `SparkContext`]]
-   [[PySpark_RDD_Operations|RDD Operations (`parallelize`, `map`, `filter`, `reduceByKey`, etc.)]]
-   [[PySpark_DataFrame_Operations|DataFrame Operations (`withColumn`, `select`, `filter`, `groupBy`, SQL functions)]]
    -   [[PySpark_SQL_Functions|`pyspark.sql.functions`]]
    -   [[PySpark_Window_Functions|Window Functions in PySpark]]
-   [[PySpark_Data_Sources|Spark Data Sources (Reading/Writing Data)]]
    -   [[Parquet_vs_CSV_Spark|Parquet vs. CSV]]
    -   Reading JSON with Spark
-   [[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables and Accumulators]]
-   [[PySpark_UDFs|User-Defined Functions (UDFs)]]

## Spark Ecosystem Components
[list2card|addClass(ab-col3)|#Spark Components]
- **Spark Core**
  - Base engine providing RDDs, task scheduling, memory management, fault recovery.
- **[[Spark_DataFrame_SQL|Spark SQL]]**
  - For working with structured data using SQL queries or DataFrame API.
- **[[Spark_Streaming_Structured_Streaming|Spark Streaming & Structured Streaming]]**
  - For processing real-time data streams.
- **[[Spark_MLlib|MLlib (Machine Learning Library)]]**
  - Distributed machine learning framework with common algorithms.
- **[[Spark_GraphX_GraphFrames|GraphX / GraphFrames]]**
  - For graph processing and analytics.

## Advanced Topics
-   [[Spark_Performance_Tuning|Performance Tuning (Partitioning, Caching, Shuffling)]]
    -   `repartition()` and `coalesce()`
-   [[Spark_explain_Plan|Understanding Query Plans (`explain()`)]]
-   Constraints and Indexes in Spark (or lack thereof)

## Notes in this Spark Section
```dataview
LIST
FROM "180_Big_Data/Spark"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---