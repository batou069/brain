---
tags: [big_data, data_processing, distributed_systems, moc, concept]
aliases: [Big Data MOC, Large Scale Data Processing MOC]
related:
  - "[[_Data_Science_AI_MOC]]"
  - "[[180_Big_Data/Hadoop/_Hadoop_MOC|Hadoop Ecosystem MOC]]"
  - "[[Apache_Spark_MOC]]" # Placeholder for Spark
  - "[[Cloud_Computing_MOC]]" # Placeholder, as Big Data often leverages cloud
worksheet: [WS_BigData_1] # New worksheet identifier
date_created: 2025-06-09
---
# Big Data MOC 

This section explores concepts, technologies, and frameworks related to **Big Data**—datasets that are too large or complex for traditional data-processing application software to adequately deal with. It focuses on distributed storage, parallel processing, and the ecosystems built around these principles.

## Core Concepts
-   [[Big_Data_Definition_Characteristics|What is Big Data? (The Vs: Volume, Velocity, Variety, Veracity, Value)]]
-   [[Distributed_Systems_Overview|Distributed Systems Overview]]
-   [[Parallel_Computing_Paradigms|Parallel Computing Paradigms]]
    -   [[Parallelism_vs_Mass_Parallelism|Parallelism vs. Mass Parallelism]]
-   [[Data_Storage_Approaches_Big_Data|Data Storage Approaches for Big Data]]
    -   [[Sharding_vs_Partitioning|Sharding vs. Partitioning]]
-   [[Fault_Tolerance_Big_Data|Fault Tolerance and Robustness in Big Data]]
-   [[Data_Replication|Data Replication Strategies]]
-   [[Data_Integrity_Big_Data|Data Integrity in Large Scale Systems]]
-   [[Data_Streaming_Big_Data|Data Streaming]]
-   [[Scalability_Big_Data|Scalability (Horizontal vs. Vertical)]]

## Key Technologies & Frameworks
-   **[[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop Ecosystem]]**
    -   [[HDFS|Hadoop Distributed File System (HDFS)]]
    -   [[MapReduce|MapReduce Programming Model]]
    -   [[YARN|Yet Another Resource Negotiator (YARN)]]
    -   [[Apache_Hive|Apache Hive]] (Data Warehousing)
    -   [[Apache_Pig|Apache Pig]] (Data Flow Language)
    -   [[Apache_HBase|Apache HBase]] (NoSQL Database)
    -   [[Apache_Sqoop|Apache Sqoop]] (Data Transfer)
    -   [[Apache_Flume|Apache Flume]] (Log Collection)
-   **[[Apache_Spark_MOC|Apache Spark]]** (Placeholder)
    -   In-memory processing, Spark SQL, Streaming, MLlib, GraphX.
-   **NoSQL Databases** (Placeholder)
    -   Key-Value Stores, Document Stores, Column-Family Stores, Graph Databases.
-   **Stream Processing Engines** (Placeholder)
    -   Apache Kafka, Apache Flink, Apache Storm.
-   **Cloud-Based Big Data Services** (Placeholder)
    -   AWS (EMR, S3, Redshift), Azure (HDInsight, Data Lake Storage, Synapse), GCP (Dataproc, Cloud Storage, BigQuery).

## Challenges in Big Data
-   Data Storage and Management
-   Processing Speed and Efficiency
-   Data Quality and Governance
-   Security and Privacy
-   Cost Management
-   Complexity of Tools and Skills Gap

## Notes in this Section (General Big Data)
```dataview
LIST
FROM "180_Big_Data"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC") AND !contains(file.folder, "Hadoop") AND !contains(file.folder, "Spark")
SORT file.name ASC
```

---