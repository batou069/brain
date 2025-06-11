---
tags:
  - spark
  - pyspark
  - data_sources
  - read_write
  - csv
  - json
  - parquet
  - jdbc
  - concept
  - example
  - hive
aliases:
  - Spark Data Sources
  - Reading Data PySpark
  - Writing Data PySpark
  - Spark Connectors
related:
  - "[[PySpark_DataFrame_Operations]]"
  - "[[Parquet_vs_CSV_Spark]]"
  - "[[HDFS]]"
  - "[[Apache_Hive]]"
  - "[[Cloud_Storage_Big_Data]]"
worksheet:
  - WS_Spark_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# PySpark: Data Sources (Reading and Writing Data)

Apache Spark provides a powerful and flexible API for reading data from and writing data to a wide variety of external storage systems and file formats. This is primarily handled through the `DataFrameReader` (`spark.read`) and `DataFrameWriter` (`df.write`) interfaces.

## `DataFrameReader` (`spark.read`)
Used to load data from external sources into a Spark [[Spark_DataFrame_SQL|DataFrame]].

**General Syntax:**
```python
# spark.read.format("source_format") \
#     .option("key", "value") \
#     .option("another_key", "another_value") \
#     .schema(your_schema) \ # Optional, but recommended for CSV/JSON
#     .load("path/to/data")
```
Or using shorthand methods:
```python
# spark.read.csv("path", header=True, inferSchema=True)
# spark.read.parquet("path")
# spark.read.json("path")
# spark.read.text("path")
```

## `DataFrameWriter` (`df.write`)
Used to save a Spark DataFrame to external storage systems.

**General Syntax:**
```python
# df.write.format("output_format") \
#     .option("key", "value") \
#     .mode("save_mode") \ # e.g., "overwrite", "append", "ignore", "errorifexists"
#     .partitionBy("col1", "col2") \ # Optional
#     .save("path/to/output")
```
Or using shorthand methods:
```python
# df.write.csv("path", header=True, mode="overwrite")
# df.write.parquet("path", mode="overwrite", compression="snappy")
# df.write.json("path", mode="overwrite")
# df.write.saveAsTable("table_name", mode="overwrite") # For Hive tables
```
-   **Save Modes:**
    -   `overwrite`: Overwrite existing data.
    -   `append`: Add new data to existing data.
    -   `ignore`: If data already exists at the path, do nothing.
    -   `error` or `errorifexists` (default): Throw an exception if data already exists.

## Common Data Sources and Formats

[list2tab|#Spark Data Sources]
- CSV (Comma-Separated Values)
    - **Reading:**
        ```python
        # from pyspark.sql import SparkSession
        # spark = SparkSession.builder.appName("CsvReadWrite").getOrCreate()
        # Read CSV inferring schema and using first line as header
        # product_reviews_csv_df = spark.read.csv(
        #     "path/to/product_reviews.csv",
        #     header=True,
        #     inferSchema=True, # Can be slow for large files, provide schema for production
        #     sep=",",
        #     quote="\"",
        #     escape="\""
        # )
        # product_reviews_csv_df.show(5)
        ```
    - **Writing:**
        ```python
        # (Assuming product_reviews_csv_df is a DataFrame)
        # product_reviews_csv_df.write.csv(
        #     "path/to/output_reviews_csv",
        #     header=True,
        #     mode="overwrite",
        #     sep="\t", # Example: write as TSV
        #     quoteAll=True
        # )
        ```
    - **Notes:** See [[Parquet_vs_CSV_Spark|Parquet vs. CSV]]. CSV is simple but less efficient for analytics than columnar formats. Defining schema explicitly is recommended for robustness and performance.
- JSON (JavaScript Object Notation)
    - **Reading:**
        ```python
        # from pyspark.sql import SparkSession
        # spark = SparkSession.builder.appName("JsonReadWrite").getOrCreate()
        # Can read single-line JSON files (one JSON object per line) or multi-line JSON files.
        # customer_interactions_df = spark.read.json("path/to/customer_interactions.json")
        # For multi-line JSON (one large JSON object/array spanning multiple lines):
        # customer_interactions_multiline_df = spark.read.option("multiline", "true").json("path/to/multiline_interactions.json")
        # customer_interactions_df.printSchema()
        # customer_interactions_df.show(5, truncate=False)
        ```
        >[!question] Can we read data directly from a JSON file using Spark? How? Why would we do that?
        >Yes, Spark can read data directly from JSON files using `spark.read.json("path/to/file.json")`.
        >
        >**How:**
        >-   Spark's JSON data source can automatically infer the schema from the JSON objects.
        >-   It supports both standard single-line JSON (each line is a separate JSON object) and multi-line JSON (a single JSON object or array spanning multiple lines, by setting `.option("multiline", "true")`).
        >
        >**Why would we do that?**
        >1.  **Common Data Interchange Format:** JSON is a very popular format for data exchange, especially from web APIs, NoSQL databases, and configuration files.
        >2.  **Semi-structured Data:** JSON handles nested structures (objects and arrays) well, making it suitable for semi-structured data where the schema might not be perfectly flat or fixed.
        >3.  **Ease of Use:** Reading JSON with Spark is straightforward, and schema inference simplifies initial loading (though explicit schemas are better for production).
        >4.  **Integration:** Many systems output data in JSON, so direct reading capability is essential for data ingestion pipelines.
        >
        >While convenient, for very large-scale analytical processing, converting JSON data to a columnar format like Parquet after initial ingestion is often beneficial for performance.
    - **Writing:**
        ```python
        # (Assuming customer_interactions_df is a DataFrame)
        # customer_interactions_df.write.json("path/to/output_interactions_json", mode="overwrite")
        ```
- Parquet (Apache Parquet)
    - **Reading:**
        ```python
        # from pyspark.sql import SparkSession
        # spark = SparkSession.builder.appName("ParquetReadWrite").getOrCreate()
        # product_catalog_df = spark.read.parquet("path/to/product_catalog.parquet")
        # product_catalog_df.printSchema() # Schema is embedded in Parquet
        # product_catalog_df.show(5)
        ```
    - **Writing:**
        ```python
        # (Assuming product_catalog_df is a DataFrame)
        # product_catalog_df.write.parquet(
        #     "path/to/output_catalog_parquet",
        #     mode="overwrite",
        #     compression="snappy" # Common compression codec
        # )
        ```
    - **Notes:** [[Parquet_vs_CSV_Spark|Columnar format]], highly efficient for analytical queries in Spark due to column pruning, predicate pushdown, and good compression. Often the recommended format for storing large datasets in a data lake.
- ORC (Optimized Row Columnar)
    - Similar to Parquet, another efficient columnar storage format.
    - `spark.read.orc("path")`, `df.write.orc("path")`.
- Text Files (`spark.read.text()`, `RDD.saveAsTextFile()`)
    - Reads each line of a text file as a single string column named "value".
    - Useful for unstructured text data that needs further parsing (e.g., with RDD operations or UDFs).
- JDBC (Relational Databases)
    - Reading from and writing to relational databases like MySQL, PostgreSQL, SQL Server, Oracle.
    - **Reading:**
        ```python
        # jdbc_df = spark.read.format("jdbc") \
        #     .option("url", "jdbc:postgresql://dbhost:5432/mydatabase") \
        #     .option("dbtable", "schema.employees") \ # Or use .option("query", "SELECT * FROM schema.employees WHERE ...")
        #     .option("user", "dbuser") \
        #     .option("password", "dbpassword") \
        #     .option("driver", "org.postgresql.Driver") \ # Ensure driver JAR is on classpath
        #     .load()
        # jdbc_df.show(5)
        ```
    - **Writing:**
        ```python
        # (Assuming some_df is a DataFrame)
        # some_df.write.format("jdbc") \
        #     .option("url", "jdbc:postgresql://dbhost:5432/mydatabase") \
        #     .option("dbtable", "schema.output_table") \
        #     .option("user", "dbuser") \
        #     .option("password", "dbpassword") \
        #     .mode("append") \ # Or "overwrite"
        #     .save()
        ```
- Hive Tables
    - If Spark is configured with Hive support (Hive metastore access), you can read from and write to Hive tables directly.
    - `spark.read.table("my_hive_database.my_hive_table")`
    - `df.write.saveAsTable("my_hive_database.new_hive_table")`
    - `spark.sql("SELECT * FROM my_hive_database.my_hive_table").show()`
- Other Sources
    - Spark has a rich ecosystem of connectors for various other data sources, including NoSQL databases (Cassandra, MongoDB, HBase), message queues (Kafka), cloud storage (S3, Azure Blob Storage, Google Cloud Storage). These often require adding specific connector dependencies/JARs.

## Common Options for `spark.read`
-   `header` (boolean, for CSV): Use the first line as column names.
-   `inferSchema` (boolean, for CSV/JSON): Infer data types. Can be slow; provide schema for production.
-   `schema` (StructType object): Explicitly define the schema.
-   `sep` or `delimiter` (string, for CSV): Specify the delimiter.
-   `multiLine` (boolean, for JSON): Handle JSON files spanning multiple lines.
-   Many format-specific options (e.g., `compression` for Parquet/ORC, date/timestamp formats).

Choosing the right data format and understanding how to read/write it efficiently is key to building effective Spark applications.

---

# PySpark: Data Sources (Reading and Writing Data)

Apache Spark provides a powerful and flexible API for reading data from and writing data to a wide variety of external storage systems and file formats. This is primarily handled through the `DataFrameReader` (`spark.read`) and `DataFrameWriter` (`df.write`) interfaces.

## `DataFrameReader` (`spark.read`)
Used to load data from external sources into a Spark [[Spark_DataFrame_SQL|DataFrame]].

**General Syntax:**
```python
# spark.read.format("source_format") \
#     .option("key", "value") \
#     .option("another_key", "another_value") \
#     .schema(your_schema) \ # Optional, but recommended for CSV/JSON
#     .load("path/to/data")
```
Or using shorthand methods:
```python
# spark.read.csv("path", header=True, inferSchema=True)
# spark.read.parquet("path")
# spark.read.json("path")
# spark.read.text("path")
```

## `DataFrameWriter` (`df.write`)
Used to save a Spark DataFrame to external storage systems.

**General Syntax:**
```python
# df.write.format("output_format") \
#     .option("key", "value") \
#     .mode("save_mode") \ # e.g., "overwrite", "append", "ignore", "errorifexists"
#     .partitionBy("col1", "col2") \ # Optional
#     .save("path/to/output")
```
Or using shorthand methods:
```python
# df.write.csv("path", header=True, mode="overwrite")
# df.write.parquet("path", mode="overwrite", compression="snappy")
# df.write.json("path", mode="overwrite")
# df.write.saveAsTable("table_name", mode="overwrite") # For Hive tables
```-   **Save Modes:**
    -   `overwrite`: Overwrite existing data.
    -   `append`: Add new data to existing data.
    -   `ignore`: If data already exists at the path, do nothing.
    -   `error` or `errorifexists` (default): Throw an exception if data already exists.

>[!question] What are the Spark data sources?
>Spark supports a wide variety of built-in and external data sources. These allow Spark to read from and write to different file formats and storage systems.
>
>**Built-in Data Sources (natively supported):**
>1.  **File-based sources:**
>    -   **[[Parquet_vs_CSV_Spark|Parquet]]:** Columnar format, highly recommended for performance and efficiency in Spark and Hadoop ecosystems. (`spark.read.parquet()`, `df.write.parquet()`)
>    -   **[[Parquet_vs_CSV_Spark|CSV (Comma-Separated Values)]]:** Common text-based format. (`spark.read.csv()`, `df.write.csv()`)
>    -   **JSON (JavaScript Object Notation):** Text-based format, good for semi-structured data. (`spark.read.json()`, `df.write.json()`)
>    -   **Text files:** Reads each line as a string. (`spark.read.text()`, `df.write.text()`)
>    -   **ORC (Optimized Row Columnar):** Another efficient columnar format, popular in the Hive ecosystem. (`spark.read.orc()`, `df.write.orc()`)
>    -   **Avro:** Row-based binary format with schema evolution capabilities. (`spark.read.format("avro").load()`, `df.write.format("avro").save()`) - often requires an external package like `spark-avro`.
>    -   **Binary files:** `spark.sparkContext.binaryFiles()` can read directories containing binary files.
>    -   **SequenceFiles:** Hadoop's native flat file format consisting of binary key-value pairs.
>2.  **JDBC Sources (Relational Databases):**
>    -   Allows reading from and writing to any relational database that has a JDBC driver (e.g., MySQL, PostgreSQL, Oracle, SQL Server).
>    -   `spark.read.jdbc(...)`, `df.write.jdbc(...)`.
>3.  **[[Apache_Hive|Apache Hive]] Tables:**
>    -   If Spark is configured with Hive support, it can read from and write to Hive tables directly using `spark.read.table("db.tableName")`, `df.write.saveAsTable("db.tableName")`, or Spark SQL queries.
>
>**External Data Sources (often require adding packages/connectors):**
>4.  **NoSQL Databases:**
>    -   Apache Cassandra (`spark-cassandra-connector`)
>    -   MongoDB (`mongo-spark-connector`)
>    -   HBase (via `spark-hbase-connector` or by reading HFiles)
>    -   Elasticsearch (`elasticsearch-hadoop`)
>5.  **[[Cloud_Storage_Big_Data|Cloud Storage Systems]]:**
>    -   Amazon S3 (natively supported with `s3a://` paths if Hadoop AWS JARs are configured)
>    -   Azure Blob Storage / Azure Data Lake Storage (ADLS Gen1/Gen2) (natively supported with `wasbs://` or `abfss://` paths if Hadoop Azure JARs are configured)
>    -   Google Cloud Storage (GCS) (natively supported with `gs://` paths if Hadoop GCS connector is configured)
>6.  **Message Queues / Streaming Sources:**
>    -   Apache Kafka (for [[Spark_Streaming_Structured_Streaming|Structured Streaming]] and Spark Streaming)
>    -   Amazon Kinesis, Azure Event Hubs (via connectors)
>7.  **Other Formats and Systems:**
>    -   Delta Lake, Apache Hudi, Apache Iceberg (table formats providing ACID transactions, schema evolution, time travel on data lakes)
    -   Many other specialized connectors are available from the Spark Packages website or third-party vendors.
>
>Spark's extensible data source API allows developers to create connectors for almost any data storage system.

## Common Options for `spark.read`
-   `header` (boolean, for CSV): Use the first line as column names.
-   `inferSchema` (boolean, for CSV/JSON): Infer data types. Can be slow; provide schema for production.
-   `schema` (StructType object): Explicitly define the schema.
-   `sep` or `delimiter` (string, for CSV): Specify the delimiter.
-   `multiLine` (boolean, for JSON): Handle JSON files spanning multiple lines.
-   Many format-specific options (e.g., `compression` for Parquet/ORC, date/timestamp formats).

Choosing the right data format and understanding how to read/write it efficiently is key to building effective Spark applications. [[Parquet_vs_CSV_Spark|Parquet]] is generally favored for intermediate storage and analytical workloads in Spark.

---