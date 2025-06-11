---
tags:
  - spark
  - pyspark
  - broadcast_variable
  - accumulator
  - shared_variables
  - performance
  - optimization
  - concept
  - example
aliases:
  - Spark Broadcast Variables
  - Spark Accumulators
  - PySpark Shared Variables
related:
  - "[[PySpark_RDD_Operations]]"
  - "[[Spark_Cluster_Architecture]]"
  - "[[Spark_Performance_Tuning]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# PySpark: Broadcast Variables and Accumulators

In Apache Spark, tasks running on [[Spark_Cluster_Architecture|executors]] operate on data in a distributed manner. By default, any variables used within task closures (e.g., functions passed to `map` or `filter`) are copied to each task. For large variables, this can be inefficient. Spark provides two types of shared variables for more optimized patterns: **broadcast variables** and **accumulators**.

These are typically created and managed via the `SparkContext` (accessible as `spark.sparkContext` if you have a `SparkSession`).

## Broadcast Variables (`sc.broadcast(value)`)

-   **Purpose:** To efficiently distribute a large, **read-only** variable to all worker nodes (executors) in the cluster.
-   **Mechanism:**
    1.  The driver program creates a broadcast variable from a local variable `v`.
    2.  Spark serializes `v` and sends it to each executor only **once**.
    3.  Tasks running on an executor can then access the value of the broadcast variable from a local cache on that executor, rather than having `v` shipped with every task closure.
-   **Advantages:**
    -   **Reduces Network Overhead:** Significantly reduces communication costs compared to shipping the variable with each task, especially if the variable is large and used by many tasks.
    -   **Reduces Driver Memory Pressure:** The driver doesn't need to manage sending large data repeatedly.
-   **When to Use:**
    -   Distributing large lookup tables, machine learning models, configuration data, or any relatively large, read-only dataset that needs to be accessed by all tasks.
    -   Commonly used to implement efficient [[Spark_Join_Strategies|broadcast joins]] where a small DataFrame is broadcasted to be joined with a large DataFrame.
-   **Accessing the Value:** Tasks access the value of a broadcast variable using its `.value` attribute.
-   **Immutability:** Broadcast variables are read-only on the executors.

**Example (Broadcasting a product category mapping for enrichment):**
```python
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("BroadcastDemo").getOrCreate()
# sc = spark.sparkContext

# Conceptual small lookup table: product_id -> category_name
# In a real scenario, this might come from a file or another DataFrame collected to the driver
product_category_lookup = {
    "P101": "Electronics",
    "P203": "Books",
    "P305": "Apparel",
    "P407": "Home Goods"
}

# Create a broadcast variable for the lookup table
broadcast_categories = sc.broadcast(product_category_lookup)

# Conceptual RDD of orders: (order_id, product_id, quantity)
orders_data = [("O1", "P101", 2), ("O2", "P305", 1), ("O3", "P101", 5), ("O4", "P999", 3)] # P999 is unknown
orders_rdd = sc.parallelize(orders_data)

# Function to enrich order data with category using the broadcast variable
def add_category_to_order(order_tuple):
    order_id, product_id, quantity = order_tuple
    # Access the broadcasted dictionary using .value
    categories = broadcast_categories.value
    category_name = categories.get(product_id, "Unknown Category") # Default if not found
    return (order_id, product_id, quantity, category_name)

# enriched_orders_rdd = orders_rdd.map(add_category_to_order)
# print("Enriched Orders with Categories:")
# for record in enriched_orders_rdd.collect():
#     print(record)
# Output might be:
# ('O1', 'P101', 2, 'Electronics')
# ('O2', 'P305', 1, 'Apparel')
# ('O3', 'P101', 5, 'Electronics')
# ('O4', 'P999', 3, 'Unknown Category')

# spark.stop()
```

## Accumulators (`sc.accumulator(initial_value)` or `sc.collectionAccumulator()`)

-   **Purpose:** Variables that are only "added" to through an associative and commutative operation. They are used to implement distributed counters (e.g., for errors, processed records) or sums that are updated by tasks running on executors.
-   **Mechanism:**
    1.  The driver program creates an accumulator with an initial value.
    2.  Tasks running on executors can increment (add to) the accumulator. Spark ensures these updates are aggregated correctly across all tasks.
    3.  **Only the driver program can read the accumulator's final value** using its `.value` attribute. Tasks on executors cannot read the accumulator's current value during computation (this prevents race conditions and ensures efficient aggregation).
-   **Types:**
    -   **Numeric Accumulators (`sc.accumulator(value)`):** For summing numbers (int, float).
    -   **Collection Accumulators (`sc.collectionAccumulator()`):** For collecting elements into a list (less common, use with care for memory).
    -   Custom accumulators can also be created by subclassing `AccumulatorParam`.
-   **Advantages:**
    -   Provides a way to aggregate global information (like counts or sums) from distributed tasks efficiently and reliably.
    -   Useful for debugging and monitoring job progress (e.g., counting malformed records).
-   **Fault Tolerance:** Spark can correctly handle accumulator updates even if tasks are re-executed due to failures (updates from failed task attempts are not applied).

**Example (Counting malformed product review lines):**
```python
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("AccumulatorDemo").getOrCreate()
# sc = spark.sparkContext

# Initialize an accumulator for counting malformed lines
# malformed_lines_counter = sc.accumulator(0)

# Conceptual RDD of product review lines
# review_lines_data = [
#     "product_id|rating|comment", # Header (potentially malformed if treated as data)
#     "P101|5|Great product!",
#     "P203|4|Good value.",
#     "P305-missing-pipe-3-Bad", # Malformed line
#     "P407|5|Excellent quality."
# ]
# review_lines_rdd = sc.parallelize(review_lines_data)

# Function to process lines and update accumulator
def validate_and_process_review(line):
    # global malformed_lines_counter # Necessary if function is defined outside task scope in some contexts
    parts = line.split('|')
    if len(parts) == 3:
        try:
            # Attempt to parse, e.g., rating = int(parts)
            return {"product_id": parts, "rating": int(parts), "comment": parts}
        except ValueError:
            malformed_lines_counter.add(1) # Increment accumulator
            return None # Or some indicator of bad record
    else:
        # For the header or other malformed lines
        if line != "product_id|rating|comment": # Don't count header as malformed
             malformed_lines_counter.add(1)
        return None

# Process RDD (filter out None which indicates malformed or header)
# processed_reviews_rdd = review_lines_rdd.map(validate_and_process_review).filter(lambda x: x is not None)

# An action is needed to trigger computations and accumulator updates
# print(f"Number of valid processed reviews: {processed_reviews_rdd.count()}")
# print(f"Total malformed lines detected: {malformed_lines_counter.value}") # Read value in driver

# spark.stop()
```

**Important Notes for Accumulators:**
-   Updates to accumulators inside transformations are only guaranteed to be executed once for each input record *if that transformation is part of an action that completes successfully*. If a stage is recomputed due to failure, accumulators might be updated multiple times for the same data unless care is taken.
-   They are primarily for side effects like debugging or simple counts/sums. For more complex aggregations, RDD/DataFrame aggregate operations are preferred.

Broadcast variables and accumulators are specialized tools in Spark for managing shared data and aggregating results in a distributed environment efficiently.

---