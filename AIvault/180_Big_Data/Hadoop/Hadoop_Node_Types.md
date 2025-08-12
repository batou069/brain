---
tags:
  - hadoop
  - node_types
  - namenode
  - datanode
  - resourcemanager
  - nodemanager
  - hdfs
  - yarn
  - concept
aliases:
  - Hadoop Nodes
  - NameNode
  - DataNode
  - ResourceManager
  - NodeManager
related:
  - "[[_Hadoop_MOC]]"
  - "[[HDFS]]"
  - "[[YARN]]"
  - "[[Hadoop_Cluster_Architecture]]"
  - "[[HDFS_NameNode_Particularity]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Hadoop Node Types

A Hadoop cluster consists of several types of nodes (servers), each playing a specific role in the distributed storage and processing of data. These roles are typically fulfilled by daemon processes running on the machines in the cluster.

The primary node types are associated with [[HDFS|HDFS]] (for storage) and [[YARN|YARN]] (for resource management and processing).

[list2tab|#Node Types & Roles]
- HDFS Nodes
    - **[[HDFS_NameNode|NameNode (Master)]]**
        -   **Role:** The centerpiece of HDFS. It manages the file system namespace (directory tree, file metadata) and regulates access to files by clients. It does **not** store the actual file data itself.
        -   **Responsibilities:**
            -   Maintains the file system tree and the metadata for all files and directories (e.g., permissions, modification times, block locations, replication factor).
            -   Maps file blocks to [[HDFS_DataNode|DataNodes]].
            -   Receives heartbeats and block reports from DataNodes to monitor their health and the blocks they store.
            -   Manages block replication and re-replication upon DataNode failures.
            -   Coordinates file system operations like opening, closing, renaming files and directories.
        -   **Metadata Storage:** Keeps metadata in memory (FsImage for namespace snapshot, EditLog for changes) for fast access. This metadata is also persisted to disk.
        -   **Criticality:** Historically a single point of failure (SPOF). Modern Hadoop supports NameNode High Availability (HA) with an Active NameNode and a Standby NameNode. See [[HDFS_NameNode_Particularity]].
    - **[[HDFS_DataNode|DataNode (Worker/Slave)]]**
        -   **Role:** Stores the actual data blocks of files on its local disks.
        -   **Responsibilities:**
            -   Manages storage attached to the nodes that they run on.
            -   Serves read and write requests from HDFS clients for the blocks it stores.
            -   Performs block creation, deletion, and replication upon instruction from the NameNode.
            -   Sends regular heartbeats to the NameNode to indicate it is alive.
            -   Sends block reports to the NameNode to list the blocks it currently stores.
        -   **Quantity:** There are many DataNodes in a typical Hadoop cluster (tens to thousands).
- YARN Nodes
    - **ResourceManager (Master)**
        -   **Role:** The master daemon for [[YARN|YARN]], responsible for global resource management and scheduling applications across the cluster.
        -   **Responsibilities:**
            -   Tracks live [[#NodeManager (Worker/Slave)|NodeManagers]] and the resources available on them.
            -   Manages the allocation of resources (CPU, memory) to applications in the form of containers.
            -   Contains two main components:
                -   **Scheduler:** Decides how to allocate resources to various running applications based on policies (e.g., CapacityScheduler, FairScheduler). It does not monitor or track application status.
                -   **ApplicationsManager (AsM):** Manages submitted applications, negotiates the first container for the ApplicationMaster, and handles ApplicationMaster restarts on failure.
        -   **High Availability:** ResourceManager can also be configured for HA.
    - **NodeManager (Worker/Slave)**
        -   **Role:** Runs on each worker node in the cluster and manages resources and containers on that specific node.
        -   **Responsibilities:**
            -   Monitors resource usage (CPU, memory, disk, network) on its node.
            -   Reports node health and resource availability to the ResourceManager.
            -   Launches and manages containers (which host application tasks like mappers, reducers, or Spark executors) as instructed by an ApplicationMaster (via the ResourceManager).
            -   Manages log aggregation for tasks running in its containers.
        -   **Quantity:** Runs on most, if not all, worker nodes that also host DataNodes.
- ApplicationMaster (AM) (Per-Application, runs on a worker node)
    -   **Role:** While not a persistent node type like the others, an ApplicationMaster is a crucial framework-specific library that runs for each submitted application (e.g., a MapReduce job, a Spark application). It runs within a YARN container on one of the worker nodes.
    -   **Responsibilities:**
        -   Negotiates resources (containers) from the ResourceManager.
        -   Works with NodeManagers to launch and monitor the application's tasks within these containers.
        -   Tracks task progress and handles task failures.
        -   Communicates status back to the ResourceManager and the client.

## Typical Hadoop Cluster Node Configuration
In a typical Hadoop cluster:
-   **Master Nodes:** Host the NameNode and ResourceManager (and often secondary NameNode or standby ResourceManager for HA). These are critical nodes.
-   **Worker Nodes (Slave Nodes):** Host both DataNode and NodeManager daemons. These nodes provide the storage capacity (via DataNodes) and the computational power (via NodeManagers launching containers) for the cluster.
-   **Client Nodes (Edge Nodes):** Machines from which users submit jobs, interact with HDFS (e.g., using `hadoop fs` commands), and access cluster services. They are not part of the core HDFS/YARN daemons but have Hadoop client libraries installed.

Understanding these roles is key to comprehending how Hadoop achieves distributed storage, parallel processing, and fault tolerance.

---