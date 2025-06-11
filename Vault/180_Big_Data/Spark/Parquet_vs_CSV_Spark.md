---
tags:
  - spark
  - data_format
  - parquet
  - csv
  - columnar_storage
  - row_based_storage
  - performance
  - compression
  - schema
  - concept_comparison
aliases:
  - Parquet vs CSV
  - CSV vs Parquet in Spark
related:
  - "[[PySpark_Data_Sources]]"
  - "[[Apache_Parquet]]"
  - "[[CSV_File_Format]]"
  - "[[Data_Serialization_Formats]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Parquet vs. CSV Files in Spark

When working with [[PySpark_Data_Sources|data sources in Apache Spark]], particularly for large datasets, the choice of file format can significantly impact performance, storage efficiency, and schema handling. Two common formats are CSV (Comma-Separated Values) and Apache Parquet.

>[!question] What is the difference between `parquet` files and `csv` files?

[list2tab|#Parquet vs CSV Comparison]
- Feature
    - CSV (Comma-Separated Values)
        - Apache Parquet
- **Storage Format**
    - **Row-based:** Data is stored row by row. Each line in the file typically represents a record, with values for each field separated by a delimiter (usually a comma).
        ```
        id,name,age
        1,Alice,30
        2,Bob,24
        ```
    -   **Columnar:** Data is stored column by column. Values for each column are stored contiguously. This means all values for 'id' are together, then all values for 'name', etc.
        -   Internally organized into row groups, column chunks, and pages.
- **Schema**
    - **Schema-less / Schema on Read:** CSV files themselves do not inherently store schema information (column names, data types). The schema must be inferred or explicitly defined when reading the file.
    -   **Schema Embedded:** Parquet files store the schema (column names, data types, nullability) within the file metadata (usually in the footer). This makes data self-describing.
- **Data Types**
    - **Typically stores everything as text.** Data types need to be inferred or specified during parsing, which can be error-prone (e.g., "123" could be string or int).
    -   Supports a rich set of **primitive data types** (INT32, INT64, FLOAT, DOUBLE, BOOLEAN, BYTE_ARRAY for strings/binary) and **complex types** (lists, maps, structs). Data is stored in its native type.
- **Compression**
    - **Limited:** CSV files are plain text and can be compressed using general-purpose compression algorithms like GZip or BZip2 applied to the *entire file*. This makes the file non-splittable for parallel processing after compression by default.
    -   **Efficient & Granular:** Supports efficient compression on a per-column basis using various codecs (e.g., Snappy, GZip, LZO, Brotli, Zstd). Since data in a column is often of the same type and has similar values, columnar compression is usually much more effective. Compressed Parquet files are often splittable.
- **Performance (Querying / Analytics)**
    - **Slower for Analytical Queries:** To read a few columns from a wide table, the entire row (all columns) must often be read from disk. Projections (selecting a subset of columns) are inefficient.
    -   **Faster for Analytical Queries (Column Pruning & Predicate Pushdown):**
        -   **Column Pruning:** Because data is stored by column, analytical queries that only need a subset of columns can read only those specific columns from disk, significantly reducing I/O.
        -   **Predicate Pushdown:** Metadata (min/max values per column chunk/page) allows query engines like Spark to skip reading entire chunks or pages of data if they don't satisfy the query's filter conditions (predicates).
- **Mutability**
    - **Easily Editable (Text):** CSV files are plain text and can be easily opened and modified by simple text editors or spreadsheet software.
    -   **Immutable (Binary):** Parquet is a binary format and is designed to be immutable once written. Updates usually involve rewriting the file or relevant partitions.
- **Splittability (for Parallel Processing)**
    - **Generally Not Splittable if Compressed:** A gzipped CSV file cannot be easily split for parallel processing by multiple Spark tasks unless special techniques are used (e.g., specific splittable compression formats or processing uncompressed). Uncompressed CSVs can be split by line.
    -   **Splittable (Even when Compressed):** Parquet files, due to their internal structure (row groups), are designed to be splittable, even when internally compressed (e.g., with Snappy). This is crucial for efficient parallel processing in Spark.
- **Complexity**
    - **Simple:** Very simple format, easy to generate and understand.
    -   **More Complex:** More complex internal structure, but this complexity is handled by libraries like Spark, Hive, Presto.
- **Use Cases**
    - Small datasets, data interchange between simple tools, human-readable data.
    - Big Data analytics, data warehousing, efficient storage and querying in distributed systems like Hadoop/Spark. Optimal for read-heavy analytical workloads.

## Spark and File Formats

**Reading CSV with Spark:**
```python
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("CSVExample").getOrCreate()

# df_csv = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)
# df_csv.show()
# df_csv.printSchema() # Schema is inferred or can be explicitly defined

# spark.stop()
```-   `header=True`: Uses the first line as column names.
-   `inferSchema=True`: Spark will try to guess data types (can be slow for large files; providing an explicit schema is better for production).

**Reading Parquet with Spark:**
```python
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("ParquetExample").getOrCreate()

# df_parquet = spark.read.parquet("path/to/your/data.parquet")
# df_parquet.show()
# df_parquet.printSchema() # Schema is read from Parquet file metadata

# spark.stop()
```
-   Reading Parquet is generally faster and more efficient because Spark can leverage column pruning and predicate pushdown. The schema is automatically available.

**Writing Data with Spark:**
```python
# (Assuming df is a Spark DataFrame)
# df.write.csv("path/to/output_csv", header=True, mode="overwrite")
# df.write.parquet("path/to/output_parquet", mode="overwrite", compression="snappy")
```
-   `mode="overwrite"` will overwrite existing data. Other modes include "append", "ignore", "errorifexists".
-   Parquet often defaults to Snappy compression, which offers a good balance of compression ratio and speed.

**Why Parquet is Preferred for Big Data Analytics in Spark:**
1.  **Performance:** Columnar storage, column pruning, and predicate pushdown lead to significantly faster query execution for analytical workloads (which typically select a subset of columns and filter rows).
2.  **Storage Efficiency:** Better compression ratios due to columnar storage (similar data types together) and efficient encoding schemes.
3.  **Schema Evolution:** Parquet supports schema evolution (e.g., adding/removing columns) more gracefully than CSV.
4.  **Splittability:** Crucial for parallel processing in distributed systems like Spark.

While CSV is simple and human-readable, **Parquet is generally the recommended file format for storing and processing large datasets in Spark and the broader Hadoop ecosystem** due to its performance and efficiency advantages.

---