---
tags: [MOC, 10_linux]
date_created: 2025-04-10
---
# Linux MOC (Map of Content)

This note serves as a central hub for all topics related to **Linux**.

## Core Concepts
- [[Operating_System]]
- [[Kernel]]
- [[Shell]]
- [[File_System]]
- [[Process]]
- [[User_space]]
- [[Kernel_space]]
- [[System_call]]
- [[POSIX]]
- [[GNU]]

## Hardware Concepts
- [[CPU]]
- [[RAM]]
- [[Hard_disk]]
- [[Bus]]
- [[BIOS]] / [[UEFI]]
- [[Boot_loader]]

## File System Specifics
- [[inode]]
- [[ext4]]
- [[BTRFS]]
- [[NTFS]]
- [[FAT-16]] / [[FAT-32]]
- [[NFS]]
- [[JFS]]
- [[Disk_partition]]

## Networking (Linux Context)
- [[IP]]
- [[TCP]]
- [[UDP]]

## Character Sets & Encoding
- [[ASCII]]
- [[Unicode]]
- [[UTF-8]]

## Notes in this Section

```dataview
LIST
FROM "10_Linux"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
````