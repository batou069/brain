---
tags:
  - big_data
  - database
  - distributed_systems
  - sharding
  - partitioning
  - data_storage
  - concept
aliases:
  - Database Sharding
  - Data Partitioning
related:
  - "[[_Big_Data_MOC]]"
  - "[[HDFS]]"
  - "[[NoSQL_Databases]]"
  - "[[Scalability_Big_Data]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# Sharding vs. Partitioning

**Sharding** and **Partitioning** are both techniques used to break down large datasets or databases into smaller, more manageable pieces. This is done to improve performance, scalability, and manageability. While the terms are often used interchangeably and their precise definitions can vary, there are common distinctions.

## Partitioning
**Partitioning** generally refers to the process of dividing a large logical data structure (like a database table or an index) into smaller, independent parts, while still often being managed as a single logical entity within the *same database instance or server*.

[list2tab|#Partitioning Aspects]
- Definition & Scope
    - **Definition:** Dividing a database object (e.g., a table) into smaller pieces based on a **partitioning key** or scheme.
    - **Scope:** Typically occurs *within a single database server or instance*. The database management system (DBMS) is aware of the partitions and routes queries appropriately.
- Types of Partitioning
    - **Horizontal Partitioning:** Divides a table into multiple smaller tables (partitions) that have the same columns but contain different rows. Rows are distributed based on a partitioning key applied to one or more columns.
        -   **Range Partitioning:** Rows are partitioned based on a range of values in the partitioning key (e.g., sales data partitioned by month or year).
        -   **List Partitioning:** Rows are partitioned based on a list of discrete values in the partitioning key (e.g., customer data partitioned by region: 'North', 'South', 'East', 'West').
        -   **Hash Partitioning:** Rows are partitioned based on a hash value computed from the partitioning key, distributing data evenly across partitions.
        -   **Composite Partitioning:** Combines two or more partitioning methods (e.g., range-hash).
    - **Vertical Partitioning:** Divides a table into multiple tables where each new table contains a subset of the original table's columns, along with the primary key or a unique row identifier to link them back.
        -   Used when some columns are accessed frequently and others rarely, or for security reasons.
- Purpose & Benefits
    - **Improved Performance:** Queries that access only a subset of data can scan fewer partitions, leading to faster query execution (partition pruning).
    - **Enhanced Manageability:** Operations like backups, maintenance, or data archiving can be performed on individual partitions.
    - **Improved Availability (Sometimes):** If one partition is unavailable, other partitions might still be accessible (depends on DBMS).
    - **Data Lifecycle Management:** Easier to roll in/out old data by adding/dropping partitions.
- Example
    - A `SalesOrders` table in a single relational database server might be horizontally partitioned by `OrderDate` (e.g., one partition per month). Queries for a specific month only scan that month's partition.

## Sharding
**Sharding** (a specific type of horizontal partitioning) typically refers to distributing these smaller pieces (shards) **across multiple database servers or instances**. Each server (shard) holds a distinct subset of the data, and the system as a whole operates as a single logical database.

[list2tab|#Sharding Aspects]
- Definition & Scope
    - **Definition:** A database architecture pattern where data is horizontally partitioned into independent databases (shards), and each shard is hosted on a separate database server instance or cluster.
    - **Scope:** Involves *multiple database servers/instances*, often in a distributed environment. This is a key differentiator from partitioning that occurs within a single server.
- Key Characteristics
    - **Shared-Nothing Architecture (Often):** Each shard is typically self-contained with its own CPU, memory, and disk, and does not share these resources with other shards.
    - **Horizontal Scaling (Scale-Out):** Allows the database to scale by adding more shards (servers) to distribute the load and data.
    - **Data Distribution:** Data is distributed across shards based on a **shard key**.
    - **Query Routing:** A mechanism (e.g., a routing layer, application logic, or a sharding-aware proxy) is needed to direct queries to the appropriate shard(s).
- Purpose & Benefits
    - **High Scalability:** Enables massive scaling of read and write throughput by distributing load across many servers.
    - **Improved Performance:** Queries can often be localized to a single shard or a small subset of shards.
    - **Increased Availability/Fault Tolerance:** If one shard fails, other shards remain operational. The impact is limited to the data on the failed shard.
    - **Geographic Distribution:** Shards can be located in different geographical regions to reduce latency for users or for disaster recovery.
- Challenges
    - **Increased Complexity:** Managing a sharded database is more complex (deployment, monitoring, backups, schema changes).
    - **Cross-Shard Queries:** Queries that need data from multiple shards can be complex and less performant. Joins across shards are particularly challenging.
    - **Data Rebalancing:** If a shard becomes too hot (overloaded) or data distribution becomes uneven, re-sharding or rebalancing data can be difficult.
    - **Transactional Consistency:** Maintaining ACID properties across shards can be challenging (often requiring distributed transactions or eventual consistency models).
    - **Choice of Shard Key:** Crucial for performance and even data distribution. A poor shard key can lead to hot spots.
- Example
    - A large social media application might shard its `Users` table by `UserID`. Users with IDs 1-1,000,000 might be on Shard A, 1,000,001-2,000,000 on Shard B, and so on. Each shard is a separate database server.

## Key Differences Summarized
[list2mdtable|#Sharding vs Partitioning]
- Feature
    - Partitioning
        - Sharding
- **Primary Goal**
    - Improve performance and manageability *within a single database server*.
        - Achieve massive scalability and availability by *distributing data across multiple servers*.
- **Scope**
    - Typically within one database instance/server.
        - Across multiple database instances/servers (distributed).
- **Hardware**
    - Data resides on the storage of a single server (though possibly different physical disks managed by that server).
        - Data resides on the storage of multiple, independent servers.
- **Scaling Type**
    - Primarily improves performance on existing hardware; doesn't inherently scale out compute/storage capacity beyond the single server's limits.
        - Enables horizontal scaling (scale-out) by adding more servers.
- **Complexity**
    - Managed by the DBMS, relatively less complex than sharding.
        - Significantly more complex to design, implement, and manage. Requires application-level awareness or specialized middleware.
- **Fault Isolation**
    - Failure of the single server affects all partitions.
        - Failure of one shard typically only affects data on that shard; other shards remain available.

**Analogy:**
-   **Partitioning:** Like having different sections (e.g., Fiction, Non-Fiction, Children's) within a single large library building. Books are organized, but all are under one roof.
-   **Sharding:** Like having multiple independent library branches across a city. Each branch holds a subset of the total collection.

In essence, sharding is a specific form of horizontal partitioning taken to a distributed, multi-server level to achieve greater scalability and availability than what a single server (even with internal partitioning) can offer. [[HDFS|HDFS]] internally partitions files into blocks and distributes these blocks across multiple DataNodes, which is conceptually similar to sharding at the file system level.

---