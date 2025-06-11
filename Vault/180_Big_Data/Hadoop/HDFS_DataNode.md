---
tags:
  - hadoop
  - hdfs
  - datanode
  - worker_node
  - storage
  - block_management
  - concept
aliases:
  - DataNode
  - HDFS Worker
related:
  - "[[HDFS]]"
  - "[[Hadoop_Node_Types]]"
  - "[[HDFS_NameNode]]"
  - "[[Data_Replication]]"
  - "[[Hadoop_Fault_Tolerance]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# HDFS DataNode

## Definition
A **DataNode** is a worker (or slave) node in the [[HDFS|Hadoop Distributed File System (HDFS)]] architecture. DataNodes are responsible for storing the actual data blocks of files on the local disks of the machines they run on. There are typically many DataNodes in a Hadoop cluster, forming the distributed storage layer.

## Core Responsibilities
-   **Storing Data Blocks:**
    -   The primary function of a DataNode is to store HDFS blocks on its local file system (e.g., ext4, XFS). Each DataNode manages multiple blocks belonging to different files.
    -   Files in HDFS are split into large blocks (e.g., 128MB or 256MB).
-   **Serving Read/Write Requests:**
    -   DataNodes handle read and write requests from HDFS clients for the blocks they store.
    -   For reads, clients first contact the [[HDFS_NameNode|NameNode]] to get block locations, then read data directly from the appropriate DataNodes.
    -   For writes, the client writes data to a pipeline of DataNodes (for replication). The first DataNode in the pipeline receives data from the client, writes it to its local disk, and forwards it to the next DataNode in the pipeline, and so on.
-   **Block Operations:**
    -   Perform block creation, deletion, and replication as instructed by the NameNode.
    -   When a block needs to be replicated (e.g., due to a DataNode failure or an increase in replication factor), a DataNode will copy the block from another DataNode holding a replica.
-   **Communication with NameNode:**
    -   **Heartbeats:** DataNodes send regular heartbeat messages to the NameNode (typically every 3 seconds) to indicate that they are alive and functioning correctly. If the NameNode doesn't receive a heartbeat from a DataNode within a timeout period, it marks that DataNode as dead.
    -   **Block Reports:** Periodically (e.g., every hour by default, but also upon startup and significant changes), each DataNode sends a block report to the NameNode. This report contains a list of all blocks currently stored on that DataNode. The NameNode uses this information to validate its block location map and manage block replication.
-   **Data Integrity:**
    -   DataNodes perform checksum verification for data they receive and store to ensure data integrity. When a client reads a block, it can verify the checksum against the data received.

## Interaction in the Cluster
-   DataNodes operate under the coordination of the NameNode.
-   They do not have knowledge of the overall HDFS file system namespace or the locations of blocks on other DataNodes (except when instructed by the NameNode to replicate a block).
-   Clients interact directly with DataNodes for data transfer (reads/writes) after obtaining block location information and security tokens from the NameNode.

## Scalability and Commodity Hardware
-   DataNodes are designed to run on commodity hardware (standard, inexpensive servers).
-   A Hadoop cluster can be scaled horizontally by adding more DataNodes, which increases both the storage capacity and the I/O bandwidth of HDFS.

## Fault Tolerance
-   If a DataNode fails:
    1.  The NameNode detects the failure via missed heartbeats.
    2.  The NameNode marks the DataNode as dead and no longer sends I/O requests to it.
    3.  Any blocks that were stored on the failed DataNode and now have fewer replicas than their configured replication factor become "under-replicated."
    4.  The NameNode identifies these under-replicated blocks and schedules their re-replication on other live DataNodes to restore the desired replication level.

DataNodes are the workhorses of HDFS, providing the distributed, replicated, and scalable storage for Big Data.

---