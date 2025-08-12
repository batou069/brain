---
tags:
  - 10_linux
  - concept
  - storage
aliases:
  - Filesystem
related:
  - "[[Operating_System]]"
  - "[[Kernel]]"
  - "[[Hard_disk]]"
  - "[[SSD]]"
  - "[[inode]]"
  - "[[File]]"
  - "[[Directory]]"
  - "[[Mounting]]"
  - "[[Disk_partition]]"
worksheet:
  - WS
date_created: 2025-04-10
---
# File System

## Definition

A **File System** is a method and data structure that an [[Operating_System]]'s [[Kernel]] uses to control how data is stored and retrieved on a storage device (like a [[Hard_disk]] or [[SSD]]). It organizes data into [[File|files]] and [[Directory|directories]], manages [[Metadata]] about these items, and tracks available space.

## Key Aspects / Characteristics

- **Organization:** Provides a hierarchical structure (tree) of [[Directory|directories]] and [[File|files]].
- **Naming:** Allows files and directories to be identified by [[Filename|filenames]].
- **Metadata:** Stores information about files, such as size, permissions, timestamps, and location on the storage device (often using structures like [[inode|inodes]]).
- **Space Management:** Tracks which parts of the storage device are free and which are allocated to files. See [[Space_allocation]].
- **API:** Provides [[System_call|system calls]] for applications to create, read, write, delete, and manage files and directories (e.g., [[open]], [[read]], [[write]], [[close]]).
- **Journaling:** Some file systems ([[ext3]], [[ext4]], [[NTFS]], [[JFS]]) use [[Journaling]] to improve reliability and speed up recovery after crashes.

## Examples / Use Cases

- **Linux:** [[ext4]], [[BTRFS]], XFS, [[JFS]]
- **Windows:** [[NTFS]], [[FAT-32]], exFAT
- **macOS:** APFS, HFS+
- **Network:** [[NFS]], SMB/CIFS
- **Older:** [[FAT-16]]

## Related Concepts
- [[File]] (The basic unit of storage)
- [[Directory]] (Container for files and other directories)
- [[inode]] (Data structure holding metadata in Unix-like systems)
- [[Metadata]] (Data about data)
- [[Mounting]] (Making a file system accessible at a specific point)
- [[Disk_partition]] (Dividing a physical disk)
- [[Journaling]] (Reliability feature)
- [[Space_allocation]] (How file data is placed on disk)
- Specific types: [[ext4]], [[BTRFS]], [[NTFS]], [[FAT-16]], [[FAT-32]], [[NFS]], [[JFS]]

## Questions / Further Study
>[!question] What is a file in Linux? (WS5)
> In Linux (and Unix-like systems), almost everything is treated as a [[File]]. This includes regular data files, [[Directory|directories]], [[Block_device|block devices]] (like disks), [[Character_device|character devices]] (like terminals), sockets, and pipes. They are all accessed through the file system interface using [[File_descriptor|file descriptors]].

>[!question] What is the directory structure of a Linux system? (WS12)
> Linux follows the Filesystem Hierarchy Standard (FHS), which defines standard directories like `/bin` (essential user binaries), `/sbin` (system binaries), `/etc` (configuration files), `/home` (user home directories), `/var` (variable files like logs), `/tmp` (temporary files), `/usr` (user programs and data), `/lib` (shared libraries), `/dev` (device files), `/proc` (process information [[File_System|filesystem]]), `/boot` (boot loader files).

---
**Source:** Worksheet WS1, WS5, WS12