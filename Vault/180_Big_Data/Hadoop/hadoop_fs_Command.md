---
tags:
  - hadoop
  - hdfs
  - command_line
  - cli
  - file_system
  - concept
  - tool
aliases:
  - hadoop fs
  - hdfs dfs
  - hadoop dfs
related:
  - "[[HDFS]]"
  - "[[_Hadoop_MOC]]"
  - "[[Linux_Commands_File_System]]"
worksheet:
  - WS_BigData_1
date_created: 2025-06-09
---
# `hadoop fs` Command-Line Interface

The `hadoop fs` command is a command-line interface (CLI) tool used to interact with file systems supported by [[180_Big_Data/Hadoop/_Hadoop_MOC|Apache Hadoop]], primarily the [[HDFS|Hadoop Distributed File System (HDFS)]], but also others like local file systems, S3, etc., depending on Hadoop's configuration.

It provides shell-like commands similar to common Unix/Linux file system commands (e.g., `ls`, `cp`, `mkdir`, `rm`) but operates on the distributed file system.

>[!question] What is the difference between `hadoop fs`, `hadoop dfs`, and `hdfs dfs`?
>These commands are often sources of confusion but generally serve the same purpose of interacting with HDFS or other Hadoop-supported file systems.
>
>1.  **`hadoop fs <args>`:**
>    -   This is the **generic file system shell command**. It can interact with any file system that Hadoop supports, as configured in `core-site.xml` (property `fs.defaultFS`). This could be HDFS, the local file system (`file:///`), Amazon S3 (`s3a://`), etc.
>    -   It's generally the **recommended and most portable** command to use for interacting with Hadoop file systems because it respects the default file system configuration.
>
>2.  **`hadoop dfs <args>`:**
>    -   This command was **specifically for HDFS operations**. In older versions of Hadoop, it was distinct from `hadoop fs`.
>    -   However, in modern Hadoop versions, `hadoop dfs` is often **deprecated or acts as an alias for `hadoop fs`**. It's generally advised to use `hadoop fs` instead for consistency and to avoid potential deprecation issues.
>
>3.  **`hdfs dfs <args>`:**
>    -   This command is also **specifically for HDFS operations**. It directly invokes the HDFS shell.
>    -   It is essentially equivalent to `hadoop fs -D fs.defaultFS=hdfs://namenode:port <args>` if your default FS is not HDFS, or simply `hadoop fs <args>` if HDFS is the default.
>    -   It's useful if you want to be explicit about operating on HDFS, regardless of the `fs.defaultFS` setting.
>
>**In summary:**
>-   **`hadoop fs`** is the generic, preferred command.
>-   **`hadoop dfs`** is largely deprecated; use `hadoop fs`.
>-   **`hdfs dfs`** is specific to HDFS and is a valid alternative to `hadoop fs` when you explicitly intend to work with HDFS.
>
>For most use cases, **`hadoop fs` is the best choice.**

## Common `hadoop fs` Commands
Here are some common commands and their typical usage. Assume `hdfs://namenode_host:port` is the prefix for HDFS paths if not the default FS. Often, if HDFS is the default, you can just use paths like `/user/yourname/data`.

[list2tab|#hadoop_fs Commands]
- Listing Files (`ls`)
    - **Syntax:** `hadoop fs -ls <path>`
    - **Purpose:** Lists the contents of a directory or details of a file. Similar to `ls -l` in Unix.
    - **Example:**
        ```bash
        hadoop fs -ls /user/hduser/input
        hadoop fs -ls hdfs://namenode:8020/data/output
        ```
    - **Output:** Shows permissions, replication factor, owner, group, size, modification date, and name.
- Creating Directories (`mkdir`)
    - **Syntax:** `hadoop fs -mkdir [-p] <path>`
    - **Purpose:** Creates a directory. The `-p` option creates parent directories if they don't exist (like `mkdir -p` in Unix).
    - **Example:**
        ```bash
        hadoop fs -mkdir /user/hduser/new_project
        hadoop fs -mkdir -p /data/processed/year=2023/month=10
        ```
- Copying Files/Dirs (`cp`)
    - **Syntax:** `hadoop fs -cp <source_path> ... <destination_path>`
    - **Purpose:** Copies files or directories from one location to another within HDFS, or between HDFS and the local file system.
    - **Example:**
        ```bash
        # Copy within HDFS
        hadoop fs -cp /user/hduser/input/file1.txt /user/hduser/archive/
        # Copy from local to HDFS (see -put)
        # Copy from HDFS to local (see -get)
        ```
- Moving Files/Dirs (`mv`)
    - **Syntax:** `hadoop fs -mv <source_path> ... <destination_path>`
    - **Purpose:** Moves files or directories within HDFS. Can also be used for renaming.
    - **Example:**
        ```bash
        hadoop fs -mv /user/hduser/input/old_file.txt /user/hduser/input/new_file.txt
        hadoop fs -mv /user/hduser/temp_data /user/hduser/processed_data
        ```
- Uploading to HDFS (`put` or `copyFromLocal`)
    - **Syntax:** `hadoop fs -put <local_source_path> ... <hdfs_destination_path>`
    - **Alias:** `hadoop fs -copyFromLocal ...`
    - **Purpose:** Copies files or directories from the local file system to HDFS.
    - **Example:**
        ```bash
        hadoop fs -put ./my_local_file.txt /user/hduser/data/
        hadoop fs -put /home/user/local_dir /user/hduser/hdfs_dir/
        ```
- Downloading from HDFS (`get` or `copyToLocal`)
    - **Syntax:** `hadoop fs -get <hdfs_source_path> <local_destination_path>`
    - **Alias:** `hadoop fs -copyToLocal ...`
    - **Purpose:** Copies files or directories from HDFS to the local file system.
    - **Example:**
        ```bash
        hadoop fs -get /user/hduser/output/part-r-00000 ./results.txt
        hadoop fs -get /user/hduser/data_backup /home/user/hdfs_backups/
        ```
- Displaying File Content (`cat`, `text`)
    - **Syntax:** `hadoop fs -cat <hdfs_path>` or `hadoop fs -text <hdfs_path>`
    - **Purpose:** Displays the content of a file in HDFS to standard output. `-text` can decompress common formats.
    - **Example:**
        ```bash
        hadoop fs -cat /user/hduser/input/sample.txt
        hadoop fs -text /user/hduser/compressed_data.gz
        ```
- Removing Files/Dirs (`rm`)
    - **Syntax:** `hadoop fs -rm [-r] [-skipTrash] <hdfs_path>`
    - **Purpose:** Deletes files. Use `-r` for recursive deletion of directories.
    - **`-skipTrash`:** If Trash is enabled, this option bypasses it for permanent deletion. Otherwise, files are moved to a `.Trash` directory.
    - **Example:**
        ```bash
        hadoop fs -rm /user/hduser/old_output/part-00000
        hadoop fs -rm -r /user/hduser/temp_project_files
        ```
- Disk Usage (`du`, `df`)
    - **`hadoop fs -du [-s] [-h] <path>`:** Displays the size of files and directories contained in the given directory or the length of a file in case it’s just a file.
        -   `-s`: Display an aggregate summary of file sizes instead of individual files.
        -   `-h`: Format file sizes in a human-readable way (e.g., 1K, 2M, 3G).
    - **`hadoop fs -df [-h] <path>`:** Displays free space.
    - **Example:**
        ```bash
        hadoop fs -du -s -h /user/hduser/data
        hadoop fs -df -h /
        ```
- Changing Permissions (`chmod`, `chown`, `chgrp`)
    - **Syntax:** Similar to Unix commands (`hadoop fs -chmod ...`, `hadoop fs -chown ...`, `hadoop fs -chgrp ...`).
    - **Purpose:** Manage file and directory permissions, ownership, and group.
    - **Example:**
        ```bash
        hadoop fs -chmod 755 /user/hduser/scripts/my_script.sh
        hadoop fs -chown new_owner:new_group /user/hduser/data/shared_file.txt
        ```
- Checking File Integrity (`checksum`)
    - **Syntax:** `hadoop fs -checksum <path>`
    - **Purpose:** Retrieves the checksum information for a file.
- Setting Replication Factor (`setrep`)
    - **Syntax:** `hadoop fs -setrep [-R] [-w] <replication_factor> <path>`
    - **Purpose:** Changes the replication factor of a file. `-R` for recursive. `-w` to wait for replication to complete.
    - **Example:**
        ```bash
        hadoop fs -setrep -w 5 /user/hduser/important_data.dat
        ```

>[!question] Explore `hadoop fs` tools. How are they different from the linux commands, such as `du` or `ls`?
>While many `hadoop fs` commands are designed to be syntactically similar to their Linux counterparts for ease of use, there are key differences stemming from the fact that `hadoop fs` operates on a **distributed file system (like HDFS)** rather than a local one:
>
>1.  **Target File System:**
>    -   **Linux commands (`ls`, `du`, `cp`):** Operate on the local file system of the machine where they are executed.
>    -   **`hadoop fs` commands:** Operate on a Hadoop-supported file system, typically HDFS, which is distributed across multiple machines. They interact with the NameNode (for metadata) and DataNodes (for data).
>2.  **Path Specification:**
>    -   **Linux:** Uses standard local paths (e.g., `/home/user/file.txt`, `./data`).
>    -   **`hadoop fs`:** Uses HDFS URIs (e.g., `hdfs://namenode:port/user/data/file.txt`) or paths relative to the HDFS root or user's HDFS home directory (e.g., `/user/data/file.txt`, `input/file.txt`).
>3.  **Underlying Operations:**
>    -   **Linux `ls`:** Reads directory information directly from the local kernel's file system driver.
>    -   **`hadoop fs -ls`:** Client communicates with the HDFS NameNode to get metadata about files and directories.
>    -   **Linux `du`:** Traverses local directories and sums file sizes.
>    -   **`hadoop fs -du`:** Queries the NameNode for file sizes (which stores this metadata).
>4.  **Performance Characteristics:**
>    -   **Linux commands:** Generally fast for local operations.
>    -   **`hadoop fs` commands:** Involve network communication with the NameNode and potentially DataNodes. Can have higher latency but are designed to handle massive scale.
>5.  **File Abstraction:**
>    -   **Linux:** Deals with files as contiguous streams of bytes on local disks.
>    -   **`hadoop fs` (for HDFS):** Deals with files that are split into large blocks and distributed/replicated across multiple DataNodes. The command abstracts this complexity.
>6.  **Specific Hadoop Features:**
>    -   `hadoop fs` has commands specific to HDFS features that have no direct Linux equivalent, such as:
>        -   `-setrep`: Change replication factor.
>        -   `-getmerge`: Merge several HDFS files into a single local file.
>        -   Commands related to HDFS snapshots, trash, quotas.
>7.  **Error Handling and Fault Tolerance:**
>    -   `hadoop fs` operations are designed to work within Hadoop's fault-tolerant environment. For example, if a DataNode is down, it might still be able to access a file's replica.
>8.  **Output Details (`ls`):**
>    -   `hadoop fs -ls` output includes HDFS-specific information like the replication factor for files, which is not present in standard Linux `ls`.
>
>In essence, `hadoop fs` provides a user-friendly shell interface to manage and interact with files in a distributed environment, mimicking familiar Linux commands but with underlying mechanisms tailored for systems like HDFS.

The `hadoop fs` (or `hdfs dfs`) command set is essential for managing data within the Hadoop ecosystem.

---