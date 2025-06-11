---
tags:
  - hadoop
  - hdfs
  - namenode
  - master_node
  - metadata
  - file_system_namespace
  - concept
aliases:
  - NameNode
  - HDFS Master
related:
  - "[[HDFS]]"
  - "[[Hadoop_Node_Types]]"
  - "[[HDFS_DataNode]]"
  - "[[HDFS_NameNode_Particularity]]"
  - "[[Hadoop_Fault_Tolerance]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# HDFS NameNode

## Definition
The **NameNode** is the master server in the [[HDFS|Hadoop Distributed File System (HDFS)]] architecture. It is a critical component that manages the file system namespace and regulates access to files by clients. The NameNode does **not** store the actual data blocks of the files; that is the responsibility of the [[HDFS_DataNode|DataNodes]].

## Core Responsibilities
-   **Managing File System Namespace:**
    -   Maintains the directory tree structure of the file system.
    -   Stores metadata for all files and directories, including:
        -   File names, directory names.
        -   Permissions (owner, group, mode).
        -   Modification and access times.
        -   Replication factor for files.
        -   Block size for files.
-   **Mapping Blocks to DataNodes:**
    -   Crucially, the NameNode knows the location of every block for every file in HDFS. It maintains a mapping of which DataNodes hold which replicas of each block.
    -   When a client wants to read a file, it contacts the NameNode to get the list of DataNodes holding the blocks for that file.
-   **Coordinating File System Operations:**
    -   Handles client requests for creating, deleting, renaming, and moving files and directories.
    -   Manages block allocation when new files are created or appended to.
-   **Monitoring DataNode Health:**
    -   Receives regular **heartbeats** from all DataNodes in the cluster. If a DataNode fails to send a heartbeat, the NameNode considers it dead.
    -   Receives **block reports** from DataNodes, which list all blocks stored on that DataNode. This allows the NameNode to keep its block location map up-to-date and consistent.
-   **Managing Block Replication:**
    -   Enforces the configured replication factor for each file's blocks.
    -   If a DataNode fails, the NameNode identifies under-replicated blocks and instructs other DataNodes to create new replicas to maintain the desired replication level.
    -   Also handles over-replicated blocks by instructing DataNodes to delete surplus replicas.
-   **Data Integrity (Metadata):**
    -   Ensures the consistency and integrity of the file system metadata.

## Metadata Storage
The NameNode stores its critical metadata in two primary files on its local disk:
1.  **FsImage:** A persistent checkpoint of the file system namespace and block map. It's a complete snapshot of the metadata at a point in time. Loaded into memory on NameNode startup.
2.  **EditLog (Journal):** A transaction log that records every change made to the file system metadata (e.g., file creation, deletion, block allocation) since the last FsImage checkpoint.

When the NameNode starts, it loads the FsImage into memory and then applies all transactions from the EditLog to bring the in-memory metadata up to date. Periodically, the EditLog is merged with the FsImage to create a new checkpoint, and the EditLog is truncated.

## Single Point of Failure (SPOF) and High Availability (HA)
-   **Historically:** In early Hadoop versions, the NameNode was a single point of failure. If the NameNode machine crashed, the entire HDFS cluster would become inaccessible until the NameNode was restored (potentially from a backup, which could involve downtime and some data loss if the latest EditLog was not saved).
-   **High Availability (HA):** Modern Hadoop (Hadoop 2.x and later) supports NameNode High Availability. This typically involves:
    -   **Active NameNode:** The NameNode currently serving client requests and managing the namespace.
    -   **Standby NameNode:** A redundant NameNode that maintains a synchronized copy of the metadata from the Active NameNode. It's ready to take over quickly if the Active NameNode fails.
    -   **Shared Storage (for EditLog/Journal):** Both Active and Standby NameNodes write to/read from a shared EditLog, often managed by a set of JournalNodes or a shared NFS.
    -   **ZooKeeper (Often):** Used for leader election and coordination to manage automatic failover from Active to Standby.

>[!question] What is the particularity of the NameNode?
>The key particularities of the NameNode are:
>1.  **Centralized Metadata Authority:** It is the *sole* authority for all metadata related to the HDFS namespace and block locations. All file system operations that modify the namespace or require block locations must go through the NameNode.
>2.  **In-Memory Metadata:** To provide fast responses to client requests and DataNode reports, the NameNode keeps the entire file system namespace and block map in its main memory (RAM). This implies that the amount of RAM available on the NameNode machine limits the number of files, directories, and blocks HDFS can manage.
>3.  **No Data Storage:** The NameNode itself does not store any of the actual file data blocks. These are stored on the [[HDFS_DataNode|DataNodes]].
>4.  **Criticality (SPOF without HA):** As the central coordinator, its failure (without an HA setup) renders the entire HDFS cluster unusable. This makes its reliability and availability paramount.
>5.  **Bottleneck Potential:** Since all metadata operations pass through the NameNode, it can become a performance bottleneck in extremely large clusters or with workloads involving a very high rate of metadata operations (e.g., creating/deleting many small files).
>6.  **Resource Requirements:** Typically requires a machine with significant RAM (due to in-memory metadata) and reliable storage for FsImage and EditLog, though not necessarily massive disk capacity for data blocks.

The NameNode is the brain of HDFS, orchestrating all file system activities and maintaining its integrity.

---