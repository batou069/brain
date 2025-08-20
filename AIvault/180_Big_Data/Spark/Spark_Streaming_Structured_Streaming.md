---
tags:
  - spark
  - streaming
  - structured_streaming
  - real_time_processing
  - micro_batch
  - continuous_processing
  - concept
aliases:
  - Spark Streaming
  - Structured Streaming
  - DStream
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Data_Streaming_Big_Data]]"
  - "[[Apache_Kafka]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
worksheet:
  - WS_Spark_1
date_created: 2025-08-20
---
# Spark Streaming & Structured Streaming

Apache Spark provides capabilities for processing [[Data_Streaming_Big_Data|streaming data]], allowing applications to analyze and act upon data in real-time or near real-time as it arrives. Spark has two main streaming APIs:

1.  **Spark Streaming (Legacy):** The original streaming library based on Discretized Streams (DStreams).
2.  **Structured Streaming (Current & Recommended):** A newer, higher-level API built on the Spark SQL engine and [[Spark_DataFrame_SQL|DataFrame]] API, designed for easier and more robust stream processing.

## 1. Spark Streaming (DStream API - Legacy)
-   **Concept:** Processes live data streams by dividing them into a sequence of small batches (micro-batches). Each batch is treated as an [[RDD_Resilient_Distributed_Dataset|RDD]]. Transformations on these DStreams (Discretized Streams) are applied to each underlying RDD in the sequence.
-   **DStream:** A DStream is a continuous sequence of RDDs representing a stream of data.
-   **Operations:** Supports transformations (e.g., `map`, `filter`, `reduceByKeyAndWindow`, `updateStateByKey`) and output operations (e.g., `print`, `saveAsTextFiles`, `foreachRDD`).
-   **Windowing:** Supports windowed computations (e.g., `window()`, `countByWindow()`, `reduceByWindow()`).
-   **Stateful Operations:** Can maintain state across batches using `updateStateByKey` or `mapWithState`.
-   **Fault Tolerance:** Inherits RDD fault tolerance.
-   **Status:** While still functional, **Spark Streaming (DStream API) is largely considered legacy**. Most new development and focus have shifted to Structured Streaming due to its advantages.

## 2. Structured Streaming (DataFrame/Dataset API - Recommended)
-   **Concept:** A scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express streaming computations in the same way you would express batch computations on static data using the DataFrame/Dataset API.
-   **Core Idea:** Treats a live data stream as a continuously appending, unbounded table. Each new item in the stream is like a new row being appended to this table.
-   **Queries:** You define a query on this "input table" as if it were a static table, using standard DataFrame/Dataset operations (e.g., `select`, `filter`, `groupBy`, `join`, window functions).
-   **Incremental Execution:** Spark automatically converts these batch-like queries into incremental execution plans that run continuously as new stream data arrives.
-   **Output Modes:**
    -   `complete`: The entire updated result table is written to the output sink at each trigger.
    -   `append`: Only new rows added to the result table since the last trigger are written to the sink. (Default, suitable for queries where existing rows don't change).
    -   `update`: Only rows that were updated in the result table since the last trigger are written. (If query has aggregations, only updated rows are output).
-   **Triggers:** Defines when to process new data (e.g., process all available data, process every N seconds).
-   **Event Time Processing & Watermarking:** Strong support for handling out-of-order data based on event timestamps embedded in the data itself, using watermarks to manage late data and state.
-   **Stateful Operations:** Supports complex stateful operations like aggregations, windowing, and joins between streams or a stream and a static table. State is managed reliably.
-   **End-to-End Exactly-Once Semantics:** Aims to provide exactly-once processing guarantees with supported sources and sinks.

### Key Components of Structured Streaming
[list2tab|#Structured Streaming]
- Input Sources
    -   **File Source:** Reads files written into a directory (e.g., CSV, JSON, Parquet, ORC). Treats new files as a stream.
    -   **[[Apache_Kafka|Kafka Source]]:** Reads data from Apache Kafka topics. Very common for stream ingestion.
    -   Socket Source (for testing).
    -   Rate Source (for testing, generates data at a fixed rate).
    -   Custom sources can be implemented.
- Query Definition (DataFrame API)
    -   Use standard DataFrame transformations (`select`, `filter`, `groupBy`, `agg`, `withWatermark`, `window`, `join`).
- Output Sinks
    -   **File Sink:** Writes the output to files (CSV, JSON, Parquet, ORC).
    -   **Kafka Sink:** Writes output to a Kafka topic.
    -   **Foreach/ForeachBatch Sink:** Allows custom logic to write output to arbitrary storage systems (e.g., databases, key-value stores).
    -   Console Sink (for debugging, prints to console).
    -   Memory Sink (for debugging, stores output in an in-memory table).
- Output Modes
    -   `append`, `complete`, `update` (as described above).
- Triggers
    -   `processingTime`: Trigger based on processing time intervals (e.g., every 10 seconds).
    -   `once`: Trigger only once to process all available data and then stop.
    -   `continuous`: (Experimental) A low-latency continuous processing mode.

### Example: Structured Streaming Word Count from a Socket Source
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import explode, split, window

# spark = SparkSession.builder \
#     .appName("StructuredStreamingWordCount") \
#     .master("local[*]") \
#     .getOrCreate()

# # Create a DataFrame representing the stream of input lines from a netcat server
# # To run this, start a netcat server: nc -lk 9999 on your terminal
# lines_df = spark.readStream \
#     .format("socket") \
#     .option("host", "localhost") \
#     .option("port", 9999) \
#     .load()

# # Split the lines into words
# # lines_df is a DataFrame with a single string column "value"
# words_df = lines_df.select(
#    explode(
#        split(lines_df.value, " ")
#    ).alias("word")
# )

# # Generate running word count
# word_counts_df = words_df.groupBy("word").count()

# # Start running the query that prints the running counts to the console
# query = word_counts_df.writeStream \
#     .outputMode("complete") \ # Show all counts every time
#     .format("console") \
#     .trigger(processingTime="5 seconds") \ # Process data every 5 seconds
#     .start()

# print("Streaming query started. Type words into netcat (localhost:9999).")
# query.awaitTermination() # Wait for the query to terminate (e.g., by Ctrl-C)

# spark.stop()
```
> To test this, you would run `nc -lk 9999` in one terminal and then run the PySpark script. Words typed into the netcat terminal will be processed.

### Example: Structured Streaming with Event Time and Watermarking (Conceptual)
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import window, col, current_timestamp, expr
# from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# spark = SparkSession.builder.appName("EventTimeWindowing").master("local[*]").getOrCreate()

# Define schema for incoming data (e.g., product click events)
# event_schema = StructType([
#     StructField("event_time", TimestampType(), True),
#     StructField("product_id", StringType(), True),
#     StructField("action", StringType(), True) # e.g., "view", "click"
# ])

# Read from a source like Kafka or a directory of files
# For example, reading from a directory of JSON files
# input_stream_df = spark.readStream \
#     .schema(event_schema) \
#     .json("path/to/streaming_event_data_json/") # Directory to monitor

# Group by a tumbling window of 10 minutes on 'event_time' and 'product_id', count actions
# Add a watermark to handle late data (e.g., events arriving up to 5 minutes late)
# windowed_counts = input_stream_df \
#     .withWatermark("event_time", "5 minutes") \
#     .groupBy(
#         window(col("event_time"), "10 minutes", "5 minutes"), # 10 min window, slides every 5 min
#         col("product_id"),
#         col("action")
#     ).count()

# query_event_time = windowed_counts.writeStream \
#     .outputMode("update") \ # Update mode for aggregations
#     .format("console") \
#     .option("truncate", "false") \
#     .trigger(processingTime="1 minute") \
#     .start()

# query_event_time.awaitTermination()
# spark.stop()
```

## Advantages of Structured Streaming over DStream API
-   **Higher-Level API:** Built on DataFrames/Datasets and Spark SQL, making it easier to write and reason about stream processing logic using familiar batch-like constructs.
-   **Unified Batch and Streaming:** Code for batch and stream processing is largely the same.
-   **Event Time Processing:** Robust support for event time semantics and handling late data with watermarks.
-   **End-to-End Guarantees:** Better support for exactly-once processing semantics with compatible sources/sinks.
-   **Catalyst Optimizer:** Leverages Spark SQL's Catalyst optimizer for query optimization.

Structured Streaming is the recommended approach for most new stream processing applications in Spark.

---