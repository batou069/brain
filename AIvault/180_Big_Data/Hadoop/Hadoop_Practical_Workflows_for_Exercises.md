---
tags:
  - hadoop
  - workflow
  - exercise_guide
  - hdfs
  - mapreduce
  - hive
  - practical
  - concept
aliases:
  - Hadoop Exercise Workflows
  - Hadoop Practical Guide
related:
  - "[[_Hadoop_MOC]]"
  - "[[hadoop_fs_Command]]"
  - "[[MapReduce]]"
  - "[[MapReduce_Python_Streaming]]"
  - "[[MapReduce_Java_Implementation]]"
  - "[[Apache_Hive]]"
  - "[[Data_Ingestion_Hadoop]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Hadoop: Practical Workflows for Exercises

This note outlines conceptual workflows and considerations for tackling common Hadoop exercises, similar to those provided in the course material. It aims to connect theoretical concepts with practical steps.

>[!note] Environment Assumption
>These workflows assume you have a Hadoop environment (single-node or multi-node cluster) set up and configured, and you can access it via a command-line interface where `hadoop` commands are available.

[list2tab|#Exercise Workflows]
- 1. HDFS Basics (Setup, Dirs, Files)
    - **Goal:** Get familiar with basic HDFS operations: creating directories, uploading files, and simple file manipulation.
    - **Conceptual Steps & Commands:**
        1.  **Verify Hadoop is Running:**
            -   Check NameNode, DataNode, ResourceManager, NodeManager processes (e.g., using `jps` command on relevant nodes).
        2.  **Create a Directory on HDFS:**
            -   Use `hadoop fs -mkdir /user/<your_username>/my_data_dir` (replace `<your_username>` with your HDFS user directory or another appropriate path).
            -   Verify: `hadoop fs -ls /user/<your_username>/`
        3.  **Prepare Local File:**
            -   Ensure you have the `american-english` dictionary file locally. Let's call it `local_dictionary.txt`.
        4.  **Upload File to HDFS:**
            -   `hadoop fs -put ./local_dictionary.txt /user/<your_username>/my_data_dir/`
            -   Verify: `hadoop fs -ls /user/<your_username>/my_data_dir/`
            -   View content: `hadoop fs -cat /user/<your_username>/my_data_dir/local_dictionary.txt | head`
        5.  **Multiply File Content (Conceptual - in HDFS):**
            -   HDFS files are typically immutable or append-only. Directly "multiplying" content in the *same file* x10 in-place isn't a standard HDFS operation.
            -   **Approach 1 (New file):** Read the file, replicate content in application logic, write to a new HDFS file.
                -   `hadoop fs -cat /user/.../local_dictionary.txt > temp_local_dict.txt`
                -   Locally: `for i in {1..10}; do cat temp_local_dict.txt >> multiplied_dict_local.txt; done` (or Python script)
                -   `hadoop fs -put ./multiplied_dict_local.txt /user/<your_username>/my_data_dir/`
            -   **Approach 2 (MapReduce/Spark - overkill for this):** A simple MapReduce job could read each line and output it 10 times, then a reducer could collect them. This is more for demonstrating the framework than a practical way to multiply a dictionary.
            -   **Approach 3 (Append if supported and desired):** If your Hadoop version and file settings allow appends robustly:
                -   `hadoop fs -appendToFile ./local_dictionary.txt /user/.../local_dictionary.txt` (repeated 9 times). This appends the local file's content to the HDFS file.
    - **Key Concepts Involved:** [[hadoop_fs_Command|`hadoop fs` commands]], HDFS paths, file immutability/append operations.
- 2. MapReduce with Python Streaming
    - **Goal:** Implement a Word Count (or similar) using Python for mapper and reducer scripts, executed via Hadoop Streaming.
    - **Conceptual Steps & Commands:**
        1.  **Write Mapper Script (`mapper.py`):**
            ```python
            #!/usr/bin/env python3
            import sys
            for line in sys.stdin:
                line = line.strip()
                words = line.split() # Or more sophisticated tokenization
                for word in words:
                    # Clean/normalize word if needed (e.g., lowercasing, remove punctuation)
                    # word_cleaned = word.lower().strip('.,!?;:"()[]')
                    # if word_cleaned: # Ensure word is not empty after cleaning
                    print(f"{word.lower()}\t1") # Output: word<TAB>1
            ```
            -   Make executable: `chmod +x mapper.py`
        2.  **Write Reducer Script (`reducer.py`):**
            ```python
            #!/usr/bin/env python3
            import sys
            current_word = None
            current_count = 0
            for line in sys.stdin:
                line = line.strip()
                try:
                    word, count_str = line.split('\t', 1)
                    count = int(count_str)
                except ValueError:
                    # Skip lines that are not properly formatted
                    continue

                if current_word == word:
                    current_count += count
                else:
                    if current_word:
                        print(f"{current_word}\t{current_count}")
                    current_word = word
                    current_count = count
            # Output the last word
            if current_word:
                print(f"{current_word}\t{current_count}")
            ```
            -   Make executable: `chmod +x reducer.py`
        3.  **Test Locally:**
            -   `echo "hello world hello hadoop world" | ./mapper.py | sort -k1,1 | ./reducer.py`
            -   Expected output:
                ```
                hadoop  1
                hello   2
                world   2
                ```
        4.  **Prepare Input Data on HDFS:**
            -   Upload a text file (e.g., your `multiplied_dict_local.txt` or any other text file) to HDFS.
                `hadoop fs -put ./my_text_file.txt /user/<your_username>/input_wordcount/`
        5.  **Run Hadoop Streaming Job:**
            ```bash
            hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
                -files ./mapper.py,./reducer.py \
                -mapper mapper.py \
                -reducer reducer.py \
                -input /user/<your_username>/input_wordcount/my_text_file.txt \
                -output /user/<your_username>/output_wordcount
            ```
            -   `$HADOOP_HOME` should point to your Hadoop installation directory.
            -   `-files` distributes your scripts to the cluster nodes.
        6.  **Check Output:**
            -   `hadoop fs -ls /user/<your_username>/output_wordcount/`
            -   `hadoop fs -cat /user/<your_username>/output_wordcount/part-00000 | head`
    - **Key Concepts Involved:** [[MapReduce|MapReduce model (map, reduce phases)]], Standard Input/Output for scripts, Hadoop Streaming utility, [[hadoop_fs_Command|`hadoop fs` commands]].
- 3. MapReduce in Java (Advanced)
    - **Goal:** Implement Word Count (or another problem) using native Java MapReduce API.
    - **Conceptual Steps:**
        1.  **Setup Java Development Environment:** JDK, Maven/Gradle (for dependency management and building).
        2.  **Add Hadoop Dependencies:** Include `hadoop-client` or specific MapReduce APIs in your `pom.xml` (Maven) or `build.gradle` (Gradle).
        3.  **Write Mapper Class:**
            -   Extend `org.apache.hadoop.mapreduce.Mapper`.
            -   Implement the `map(Object key, Text value, Context context)` method.
            -   Input `key` is often `LongWritable` (byte offset), `value` is `Text` (line).
            -   Output intermediate key/value pairs using `context.write(new Text(word), new IntWritable(1))`.
        4.  **Write Reducer Class:**
            -   Extend `org.apache.hadoop.mapreduce.Reducer`.
            -   Implement the `reduce(Text key, Iterable<IntWritable> values, Context context)` method.
            -   Iterate through `values` to sum counts for the given `key` (word).
            -   Output final key/value using `context.write(key, new IntWritable(sum))`.
        5.  **Write Driver Class (Main Class):**
            -   Configure the MapReduce job (`org.apache.hadoop.mapreduce.Job`).
            -   Set Mapper, Reducer, Combiner (optional) classes.
            -   Set input/output formats (e.g., `TextInputFormat`, `TextOutputFormat`).
            -   Set input/output paths (HDFS paths).
            -   Set output key/value classes.
            -   Submit the job and wait for completion.
        6.  **Compile and Package:** Build a JAR file (e.g., using `mvn package`).
        7.  **Run on Hadoop Cluster:**
            -   `hadoop jar YourWordCount.jar com.example.YourDriverClass /user/input_path /user/output_path`
    - **Key Concepts Involved:** Java programming, Hadoop MapReduce API (Writables, Input/Output Formats, Job configuration), JAR packaging.
- 4. Analytics using Hive
    - **Goal:** Perform SQL-like queries on data stored in HDFS using Hive.
    - **Conceptual Steps:**
        1.  **Prepare Data:** Ensure your dataset (e.g., OULAD dataset, or any CSV/TSV/JSON) is in HDFS.
            -   `hadoop fs -put ./oulad_dataset.csv /user/<your_username>/oulad_data/`
        2.  **Convert to Optimized Format (Optional but Recommended - e.g., Parquet):**
            -   This can be done using Spark, another Hive table (CTAS), or a custom script. For simplicity, we might initially load CSV.
            -   If converting: Create an external Hive table over the CSV, then `CREATE TABLE oulad_parquet STORED AS PARQUET AS SELECT * FROM oulad_csv_external;`
        3.  **Start Hive CLI or Beeline:**
            -   `hive` or `beeline -u jdbc:hive2://<hiveserver2_host>:<port>`
        4.  **Create Hive Table (Define Schema):**
            ```hiveql
            CREATE EXTERNAL TABLE IF NOT EXISTS oulad_students (
                code_module STRING,
                code_presentation STRING,
                id_student INT,
                gender STRING,
                region STRING,
                highest_education STRING,
                imd_band STRING,
                age_band STRING,
                num_of_prev_attempts INT,
                studied_credits INT,
                disability STRING,
                final_result STRING
            )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE -- Or ORC, PARQUET if data is already in that format
            LOCATION '/user/<your_username>/oulad_data/'; -- Points to HDFS directory
            -- TBLPROPERTIES ("skip.header.line.count"="1"); -- If CSV has a header
            ```
            -   Use `EXTERNAL TABLE` so Hive doesn't delete HDFS data if table is dropped.
            -   Adjust `FIELDS TERMINATED BY`, `STORED AS`, and schema according to your actual file.
        5.  **Load Data (if table is managed and not external pointing to existing data):**
            -   `LOAD DATA INPATH '/user/<your_username>/oulad_data/oulad_dataset.csv' INTO TABLE oulad_students_managed;` (This moves data into Hive's warehouse directory).
            -   For external tables, the `LOCATION` clause already points to the data.
        6.  **Run HiveQL Queries:**
            ```hiveql
            -- Example: Count students by region
            SELECT region, COUNT(*) as student_count
            FROM oulad_students
            GROUP BY region;

            -- Example: Average studied credits by final result
            SELECT final_result, AVG(studied_credits) as avg_credits
            FROM oulad_students
            GROUP BY final_result;
            ```
        7.  **Explore Results:** Hive CLI will display results, or you can save them to a new table or HDFS path.
    - **Key Concepts Involved:** [[Apache_Hive|Apache Hive]], HiveQL, Metastore, Schemas, External vs. Managed Tables, Partitions (if used), File Formats (TEXTFILE, PARQUET, ORC).

These workflows provide a starting point. Each exercise often involves debugging, exploring data characteristics, and refining commands or code.

---