---
tags:
  - spark
  - pyspark
  - rdd
  - transformations
  - actions
  - parallelize
  - broadcast
  - map
  - filter
  - reduce
  - concept
  - example
aliases:
  - PySpark RDD API
  - RDD Operations
related:
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[PySpark_SparkSession_SparkContext]]"
  - "[[Spark_Transformations_Actions]]"
  - "[[Spark_Lazy_vs_Eager_Execution]]"
  - "[[PySpark_Broadcast_Variables_Accumulators]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: RDD Operations (`parallelize`, `broadcast`, etc.)

While [[Spark_DataFrame_SQL|DataFrames]] are the preferred API for most structured data tasks in modern PySpark, understanding [[RDD_Resilient_Distributed_Dataset|RDD (Resilient Distributed Dataset)]] operations is still valuable as RDDs are the underlying foundation and are useful for unstructured data or low-level control. RDD operations are accessed via the `SparkContext` object (usually `sc`).

## Creating RDDs

1.  **`sc.parallelize(collection, numSlices=None)`:**
    -   **Purpose:** Creates an RDD from an existing Python collection (e.g., a list, tuple) in your driver program.
    -   **`collection`**: The Python iterable to parallelize.
    -   **`numSlices`**: The desired number of partitions for the RDD. If not specified, Spark tries to set it automatically based on the cluster configuration.
    -   **Use Case:** Good for creating RDDs from small datasets for testing, prototyping, or when data originates in the driver. Not suitable for very large datasets that should be read from distributed storage.
    -   **Example (Creating an RDD of product IDs):**
        ```python
        # from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName("ParallelizeExample").getOrCreate()
        sc = spark.sparkContext

        product_ids_list = 
        product_ids_rdd = sc.parallelize(product_ids_list, 4) # Create RDD with 4 partitions

        print(f"Number of partitions: {product_ids_rdd.getNumPartitions()}")
        print(f"First 5 product IDs: {product_ids_rdd.take(5)}")
        spark.stop()
        ```

2.  **`sc.textFile(path, minPartitions=None)`:**
    -   **Purpose:** Reads a text file (or multiple files from a directory) from HDFS, a local file system, or any Hadoop-supported file system URI, and returns it as an RDD of strings (each string is a line).
    -   **`path`**: Path to the text file(s). Can use wildcards (e.g., `input/*.txt`).
    -   **`minPartitions`**: A suggestion for the minimum number of partitions.
    -   **Example (Reading product reviews from a text file):**
        ```python
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName("TextFileExample").getOrCreate()
        sc = spark.sparkContext

        # Assume 'product_reviews.txt' exists in HDFS or locally accessible path
        # For local testing, you might use: file_path = "file:///path/to/your/product_reviews.txt"
        file_path = "product_reviews.txt" # Assuming it's in the working directory or HDFS home
        try:
            reviews_rdd = sc.textFile(file_path, 2) # Suggest 2 partitions
            print(f"Number of lines (reviews): {reviews_rdd.count()}") # count() is an action
            print(f"First review: {reviews_rdd.first()}") # first() is an action
        except Exception as e:
            print(f"Could not read file (ensure it exists and path is correct): {e}")
        #     # Create a dummy RDD if file reading fails for example continuation
            dummy_reviews = ["great product", "bad quality", "love it"]
            reviews_rdd = sc.parallelize(dummy_reviews)


        spark.stop()
        ```

## Common RDD Transformations (Lazy)
Transformations create new RDDs from existing ones.

[list2tab|#RDD Transformations]
- map(func)
    -   Applies a function `func` to each element of the RDD, returning a new RDD of the results.
    -   **Example (Extracting price from a product string RDD):**
        ```python
        product_data_rdd = sc.parallelize(["ProductA:19.99", "ProductB:25.50"])
        prices_rdd = product_data_rdd.map(lambda line: float(line.split(":")))
        print(f"Extracted prices: {prices_rdd.collect()}") # [19.99, 25.5]
        ```
- filter(func)
    -   Returns a new RDD containing only the elements for which `func` returns `True`.
    -   **Example (Filtering for expensive products):**
        ```python
        prices_rdd = sc.parallelize() # From previous example
        expensive_prices_rdd = prices_rdd.filter(lambda price: price > 20.0)
        print(f"Expensive prices: {expensive_prices_rdd.collect()}") # [25.5]
        ```
- flatMap(func)
    -   Similar to `map`, but each input item can be mapped to 0 or more output items (func should return a sequence). The resulting sequences are then flattened.
    -   **Example (Splitting product review lines into words):**
        ```python
        reviews_rdd = sc.parallelize(["good product", "great service fast"])
        words_rdd = reviews_rdd.flatMap(lambda line: line.lower().split(" "))
        print(f"Words: {words_rdd.collect()}") # ['good', 'product', 'great', 'service', 'fast']
        ```
- distinct()
    -   Returns a new RDD containing the distinct elements of the source RDD. Involves a shuffle.
- union(otherRDD)
    -   Returns a new RDD containing all elements from both RDDs (duplicates included).
- intersection(otherRDD)
    -   Returns a new RDD containing only elements present in both RDDs. Involves a shuffle.
- subtract(otherRDD)
    -   Returns a new RDD with elements from the first RDD that are not in the second RDD. Involves a shuffle.
- groupByKey()
    -   For RDDs of key-value pairs `(K, V)`, groups all values for each key into a single sequence. Returns an RDD of `(K, Iterable<V>)`. Involves a shuffle. **Often less efficient than `reduceByKey` or `aggregateByKey`** if aggregation is the goal, as it brings all values for a key to one reducer.
- reduceByKey(func, numPartitions=None)
    -   For RDDs of key-value pairs `(K, V)`, aggregates values for each key using an associative and commutative reduce function `func`. More efficient than `groupByKey().mapValues(...)` because it can perform partial aggregation on the map side (like a combiner). Involves a shuffle.
    -   **Example (Word count - reduce step):**
        ```python
        word_pairs_rdd = sc.parallelize([("product", 1), ("good", 1), ("product", 1)])
        word_counts_rdd = word_pairs_rdd.reduceByKey(lambda a, b: a + b)
        print(f"Word counts: {word_counts_rdd.collect()}") # [('product', 2), ('good', 1)]
        ```
- sortByKey(ascending=True, numPartitions=None)
    -   Sorts an RDD of key-value pairs by key. Involves a shuffle.
- join(otherRDD, numPartitions=None)
    -   For RDDs of key-value pairs `(K, V)` and `(K, W)`, returns an RDD of `(K, (V, W))` for keys present in both. Different join types (`leftOuterJoin`, `rightOuterJoin`, `fullOuterJoin`) are also available. Involves a shuffle.

## Common RDD Actions (Trigger Execution)
Actions return values to the driver or write to storage.

[list2tab|#RDD Actions]
- collect()
    -   Returns all elements of the RDD as a list to the driver program. **Use with extreme caution on large RDDs.**
- count()
    -   Returns the number of elements in the RDD.
- first()
    -   Returns the first element of the RDD.
- take(n)
    -   Returns the first $n$ elements of the RDD as a list.
- reduce(func)
    -   Aggregates all elements of the RDD using `func` (must be commutative and associative).
- foreach(func)
    -   Applies a function `func` to each element of the RDD (usually for side effects, like saving to a database).
- saveAsTextFile(path)
    -   Saves the RDD content as text files in a directory (one file per partition).

## Shared Variables
-   **[[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables (`sc.broadcast(value)`)]]:**
    -   Used to efficiently send a large, read-only variable (e.g., a lookup table, a machine learning model) to all worker nodes.
    -   The variable is sent to each executor only once and cached, rather than being sent with every task. Tasks access it via `broadcast_var.value`.
    -   **Example (Broadcasting a product category mapping):**
        ```python
        category_map = {"P101": "Electronics", "P203": "Books", "P305": "Clothing"}
        broadcast_category_map = sc.broadcast(category_map)

        product_rdd = sc.parallelize([("P101", "Laptop"), ("P203", "Novel")])
        def map_category(item):
            prod_id, prod_name = item
            cat_map_value = broadcast_category_map.value # Access broadcasted value
            category = cat_map_value.get(prod_id, "Unknown")
            return (prod_id, prod_name, category)
        
        categorized_rdd = product_rdd.map(map_category)
        print(f"Categorized products: {categorized_rdd.collect()}")
        ```
-   **[[PySpark_Broadcast_Variables_Accumulators|Accumulators (`sc.accumulator(initial_value)`)]]:**
    -   Variables that are only "added" to through an associative and commutative operation and can therefore be efficiently supported in parallel.
    -   Used for implementing counters (e.g., number of bad records) or sums that are updated by tasks running on executors. The driver can then read their final value.
    -   Only the driver can read the accumulator's value, not tasks. Tasks can only add to it.
    -   **Example (Counting lines with errors):**
        ```python
        error_counter = sc.accumulator(0) # Initialize with 0

        data_rdd = sc.parallelize(["line1", "error_line_2", "line3", "error_line_4"])
        def process_line(line):
            global error_counter # Make sure to use global for accumulators in functions
            if "error" in line:
                error_counter += 1
                return False # Filter out error lines
            return True
        
        valid_lines_rdd = data_rdd.filter(process_line)
        valid_lines_rdd.count() # Action to trigger processing and accumulator updates
        print(f"Number of error lines: {error_counter.value}")
        ```

While the DataFrame API is generally preferred for structured data, a solid understanding of RDDs and their operations is beneficial for advanced Spark programming and for situations where RDDs offer more flexibility.

---