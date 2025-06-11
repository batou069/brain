---
tags:
  - hadoop
  - big_data
  - distributed_computing
  - hdfs
  - mapreduce
  - yarn
  - moc
  - concept
aliases:
  - Hadoop Ecosystem MOC
  - Apache Hadoop MOC
related:
  - "[[_Big_Data_MOC]]"
  - "[[HDFS]]"
  - "[[MapReduce]]"
  - "[[YARN]]"
  - "[[Apache_Hive]]"
  - "[[hadoop_fs_Command]]"
  - "[[Hadoop_Node_Types]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Apache Hadoop Ecosystem MOC 🐘

**Apache Hadoop** is an open-source framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures. [1]

## Core Hadoop Components
[list2card|addClass(ab-col3)|#Core Hadoop]
- **[[HDFS|Hadoop Distributed File System (HDFS)]]**
  - A distributed file system designed to run on commodity hardware. Provides high-throughput access to application data.
  - Key concepts: [[HDFS_NameNode|NameNode]], [[HDFS_DataNode|DataNode]], Blocks, [[Data_Replication|Replication]].
- **[[MapReduce|MapReduce Programming Model]]**
  - A software framework for easily writing applications that process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner. [2]
  - Key phases: Map, Shuffle & Sort, Reduce.
- **[[YARN|Yet Another Resource Negotiator (YARN)]]**
  - The resource management and job scheduling technology in Hadoop. Separates resource management from processing logic.
  - Key concepts: ResourceManager, NodeManager, ApplicationMaster, Containers.

## Key Concepts & Terminology
-   [[Hadoop_Node_Types|Hadoop Node Types]] (NameNode, DataNode, ResourceManager, NodeManager)
-   [[Hadoop_Cluster_Architecture|Hadoop Cluster Architecture]]
-   [[Hadoop_Fault_Tolerance|Fault Tolerance in Hadoop]]
-   [[Data_Locality_Hadoop|Data Locality]]
-   [[hadoop_fs_Command|`hadoop fs` Command Line Interface]]

## Common Hadoop Ecosystem Tools
While HDFS, MapReduce, and YARN form the core, the Hadoop ecosystem includes many other tools:
-   **[[Apache_Hive|Apache Hive]]:** A data warehouse system for Hadoop that facilitates reading, writing, and managing large datasets residing in distributed storage using SQL-like queries (HiveQL).
-   **[[Apache_Pig|Apache Pig]]:** (Placeholder) A high-level platform for creating MapReduce programs used with Hadoop. The language for this platform is called Pig Latin.
-   **[[Apache_HBase|Apache HBase]]:** (Placeholder) A non-relational, distributed database (NoSQL) that runs on top of HDFS. Provides random, real-time read/write access to Big Data.
-   **[[Apache_Sqoop|Apache Sqoop]]:** (Placeholder) A tool designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases.
-   **[[Apache_Flume|Apache Flume]]:** (Placeholder) A distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.
-   **Apache Oozie:** (Placeholder) A workflow scheduler system to manage Apache Hadoop jobs.
-   **Apache ZooKeeper:** (Placeholder) A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.

## Notes in this Hadoop Section
```dataview
LIST
FROM "180_Big_Data/Hadoop"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---