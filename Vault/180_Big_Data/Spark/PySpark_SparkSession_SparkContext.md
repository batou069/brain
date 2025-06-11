---
tags:
  - spark
  - pyspark
  - sparksession
  - sparkcontext
  - entry_point
  - configuration
  - concept
aliases:
  - SparkSession
  - SparkContext
  - PySpark Entry Points
related:
  - "[[PySpark_Overview]]"
  - "[[Spark_Cluster_Architecture]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: `SparkSession` and `SparkContext`

In PySpark, `SparkSession` and `SparkContext` are the primary entry points to interact with Apache Spark functionality. Understanding their roles is key to writing Spark applications.

## `SparkContext` (`sc`)
-   **Role:** The original main entry point for Spark functionality (prominent in Spark 1.x). It represents the connection to a Spark cluster and can be used to create [[RDD_Resilient_Distributed_Dataset|RDDs]], accumulators, and broadcast variables on that cluster.
-   **Creation:** In older Spark versions (1.x), you would explicitly create a `SparkConf` object to configure the application and then use it to initialize a `SparkContext`.

>[!caution] 
> This is Spark 1.x style

```python
    # Spark 1.x style (less common now for new applications)
    from pyspark import SparkConf, SparkContext
    conf = SparkConf().setAppName("MyRDDApp").setMaster("local")
    sc = SparkContext(conf=conf)
```
-   **Functionality:**
    -   Creating RDDs: `sc.parallelize()`, `sc.textFile()`, etc.
    -   Creating [[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]: `sc.broadcast()`.
    -   Creating [[PySpark_Broadcast_Variables_Accumulators|Accumulators]]: `sc.accumulator()`.
    -   Getting cluster configuration.
    -   Setting application name and master URL.

>[!question] What is a Spark Context?
>A **`SparkContext`** is the main entry point for Spark functionality related to [[RDD_Resilient_Distributed_Dataset|RDDs]]. It represents the connection to a Spark cluster and is used to coordinate jobs on that cluster. It tells Spark how and where to access a cluster. Key responsibilities include:
>1.  **Cluster Connection:** Establishing communication with the [[Spark_Cluster_Manager|Cluster Manager]] (Standalone, YARN, Mesos, Kubernetes).
>2.  **Resource Allocation:** Requesting resources (executors) from the Cluster Manager.
>3.  **RDD Creation:** Providing methods to create RDDs from various sources (e.g., existing Python collections, HDFS, local files).
>4.  **Job Submission:** Submitting RDD operations (jobs composed of stages and tasks) for execution on the cluster.
>5.  **Configuration Management:** Holding the application's configuration settings.
>
>Essentially, the `SparkContext` is the heart of an RDD-based Spark application, managing the distributed execution environment.

## `SparkSession` (`spark`)
-   **Role:** Introduced in Spark 2.0 as a unified entry point for Spark, especially for the newer structured APIs like [[Spark_DataFrame_SQL|DataFrames]] and Datasets (though Datasets are primarily a Scala/Java concept; in PySpark, we mainly use DataFrames).
-   **Superset of `SparkContext`:** A `SparkSession` object internally creates and manages a `SparkContext`. You can access the `SparkContext` from a `SparkSession` via `spark.sparkContext`.
-   **Unified Entry Point:** Provides a single point of entry to interact with various Spark functionalities, including Spark SQL, Hive, Streaming, etc., without needing to create separate contexts (like `SQLContext`, `HiveContext` which were used in Spark 1.x).
-   **Creation (Recommended Way):** Using the `builder` pattern.
    ```python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("MyModernSparkApp") \
        .master("local[*]") \  # Example: run locally using all available cores
        .config("spark.some.config.option", "some-value") \ # Optional configurations
        .getOrCreate()
    
    # Access SparkContext if needed
    # sc = spark.sparkContext
    ```
    -   `appName("name")`: Sets the application name.
    -   `master("url")`: Sets the Spark master URL (e.g., "local", "local[k]", "spark://host:port", "yarn", "mesos://host:port", "k8s://host:port").
    -   `config("key", "value")`: Sets various Spark configuration properties.
    -   `getOrCreate()`: Gets an existing `SparkSession` or, if there is none, creates a new one based on the options set in the builder. This ensures that only one `SparkSession` is active per JVM (or Python process in PySpark's case for the driver).

-   **Functionality:**
    -   Creating DataFrames: `spark.createDataFrame()`, `spark.read.format(...).load()`.
    -   Executing SQL queries: `spark.sql("SELECT ...")`.
    -   Accessing configuration: `spark.conf.get()`, `spark.conf.set()`.
    -   Accessing the underlying `SparkContext`: `spark.sparkContext`.
    -   Interacting with the Spark Catalog (metadata about tables, databases, functions): `spark.catalog`.

>[!question] What is the difference between a Session and a Context?
>
| Feature | SparkContext (`sc`) | SparkSession (`spark`) |
|---------|--------------------|-----------------------|
| **Primary Focus** | Core Spark functionality, RDDs. | Unified entry point for structured data (DataFrames, SQL), streaming, MLlib, and also includes RDD functionality via its `sparkContext` attribute. |
| **Introduced** | Spark 1.0 | Spark 2.0 (to unify previous contexts like `SQLContext`, `HiveContext`) |
| **Creation** | `sc = SparkContext(conf=SparkConf())` (older style) | `spark = SparkSession.builder...getOrCreate()` (modern style) |
| **RDD API** | Direct access (e.g., `sc.parallelize()`) | Accessible via `spark.sparkContext` (e.g., `spark.sparkContext.parallelize()`) |
| **DataFrame/SQL API** | Requires separate `SQLContext` or `HiveContext` (in Spark 1.x). | Direct access (e.g., `spark.createDataFrame()`, `spark.sql()`) |
| **Usage Trend** | Less direct usage in new applications favoring DataFrames. Still fundamental internally. | **Recommended entry point** for most modern Spark applications. |
>
>**Analogy:**
>-   Think of `SparkContext` as the fundamental connection to the "engine room" of Spark, primarily dealing with the raw power of RDDs and cluster communication.
>-   `SparkSession` is like a more user-friendly "front office" or "dashboard" built on top of the engine room. It provides convenient access to all major Spark functionalities, including the engine room itself (`spark.sparkContext`), but with added features and abstractions for structured data and other Spark libraries.
>
>In modern PySpark (Spark 2.0+), you almost always start by creating a `SparkSession`. If you need to work directly with RDDs or use RDD-specific functionalities like broadcast variables or accumulators, you then access the `SparkContext` via `spark.sparkContext`.

## `builder` and `getOrCreate`
-   **`SparkSession.builder`**: This is a static attribute of the `SparkSession` class that returns a `SparkSession.Builder` object. The builder pattern allows you to chain configuration methods (`appName()`, `master()`, `config()`, etc.) to set up the desired session properties.
-   **`getOrCreate()`**: A method of the `SparkSession.Builder` object.
    -   If a `SparkSession` already exists in the current JVM (Python process for driver), this method returns the existing session, ignoring any new configurations passed to the builder (except for some specific cases like Spark Connect). This is important for ensuring a single active session.
    -   If no `SparkSession` exists, it creates a new one based on the configurations set via the builder.

This `getOrCreate()` behavior is useful in interactive environments (like notebooks or shells) where a Spark session might already be implicitly started, or in applications to prevent accidental creation of multiple conflicting sessions.

---