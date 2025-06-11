## **Questions**

**1. What is the difference between Hadoop and Spark?**

- **Hadoop:** Primarily a distributed storage system (HDFS) and a batch processing framework (MapReduce v1). It's disk-based, making it slower for iterative tasks.
    
- **Spark:** A general-purpose, in-memory distributed processing framework. It's much faster than Hadoop MapReduce for many workloads, especially iterative algorithms and interactive queries, due to its in-memory processing and more flexible computation model. Spark can run on top of HDFS or other storage systems.
    
- **What is the difference between MapReduce and Spark?**
    
    - **MapReduce (Hadoop):** A rigid, two-stage (Map then Reduce) programming model, heavily reliant on disk I/O between stages.
        
    - **Spark:** Offers a more flexible and general computation model using DAGs, allowing for multiple stages and efficient in-memory data sharing between them, significantly reducing disk I/O. It supports a wider range of operations beyond just map and reduce.
        

**2. Why do we need Spark? Can't we just easily read files/databases directly?**  
While you can read files/databases directly with standard tools, Spark is needed for:

- **Scalability for Big Data:** Processing datasets that are too large to fit or be processed efficiently on a single machine. Spark distributes the data and computation across a cluster.
    
- **Performance:** Its in-memory processing and optimized execution engine (Catalyst, Tungsten) make it much faster than traditional disk-based approaches (like Hadoop MapReduce) for many analytical workloads.
    
- **Fault Tolerance:** It handles node failures gracefully by recomputing lost partitions of data using lineage information.
    
- **Unified Analytics Engine:** Spark provides APIs for batch processing, SQL queries (Spark SQL), stream processing (Structured Streaming), machine learning (MLlib), and graph processing (GraphFrames), all within one framework.
    

**3. What is a Spark Context?**  
The SparkContext (often abbreviated sc) is the main entry point for Spark's core RDD-based functionality. It represents the connection to a Spark cluster and is used to create RDDs, accumulators, and broadcast variables, and to submit jobs to the cluster.

**4. What is the difference between a Session and a Context?**

- **SparkContext (sc):** The older entry point, primarily for RDDs. It manages the connection to the cluster and coordinates job execution.
    
- **SparkSession (spark):** Introduced in Spark 2.0, it's the unified entry point for DataFrame and Dataset APIs. It encapsulates a SparkContext (accessible via spark.sparkContext) and also provides access to Spark SQL, Hive integration, and streaming capabilities. For new applications, SparkSession is the recommended entry point.
    

**5. What is the purpose of a Spark Cluster?**  
The purpose of a Spark Cluster is to enable **distributed and parallel processing of large datasets**. It pools the CPU, memory, and sometimes disk resources of multiple machines (nodes) to execute Spark applications much faster and handle data volumes that a single machine cannot.

**6. For each ofนอก the following modules/classes, explain what is its purpose and its advantages:**

- **RDD (Resilient Distributed Dataset):**
    
    - **Purpose:** Spark's foundational, low-level abstraction for distributed data. Represents an immutable, partitioned collection of records that can be operated on in parallel.
        
    - **Advantages:** Fault tolerance (recomputable via lineage), control over data partitioning and persistence, good for unstructured data or when fine-grained control over execution is needed.
        
- **DataFrame and SQL:**
    
    - **Purpose:** Provides a higher-level, structured data abstraction (like tables) with named columns. Allows SQL queries and a rich set of domain-specific language (DSL) operations.
        
    - **Advantages:** Easier to use for structured/semi-structured data, significant performance optimizations via Catalyst optimizer and Tungsten execution engine, schema enforcement, interoperability with various data sources.
        
- **Streaming (Structured Streaming & older Spark Streaming):**
    
    - **Purpose:** Enables processing of live data streams in near real-time. Structured Streaming treats data streams as continuously appended tables.
        
    - **Advantages:** Fault tolerance for stream processing, exactly-once processing semantics (Structured Streaming), integration with batch processing code, high throughput.
        
- **MLlib (Machine Learning Library):**
    
    - **Purpose:** Spark's built-in library for scalable machine learning. Provides common learning algorithms and utilities.
        
    - **Advantages:** Can train models on very large datasets distributed across the cluster, includes algorithms for classification, regression, clustering, collaborative filtering, and feature engineering tools.
        
- **GraphFrames (and older GraphX for RDDs):**
    
    - **Purpose:** Provides APIs for graph analytics and parallel graph computations. GraphFrames are built on DataFrames.
        
    - **Advantages:** Enables scalable analysis of graph-structured data (e.g., social networks, web graphs), provides common graph algorithms like PageRank, connected components, shortest paths.
        
- **Resource (Cluster Manager):**
    
    - **Purpose:** Not a Spark module itself, but what Spark relies on (YARN, Mesos, Kubernetes, Standalone) to acquire and manage cluster resources (CPU, memory) for its driver and executors.
        
    - **Advantages:** Allows Spark to run in diverse environments, share cluster resources with other applications (e.g., in YARN), and scale dynamically.
        

**7. What is the difference between a Spark DataFrame and a Pandas DataFrame?**

- **Distribution:** Spark DataFrames are **distributed** across multiple nodes in a cluster. Pandas DataFrames reside **in memory on a single machine**.
    
- **Scalability:** Spark DataFrames can handle datasets much larger than a single machine's memory. Pandas DataFrames are limited by the memory of the machine they run on.
    
- **Execution:** Spark operations are **lazily evaluated** and executed in parallel across the cluster. Pandas operations are generally **eagerly evaluated** and run on a single core (unless using libraries like Dask).
    
- **API:** While both offer similar tabular data manipulation functionalities, their APIs have differences. PySpark's DataFrame API is designed for distributed computation and has its own set of transformations and actions.
    
- **Immutability:** Spark DataFrames are immutable (transformations create new DataFrames). Pandas DataFrames can be modified in-place (though it's often discouraged).
    

**8. What are the Spark data sources?**  
Spark can read from and write to a wide variety of data sources, including:

- **File Systems:** HDFS, local file system, Amazon S3, Azure Blob Storage, Google Cloud Storage.
    
- **File Formats:** CSV, JSON, Parquet, ORC, Avro, text files, SequenceFiles.
    
- **Databases:** Relational databases via JDBC (e.g., MySQL, PostgreSQL, SQL Server, Oracle).
    
- **NoSQL Databases:** HBase, Cassandra, MongoDB, Elasticsearch.
    
- **Message Queues:** Apache Kafka (for streaming).
    
- **Hive Tables.**
    

**9. What is the difference between a transformation and an action?**

- **Transformation:** An operation on an RDD or DataFrame that produces a new RDD or DataFrame (e.g., map, filter, select, groupBy). Transformations are **lazily evaluated**; they define a part of the computation DAG but don't execute until an action is called.
    
- **Action:** An operation that triggers the execution of all previously defined transformations to compute a result and either return it to the driver program or save it to an external storage system (e.g., count, collect, take, save, show).
    

**10. What are the advantages of laziness (lazy execution)?**

- **Optimization:** Spark can analyze the entire DAG of transformations before execution and apply optimizations like pipelining operations, reordering them, or choosing efficient join strategies (Catalyst optimizer).
    
- **Reduced Computation:** Only necessary computations are performed. If data is filtered early, subsequent operations work on a smaller dataset.
    
- **Efficiency:** Avoids materializing intermediate datasets in memory or on disk unless explicitly required, saving resources.
    

**11. When is a shuffle operation needed?**  
A shuffle operation is needed when data from different partitions needs to be redistributed across the cluster to group related data together on the same partition. This typically occurs during **wide transformations**, such as:

- groupByKey(), reduceByKey(), aggregateByKey()
    
- join() (when data is not already co-partitioned or one table cannot be broadcast)
    
- distinct()
    
- repartition(), coalesce() (if increasing partitions or changing partitioning scheme)
    
- Sorting operations like orderBy() or sortByKey().  
    Shuffles are expensive as they involve network I/O and disk I/O.
    

**12. Explain explain()**  
The explain(extended=False) method on a Spark DataFrame displays the **logical and physical execution plans** that Spark's Catalyst optimizer has generated for the sequence of transformations leading to that DataFrame.

- **Logical Plan:** A high-level, abstract representation of the computation, showing unresolved attributes and operations.
    
- **Analyzed Logical Plan:** The logical plan after attributes have been resolved against the schema.
    
- **Optimized Logical Plan:** The logical plan after various rule-based and cost-based optimizations have been applied by Catalyst.
    
- **Physical Plan:** The actual sequence of operations (RDD transformations) that Spark will execute on the cluster. It details how data will be moved, joined, and processed.  
    Using explain(extended=True) provides more detailed information. It's a crucial tool for understanding and debugging Spark query performance.
    

**13. What is the importance of repartition()?**  
repartition(numPartitions) is a transformation that reshuffles the data in a DataFrame or RDD to create a new DataFrame/RDD with a specified numPartitions.

- **Importance:**
    
    - **Controlling Parallelism:** Can increase or decrease the number of partitions to better match the available cluster resources (cores) and improve parallelism.
        
    - **Data Skew:** Can help mitigate data skew by redistributing data more evenly if some partitions are much larger than others.
        
    - **Performance Tuning:** The number of partitions affects task granularity. Too few partitions lead to underutilized cores; too many can lead to excessive overhead.
        
    - **Preparing for Joins/Aggregations:** Repartitioning by a key before a join or aggregation can sometimes improve performance by ensuring related data is on the same partition, though Spark often handles this.
        
- repartition() always incurs a full shuffle. coalesce(numPartitions) is a more optimized way to decrease the number of partitions and tries to avoid a full shuffle if possible by combining existing partitions.
    

**14. Describe a use case for map and another for mapPartitions.**

- **map(func):**
    
    - **Use Case:** Applying a simple transformation to each individual element of an RDD or each row of a DataFrame. For example, converting all words in an RDD of strings to uppercase, or extracting a specific field from each JSON object in an RDD.
        
    - rdd_strings = sc.parallelize(["hello", "world"])
        
    - rdd_upper = rdd_strings.map(lambda s: s.upper())
        
    - **How it works:** The function func is applied to every single element independently.
        
- **mapPartitions(func):**
    
    - **Use Case:** When you need to perform an expensive setup (e.g., initializing a database connection, loading a large model) once per partition rather than once per element. The function func receives an iterator for all elements within a partition and should return an iterator of results.
        
    - def process_partition(iterator):  
        db_connection = connect_to_db() # Expensive setup  
        results = []  
        for record in iterator:  
        results.append(db_connection.query(record))  
        db_connection.close()  
        return iter(results)
        
    - processed_rdd = data_rdd.mapPartitions(process_partition)
        
    - **How it works:** The function func is called once for each partition, receiving all elements of that partition as an iterator. This is more efficient if the setup cost is high relative to per-element processing.
        

**15. Is there a parallel for SQL constraints in Spark? What about indexes? If yes - what is it? If no - why?**

- **SQL Constraints (e.g., PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL):**
    
    - **No, Spark DataFrames do not enforce these constraints in the same way relational databases do.** Spark is designed for large-scale, often read-heavy analytics and ETL. Enforcing constraints during writes across a distributed system would be very expensive and slow down ingestion significantly.
        
    - You can validate data against such rules (e.g., check for nulls, count distinct values to check uniqueness) as part of your Spark jobs, but Spark won't automatically reject data that violates them. Data quality checks are typically a separate step.
        
- **Indexes:**
    
    - **No, Spark DataFrames do not have traditional B-tree or hash indexes like relational databases.** Indexes are primarily for speeding up point lookups or small range scans, which is not the typical access pattern for Spark's full-scan analytical workloads.
        
    - **Alternatives for performance:**
        
        - **Partitioning (Data Skipping):** Data can be physically partitioned on disk by certain column values (e.g., by date). When querying with a filter on that partition column, Spark can skip reading irrelevant partitions, which acts like a coarse-grained index.
            
        - **Bucketing (Data Skipping & Join Optimization):** Data can be bucketed (hashed into a fixed number of buckets) by a column. This can help with join performance if tables are bucketed on the join key and can also provide some data skipping.
            
        - **Columnar File Formats (e.g., Parquet, ORC):** These formats store data by column and often include metadata (min/max values per column chunk) that allows Spark to skip reading entire row groups if they don't satisfy query predicates (predicate pushdown). This is a form of data skipping.
            
        - **Data Caching (.cache(), .persist()):** Caching frequently accessed DataFrames in memory can significantly speed up subsequent queries.
            

**16. Why and when are lit() and col() useful?**  
From pyspark.sql.functions:

- **lit(literalValue):**
    
    - **Why/When:** Used to create a Spark Column object from a literal (constant) value. This is necessary when you want to add a new column with a fixed value to a DataFrame, or use a constant in an expression where a Column object is expected.
        
    - from pyspark.sql.functions import lit
        
    - df_with_literal = df.withColumn("status", lit("active"))
        
    - df_filtered = df.filter(col("age") > lit(18))
        
- **col(colName) (or df["colName"] or df.colName):**
    
    - **Why/When:** Used to refer to an existing column in a DataFrame by its name and return it as a Column object. This is essential for most DataFrame transformations and expressions where you operate on columns.
        
    - from pyspark.sql.functions import col
        
    - selected_df = df.select(col("name"), col("age"))
        
    - df_transformed = df.withColumn("age_plus_5", col("age") + 5)
        

**17. What is the difference between parquet files and csv files?**

- **CSV (Comma Separated Values):**
    
    - **Format:** Plain text, row-oriented. Each line is a record, values separated by delimiters (usually commas).
        
    - **Schema:** No schema embedded; schema must be inferred or supplied during reading.
        
    - **Compression:** Not inherently compressed, though can be gzipped.
        
    - **Performance:** Slower to read for analytical queries because entire rows must be read even if only a few columns are needed. No support for predicate pushdown within the file itself.
        
- **Parquet:**
    
    - **Format:** Binary, **columnar** storage format. Data for each column is stored together.
        
    - **Schema:** Schema is embedded within the file, making it self-describing.
        
    - **Compression:** Excellent compression ratios due to columnar storage (similar data types together compress well) and various compression codecs (snappy, gzip, lzo).
        
    - **Performance:** Significantly faster for analytical queries that select a subset of columns (only needed columns are read). Supports predicate pushdown (skipping row groups based on filter conditions using metadata).
        
- **Key takeaway:** Parquet is highly optimized for analytical workloads in distributed systems like Spark due to its columnar nature, schema embedding, and compression. CSV is simpler but less efficient for big data analytics.
    

**18. Can we read data directly from a JSON file using Spark? How? Why would we do that?**

- **Yes, Spark can read data directly from JSON files.**
    
- **How:**
```
# For line-delimited JSON (one JSON object per line - most common for Spark)
df_json = spark.read.json("path/to/your/data.json")

# For multi-line JSON (a single JSON array or object spanning multiple lines)
# df_json_multiline = spark.read.option("multiline", "true").json("path/to/your/multiline_data.json")
```

- Spark will attempt to infer the schema from the JSON structure. You can also provide an explicit schema.
    
- **Why would we do that?**
    
    - **Common Data Format:** JSON is a very common format for web APIs, configuration files, and semi-structured data logging.
        
    - **Flexibility:** JSON's flexible schema is well-suited for evolving data or data with nested structures.
        
    - **Ease of Use:** Spark's built-in JSON reader makes it straightforward to ingest this data into DataFrames for analysis, transformation, or further processing.
        
    - **Semi-structured Data Analysis:** Allows you to query and analyze data that doesn't fit neatly into rigid relational tables.
Understood! We'll prioritize Docker for Spark setup and `uv` for Python package management within our Spark environment if needed (though for PySpark, the core dependencies are usually handled by the Spark installation itself, and `uv` would be more for additional libraries your Python UDFs or driver script might need).

---
**Exercise 1: Install Spark and run a worker on your machine**
---

*   **Goal:** Get a basic Spark standalone cluster running locally using Docker. This will involve a Spark master container and one Spark worker container.
*   **Docker Approach:** We'll use Docker Compose for this to manage the master and worker services.

**Step-by-Step (using Docker Compose):**

1.  **Choose a Spark Docker Image:**
    *   Bitnami provides well-maintained Spark images: `bitnami/spark`
    *   You can also find official (though sometimes more complex to configure) images or build your own. Let's aim for a Bitnami image for simplicity.

2.  **Create `docker-compose.yml` for Spark Standalone Cluster:**
    Create a file named `docker-compose.yml` in a new directory for this exercise.

    ```yaml
    version: '3.8'

    services:
      spark-master:
        image: bitnami/spark:3.5 # Use a recent Spark 3.x version
        container_name: spark-master
        hostname: spark-master
        environment:
          - SPARK_MODE=master
          - SPARK_RPC_AUTHENTICATION_ENABLED=no
          - SPARK_RPC_ENCRYPTION_ENABLED=no
          - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
          - SPARK_SSL_ENABLED=no
          # - SPARK_MASTER_HOST=spark-master # Often inferred, but can be explicit
          # - SPARK_MASTER_PORT=7077 # Default
          # - SPARK_MASTER_WEBUI_PORT=8080 # Default
        ports:
          - "8080:8080"  # Master Web UI
          - "7077:7077"  # Master RPC port for workers to connect
        networks:
          - spark_network

      spark-worker-1:
        image: bitnami/spark:3.5
        container_name: spark-worker-1
        hostname: spark-worker-1
        depends_on:
          - spark-master
        environment:
          - SPARK_MODE=worker
          - SPARK_MASTER_URL=spark://spark-master:7077 # Tells worker where the master is
          - SPARK_WORKER_CORES=1 # Adjust as needed for your machine
          - SPARK_WORKER_MEMORY=1g # Adjust as needed
          # - SPARK_WORKER_WEBUI_PORT=8081 # Default
          - SPARK_RPC_AUTHENTICATION_ENABLED=no
          - SPARK_RPC_ENCRYPTION_ENABLED=no
          - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
          - SPARK_SSL_ENABLED=no
        ports:
          - "8081:8081" # Worker 1 Web UI
        networks:
          - spark_network
        # You can add more workers by copying this service block and changing names/ports

    networks:
      spark_network:
        driver: bridge
    ```
    *   **Notes on Environment Variables:** The Bitnami Spark image uses these environment variables to configure Spark. Disabling authentication/encryption simplifies local setup.
    *   `SPARK_MASTER_URL=spark://spark-master:7077`: This is crucial for the worker to find the master. `spark-master` is the service name defined in this compose file.

3.  **Start the Spark Standalone Cluster:**
    In the directory containing your `docker-compose.yml`:
    ```bash
    docker-compose up -d
    ```

4.  **Verify the Cluster:**
    *   **Check Docker Containers:**
        ```bash
        docker ps
        ```
        You should see `spark-master` and `spark-worker-1` running.
    *   **Spark Master Web UI:** Open your browser and go to `http://localhost:8080`.
        *   You should see the Spark Master page.
        *   Under "Workers", you should see one worker listed (it might take a few seconds to register). It will show its ID, address, state (ALIVE), cores, and memory.
    *   **Spark Worker Web UI:** Open `http://localhost:8081`.
        *   You'll see details for that specific worker.

5.  **Running a Simple PySpark Application (to confirm connectivity):**
    We need a way to submit a PySpark job. The easiest way for now is to run `pyspark` shell from *within* one of the containers (e.g., the master, or you could add a dedicated "spark-client" service to your compose file).

    *   **Option A: Run PySpark shell from the master container:**
        ```bash
        docker exec -it spark-master bash
        ```
        Inside the container:
        ```bash
        # The Bitnami image should have pyspark in the PATH
        # Connect to the standalone master
        pyspark --master spark://spark-master:7077
        ```
        Once the PySpark shell starts, try a simple command:
        ```python
        # Inside PySpark shell
        data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
        rdd = sc.parallelize(data)
        print(rdd.count())
        # Expected output: 3
        rdd.collect()
        # Expected output: [('Alice', 1), ('Bob', 2), ('Charlie', 3)]
        spark.stop() # or sc.stop() then exit()
        ```
        When you run `rdd.count()`, go back to the Spark Master Web UI (`http://localhost:8080`). You should see a "Running Application" or "Completed Application" briefly. This confirms your PySpark shell connected to the master, and the master used the worker to perform the computation.

    *   **Option B: Submit a Python script using `spark-submit` (more realistic):**
        1.  Create a simple Python script on your host machine, e.g., `test_spark.py`:
            ```python
            # test_spark.py
            from pyspark.sql import SparkSession

            # When submitting to a standalone cluster, the master URL is given
            # via --master in spark-submit, so we don't strictly need it here,
            # but it's good practice for local testing if running script directly.
            spark = SparkSession.builder \
                .appName("TestSparkApp") \
                .getOrCreate() # Master will be picked from spark-submit

            data = [("Alice", 1), ("Bob", 2), ("Charlie", 3), ("David", 4), ("Eve", 5)]
            df = spark.createDataFrame(data, ["Name", "ID"])

            print(f"DataFrame count: {df.count()}")
            df.show()

            spark.stop()
            ```
        2.  Copy this script into the `spark-master` container (or mount a volume in `docker-compose.yml` for your scripts).
            ```bash
            # On your host
            docker cp test_spark.py spark-master:/tmp/
            ```
        3.  Execute `spark-submit` from inside the `spark-master` container:
            ```bash
            docker exec -it spark-master bash
            ```
            Inside the container:
            ```bash
            $SPARK_HOME/bin/spark-submit \
              --master spark://spark-master:7077 \
              /tmp/test_spark.py
            ```
            You should see the output of the print statement and `df.show()`. Again, check the Master UI for application activity.

You now have a basic Spark standalone cluster with one master and one worker running via Docker!

---
**Exercise 2: Using Spark, inspect the Bank Marketing dataset**
---

*   **Goal:** Load a dataset into a Spark DataFrame and perform basic exploratory data analysis (EDA).
*   **Dataset:** Bank Marketing Dataset. You can find this on the UCI Machine Learning Repository or Kaggle. A common version is `bank-full.csv` or `bank.csv`. It typically has a semicolon (`;`) as a delimiter.
    *   Download it and make it accessible to your Spark cluster (e.g., copy it into the `spark-master` container or mount a volume).

**Step-by-Step:**

1.  **Get the Dataset:**
    *   Download `bank-full.csv` (or a similar version). Let's assume you download it to your current host directory where `docker-compose.yml` is.

2.  **Make Dataset Accessible to Spark:**
    The easiest way is to copy it into the running `spark-master` container.
    ```bash
    # On your host machine
    docker cp bank-full.csv spark-master:/tmp/bank-full.csv
    ```
    (Alternatively, you could add a volume mount to your `docker-compose.yml` for the `spark-master` service to map a local data directory into the container, e.g., `- ./data:/data_in_container`)

3.  **Start a PySpark Shell or Use `spark-submit`:**
    For interactive exploration, the PySpark shell is convenient.
    ```bash
    docker exec -it spark-master bash
    ```
    Inside the container:
    ```bash
    pyspark --master spark://spark-master:7077
    ```

4.  **Load the Dataset (inside PySpark shell):**
    ```python
    # Inside PySpark shell
    from pyspark.sql.functions import col, when, count, desc, round, avg, min, max, isnan, isnull
    from pyspark.sql.types import IntegerType, FloatType, StringType, StructType, StructField

    # Define the schema - crucial for CSVs to get correct data types and avoid issues
    # Adjust column names and types based on your specific bank-full.csv version
    schema = StructType([
        StructField("age", IntegerType(), True),
        StructField("job", StringType(), True),
        StructField("marital", StringType(), True),
        StructField("education", StringType(), True),
        StructField("default", StringType(), True),
        StructField("balance", IntegerType(), True), # Often needs to be Integer or Float
        StructField("housing", StringType(), True),
        StructField("loan", StringType(), True),
        StructField("contact", StringType(), True),
        StructField("day", IntegerType(), True),
        StructField("month", StringType(), True),
        StructField("duration", IntegerType(), True),
        StructField("campaign", IntegerType(), True),
        StructField("pdays", IntegerType(), True),
        StructField("previous", IntegerType(), True),
        StructField("poutcome", StringType(), True),
        StructField("deposit", StringType(), True) # Target variable, often 'y' or 'yes'/'no'
    ])

    # Path to the CSV file inside the container
    file_path = "file:///tmp/bank-full.csv" # Use file:/// for local paths within the container

    # Read the CSV
    bank_df = spark.read.csv(file_path, header=True, sep=";", schema=schema)

    # Cache it for faster subsequent operations during EDA
    bank_df.cache()

    # Show a few rows and the schema to verify
    bank_df.show(5)
    bank_df.printSchema()
    print(f"Total rows in dataset: {bank_df.count()}")
    ```

5.  **Print 10 random rows from the dataset:**
    ```python
    bank_df.sample(withReplacement=False, fraction=0.001, seed=42).limit(10).show()
    # Adjust fraction if dataset is small to ensure you get ~10 rows.
    # Or more simply for a small sample:
    # bank_df.orderBy(rand()).limit(10).show() # rand() is from pyspark.sql.functions
    # For truly random sample without replacement (if dataset fits for a moment for takeSample)
    # bank_df.rdd.takeSample(False, 10, seed=42) # This returns a list of Row objects
    # For DataFrame output of random sample:
    sampled_rows = bank_df.take(100) # Take more than needed
    import random
    random.shuffle(sampled_rows)
    spark.createDataFrame(sampled_rows[:10], schema=bank_df.schema).show()
    # A more robust way for large datasets is often to add a random column and sort by it
    # from pyspark.sql.functions import rand
    # bank_df.orderBy(rand(seed=42)).limit(10).show()
    ```
    The `sample()` method is good. For just viewing, `orderBy(rand())` is often sufficient for a quick look.

6.  **What are the relative proportions of `no` and `yes` for the `deposit` feature? (inspect also other qualitative variables)**
    ```python
    # Proportions for 'deposit'
    deposit_counts = bank_df.groupBy("deposit").count()
    total_deposits = bank_df.count() # Recalculate or use the one from above
    deposit_proportions = deposit_counts.withColumn("proportion", round(col("count") / total_deposits, 4))
    print("Proportions for 'deposit':")
    deposit_proportions.show()

    # Function to inspect other qualitative variables
    def show_proportions(df, column_name):
        print(f"\nProportions for '{column_name}':")
        counts = df.groupBy(column_name).count().orderBy(desc("count"))
        total = df.count()
        proportions_df = counts.withColumn("proportion", round(col("count") / total, 4))
        proportions_df.show(truncate=False)

    qualitative_cols = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome"]
    for q_col in qualitative_cols:
        show_proportions(bank_df, q_col)
    ```

7.  **Get descriptive statistics for numerical variables:**
    ```python
    numerical_cols = ["age", "balance", "day", "duration", "campaign", "pdays", "previous"]
    print("\nDescriptive statistics for numerical variables:")
    bank_df.select(numerical_cols).describe().show(truncate=False)
    # describe() gives: count, mean, stddev, min, max
    ```

8.  **Use relevant visualizations to inspect variables and relations between them:**
    *   Direct plotting with PySpark is limited. Typically, you'd:
        *   Collect a sample of the data to the driver: `pandas_df = bank_df.sample(0.1).toPandas()`
        *   Then use Matplotlib/Seaborn on the Pandas DataFrame.
        *   Alternatively, use tools like Spark Koalas (now part of PySpark as `pyspark.pandas`) or integrate with BI tools.
    *   For this exercise, let's focus on what Spark can tell us, and *describe* the plots.

    *   **Distribution of `age` (Numerical):**
        *   Spark: You can approximate a histogram using `groupBy` on binned ages or use the RDD `histogram()` method if you convert a column to an RDD.
            ```python
            # Approximate histogram for age
            age_hist = bank_df.select("age").rdd.flatMap(lambda x: x).histogram(10) # 10 bins
            print("\nAge Histogram (bins, counts):")
            print(age_hist)
            # For better bucketing:
            # bank_df.select(F.floor(F.col("age")/10)*10).alias("age_bucket")).groupBy("age_bucket").count().orderBy("age_bucket").show()
            ```
        *   **Plot Type:** Histogram or Density Plot.
        *   **What to look for:** Skewness, central tendency, presence of multiple modes.

    *   **`balance` vs. `deposit` (Numerical vs. Categorical):**
        *   Spark: Group by `deposit` and calculate average/median balance.
            ```python
            print("\nBalance statistics by deposit status:")
            bank_df.groupBy("deposit").agg(
                avg("balance").alias("avg_balance"),
                expr("percentile_approx(balance, 0.5)").alias("median_balance"), # Median
                min("balance").alias("min_balance"),
                max("balance").alias("max_balance")
            ).show()
            ```
        *   **Plot Type:** Box plots of `balance` for each `deposit` category (`yes`/`no`).
        *   **What to look for:** Differences in distribution, median, spread, outliers.

    *   **`education` vs. `deposit` (Categorical vs. Categorical):**
        *   Spark: Create a contingency table (crosstab).
            ```python
            print("\nCrosstab: Education vs. Deposit:")
            bank_df.crosstab("education", "deposit").show(truncate=False)
            # To get proportions:
            # education_deposit_counts = bank_df.groupBy("education", "deposit").count()
            # windowSpec = Window.partitionBy("education")
            # education_deposit_props = education_deposit_counts.withColumn("proportion", col("count") / sum("count").over(windowSpec))
            # education_deposit_props.orderBy("education", "deposit").show()
            ```
        *   **Plot Type:** Grouped or Stacked Bar Chart.
        *   **What to look for:** If certain education levels have a higher proportion of 'yes' for deposit.

9.  **Answer the following questions (using PySpark):**

    *   **Who is the client with the biggest balance?**
        (Assuming there's an `id` column or we just show the row. The provided schema doesn't have a unique client ID, so we'll show the row with max balance.)
        ```python
        print("\nClient(s) with the biggest balance:")
        max_balance_val = bank_df.select(max("balance")).first()[0]
        bank_df.filter(col("balance") == max_balance_val).show(truncate=False)
        # Or, more directly if you only need one such row:
        # bank_df.orderBy(desc("balance")).limit(1).show(truncate=False)
        ```

    *   **What is the proportion of clients whose balance is more than twice the average?**
        ```python
        avg_balance_val = bank_df.select(avg("balance")).first()[0]
        print(f"\nAverage balance: {avg_balance_val}")
        threshold_balance = 2 * avg_balance_val
        print(f"Threshold balance (2 * avg): {threshold_balance}")

        count_above_threshold = bank_df.filter(col("balance") > threshold_balance).count()
        total_clients = bank_df.count() # Already calculated
        proportion_above_threshold = count_above_threshold / total_clients
        print(f"Proportion of clients with balance > 2 * average: {proportion_above_threshold:.4f}")
        ```

    *   **Do people with higher education have a better chance to deposit?**
        (We need to define "higher education" and then compare deposit rates. Let's assume 'tertiary' is higher than 'secondary', which is higher than 'primary'. 'unknown' is tricky.)
        ```python
        from pyspark.sql.window import Window
        from pyspark.sql.functions import sum as spark_sum # avoid conflict with Python's sum

        print("\nDeposit proportion by education level:")
        # Calculate counts for each education level and deposit status
        education_deposit_counts = bank_df.groupBy("education", "deposit").count()

        # Calculate total counts for each education level to find proportions
        window_spec_education = Window.partitionBy("education")
        education_deposit_proportions = education_deposit_counts.withColumn(
            "proportion_of_deposit_status_within_education",
            round(col("count") / spark_sum("count").over(window_spec_education), 4)
        )

        # Filter for 'yes' deposit and order
        education_deposit_proportions.filter(col("deposit") == "yes") \
            .select("education", "proportion_of_deposit_status_within_education") \
            .orderBy(desc("proportion_of_deposit_status_within_education")) \
            .show(truncate=False)

        # Interpretation: Look at the proportion of 'yes' for deposit within each education category.
        # A higher proportion for 'tertiary' would suggest a better chance.
        ```

    *   **What are the best predictors for deposit?**
        *   This is a machine learning question. With EDA, we can find strong correlations or associations, but "best predictors" usually implies building a predictive model (e.g., logistic regression, decision tree) and evaluating feature importance.
        *   **EDA approach:**
            *   **Correlation for numerical:** Calculate correlation between numerical features and a binarized `deposit` (0 for no, 1 for yes).
            *   **Chi-squared test for categorical:** For categorical features vs. `deposit`.
            *   **Visual inspection:** Grouped bar charts showing deposit rates for different categories of variables (like we did for education).

            ```python
            # Binarize 'deposit' for correlation
            df_with_deposit_numeric = bank_df.withColumn("deposit_numeric", when(col("deposit") == "yes", 1).otherwise(0))

            print("\nCorrelation with deposit_numeric (for numerical features):")
            for num_col in numerical_cols:
                try:
                    correlation = df_with_deposit_numeric.stat.corr("deposit_numeric", num_col)
                    print(f"Correlation between deposit_numeric and {num_col}: {correlation:.4f}")
                except Exception as e:
                    print(f"Could not calculate correlation for {num_col}: {e}") # e.g. if stddev is zero

            # For categorical, we've already looked at crosstabs and proportions.
            # 'duration' is often a very strong predictor, but it's known *after* the call,
            # so it's often removed if predicting *before* the call.
            # 'poutcome' (previous outcome) is also usually important if 'previous' > 0.
            ```
        *   **Conclusion from EDA:** Based on typical findings for this dataset: `duration` (if kept), `poutcome`, `month`, `contact`, `housing`, `loan` often show notable associations. `balance` and `age` can also play a role. A proper ML model would quantify this better.

Remember to stop your PySpark shell when done:
```python
spark.stop()
exit()
```
And then stop your Docker containers:
```bash
# On your host
docker-compose down
```

This exercise provides a good overview of EDA with PySpark. The visualization part is best done by sampling to Pandas and using Matplotlib/Seaborn, or by connecting a BI tool to your Spark cluster if you had a more persistent setup.
Okay, let's continue with the Spark exercises.

---
**Exercise 3: Load the OULAD data and translate At least 7 queries you wrote for the "SQL - Analytics" worksheet into PySpark syntax.**
---

*   **Goal:** Practice translating SQL queries (especially those with joins, window functions, and aggregations) into PySpark DataFrame API syntax.
*   **Dataset:** Open University Learning Analytics Dataset (OULAD). You'll need to download it and have the relevant CSV files. Common files include:
    *   `studentInfo.csv`
    *   `courses.csv`
    *   `assessments.csv`
    *   `studentAssessment.csv`
    *   `studentRegistration.csv`
    *   `studentVle.csv` (VLE = Virtual Learning Environment interactions)
    *   `vle.csv`

**Prerequisites:**

1.  **Spark Cluster Running:** Ensure your Docker Spark standalone cluster from Exercise 1 is running (`docker-compose up -d`).
2.  **OULAD CSV Files Downloaded:** Download the OULAD dataset and have the CSV files ready.
3.  **Make Data Accessible:** Copy the OULAD CSV files into your `spark-master` container (e.g., to a `/tmp/oulad_data/` directory) or mount a volume.
    ```bash
    # On your host, assuming CSVs are in a local 'oulad_csvs' directory
    docker cp ./oulad_csvs spark-master:/tmp/oulad_data
    ```

**Step-by-Step (inside PySpark shell on `spark-master`):**

1.  **Start PySpark Shell:**
    ```bash
    docker exec -it spark-master bash
    pyspark --master spark://spark-master:7077
    ```

2.  **Import necessary functions and define schemas:**
    ```python
    # Inside PySpark shell
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, when, count, desc, asc, round, avg, min, max, sum as spark_sum, year, month, dayofmonth, to_date, datediff, first, last, lead, lag, rank, dense_rank, row_number, explode, expr
    from pyspark.sql.types import IntegerType, StringType, FloatType, DateType, StructType, StructField
    from pyspark.sql.window import Window

    # It's good practice to define schemas, especially for CSVs
    # Adjust these based on the actual OULAD CSV headers and data types

    student_info_schema = StructType([
        StructField("code_module", StringType(), True), StructField("code_presentation", StringType(), True),
        StructField("id_student", IntegerType(), True), StructField("gender", StringType(), True),
        StructField("region", StringType(), True), StructField("highest_education", StringType(), True),
        StructField("imd_band", StringType(), True), StructField("age_band", StringType(), True),
        StructField("num_of_prev_attempts", IntegerType(), True), StructField("studied_credits", IntegerType(), True),
        StructField("disability", StringType(), True), StructField("final_result", StringType(), True)
    ])

    courses_schema = StructType([
        StructField("code_module", StringType(), True), StructField("code_presentation", StringType(), True),
        StructField("module_presentation_length", IntegerType(), True)
    ])

    assessments_schema = StructType([
        StructField("code_module", StringType(), True), StructField("code_presentation", StringType(), True),
        StructField("id_assessment", IntegerType(), True), StructField("assessment_type", StringType(), True),
        StructField("date", StringType(), True), # Will convert to DateType later if needed
        StructField("weight", FloatType(), True)
    ])

    student_assessment_schema = StructType([
        StructField("id_assessment", IntegerType(), True), StructField("id_student", IntegerType(), True),
        StructField("date_submitted", IntegerType(), True), StructField("is_banked", IntegerType(), True),
        StructField("score", FloatType(), True) # Can be null
    ])

    student_registration_schema = StructType([
        StructField("code_module", StringType(), True), StructField("code_presentation", StringType(), True),
        StructField("id_student", IntegerType(), True),
        StructField("date_registration", StringType(), True), # Can be null, will convert
        StructField("date_unregistration", StringType(), True) # Can be null, will convert
    ])
    ```

3.  **Load the DataFrames:**
    ```python
    base_path = "file:///tmp/oulad_data/" # Adjust if you copied elsewhere

    student_info_df = spark.read.csv(base_path + "studentInfo.csv", header=True, schema=student_info_schema)
    courses_df = spark.read.csv(base_path + "courses.csv", header=True, schema=courses_schema)
    assessments_df = spark.read.csv(base_path + "assessments.csv", header=True, schema=assessments_schema)
    student_assessment_df = spark.read.csv(base_path + "studentAssessment.csv", header=True, schema=student_assessment_schema)
    student_registration_df = spark.read.csv(base_path + "studentRegistration.csv", header=True, schema=student_registration_schema)

    # Cache them if you'll be querying them multiple times
    student_info_df.cache()
    courses_df.cache()
    assessments_df.cache()
    student_assessment_df.cache()
    student_registration_df.cache()

    # Verify counts (optional)
    # print(f"student_info_df count: {student_info_df.count()}")
    # student_info_df.show(5)
    ```

4.  **Translate SQL Queries to PySpark:**
    Let's assume some example SQL queries you might have written and translate them.

    **SQL Query 1: Count of students by region and their final result.**
    ```sql
    -- SELECT region, final_result, COUNT(id_student) as num_students
    -- FROM studentInfo
    -- GROUP BY region, final_result
    -- ORDER BY region, num_students DESC;
    ```
    **PySpark Translation 1:**
    ```python
    print("\n--- Query 1: Students by region and final result ---")
    query1_df = student_info_df.groupBy("region", "final_result") \
        .agg(count("id_student").alias("num_students")) \
        .orderBy("region", desc("num_students"))
    query1_df.show(truncate=False)
    ```

    **SQL Query 2: Average score for each assessment type in a specific module 'AAA'.**
    ```sql
    -- SELECT a.assessment_type, AVG(sa.score) as average_score
    -- FROM assessments a
    -- JOIN studentAssessment sa ON a.id_assessment = sa.id_assessment
    -- WHERE a.code_module = 'AAA' AND sa.score IS NOT NULL
    -- GROUP BY a.assessment_type
    -- ORDER BY average_score DESC;
    ```
    **PySpark Translation 2:**
    ```python
    print("\n--- Query 2: Average score by assessment type for module AAA ---")
    query2_df = assessments_df.alias("a") \
        .join(student_assessment_df.alias("sa"), col("a.id_assessment") == col("sa.id_assessment")) \
        .filter((col("a.code_module") == "AAA") & col("sa.score").isNotNull()) \
        .groupBy("a.assessment_type") \
        .agg(round(avg("sa.score"), 2).alias("average_score")) \
        .orderBy(desc("average_score"))
    query2_df.show()
    ```

    **SQL Query 3: Students who registered but later unregistered from module 'BBB' in presentation '2013J'.**
    ```sql
    -- SELECT id_student, date_registration, date_unregistration
    -- FROM studentRegistration
    -- WHERE code_module = 'BBB' AND code_presentation = '2013J' AND date_unregistration IS NOT NULL;
    ```    **PySpark Translation 3:**
    ```python
    print("\n--- Query 3: Students who unregistered from BBB in 2013J ---")
    # Convert date strings to actual dates if they are not null
    # Assuming date_registration and date_unregistration are days relative to start, so keep as is for now
    # If they were actual dates 'YYYY-MM-DD', you'd use to_date()
    query3_df = student_registration_df \
        .filter(
            (col("code_module") == "BBB") & \
            (col("code_presentation") == "2013J") & \
            col("date_unregistration").isNotNull() & \
            (col("date_unregistration") != "") # Handle empty strings if not truly null
        ) \
        .select("id_student", "date_registration", "date_unregistration")
    query3_df.show(5)
    ```

    **SQL Query 4: Rank students within each module and presentation by their total score on exams (TMA).**
    (This requires joining studentAssessment with assessments, filtering for TMAs, summing scores per student, then ranking).
    ```sql
    -- WITH StudentTotalTMAScore AS (
    --   SELECT
    --     sa.id_student,
    --     a.code_module,
    --     a.code_presentation,
    --     SUM(sa.score) as total_tma_score
    --   FROM studentAssessment sa
    --   JOIN assessments a ON sa.id_assessment = a.id_assessment
    --   WHERE a.assessment_type = 'TMA' AND sa.score IS NOT NULL
    --   GROUP BY sa.id_student, a.code_module, a.code_presentation
    -- )
    -- SELECT
    --   id_student,
    --   code_module,
    --   code_presentation,
    --   total_tma_score,
    --   RANK() OVER (PARTITION BY code_module, code_presentation ORDER BY total_tma_score DESC) as student_rank
    -- FROM StudentTotalTMAScore
    -- ORDER BY code_module, code_presentation, student_rank;
    ```
    **PySpark Translation 4:**
    ```python
    print("\n--- Query 4: Rank students by total TMA score within module/presentation ---")
    student_total_tma_score_df = student_assessment_df.alias("sa") \
        .join(assessments_df.alias("a"), col("sa.id_assessment") == col("a.id_assessment")) \
        .filter((col("a.assessment_type") == "TMA") & col("sa.score").isNotNull()) \
        .groupBy("sa.id_student", "a.code_module", "a.code_presentation") \
        .agg(spark_sum("sa.score").alias("total_tma_score"))

    window_spec_rank = Window.partitionBy("code_module", "code_presentation").orderBy(desc("total_tma_score"))

    query4_df = student_total_tma_score_df.withColumn("student_rank", rank().over(window_spec_rank)) \
        .orderBy("code_module", "code_presentation", "student_rank")
    query4_df.filter(col("code_module") == "AAA").show(10) # Show sample for one module
    ```

    **SQL Query 5: For each student, find their first registration date and last unregistration date across all modules.**
    ```sql
    -- SELECT
    --   id_student,
    --   MIN(date_registration) as first_registration_date,
    --   MAX(date_unregistration) as last_unregistration_date
    -- FROM studentRegistration
    -- GROUP BY id_student;
    ```
    **PySpark Translation 5:**
    ```python
    print("\n--- Query 5: First registration and last unregistration per student ---")
    # Assuming date_registration and date_unregistration are numerical (days from start)
    # If they were date strings, you'd convert them first using to_date()
    query5_df = student_registration_df \
        .filter(col("date_registration").isNotNull()) \
        .groupBy("id_student") \
        .agg(
            min("date_registration").alias("first_registration_date"),
            max("date_unregistration").alias("last_unregistration_date") # Max of nulls and numbers will be the number
        )
    query5_df.show(5)
    ```

    **SQL Query 6: Number of distinct assessments per module and presentation.**
    ```sql
    -- SELECT code_module, code_presentation, COUNT(DISTINCT id_assessment) as distinct_assessments
    -- FROM assessments
    -- GROUP BY code_module, code_presentation
    -- ORDER BY code_module, code_presentation;
    ```
    **PySpark Translation 6:**
    ```python
    from pyspark.sql.functions import countDistinct
    print("\n--- Query 6: Distinct assessments per module/presentation ---")
    query6_df = assessments_df.groupBy("code_module", "code_presentation") \
        .agg(countDistinct("id_assessment").alias("distinct_assessments")) \
        .orderBy("code_module", "code_presentation")
    query6_df.show(10)
    ```

    **SQL Query 7: Students who passed and their average score on exams ('Exam') compared to the overall average exam score for their module and presentation.**
    ```sql
    -- WITH StudentExamAvg AS (
    --   SELECT
    --     sa.id_student,
    --     a.code_module,
    --     a.code_presentation,
    --     AVG(sa.score) as student_avg_exam_score
    --   FROM studentAssessment sa
    --   JOIN assessments a ON sa.id_assessment = a.id_assessment
    --   WHERE a.assessment_type = 'Exam' AND sa.score IS NOT NULL
    --   GROUP BY sa.id_student, a.code_module, a.code_presentation
    -- ),
    -- ModulePresentationExamAvg AS (
    --   SELECT
    --     a.code_module,
    --     a.code_presentation,
    --     AVG(sa.score) as overall_avg_exam_score
    --   FROM studentAssessment sa
    --   JOIN assessments a ON sa.id_assessment = a.id_assessment
    --   WHERE a.assessment_type = 'Exam' AND sa.score IS NOT NULL
    --   GROUP BY a.code_module, a.code_presentation
    -- )
    -- SELECT
    --   s.id_student,
    --   si.final_result,
    --   s.code_module,
    --   s.code_presentation,
    --   s.student_avg_exam_score,
    --   m.overall_avg_exam_score
    -- FROM StudentExamAvg s
    -- JOIN ModulePresentationExamAvg m
    --   ON s.code_module = m.code_module AND s.code_presentation = m.code_presentation
    -- JOIN studentInfo si
    --   ON s.id_student = si.id_student AND s.code_module = si.code_module AND s.code_presentation = si.code_presentation
    -- WHERE si.final_result = 'Pass';
    ```
    **PySpark Translation 7:**
    ```python
    print("\n--- Query 7: Passed students' avg exam score vs. module's avg exam score ---")
    student_exam_avg_df = student_assessment_df.alias("sa") \
        .join(assessments_df.alias("a"), col("sa.id_assessment") == col("a.id_assessment")) \
        .filter((col("a.assessment_type") == "Exam") & col("sa.score").isNotNull()) \
        .groupBy("sa.id_student", "a.code_module", "a.code_presentation") \
        .agg(avg("sa.score").alias("student_avg_exam_score"))

    module_presentation_exam_avg_df = assessments_df.alias("a") \
        .join(student_assessment_df.alias("sa"), col("a.id_assessment") == col("sa.id_assessment")) \
        .filter((col("a.assessment_type") == "Exam") & col("sa.score").isNotNull()) \
        .groupBy("a.code_module", "a.code_presentation") \
        .agg(avg("sa.score").alias("overall_avg_exam_score"))

    query7_df = student_exam_avg_df.alias("s") \
        .join(module_presentation_exam_avg_df.alias("m"),
              (col("s.code_module") == col("m.code_module")) & \
              (col("s.code_presentation") == col("m.code_presentation"))) \
        .join(student_info_df.alias("si"),
              (col("s.id_student") == col("si.id_student")) & \
              (col("s.code_module") == col("si.code_module")) & \
              (col("s.code_presentation") == col("si.code_presentation"))) \
        .filter(col("si.final_result") == "Pass") \
        .select("s.id_student", "si.final_result", "s.code_module", "s.code_presentation",
                round("s.student_avg_exam_score", 2).alias("student_avg_exam_score"),
                round("m.overall_avg_exam_score", 2).alias("overall_avg_exam_score"))
    query7_df.show(10, truncate=False)
    ```

5.  **Stop SparkSession when done:**
    ```python
    spark.stop()
    exit() # Exit bash
    ```
    Then, on your host: `docker-compose down`

This exercise demonstrates the power of the DataFrame API for complex analytical tasks. The syntax is different from SQL but achieves the same results in a distributed manner.

---
**Exercise 4: Use PySpark syntax to find pairs of coprimes up to some constant n.**
---

*   **Goal:** Use Spark DataFrame operations, possibly including array functions, to solve a number theory problem. Two numbers are coprime if their greatest common divisor (GCD) is 1.
*   **Approach:**
    1.  Generate all possible pairs of numbers `(a, b)` where `1 <= a < b <= n`.
    2.  For each pair, calculate their GCD.
    3.  Filter pairs where GCD is 1.

**Step-by-Step (inside PySpark shell):**

1.  **Start PySpark Shell (if not already running):**
    ```bash
    # If needed:
    # docker exec -it spark-master bash
    # pyspark --master spark://spark-master:7077
    ```

2.  **Import functions and set `n`:**
    ```python
    from pyspark.sql.functions import col, explode, sequence, array, struct, udf, lit
    from pyspark.sql.types import IntegerType, BooleanType
    import math # For math.gcd

    N = 30 # Find coprimes up to 30. Adjust as needed.
    ```

3.  **Define a UDF (User Defined Function) for GCD:**
    Spark SQL doesn't have a built-in GCD function for two columns directly in the same way as some SQL dialects. We can define a UDF.
    ```python
    def gcd_py(a, b):
        return math.gcd(int(a), int(b))

    gcd_udf = udf(gcd_py, IntegerType())
    ```

4.  **Generate pairs and find coprimes:**

    *   **Method 1: Using `explode` and `crossJoin` (can be inefficient for large N but conceptually simple)**
        ```python
        print(f"\n--- Finding coprimes up to N={N} using crossJoin ---")
        # Create a DataFrame with numbers from 1 to N
        numbers_df = spark.range(1, N + 1).withColumnRenamed("id", "num")
        # numbers_df.show()

        # Cross join to get all pairs (a, b)
        # Then filter for a < b to avoid duplicates like (2,1) if (1,2) is present, and (x,x)
        pairs_df = numbers_df.alias("df1").crossJoin(numbers_df.alias("df2")) \
            .filter(col("df1.num") < col("df2.num")) \
            .select(col("df1.num").alias("a"), col("df2.num").alias("b"))
        # pairs_df.show(10)

        # Calculate GCD and filter for coprimes
        coprimes_df = pairs_df.withColumn("gcd_val", gcd_udf(col("a"), col("b"))) \
            .filter(col("gcd_val") == 1) \
            .select("a", "b")

        print(f"Coprime pairs up to {N}:")
        coprimes_df.orderBy("a", "b").show(50, truncate=False)
        print(f"Total coprime pairs found: {coprimes_df.count()}")
        ```

    *   **Method 2: Using RDDs for pair generation (potentially more control for very large N if crossJoin becomes too slow, but DataFrame API is generally preferred)**
        This method is more complex to set up for this specific pair generation compared to the DataFrame `crossJoin`. For this problem scale, `crossJoin` is fine. If `N` were extremely large, one might consider RDD approaches to generate pairs more carefully to manage intermediate data size, but the UDF for GCD would still be the main computation.

    *   **Using Array Functions (More advanced, might be less intuitive for simple pair generation):**
        You could generate an array of numbers, then try to use functions like `array_repeat`, `explode`, and then combinations. However, for generating distinct pairs `(a,b)` where `a < b`, the `crossJoin` and filter approach on a sequence DataFrame is quite direct.
        If the question implies using array functions *after* pairs are generated (e.g., if numbers had associated arrays of factors), then `array_intersect` on factor lists could find common factors. But for direct coprime check, GCD is standard.

        Let's stick to the `crossJoin` method as it's idiomatic Spark SQL for generating pairs from a set. The "array functions" part of the question might be a general suggestion for Spark capabilities rather than a strict requirement for *this specific* coprime generation. If the intent was to find factors first and then check for intersection of factor sets (excluding 1), that's a different algorithm for primality/coprimality.

        The `apply` function in Pandas API on Spark could be used if you convert to `pyspark.pandas.DataFrame` and then apply a Python function that takes a row (pair) and returns GCD, but UDFs are more standard for Spark DataFrames. `collect_set` is an aggregate function, useful for collecting unique items within a group, not directly for generating pairs or GCD.

The `crossJoin` with UDF for GCD is the most straightforward PySpark way to address this.

---
**Exercise 5: Advanced: Using Spark and the CommonCrawl dataset, investigate the occurring evolution of the expression "Artificial Intelligence" over time.**
---

*   **Goal:** Perform a large-scale text analysis on a massive dataset. This is a true big data problem.
*   **Dataset:** Common Crawl (petabytes of web crawl data). Accessing and processing this typically requires:
    *   Significant cloud storage (like S3 where it's hosted).
    *   A reasonably sized Spark cluster running in the cloud (e.g., AWS EMR, Databricks, Google Cloud Dataproc).
    *   **This is NOT feasible to run on your local Docker setup.**
*   **Leanest Approach (Conceptual for this exercise):**
    1.  **Understand Common Crawl Structure:** It's usually stored in WARC (Web ARChive) format, or sometimes as WAT (metadata) or WET (extracted text) files.
    2.  **Focus on WET files:** These contain extracted plain text, which is easiest for this task.
    3.  **Filtering by Date:** Common Crawl data is organized by crawl date (e.g., `CC-MAIN-YYYY-WW`). You'd select a range of crawls over several years.
    4.  **Spark Job Logic (Conceptual):**
        *   **Input:** Paths to relevant WET files on S3 for different time periods.
        *   **Mapper-like operation:**
            *   Read each WET file (which contains many web pages).
            *   For each page's text:
                *   Extract the year/month from the crawl information or page metadata if available.
                *   Count occurrences of "Artificial Intelligence" (case-insensitive).
                *   Emit `((year, month), count_of_AI_mentions_in_page, 1_for_page_count)`.
        *   **Reducer-like operation (Aggregation):**
            *   Group by `(year, month)`.
            *   Sum `count_of_AI_mentions_in_page` to get total mentions for that month.
            *   Sum `1_for_page_count` to get total pages processed for that month.
            *   Calculate `total_mentions / total_pages` as a normalized frequency.
        *   **Output:** `(year, month, normalized_frequency_of_AI)`
    5.  **Visualization:** Plot the normalized frequency over time to see the trend.

*   **PySpark Snippets (Highly Conceptual - would need actual Common Crawl access and parsing libraries):**
    ```python
    # spark = SparkSession.builder.appName("CommonCrawlAI").getOrCreate()

    # Assume you have a function to get WET file paths for a given crawl date range
    # wet_file_paths = get_cc_wet_paths_for_range("s3://commoncrawl/crawl-data/CC-MAIN-YYYY-WW/segments/.../wet/")

    # def extract_year_month_and_ai_count(wet_page_content_and_metadata):
    #     year, month = parse_date_from_metadata(wet_page_content_and_metadata.metadata)
    #     text = wet_page_content_and_metadata.text
    #     ai_count = text.lower().count("artificial intelligence")
    #     return ((year, month), (ai_count, 1)) # (ai_mentions, page_count)

    # raw_wet_rdd = spark.sparkContext.newAPIHadoopFile(path, inputFormatClass, keyClass, valueClass) # Using appropriate WARC/WET reader
    # This part is complex as it requires a custom InputFormat for WARC/WET or using a library.
    # A simpler approach if WET files are just gzipped text:
    # text_rdd = spark.sparkContext.textFile("s3://path_to_many_wet_files/*/*.wet.gz")

    # For demonstration, let's assume text_rdd where each record is page text and we can get date
    # This is a MAJOR simplification.
    # def process_page_text(page_text_with_date_info):
    #     # date_info would come from the file path or metadata
    #     year, month = extract_year_month_from_date_info(page_text_with_date_info.date_info)
    #     text = page_text_with_date_info.text
    #     ai_count = text.lower().count("artificial intelligence")
    #     if ai_count > 0: # Only emit if AI is mentioned to reduce data
    #         return ((year, month), (ai_count, 1)) # (ai_mentions, page_count)
    #     else:
    #         return ((year, month), (0, 1)) # Still count the page

    # This would need a proper way to read WET and associate dates.
    # Assuming we have an RDD: year_month_ai_counts_rdd = some_processed_rdd.map(process_page_text)

    # aggregated_rdd = year_month_ai_counts_rdd \
    #     .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1])) \ # Sum AI counts and page counts
    #     .mapValues(lambda v: v[0] / v[1] if v[1] > 0 else 0) # Calculate normalized frequency

    # result_df = aggregated_rdd.toDF(["year_month", "normalized_ai_frequency"])
    # result_df.orderBy("year_month").show()
    ```
*   **Key takeaway for this exercise:** Understand the scale and the general MapReduce-like approach. Actually running it is a significant engineering effort. Libraries like `cc_pyspark` exist to help read Common Crawl data with Spark.

---
**Exercise 6: Advanced: Store the NASA small body dataset in a S3 server, inspect it with SparkML**
---

*   **Goal:** Combine cloud storage (S3), Spark, and Spark MLlib for a machine learning task.
*   **Dataset:** NASA JPL Small-Body Database (SBDB). You'd typically download data via their API or specific data files. (Search "NASA JPL SBDB data download" or "JPL Small-Body Database Query API"). Data might include orbital elements, physical parameters, discovery information for asteroids and comets.
*   **This also requires cloud resources (AWS S3 account, Spark cluster capable of accessing S3, e.g., EMR).**

**Leanest Approach (Conceptual):**

1.  **Obtain and Prepare Data:**
    *   Download relevant data from SBDB. This will likely be in JSON or text/CSV format.
    *   Clean and preprocess it into a suitable tabular format (e.g., Parquet or CSV).

2.  **Upload to S3:**
    *   Create an S3 bucket in your AWS account.
    *   Upload the prepared dataset to this bucket.
    *   Ensure your Spark cluster has the necessary IAM permissions and configurations (e.g., S3A connector, access keys) to read from this S3 bucket.

3.  **Spark ML Task (Example: Predict if an asteroid is a "Near-Earth Object" - NEO):**
    *   **Load Data into Spark DataFrame from S3:**
        ```python
        # spark = SparkSession.builder.appName("NASASmallBodyML").getOrCreate()
        # Configure S3 access if not done globally in Spark setup
        # spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "YOUR_ACCESS_KEY")
        # spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "YOUR_SECRET_KEY")
        # spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.amazonaws.com")

        # s3_path = "s3a://your-s3-bucket-name/path/to/nasa_sb_data.parquet"
        # data_df = spark.read.parquet(s3_path)
        # data_df.printSchema()
        ```
    *   **Feature Engineering:**
        *   Select relevant features (e.g., orbital elements like `a`, `e`, `i`, `q`, `Q`; physical parameters like `H` absolute magnitude).
        *   Handle missing values.
        *   Convert categorical features to numerical (e.g., using `StringIndexer`, `OneHotEncoder`).
        *   Assemble features into a single `features` vector column using `VectorAssembler`.
    *   **Define Label:**
        *   Create a binary label column, e.g., `is_neo` (1 if it's a Near-Earth Object, 0 otherwise). This information is usually available in the dataset.
    *   **Split Data:**
        *   `train_df, test_df = data_df.randomSplit([0.8, 0.2], seed=42)`
    *   **Train a Model:**
        *   Example: Logistic Regression or Random Forest.
        ```python
        # from pyspark.ml.feature import StringIndexer, VectorAssembler, OneHotEncoder
        # from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
        # from pyspark.ml import Pipeline
        # from pyspark.ml.evaluation import BinaryClassificationEvaluator

        # # Example: Assuming 'orbit_class' is categorical and 'is_neo_flag' is the string label 'Y'/'N'
        # label_indexer = StringIndexer(inputCol="is_neo_flag", outputCol="label").fit(data_df)
        # orbit_class_indexer = StringIndexer(inputCol="orbit_class", outputCol="orbit_class_index")
        # orbit_class_encoder = OneHotEncoder(inputCol="orbit_class_index", outputCol="orbit_class_vec")

        # feature_cols = ["a", "e", "i", "H", "q", "Q", "orbit_class_vec"] # Example features
        # assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")

        # lr = LogisticRegression(featuresCol="features", labelCol="label")
        # pipeline = Pipeline(stages=[label_indexer, orbit_class_indexer, orbit_class_encoder, assembler, lr])

        # model = pipeline.fit(train_df)
        ```
    *   **Make Predictions and Evaluate:**
        ```python
        # predictions = model.transform(test_df)
        # predictions.select("label", "prediction", "probability").show(5)

        # evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction", labelCol="label", metricName="areaUnderROC")
        # auc = evaluator.evaluate(predictions)
        # print(f"Area Under ROC: {auc}")
        ```

*   **Key takeaway for this exercise:** Understand the workflow of using Spark MLlib with data from cloud storage. The actual ML part involves standard steps: feature engineering, model training, and evaluation, but performed at scale with Spark.

These advanced exercises (5 and 6) are more about understanding the potential and workflow with very large datasets and cloud services rather than something you'd typically execute fully on a small local Docker setup. The core Spark concepts from exercises 1-4 are the foundation.