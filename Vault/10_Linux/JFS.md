---
tags:
  - linux
  - filesystem
  - concept
  - storage
  - journaling
aliases:
  - Journaled File System (IBM)
related:
  - "[[File_System]]"
  - "[[Journaling]]"
  - "[[ext3]]"
  - "[[ext4]]"
  - "[[XFS]]"
  - "[[BTRFS]]"
  - "[[AIX]]"
  - "[[OS/2]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# JFS (Journaled File System)

## Definition

**JFS (Journaled File System)** refers to a 64-bit [[Journaling|journaling]] [[File_System]] originally developed by IBM for its AIX operating system. It was later ported to OS/2 and subsequently open-sourced and made available for Linux. There are technically two generations (JFS1 on AIX, JFS2 often just called JFS on Linux/OS/2). When discussed in the Linux context, it usually refers to JFS2.

## Key Features (JFS on Linux)

- **[[Journaling]]:** Provides metadata journaling (logging changes to filesystem structure before committing them) to ensure filesystem consistency and fast recovery after crashes or power failures. It journals metadata only, not necessarily file data content by default.
- **64-bit:** Supports large file sizes and large volume sizes.
- **Extent-Based Allocation:** Allocates disk space to files in contiguous blocks called extents, which can improve performance for large files and reduce metadata overhead compared to block-pointer based systems (like ext2/3).
- **Dynamic Inode Allocation:** Allocates [[inode|inodes]] (which store file metadata) dynamically as needed, rather than reserving a fixed number at filesystem creation time. Avoids running out of inodes even if many small files exist.
- **Directory Organization:** Uses B+ trees for organizing directories, allowing for efficient handling of directories containing very large numbers of files.
- **Performance:** Generally known for good performance and relatively low CPU usage compared to some other journaling filesystems, particularly on older or less powerful hardware.
- **Online Resizing:** Supports growing the filesystem while it is mounted (though shrinking might not be supported or require unmounting).

## Usage

- While available for Linux and offering good performance and reliability, JFS is less commonly used as a default filesystem compared to [[ext4]], [[XFS]], or [[BTRFS]] in major distributions.
- It remains a viable option, particularly valued for its low resource usage and stability inherited from its AIX origins.

## Related Concepts
- [[File_System]]
- [[Journaling]] (Core feature)
- [[inode]] (Uses dynamic allocation)
- Extents (Allocation strategy)
- B+ Trees (Used for directories)
- [[ext3]], [[ext4]], [[XFS]], [[BTRFS]] (Other common Linux journaling filesystems)
- [[AIX]], [[OS/2]] (Original platforms)

---
**Source:** Worksheet WS1