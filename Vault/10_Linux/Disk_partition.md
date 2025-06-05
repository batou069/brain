---
tags:
  - linux
  - concept
  - storage
  - filesystem
  - os
aliases:
  - Partitioning
  - Disk Partitions
related:
  - "[[Hard_disk]]"
  - "[[SSD]]"
  - "[[File_System]]"
  - "[[Master_boot_record]]"
  - "[[GPT]]"
  - "[[Primary_Partition]]"
  - "[[Extended_Partition]]"
  - "[[Logical_Partition]]"
  - "[[Mounting]]"
  - "[[fdisk]]"
  - "[[parted]]"
  - "[[gparted]]"
worksheet:
  - WS1
  - WS12
date_created: 2025-04-20
---
# Disk Partitioning

## Definition

**Disk Partitioning** is the act of dividing a physical mass storage device (like a [[Hard_disk|hard disk drive (HDD)]] or [[SSD|solid-state drive (SSD)]]) into multiple isolated logical sections called **partitions**. Each partition can then be treated by the [[Operating_System]] as a separate logical disk, allowing different [[File_System|file systems]] to be installed on each or serving other specific purposes (like [[Swap_Partition|swap space]]).

## Purpose

- **Multiple Filesystems:** Allows installing different file systems on the same physical disk (e.g., one partition for Linux ext4, another for Windows NTFS).
- **Multiple Operating Systems (Multi-boot):** Enables installing different OSes on separate partitions of the same drive.
- **Separation of Data:** Isolate OS files from user data, application data, or swap space. This can improve organization, simplify backups, and potentially limit damage if one filesystem becomes corrupted.
- **Performance (Historically):** Sometimes used to place frequently accessed data on faster parts of a spinning HDD (outer tracks), though less relevant with SSDs.
- **Resource Management:** Can be used with quotas or specific mount options applied per partition.
- **Meeting System Requirements:** Some OSes or boot processes require specific partition layouts (e.g., an [[ESP_EFI_System_Partition]] for [[UEFI]] booting).

## Partitioning Schemes

How partitions are defined and stored on the disk depends on the partitioning scheme used:

1.  **[[Master_boot_record|MBR (Master Boot Record)]]:**
    -   Legacy scheme used with [[BIOS]].
    -   Stores partition table within the first sector (MBR).
    -   **Limitations:** Max 4 [[Primary_Partition|primary partitions]] (or 3 primary + 1 [[Extended_Partition|extended]] containing multiple [[Logical_Partition|logical partitions]]), max disk size ~2 TiB.

2.  **[[GPT|GPT (GUID Partition Table)]]:**
    -   Modern scheme used with [[UEFI]] (but can also be used with BIOS).
    -   Stores partition table information in headers at the beginning and end of the disk (providing redundancy).
    -   **Advantages:** Supports vastly larger disks (zettabytes), allows a large number of partitions (typically 128 by default, but configurable), uses globally unique identifiers (GUIDs) for disks and partitions, includes checksums for integrity.

## Partition Types (MBR Context)

- **[[Primary_Partition]]:** A bootable partition defined directly in the MBR's main partition table. Max 4 per disk.
- **[[Extended_Partition]]:** A special type of primary partition that acts as a container. It does not hold a filesystem directly but contains [[Logical_Partition|logical partitions]]. Max 1 per disk.
- **[[Logical_Partition]]:** A partition defined within an extended partition. Multiple logical partitions can exist within the extended partition.

*(Note: GPT does not use the primary/extended/logical distinction; all partitions are effectively "primary".)*

## Tools (Linux)

- `fdisk`: Classic command-line tool for MBR partitioning.
- `gdisk`: Command-line tool for GPT partitioning (similar interface to fdisk).
- `parted`: Powerful command-line tool supporting both MBR and GPT, resizing, etc.
- `gparted`: Graphical partition editor (uses libparted).

## Related Concepts
- [[Hard_disk]], [[SSD]] (Devices being partitioned)
- [[File_System]] (Installed *on* partitions)
- [[Master_boot_record]], [[GPT]] (Partitioning schemes)
- [[Primary_Partition]], [[Extended_Partition]], [[Logical_Partition]] (MBR partition types)
- [[Mounting]] (Making the filesystem on a partition accessible)
- Partitioning Tools (`fdisk`, `gdisk`, `parted`, `gparted`)
- [[Volume_Management]] (LVM - Higher-level abstraction over partitions/disks - *Implied*)

---
**Source:** Worksheet WS1, WS12