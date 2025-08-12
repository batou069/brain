---
tags:
  - hadoop
  - yarn
  - resource_management
  - job_scheduling
  - big_data
  - distributed_computing
  - concept
aliases:
  - Yet Another Resource Negotiator
  - Hadoop YARN
related:
  - "[[_Hadoop_MOC]]"
  - "[[MapReduce]]"
  - "[[Apache_Spark_MOC]]"
  - "[[Hadoop_Node_Types]]"
  - "[[Hadoop_Cluster_Architecture]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# YARN (Yet Another Resource Negotiator)

## Definition
**YARN (Yet Another Resource Negotiator)** is the resource management and job scheduling layer in [[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop]] (introduced in Hadoop 2.0). Its fundamental idea is to split up the two major responsibilities of the JobTracker from Hadoop 1.0 (MapReduce v1) – resource management and job scheduling/monitoring – into separate daemons.

YARN provides a generic platform capable of running various distributed applications beyond just [[MapReduce|MapReduce]] (e.g., Apache Spark, Apache Tez, Apache Flink).

>[!question] What is the role of YARN? When does it "negotiate resources"?
>
>**Role of YARN:**
>The primary role of YARN is to **manage and allocate cluster resources** (CPU, memory, disk, network) among various applications running in the Hadoop cluster and to **schedule and monitor the execution of tasks** for these applications.
>
>Key responsibilities include:
>1.  **Global Resource Management:** The ResourceManager component of YARN has a global view of all available resources in the cluster.
>2.  **Application Lifecycle Management:** It manages the lifecycle of applications submitted to the cluster, from submission to completion.
>3.  **Resource Negotiation and Allocation:** Applications request resources from YARN, and YARN allocates these resources in the form of "containers" on available nodes.
>4.  **Scalability:** YARN is designed to scale to thousands of nodes.
>5.  **Multi-tenancy & Support for Diverse Workloads:** YARN allows multiple different application frameworks (MapReduce, Spark, Flink, etc.) to run concurrently on the same Hadoop cluster, sharing resources efficiently.
>6.  **Job Scheduling:** It includes a pluggable scheduler that determines how resources are allocated to competing applications and queues (e.g., Capacity Scheduler, Fair Scheduler).
>
>**When does YARN "negotiate resources"?**
>Resource negotiation is a continuous process that happens primarily when:
>7.  **Application Submission:** When a new application (e.g., a MapReduce job, a Spark application) is submitted to the cluster, its **ApplicationMaster (AM)** is launched. The AM's first responsibility is to register with the ResourceManager.
>8.  **ApplicationMaster Requests:** The ApplicationMaster then **negotiates with the ResourceManager** for the resources (containers) needed to run the application's tasks (e.g., mappers and reducers for a MapReduce job; executors for Spark).
>    -   The AM sends resource requests to the ResourceManager, specifying its needs (e.g., amount of memory, number of CPU cores per container, locality preferences).
>9.  **ResourceManager Allocation:** The ResourceManager's Scheduler component evaluates these requests based on available resources, queue capacities, fairness policies, and priorities.
>    -   When resources become available on [[Hadoop_Node_Types|NodeManagers]], the ResourceManager allocates a **container** (a bundle of resources) to the ApplicationMaster.
>10.  **Task Launch:** The ApplicationMaster then contacts the appropriate NodeManager(s) to launch tasks within the allocated containers.
>11.  **Dynamic Requests:** An ApplicationMaster can dynamically request more resources or release unneeded resources during the application's lifecycle, leading to further negotiation with the ResourceManager.
>
>So, resource negotiation is an interactive dialogue primarily between the ApplicationMaster (representing the application's needs) and the ResourceManager (managing cluster-wide resources). This negotiation happens at the start of an application and can continue throughout its execution as resource needs change or become available.

## YARN Architecture Components
YARN has a master/slave architecture with the following key components:

[list2tab|#YARN Components]
- ResourceManager (Master)
    - **Location:** Runs on a master node.
    - **Responsibilities:**
        -   Manages global resource allocation across all applications in the cluster.
        -   Tracks live [[Hadoop_Node_Types|NodeManagers]] and available resources.
        -   Accepts job submissions.
        -   Consists of two main components:
            -   **Scheduler:** Responsible for allocating resources to various running applications subject to constraints of capacities, queues etc. It is a pure scheduler in the sense that it performs no monitoring or tracking of status for the application. It does not guarantee restarting tasks that failed either due to hardware failures or application failures. The Scheduler performs its scheduling function based on the resource requirements of the applications. It has a pluggable policy (e.g., CapacityScheduler, FairScheduler).
            -   **ApplicationsManager (AsM):** Responsible for accepting job submissions, negotiating the first container for executing the application-specific ApplicationMaster, and providing the service for restarting the ApplicationMaster container on failure.
- NodeManager (Slave)
    - **Location:** Runs on each worker/slave node in the cluster.
    - **Responsibilities:**
        -   Manages resources on its individual node (CPU, memory, disk, network).
        -   Monitors resource usage of containers on its node.
        -   Reports its node status and resource availability to the ResourceManager.
        -   Launches and manages containers on its node as instructed by the ApplicationMaster (via the ResourceManager).
        -   Manages log aggregation for applications running in its containers.
- ApplicationMaster (AM) (Per-Application)
    - **Location:** Runs in a container on one ofthe worker nodes. There is one ApplicationMaster per submitted application.
    - **Responsibilities:**
        -   Manages the lifecycle of a single application.
        -   Negotiates with the ResourceManager's Scheduler for necessary resources (containers).
        -   Once resources are allocated, it works with NodeManagers to launch tasks within those containers.
        -   Monitors the status of its tasks and can request re-execution of failed tasks.
        -   Specific to the application framework (e.g., MapReduce AM, Spark AM).
- Container
    - **Concept:** A **container** represents an allocation of resources (CPU cores, memory, etc.) on a specific NodeManager.
    - **Execution Unit:** Tasks of an application (e.g., a map task, a reduce task, a Spark executor task) run within containers.
    - The ApplicationMaster requests containers from the ResourceManager, and NodeManagers launch these containers.

## YARN Workflow (Simplified)
1.  **Client Submission:** A client submits an application (e.g., a MapReduce job) to the ResourceManager.
2.  **AM Launch:** The ResourceManager (via ApplicationsManager) negotiates with a NodeManager to launch the ApplicationMaster (AM) for that specific application in a container.
3.  **AM Registration:** The AM registers with the ResourceManager.
4.  **Resource Negotiation:** The AM calculates its resource needs and sends resource requests (for containers) to the ResourceManager's Scheduler.
5.  **Container Allocation:** The Scheduler allocates available containers on NodeManagers to the AM based on its policy.
6.  **Task Execution:** The AM contacts the relevant NodeManagers to launch application tasks within the allocated containers.
7.  **Progress Monitoring:** The AM monitors its tasks and reports progress/status back to the ResourceManager and the client.
8.  **Resource Release:** Upon task completion, the AM can release containers back to the ResourceManager.
9.  **Application Completion:** Once all tasks are done, the AM unregisters from the ResourceManager, and its own container is released.

By decoupling resource management from specific processing frameworks, YARN makes Hadoop a more general-purpose data processing platform.

---