---
tags:
  - hadoop
  - hdfs
  - distributed_file_system
  - big_data
  - storage
  - concept
aliases:
  - Hadoop Distributed File System
  - HDFS Architecture
related:
  - "[[_Hadoop_MOC]]"
  - "[[HDFS_NameNode]]"
  - "[[HDFS_DataNode]]"
  - "[[Hadoop_Node_Types]]"
  - "[[Data_Replication]]"
  - "[[Hadoop_Fault_Tolerance]]"
  - "[[hadoop_fs_Command]]"
  - "[[Sharding_vs_Partitioning]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# HDFS (Hadoop Distributed File System)

## Definition
The **Hadoop Distributed File System (HDFS)** is a distributed, scalable, and fault-tolerant file system designed to store very large datasets (terabytes to petabytes) across clusters of commodity hardware. It is a core component of the [[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop]] framework and provides the storage layer for [[MapReduce|MapReduce]] processing and other Hadoop ecosystem tools. [3]

HDFS is optimized for batch processing of large files with a write-once-read-many access model. It prioritizes high throughput for sequential data access over low-latency random access.

>[!question] Why does Hadoop have a file system?
>Hadoop has its own distributed file system (HDFS) for several key reasons, primarily to handle the unique challenges posed by [[Big_Data_Definition_Characteristics|Big Data]] processing in a distributed environment:
>1.  **Store Massive Datasets:** Traditional file systems on single machines cannot store the terabytes or petabytes of data that Hadoop is designed to process. HDFS allows data to be distributed across hundreds or thousands of commodity servers, providing vast storage capacity.
>2.  **Enable Parallel Processing ([[MapReduce|MapReduce]]):** HDFS works in tandem with processing frameworks like MapReduce. By distributing data across many nodes, computations can be performed in parallel on local subsets of data, significantly speeding up processing. This is crucial for [[Data_Locality_Hadoop|data locality]].
>3.  **[[Hadoop_Fault_Tolerance|Fault Tolerance and High Availability]]:** Commodity hardware is prone to failures. HDFS provides fault tolerance through [[Data_Replication|data replication]] (storing multiple copies of data blocks on different nodes) and automatic recovery mechanisms. If a node fails, data can still be accessed from its replicas, and the system can re-replicate lost blocks.
>4.  **High Throughput for Sequential Access:** HDFS is optimized for streaming large files sequentially, which is typical for batch processing jobs like MapReduce. It achieves high aggregate read/write bandwidth by parallelizing I/O across many disks and nodes.
>5.  **Scalability:** HDFS can scale horizontally by adding more [[HDFS_DataNode|DataNodes]] to the cluster, increasing both storage capacity and processing power.
>6.  **Cost-Effectiveness:** It's designed to run on clusters of inexpensive commodity hardware, making large-scale storage and processing more affordable than relying on specialized, high-end storage systems.
>7.  **Abstraction for Distributed Storage:** HDFS provides a familiar file system interface (though not fully POSIX-compliant) that abstracts away the complexities of distributed storage, making it easier for applications to access and manage data spread across a cluster.

## HDFS Architecture
HDFS has a master/slave architecture:

[list2tab|#HDFS Components]
- NameNode (Master)
	[[HDFS_NameNode|NameNode (Master)]]
    - **Role:** Manages the file system namespace (directory tree, file metadata like permissions, modification times, block locations). It keeps track of which [[HDFS_DataNode|DataNodes]] store the blocks for each file.
    - **Metadata:** Stores the file system metadata in memory for fast access (FsImage and EditLog).
    - **Client Interaction:** Clients contact the NameNode to locate data blocks or to perform file system operations (create, delete, rename files/directories).
    - **Single Point of Failure (Historically):** In older Hadoop versions, the NameNode was a single point of failure. Modern Hadoop has High Availability (HA) configurations with Active and Standby NameNodes.
    - See [[HDFS_NameNode_Particularity|Particularity of the NameNode]].
- DataNodes (Slaves)
	[[HDFS_DataNode|DataNodes (Slaves)]]
    - **Role:** Store the actual data blocks on the local disks of the machines they run on.
    - **Block Operations:** Perform read and write requests from clients, as instructed by the NameNode or directly by clients for data transfer.
    - **Block Reports & Heartbeats:** Periodically send heartbeats and block reports to the NameNode to indicate they are alive and to report the list of blocks they store.
- Blocks
    - **Concept:** HDFS splits large files into fixed-size **blocks** (typically 128MB or 256MB by default in modern Hadoop, configurable). These blocks are the basic unit of storage and replication.
    - **Distribution:** Blocks of a file are distributed across multiple DataNodes in the cluster.
    - **Replication:** Each block is replicated (by default, 3 times) on different DataNodes to ensure [[Hadoop_Fault_Tolerance|fault tolerance]] and data availability. The NameNode manages replica placement.

## Key Features of HDFS
[list2tab|#HDFS Features]
- Distributed Storage
    -   Files are broken into large blocks and distributed across many machines in a cluster.
- [[Data_Replication|Data Replication]]
    -   Each block is replicated multiple times (default 3) on different DataNodes, often on different racks, to protect against data loss due to hardware failure.
    -   Ensures high data availability.
- [[Hadoop_Fault_Tolerance|Fault Tolerance]]
    -   The NameNode monitors DataNodes via heartbeats. If a DataNode fails, the NameNode initiates re-replication of its blocks from existing replicas to other live DataNodes.
    -   How Hadoop handles hardware failures is primarily through this replication and re-replication mechanism.
- High Throughput for Large Files
    -   Optimized for streaming reads of large files. Parallel I/O from multiple DataNodes contributes to high aggregate bandwidth.
- Scalability
    -   Can scale to store petabytes of data and run on thousands of nodes by adding more DataNodes.
- [[Data_Locality_Hadoop|Data Locality]]
    -   Hadoop tries to schedule [[MapReduce|MapReduce]] tasks on the DataNodes where the data blocks reside to minimize network traffic by moving computation to the data. See [[Move_Computation_vs_Move_Data|Is it cheaper to move data or computation?]].
- Commodity Hardware
    -   Designed to run on clusters of inexpensive, standard servers.
- Write-Once-Read-Many (WORM) Access Model
    -   Optimized for files that are written once and then read many times. Appends are supported, but in-place modifications to existing data within a file are generally not (or are very complex).
- File System Namespace
    -   Provides a hierarchical file system similar to traditional file systems, with directories and files.
    -   Accessible via [[hadoop_fs_Command|`hadoop fs` command-line interface]] or APIs.

## HDFS Read/Write Operations (Simplified)

**Read Operation:**
1.  Client contacts NameNode for block locations of the desired file.
2.  NameNode returns a list of DataNodes for each block (prioritizing local or nearby replicas).
3.  Client reads blocks directly from the chosen DataNodes in parallel.

**Write Operation:**
1.  Client contacts NameNode to create a new file entry in the namespace.
2.  NameNode determines DataNodes for the first block and provides their addresses to the client.
3.  Client writes data to the first DataNode in the pipeline. This DataNode forwards the data to the second DataNode, which forwards to the third (for a replication factor of 3).
4.  Acknowledgements flow back through the pipeline.
5.  Process repeats for subsequent blocks. NameNode is updated with block locations.

>[!question] How many writers/readers can work on a Hadoop cluster?
>HDFS is designed for high concurrent read access and can support many simultaneous readers. The number of readers is primarily limited by the aggregate I/O bandwidth of the DataNodes and the NameNode's capacity to serve block locations.
>
>For writers, HDFS is optimized for a smaller number of concurrent writers, especially for a single file.
>-   **Single Writer per File (Strict):** Traditionally, HDFS enforces a strict single-writer-per-file model at any given time for appends or new files. Once a file is closed, it's typically immutable (though appends were added later).
>-   **Concurrent Writes to Different Files:** Many clients can write to *different* files simultaneously.
>-   **Append Support:** HDFS supports appending to existing files, but this also generally involves a single appender at a time for a given file to maintain consistency.
>
>The bottleneck for writes can also be the NameNode, as it has to manage metadata for new blocks and files. While HDFS can handle many readers, its architecture is less suited for high-concurrency, low-latency random writes, which is where NoSQL databases like [[Apache_HBase|HBase]] (that run on top of HDFS) come into play for different access patterns.

>[!question] Is Hadoop a NAS?
>No, Hadoop (specifically HDFS) is **not a Network Attached Storage (NAS)** in the traditional sense, although it provides network-accessible storage.
>
>-   **NAS:** Typically a dedicated hardware device (or specialized server) that provides file-based storage services to other devices on the network using standard network file sharing protocols like NFS (Network File System) or CIFS/SMB (Common Internet File System/Server Message Block). NAS devices often present a POSIX-like file system interface and are designed for general-purpose file sharing with lower latency and more random access patterns. They usually have tighter consistency models.
>-   **HDFS:** A software-based distributed file system designed to run on clusters of commodity servers. It has its own specialized protocols and APIs. While it provides a file system abstraction, it's optimized for:
    -   Very large files.
    -   Streaming data access (high throughput for sequential reads).
    -   Write-once-read-many semantics.
    -   Fault tolerance through replication across many nodes.
    -   Integration with distributed processing frameworks like MapReduce (data locality).
>
>Key differences:
>-   **Hardware:** NAS is often specialized hardware; HDFS runs on general-purpose servers.
>-   **Protocols:** NAS uses standard network file protocols; HDFS uses its own.
>-   **Access Patterns:** NAS supports general-purpose file access with random I/O; HDFS is optimized for large sequential reads.
>-   **POSIX Compliance:** NAS systems aim for high POSIX compliance; HDFS is not fully POSIX compliant (e.g., file modification is restricted).
>-   **Scale:** HDFS is designed for much larger scale (petabytes) and higher aggregate throughput for specific workloads than typical NAS.
>-   **Primary Use Case:** NAS is for general network file sharing; HDFS is for storing and processing Big Data with distributed frameworks.

While both provide network storage, their design goals, architecture, and optimal use cases are quite different.

---