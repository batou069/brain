---
tags:
  - hadoop
  - fault_tolerance
  - hdfs
  - mapreduce
  - yarn
  - big_data
  - distributed_systems
  - concept
aliases:
  - Hadoop Failure Handling
  - Robustness in Hadoop
related:
  - "[[HDFS]]"
  - "[[MapReduce]]"
  - "[[YARN]]"
  - "[[Data_Replication]]"
  - "[[HDFS_NameNode]]"
  - "[[HDFS_DataNode]]"
  - "[[Hadoop_Node_Types]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Fault Tolerance in Hadoop

**Fault tolerance** is a critical design principle in [[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop]], enabling it to operate reliably on large clusters of commodity hardware where individual component failures are expected. Hadoop achieves fault tolerance at both the storage layer ([[HDFS|HDFS]]) and the processing layer ([[MapReduce|MapReduce]] and other applications running on [[YARN|YARN]]).

>[!question] How does Hadoop handle hardware failures?
>Hadoop handles hardware failures through a combination of mechanisms primarily within HDFS and the YARN/MapReduce framework:
>
>1.  **[[Data_Replication|Data Replication in HDFS]]:**
>    -   HDFS automatically replicates each data block across multiple [[HDFS_DataNode|DataNodes]] (default replication factor is 3).
>    -   These replicas are typically stored on different racks to protect against rack-level failures.
>    -   If a DataNode fails, the [[HDFS_NameNode|NameNode]] detects this (via missed heartbeats) and initiates re-replication of the blocks that were stored on the failed node from their existing replicas to other live DataNodes, thus maintaining the desired replication factor.
>
>2.  **NameNode High Availability (HA):**
>    -   The NameNode, being the master metadata server for HDFS, is a critical component. To avoid it being a single point of failure (SPOF), Hadoop supports NameNode HA.
>    -   This involves an Active NameNode and one or more Standby NameNodes. The Standby NameNode(s) maintain up-to-date metadata.
>    -   If the Active NameNode fails, a Standby NameNode can quickly take over, minimizing downtime. This usually involves shared storage for the edit log (e.g., JournalNodes) and a coordination service like ZooKeeper for failover.
>
>3.  **MapReduce/YARN Task Failure Handling:**
>    -   **Task Attempts:** If a Map or Reduce task fails (due to hardware issues on the worker node, software bugs in the task, etc.), the ApplicationMaster (AM) for the job can reschedule the task to be re-executed on a different NodeManager, possibly multiple times (configurable number of attempts).
>    -   **NodeManager Failure:** If an entire NodeManager fails, YARN's ResourceManager detects this. All tasks running on that NodeManager are considered failed, and the respective ApplicationMasters will request resources to re-run those tasks on other available NodeManagers.
>    -   **ApplicationMaster Failure:** If an ApplicationMaster itself fails, YARN's ResourceManager can restart it. The restarted AM can then recover the state of its application (e.g., completed tasks) and resume scheduling remaining tasks.
>
>4.  **Speculative Execution (Optional):**
>    -   For MapReduce, Hadoop can optionally enable speculative execution. If a task is running unusually slowly (a "straggler," possibly due to a slow or partially failing node), the framework might proactively launch a duplicate copy of that task on another node. Whichever copy finishes first is taken, and the other is killed. This helps mitigate the impact of slow nodes.
>
>5.  **Checksums for Data Integrity:**
>    -   HDFS uses checksums (e.g., CRC32) for data blocks. When data is written or read, checksums are computed and verified to detect corruption. If corruption is detected in a block, HDFS will attempt to read a replica of that block from another DataNode.
>
>By combining these mechanisms, Hadoop can tolerate common hardware failures (disk failures, node outages, network issues for individual nodes) and continue processing jobs and serving data without significant interruption or data loss.

>[!question] What is robustness in the context of Big Data?
>**Robustness** in the context of Big Data refers to the ability of a system (like Hadoop) to:
>6.  **Maintain correct operation and data integrity** despite component failures (hardware, software, network), errors in input data, or unexpected operating conditions.
>7.  **Continue functioning (possibly in a degraded mode)** rather than failing completely when parts of the system experience issues.
>8.  **Recover gracefully** from failures and return to a normal operational state.
>9.  **Handle variability and imperfections in data** (e.g., missing values, corrupted records, diverse formats) without crashing or producing grossly incorrect results.
>
>Hadoop's fault tolerance mechanisms (data replication, task re-execution, HA for master nodes) are key contributors to its robustness.

## Mechanisms Contributing to Fault Tolerance

[list2tab|#Fault Tolerance Mechanisms]
- HDFS Level
    - **[[Data_Replication|Block Replication]]:**
        -   Each HDFS block is replicated across multiple DataNodes (default 3).
        -   Replicas are often rack-aware (e.g., one replica on one rack, two on another).
        -   If a DataNode goes offline, the NameNode detects this and initiates re-replication of its blocks from available replicas to other DataNodes to maintain the desired replication factor.
    - **[[HDFS_NameNode|NameNode High Availability (HA)]]:**
        -   Uses an Active/Standby NameNode configuration with shared edit logs (often via JournalNodes) and ZooKeeper for failover coordination.
        -   Ensures that if the Active NameNode fails, a Standby can take over quickly, minimizing HDFS downtime.
    - **Checksums:**
        -   HDFS computes checksums for all data written. These checksums are verified when data is read to detect corruption. If a corrupt block is found, the client can retrieve a replica from another DataNode.
    - **Heartbeats and Block Reports:**
        -   DataNodes send regular heartbeats to the NameNode. Missed heartbeats indicate a DataNode failure.
        -   Block reports allow the NameNode to maintain an accurate map of block locations and detect missing or corrupt replicas.
- YARN / MapReduce Level
    - **ApplicationMaster (AM) Resiliency:**
        -   YARN's ResourceManager can restart an ApplicationMaster if it fails. The AM can then recover its state (e.g., which tasks have completed) and resume the application.
    - **Task Re-attempts:**
        -   If an individual Map or Reduce task fails (due to code errors, transient hardware issues on the worker node, etc.), the ApplicationMaster can reschedule it to run again on the same or a different NodeManager, up to a configurable number of attempts.
    - **NodeManager Failure Handling:**
        -   If a NodeManager fails, the ResourceManager marks it as lost. Any tasks running on that NodeManager are considered failed, and their respective ApplicationMasters will request resources to re-run them on other available NodeManagers.
    - **Speculative Execution (MapReduce):**
        -   An optional feature where slow-running tasks (stragglers) may have duplicate copies launched on other nodes. The first one to complete is used, and the other is killed. This helps mitigate issues with "bad" but not entirely failed nodes.
- Job and Task Monitoring
    -   YARN and ApplicationMasters continuously monitor the progress and health of jobs and their constituent tasks.
    -   Detailed logs are collected, which can help diagnose failures.

These mechanisms collectively make Hadoop a robust platform capable of handling failures gracefully, which is essential when working with large clusters of commodity hardware where individual component failures are inevitable.

---