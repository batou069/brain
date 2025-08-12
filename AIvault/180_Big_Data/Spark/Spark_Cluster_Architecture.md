---
tags:
  - spark
  - architecture
  - cluster
  - driver
  - executor
  - worker
  - cluster_manager
  - concept
aliases:
  - Spark Cluster Components
  - Spark Execution Model
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Spark_Cluster_Manager]]"
  - "[[PySpark_SparkSession_SparkContext|SparkSession and SparkContext]]"
worksheet:
  - WS_Spark_1
date_created: 2025-06-11
---
# Spark Cluster Architecture

Apache Spark applications run as independent sets of processes on a cluster, coordinated by the `SparkContext` object in your main program (called the **driver program**).

To run on a cluster, the SparkContext connects to a type of **[[Spark_Cluster_Manager|cluster manager]]**, which is responsible for allocating resources across applications. Once connected, Spark acquires **executors** on nodes in the cluster, which are processes that run computations and store data for your application. Next, it sends your application code (defined by JAR or Python files passed to SparkContext) to the executors. Finally, SparkContext sends tasks to the executors to run.

## Key Components

[d2]
```d2
direction: right
shape: sequence_diagram

DriverProgram: "Driver Program\n(Your Application, SparkContext)" {
  shape: person # Represents the user's main code
  style.fill: "#E0F2F7"
}

ClusterManager: "Cluster Manager\n(Standalone, YARN, Mesos, K8s)" {
  shape: process
  style.fill: "#FFF9C4"
}

WorkerNode1: "Worker Node 1" {
  shape: package
  style.fill: "#C8E6C9"
  Executor1: "Executor 1\n(JVM, Tasks, Cache)" {
    shape: process
    style.fill: "#A5D6A7"
  }
}

WorkerNode2: "Worker Node 2" {
  shape: package
  style.fill: "#C8E6C9"
  Executor2: "Executor 2\n(JVM, Tasks, Cache)" {
    shape: process
    style.fill: "#A5D6A7"
  }
}

WorkerNodeN: "Worker Node N ..." {
  shape: package
  style.fill: "#C8E6C9"
  ExecutorN: "Executor N ..." {
    shape: process
    style.fill: "#A5D6A7"
  }
}

DriverProgram -> ClusterManager: "1. Requests Resources (Executors)"
ClusterManager -> WorkerNode1.Executor1: "2. Launches Executor"
ClusterManager -> WorkerNode2.Executor2: "2. Launches Executor"
ClusterManager -> WorkerNodeN.ExecutorN: "2. Launches Executor"

WorkerNode1.Executor1 -> DriverProgram: "3. Registers with Driver"
WorkerNode2.Executor2 -> DriverProgram: "3. Registers with Driver"
WorkerNodeN.ExecutorN -> DriverProgram: "3. Registers with Driver"

DriverProgram -> WorkerNode1.Executor1: "4. Sends Application Code & Tasks"
DriverProgram -> WorkerNode2.Executor2: "4. Sends Application Code & Tasks"
DriverProgram -> WorkerNodeN.ExecutorN: "4. Sends Application Code & Tasks"

WorkerNode1.Executor1 -> DriverProgram: "5. Sends Task Results"
WorkerNode2.Executor2 -> DriverProgram: "5. Sends Task Results"
WorkerNodeN.ExecutorN -> DriverProgram: "5. Sends Task Results"


style DriverProgram { icon: "🧑‍💻" }
style ClusterManager { icon: "⚙️" }
style WorkerNode1 { icon: "🖥️" }
style WorkerNode2 { icon: "🖥️" }
style WorkerNodeN { icon: "🖥️" }
style Executor1 { icon: "🔥" }
style Executor2 { icon: "🔥" }
style ExecutorN { icon: "🔥" }
```

[list2tab|#Spark Components]
- Driver Program
    -   **Role:** The process running the `main()` function of your Spark application and creating the [[PySpark_SparkSession_SparkContext|`SparkContext`]] (or `SparkSession`).
    -   **Responsibilities:**
        -   Coordinates the overall execution of the Spark application.
        -   Connects to a [[Spark_Cluster_Manager|Cluster Manager]] to request resources.
        -   Analyzes, distributes, and schedules tasks across [[#Executor|Executors]].
        -   Collects results from executors.
        -   Hosts the Spark Web UI for monitoring the application.
    -   The driver program must be network-addressable from the worker nodes.
- Cluster Manager
	[[Spark_Cluster_Manager|Cluster Manager]]
    -   **Role:** An external service responsible for acquiring and managing cluster resources (CPU, memory) for Spark applications.
    -   **Types:**
        -   **Standalone:** A simple cluster manager included with Spark. Good for basic setups.
        -   **Apache Mesos:** A general-purpose cluster manager.
        -   **[[YARN|Hadoop YARN]]:** The resource manager from Hadoop. Very common when Spark runs in Hadoop environments.
        -   **Kubernetes:** An open-source system for automating deployment, scaling, and management of containerized applications. Increasingly popular for running Spark.
    -   Spark is agnostic to the underlying cluster manager.
- Worker Node
    -   **Role:** Any node in the cluster that can run application code. It hosts one or more [[#Executor|Executors]].
    -   **Responsibilities:**
        -   Runs the Executor processes.
        -   Reports available resources to the Cluster Manager (or directly to the Driver in Standalone mode sometimes).
- Executor
    -   **Role:** A process launched for an application on a worker node.
    -   **Responsibilities:**
        -   Executes the tasks assigned to it by the Driver program.
        -   Stores data in memory (caching [[RDD_Resilient_Distributed_Dataset|RDDs]] or [[Spark_DataFrame_SQL|DataFrames]]) or on disk.
        -   Communicates results back to the Driver.
    -   Each application has its own set of executors, which typically run for the entire lifetime of the application. Executors run tasks in parallel (multiple tasks per executor if it has multiple cores).
- Task
    -   **Role:** A unit of work that will be sent to one executor to be performed on a partition of data.
    -   The Driver breaks down a Spark job (triggered by an [[Spark_Transformations_Actions|action]]) into stages, and each stage into tasks.

## Application Execution Flow
1.  The user submits a Spark application (e.g., a Python script using PySpark, a JAR file).
2.  The **Driver Program** starts, and its `SparkContext` (or `SparkSession`) connects to the **Cluster Manager**.
3.  The Cluster Manager allocates resources by launching **Executors** on **Worker Nodes**.
4.  The Driver Program sends the application code (e.g., Python files, JARs) and serialized tasks to the Executors.
5.  Executors run the tasks on their assigned data partitions and send results back to the Driver.
6.  The Driver Program collects results or writes them to an external storage system.
7.  Once the application's `main()` method finishes or `SparkContext.stop()` is called, all executors are terminated, and resources are released back to the Cluster Manager.

>[!question] What is the purpose of a Spark Cluster?
>The purpose of a Spark Cluster is to enable **fast and scalable distributed processing of large datasets**. Key goals include:
>1.  **Parallel Processing:** To execute computations in parallel across multiple machines (worker nodes), significantly speeding up data processing tasks compared to a single machine.
>2.  **Handling Big Data:** To process datasets that are too large to fit into the memory or be efficiently processed by a single computer. Data is distributed across the cluster.
>3.  **Scalability:** To allow applications to scale horizontally by adding more worker nodes to the cluster, increasing both processing power and storage capacity (if using distributed storage like HDFS).
>4.  **Fault Tolerance (for RDDs/DataFrames):** Spark is designed to recover from worker node failures by re-computing lost partitions of RDDs or DataFrames based on their lineage (the [[Spark_DAG_Scheduler|DAG]] of transformations).
>5.  **In-Memory Computing:** A key advantage of Spark is its ability to keep intermediate data in memory across multiple operations, which drastically reduces disk I/O and speeds up iterative algorithms and interactive queries compared to systems like traditional MapReduce.
>6.  **Unified Analytics Engine:** To provide a single platform for various data processing workloads, including batch processing, SQL queries, stream processing, machine learning, and graph analytics.

Spark's cluster architecture is designed to be flexible and efficient for a wide range of Big Data processing tasks.

---