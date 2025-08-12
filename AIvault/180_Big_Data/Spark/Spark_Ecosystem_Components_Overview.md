---
tags:
  - spark
  - ecosystem
  - spark_sql
  - streaming
  - mllib
  - graphx
  - graphframes
  - concept
aliases:
  - Spark Components
  - Spark Libraries Overview
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_Streaming_Structured_Streaming]]"
  - "[[Spark_MLlib]]"
  - "[[Spark_GraphX_GraphFrames]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark Ecosystem Components Overview

Apache Spark is not just a single processing engine; it's a unified analytics engine comprising several closely integrated components built on top of the Spark Core. These components allow Spark to handle a wide variety of Big Data workloads.

>[!question] For each of the following modules/classes, explain what is its purpose and its advantages: RDD, DataFrame and SQL, Streaming, MLlib, GraphFrames, Resource
>
>*(Note: "Resource" is not a standard top-level Spark module/class in the same way as the others. It might refer to resource management aspects handled by the [[Spark_Cluster_Manager|Cluster Manager]] (like YARN, Mesos) or Spark's internal memory/CPU allocation, which are more cross-cutting concerns. I will focus on the other listed components.)*

[list2tab|#Spark Components & Purpose]
- [[RDD_Resilient_Distributed_Dataset|RDD (Resilient Distributed Dataset)]]
    -   **Purpose:**
        -   RDDs are Spark's fundamental, low-level data abstraction representing an immutable, partitioned collection of elements that can be operated on in parallel.
        -   They provide a fault-tolerant way to store and process large datasets distributed across a cluster by tracking their lineage (the sequence of transformations used to create them).
    -   **Advantages:**
        -   **Fault Tolerance:** Can be recomputed from lineage if a partition is lost.
        -   **Immutability:** Simplifies consistency and reasoning about transformations.
        -   **Flexibility:** Can store any type of Python, Java, or Scala objects, making them suitable for unstructured or semi-structured data.
        -   **Low-Level Control:** Offers fine-grained control over data partitioning and physical execution.
        -   **[[Spark_Lazy_vs_Eager_Execution|Lazy Evaluation]]:** Enables optimizations by deferring computation until an action is called.
    -   **Primary Use:** While still the foundation, direct RDD programming is less common for structured data now, with [[Spark_DataFrame_SQL|DataFrames]] being preferred. RDDs are still useful for unstructured data, low-level operations, or when maximum control is needed.
- [[Spark_DataFrame_SQL|DataFrame and Spark SQL]]
    -   **Purpose:**
        -   **DataFrame:** A distributed collection of data organized into named columns, conceptually similar to a table in a relational database or a Pandas DataFrame. It imposes a schema on the data.
        -   **Spark SQL:** A Spark module for structured data processing that allows querying data via SQL (using standard SQL syntax or HiveQL) as well as with the DataFrame API.
    -   **Advantages:**
        -   **Optimization (Catalyst Optimizer & Tungsten):** DataFrames benefit from Spark's Catalyst optimizer, which performs extensive logical and physical query optimization (e.g., predicate pushdown, column pruning, join reordering) and the Tungsten execution engine for efficient in-memory columnar storage and code generation. This often leads to significantly better performance than raw RDD operations for structured data.
        -   **Schema:** Provides structure to the data, enabling better error checking and more efficient storage and processing.
        -   **Ease of Use:** The DataFrame API (with its rich set of transformations like `select`, `filter`, `groupBy`, `join`) and SQL queries are often more intuitive and concise for structured data manipulation than RDD operations.
        -   **Data Source Integration:** Easily reads from and writes to various structured data sources (JSON, Parquet, CSV, JDBC, Hive tables, etc.).
        -   **Interoperability:** Can be seamlessly converted to/from RDDs and Pandas DataFrames.
    -   **Primary Use:** The standard and recommended way for most structured and semi-structured data processing in Spark.
- [[Spark_Streaming_Structured_Streaming|Spark Streaming / Structured Streaming]]
    -   **Purpose:**
        -   **Spark Streaming (Older DStream API):** Enables scalable, high-throughput, fault-tolerant processing of live data streams. It processes data in mini-batches.
        -   **Structured Streaming (Newer API, built on Spark SQL engine):** A scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It treats a live data stream as a continuously appending table, allowing users to express stream computations similarly to batch computations on static data (using DataFrame/Dataset API and SQL).
    -   **Advantages:**
        -   **Unified API (Structured Streaming):** Allows using largely the same DataFrame/Dataset/SQL API for both batch and stream processing, simplifying development.
        -   **Fault Tolerance:** Provides end-to-end exactly-once processing guarantees (for Structured Streaming with supported sources/sinks).
        -   **Integration:** Integrates well with various data sources (Kafka, Flume, Kinesis, HDFS/S3 for file streams) and sinks.
        -   **Stateful Operations:** Supports complex stateful operations like windowed aggregations, stream-stream joins, and arbitrary stateful logic.
        -   **High Throughput & Scalability:** Leverages Spark's core engine for distributed processing.
    -   **Primary Use:** Real-time data processing, continuous ETL, real-time analytics, monitoring, alerting. Structured Streaming is generally preferred for new applications.
- [[Spark_MLlib|MLlib (Machine Learning Library)]]
    -   **Purpose:** Spark's built-in machine learning library. It aims to make practical machine learning scalable and easy.
    -   **Components & Algorithms:**
        -   **ML Algorithms:** Common learning algorithms such as classification (logistic regression, decision trees, random forests, gradient-boosted trees, naive Bayes, SVMs), regression (linear regression, decision trees, GBTs), clustering (K-Means, LDA, GMMs), and collaborative filtering.
        -   **Featurization:** Feature extraction (TF-IDF, Word2Vec, CountVectorizer), transformation (StandardScaler, MinMaxScaler, PCA), and selection.
        -   **Pipelines:** Tools for constructing, evaluating, and tuning ML Pipelines (sequences of feature transformations and models).
        -   **Persistence:** Saving and loading algorithms, models, and Pipelines.
        -   **Utilities:** Linear algebra, statistics.
    -   **Advantages:**
        -   **Scalability:** Designed to run on large datasets distributed across a cluster.
        -   **Integration with Spark:** Works seamlessly with Spark DataFrames for data input and feature engineering.
        -   **Ease of Use:** Provides a relatively high-level API for common ML tasks.
    -   **Primary Use:** Building and deploying scalable machine learning models within the Spark ecosystem. It has two main packages:
        -   `spark.mllib`: The original RDD-based API (now in maintenance mode).
        -   `spark.ml`: The newer DataFrame-based API (recommended for new development).
- [[Spark_GraphX_GraphFrames|GraphX / GraphFrames]]
    -   **Purpose:** Libraries for graph processing and analytics on Spark.
    -   **GraphX:**
        -   The original RDD-based graph processing API in Spark.
        -   Provides RDDs for vertices (`VertexRDD`) and edges (`EdgeRDD`), and a `Graph` class.
        -   Includes common graph algorithms like PageRank, Connected Components, Triangle Counting.
        -   Offers a Pregel-like API for iterative graph computations.
    -   **GraphFrames:**
        -   A newer, DataFrame-based API for graph processing. It represents graphs using DataFrames for vertices and edges.
        -   Allows leveraging Spark SQL optimizations and DataFrame operations for graph queries.
        -   Provides a similar set of algorithms to GraphX and also integrates with graph query languages like Cypher (via connectors).
        -   Often easier to use if data is already in DataFrames.
    -   **Advantages:**
        -   **Scalable Graph Processing:** Enables analysis of large-scale graphs that don't fit on a single machine.
        -   **Integration with Spark:** Can combine graph processing with other Spark components (SQL, MLlib, Streaming).
    -   **Primary Use:** Social network analysis, recommendation systems, fraud detection, network topology analysis, bioinformatics. GraphFrames is generally becoming more favored due to its DataFrame integration.

These components make Apache Spark a versatile and powerful platform for a wide range of Big Data processing and analytics tasks.

---