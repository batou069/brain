---
tags:
  - hadoop
  - hive
  - data_warehouse
  - sql
  - hql
  - big_data
  - mapreduce
  - tez
  - spark
  - concept
aliases:
  - Hive
  - HiveQL
related:
  - "[[_Hadoop_MOC]]"
  - "[[HDFS]]"
  - "[[MapReduce]]"
  - "[[Apache_Spark_MOC]]"
  - "[[Apache_Tez]]"
  - "[[SQL_MOC]]"
  - "[[Data_Warehousing_Concepts]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Apache Hive

## Definition
**Apache Hive** is a data warehouse infrastructure built on top of [[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop]] for providing data summarization, query, and analysis. It provides an SQL-like interface called **HiveQL (Hive Query Language)** to query data stored in various databases and file systems that integrate with Hadoop, primarily the [[HDFS|Hadoop Distributed File System]].

Hive was initially developed by Facebook and later open-sourced. It allows users familiar with SQL to perform ad-hoc querying, data analysis, and ETL (Extract, Transform, Load) tasks on large datasets without needing to write complex [[MapReduce|MapReduce]] programs directly in Java or Python.

## Key Features and Concepts
[list2tab|#Hive Features]
- SQL-like Interface (HiveQL)
    -   Provides a familiar query language that is syntactically similar to SQL. This lowers the barrier to entry for data analysts and SQL developers to work with Big Data in Hadoop.
    -   HiveQL supports many standard SQL operations like `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY`, `JOIN`s, window functions, etc.
- Schema on Read
    -   Unlike traditional relational databases (schema on write), Hive imposes a schema on the data *when it is read* during query execution.
    -   Data can be loaded into HDFS in various formats (e.g., CSV, TSV, JSON, Parquet, ORC) without prior schema validation. The table schema (column names, data types) is defined in Hive's metastore and applied when a query is run.
    -   This offers flexibility in handling diverse and evolving data formats.
- Metastore
    -   Hive uses a **metastore** (typically a relational database like MySQL or PostgreSQL) to store schema information about tables, partitions, data locations, and data formats.
    -   This separation of metadata from data allows Hive to manage structured data stored in HDFS.
- Execution Engines
    -   HiveQL queries are translated into execution plans that can run on different distributed computing frameworks:
        -   **[[MapReduce|MapReduce]] (Traditional):** Originally, Hive queries were primarily converted into a series of MapReduce jobs.
        -   **[[Apache_Tez|Apache Tez]]:** A more optimized execution engine that represents dataflows as Directed Acyclic Graphs (DAGs), often providing significant performance improvements over MapReduce for Hive queries.
        -   **[[Apache_Spark_MOC|Apache Spark]]:** Hive can also use Spark as an execution engine (Hive on Spark), leveraging Spark's in-memory processing capabilities for faster query execution.
- Partitions and Buckets
    -   **Partitions:** Hive tables can be partitioned based on the values of one or more columns (e.g., a table `sales_data` partitioned by `year` and `month`). This divides the table data into separate subdirectories in HDFS. Queries that filter on partition columns can significantly improve performance by only scanning relevant partitions (partition pruning).
    -   **Buckets (Clustering):** Within partitions (or unpartitioned tables), data can be further divided into fixed-size buckets based on the hash of one or more columns. This can improve query performance for joins or sampling by organizing data within each partition.
- User-Defined Functions (UDFs)
    -   Hive allows users to write custom functions (UDFs for scalar operations, UDAFs for aggregations, UDTFs for table-generating functions) in Java or other languages to extend HiveQL's capabilities.
- Storage Formats
    -   Hive can read and write data in various file formats stored in HDFS, including:
        -   Text files (CSV, TSV)
        -   SequenceFile (Hadoop's native binary format)
        -   Avro
        -   **Parquet** (Columnar storage, good for analytical queries)
        -   **ORC (Optimized Row Columnar)** (Columnar storage, highly optimized for Hive)
        Columnar formats like Parquet and ORC offer better compression and query performance for analytical workloads.
- Extensibility and Integration
    -   Integrates with other Hadoop ecosystem tools and can access data in HDFS, HBase, S3, etc.

## Hive Architecture (Simplified)
1.  **User Interface (UI):** Clients submit HiveQL queries (e.g., Hive CLI, Beeline, JDBC/ODBC drivers from BI tools).
2.  **Driver:** Receives the query.
3.  **Compiler:** Parses the query, performs semantic analysis, and generates an execution plan (often a DAG of MapReduce/Tez/Spark stages). This involves consulting the Metastore for schema information.
4.  **Metastore:** Stores table definitions, schemas, partition information, and data locations.
5.  **Execution Engine (MapReduce, Tez, Spark):** Executes the plan on the Hadoop cluster, interacting with HDFS for data and YARN for resources.
6.  **HDFS/Storage:** Actual data resides in HDFS or other compatible storage.

## Example HiveQL Queries
Assuming a table `employees` (id INT, name STRING, department STRING, salary DOUBLE, hire_date DATE) and `departments` (dept_id STRING, dept_name STRING).

```hiveql
-- Select specific columns
SELECT name, salary FROM employees WHERE department = 'Sales';

-- Aggregate data: Average salary per department
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Join tables
SELECT e.name, d.dept_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.dept_id; -- Assuming employees has department_id

-- Create a partitioned table (DDL)
CREATE TABLE sales_logs (
    transaction_id INT,
    product_name STRING,
    amount DECIMAL(10,2)
)
PARTITIONED BY (sale_date DATE, region STRING)
STORED AS PARQUET;

-- Load data into a partition
LOAD DATA INPATH '/user/data/sales/2023-10-26/US'
INTO TABLE sales_logs
PARTITION (sale_date='2023-10-26', region='US');

-- Query a specific partition
SELECT product_name, SUM(amount)
FROM sales_logs
WHERE sale_date = '2023-10-26' AND region = 'US'
GROUP BY product_name;
```

>[!question] What is the best way to query data inside a Hadoop cluster?
>The "best" way depends on the specific requirements (latency, complexity of query, data structure, user skills), but **Apache Hive is a very common and often preferred method for SQL-like ad-hoc querying and batch analytics on data stored in Hadoop (HDFS).**
>
>Reasons Hive is often considered "best" or very good:
>1.  **SQL Familiarity:** HiveQL's similarity to SQL makes it accessible to a wide range of users (analysts, data scientists, SQL developers) without needing to learn complex Java/Scala/Python for MapReduce or Spark directly.
>2.  **Batch Analytics & Reporting:** Excellent for complex analytical queries, aggregations, joins, and generating reports over large datasets.
>3.  **Schema Management:** Provides a way to impose structure (schema) on unstructured or semi-structured data in HDFS.
>4.  **Optimization:** Modern Hive with execution engines like Tez or Spark can be quite performant for many analytical workloads, especially with columnar storage formats like Parquet or ORC.
>5.  **Ecosystem Integration:** Well-integrated with the Hadoop ecosystem.
>
>Other ways to query data in Hadoop and their contexts:
>-   **[[MapReduce|MapReduce]] (Java, Python Streaming):** For highly customized, complex data processing tasks where SQL is not expressive enough or for fine-grained control over execution. More development effort.
>-   **[[Apache_Spark_MOC|Apache Spark]] (Spark SQL, DataFrames/Datasets API):** Often faster than Hive on MapReduce/Tez due to in-memory processing. Spark SQL is also SQL-like and very powerful. Spark is a strong alternative or complement to Hive. Many systems now use Spark as the execution engine for Hive queries ("Hive on Spark").
>-   **[[Apache_Pig|Apache Pig]]:** Uses Pig Latin, a data flow language. Good for ETL and complex data transformations that are less natural in SQL.
>-   **[[Apache_HBase|HBase]]:** For low-latency, random read/write access to individual records or small ranges (NoSQL). Not for complex analytical queries across the entire dataset. Queried via its own API or tools like Apache Phoenix (SQL layer on HBase).
>-   **Presto / Trino:** Distributed SQL query engines designed for high-performance, interactive analytics on various data sources, including HDFS. Can be faster than Hive for certain interactive queries.
>-   **Impala:** Another distributed SQL query engine for Hadoop, known for low-latency queries.
>
>**Conclusion:** For general-purpose, SQL-based batch analytics and data warehousing tasks on Hadoop, **Hive (often with Tez or Spark execution engines)** is a robust and widely adopted solution. For more interactive or lower-latency SQL queries, Presto/Trino or Impala might be preferred. For programmatic data processing with more flexibility, Spark is a leading choice.

## Use Cases
-   Data warehousing and business intelligence (BI).
-   Ad-hoc querying and exploration of large datasets.
-   ETL (Extract, Transform, Load) pipelines.
-   Log analysis.
-   Reporting.
-   Batch processing for analytics.

Hive simplifies working with large datasets in Hadoop by providing a familiar SQL abstraction, making Big Data analytics more accessible.

---