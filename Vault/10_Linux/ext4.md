---
tags:
  - linux
  - filesystem
  - concept
  - storage
  - journaling
aliases:
  - Fourth Extended Filesystem
related:
  - "[[File_System]]"
  - "[[ext2]]"
  - "[[ext3]]"
  - "[[Journaling]]"
  - "[[inode]]"
  - "[[Extents]]"
  - "[[BTRFS]]"
  - "[[XFS]]"
worksheet:
  - WS1
  - WS12
date_created: 2025-04-20
---
# ext4 (Fourth Extended Filesystem)

## Definition

**ext4 (Fourth Extended Filesystem)** is a widely used [[Journaling|journaling]] [[File_System]] for Linux. It is the successor to [[ext3]] and incorporates numerous improvements for performance, reliability, and scalability. For many years, it has been the default filesystem for many major Linux distributions.

## Key Features & Improvements over ext3

- **Large Filesystem Support:** Supports much larger volume sizes (up to 1 EiB) and larger file sizes (up to 16 TiB) compared to ext3.
- **[[Extents]]:** Replaces the traditional indirect block mapping scheme (used in ext2/ext3) with extents for allocating space for large files. An extent is a range of contiguous physical blocks. This reduces metadata overhead, improves performance (especially for large files), and helps reduce [[Fragmentation]]. Smaller files or fragmented files might still use indirect blocks.
- **Delayed Allocation (allocate-on-flush):** Delays allocating actual disk blocks until data is flushed from cache to disk. This allows the filesystem allocator to make better decisions based on larger amounts of data, improving contiguity and performance.
- **Journal Checksums:** Adds checksums to the journal data to improve reliability and detect corruption in the journal itself, speeding up recovery.
- **Faster Filesystem Checking (`fsck`):** Optimizations like marking unallocated block groups speed up filesystem checks significantly compared to ext3.
- **Persistent Pre-allocation:** Allows applications to pre-allocate disk space for a file without writing zeros, ensuring space is available and potentially improving contiguity.
- **Sub-second Timestamps:** Provides nanosecond resolution for timestamps (ext3 had second resolution).
- **Backward/Forward Compatibility (Limited):** An ext3 filesystem can often be mounted as ext4 (though without gaining all features). An ext4 filesystem *can* be mounted as ext3 if certain ext4-specific features (like extents) are not used, but this is generally not recommended.

## Usage

- Default filesystem for many Linux distributions (e.g., Debian, Ubuntu, Fedora in the past, though some are shifting towards BTRFS or XFS for defaults).
- A very stable, reliable, and well-tested general-purpose filesystem suitable for desktops, servers, and root filesystems.

## Related Concepts
- [[File_System]]
- [[ext2]], [[ext3]] (Predecessors)
- [[Journaling]] (Core feature)
- [[inode]] (Still uses inodes for metadata)
- [[Extents]] (Improved allocation strategy)
- Delayed Allocation
- [[BTRFS]], [[XFS]] (Other modern Linux filesystems often compared with ext4)
- `fsck` (Filesystem check utility)

---
**Source:** Worksheet WS1, WS12