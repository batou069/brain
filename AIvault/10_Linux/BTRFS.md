---
tags:
  - linux
  - filesystem
  - concept
  - storage
  - advanced_filesystem
  - copy_on_write
aliases:
  - B-tree file system
  - Butter FS
related:
  - "[[File_System]]"
  - "[[Copy-on-Write]]"
  - "[[Snapshotting]]"
  - "[[Checksumming]]"
  - "[[RAID]]"
  - "[[Subvolumes]]"
  - "[[Compression]]"
  - "[[ext4]]"
  - "[[XFS]]"
  - "[[ZFS]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# Btrfs (B-tree file system)

## Definition

**Btrfs (B-tree file system)** is a modern [[Copy-on-Write|copy-on-write (CoW)]] [[File_System]] for Linux aimed at implementing advanced features while focusing on fault tolerance, repair, and easy administration. It offers features beyond traditional Linux filesystems like [[ext4]].

## Key Features

- **[[Copy-on-Write]] (CoW):** When data is modified, the changes are written to a new location on disk rather than overwriting the old data in place. The metadata pointers are then updated to point to the new location. This is fundamental to enabling features like snapshots and checksumming.
- **[[Snapshotting]]:** Allows creating instantaneous, writable or read-only snapshots of the filesystem or specific [[Subvolumes]]. Snapshots initially share data with the original (due to CoW) and only consume extra space as changes are made to either the original or the snapshot. Excellent for backups and rollbacks.
- **[[Checksumming]]:** Stores checksums (e.g., CRC32C) for both data and metadata blocks. This allows the filesystem to detect silent data corruption (bit rot). If corruption is detected and redundant copies exist (e.g., via built-in [[RAID]]), Btrfs can potentially self-heal by using a good copy.
- **Integrated Volume Management & [[RAID]]:** Can manage multiple underlying block devices within a single filesystem. Supports software RAID levels (RAID 0, RAID 1, RAID 10, RAID 5/6 - though RAID 5/6 stability has historically been questionable). Allows adding/removing devices from a live filesystem.
- **[[Subvolumes]]:** Allows partitioning the filesystem into independently mountable subvolumes, which can be snapshotted individually. Can be used similarly to LVM logical volumes but integrated within the filesystem.
- **Transparent [[Compression]]:** Supports on-the-fly compression of file data (e.g., using zlib, LZO, Zstd), saving disk space at the cost of some CPU overhead.
- **SSD Optimizations:** Includes features beneficial for [[SSD|SSDs]], such as TRIM/discard support.
- **Online Operations:** Supports online filesystem checks, defragmentation, resizing, and balancing across multiple devices.
- **Send/Receive:** Allows efficiently sending incremental differences between snapshots to another Btrfs filesystem (useful for backups and replication).

## Usage

- Increasingly used as the default filesystem in some Linux distributions (e.g., Fedora Workstation, openSUSE).
- Popular for systems where advanced features like snapshots, checksumming, and integrated volume management are desired.
- Suitable for both desktops and servers, though its RAID 5/6 implementation has had stability concerns in the past (always check current status).

## Related Concepts
- [[File_System]]
- [[Copy-on-Write]] (CoW)
- [[Snapshotting]]
- [[Checksumming]], Data Integrity
- [[RAID]] (Software RAID capabilities)
- [[Subvolumes]]
- [[Compression]]
- [[ext4]], [[XFS]] (Other Linux filesystems)
- [[ZFS]] (Another advanced CoW filesystem with similar features, originally from Sun/Oracle)

---
**Source:** Worksheet WS1