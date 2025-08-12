---
tags:
  - linux
  - windows
  - filesystem
  - concept
  - storage
  - legacy
aliases:
  - FAT16
  - FAT32
  - File Allocation Table
related:
  - "[[File_System]]"
  - "[[NTFS]]"
  - "[[exFAT]]"
  - "[[Disk_partition]]"
  - "[[Cluster]]"
  - "[[Fragmentation]]"
  - "[[USB_Drive]]"
  - "[[SD_Card]]"
worksheet:
  - WS1
date_created: 2025-04-21
---
# FAT (File Allocation Table) - FAT16 & FAT32

## Definition

**FAT (File Allocation Table)** is a family of relatively simple, legacy [[File_System|file systems]] originally developed for MS-DOS and widely used in earlier versions of Windows and on removable media. The name comes from its core data structure: a table (the File Allocation Table) stored on the volume that acts as a map, indicating which allocation units (**[[Cluster|clusters]]**) on the disk are used by which files. The most common variants are **FAT16** and **FAT32**.

## Key Aspects / Characteristics

- **Simplicity:** Relatively simple design compared to more modern filesystems like [[NTFS]] or ext4.
- **File Allocation Table (FAT):** The central structure. It's an array where each entry corresponds to a cluster on the disk. Each entry contains either:
    - The index of the *next* cluster belonging to the file.
    - A special marker indicating the end of the file's cluster chain.
    - A marker indicating the cluster is bad/unusable.
    - A marker indicating the cluster is free.
    Files are stored as linked lists of clusters via this table.
- **Clusters:** Disk space is allocated in fixed-size units called clusters (or allocation units). Cluster size varies depending on volume size and FAT type.
- **Directory Entries:** Store basic file metadata (name - 8.3 format for FAT16, long filenames supported via VFAT extension often used with FAT32, attributes, start cluster, size, timestamps). Stored within special directory files.
- **FAT16:**
    - Uses 16-bit entries in the FAT.
    - **Limitations:** Maximum volume size typically 2 GiB (sometimes 4 GiB with larger clusters), maximum file size 2 GiB (or 4 GiB), limited number of root directory entries. Prone to wasted space (slack space) on larger volumes due to large cluster sizes.
- **FAT32:**
    - Uses 32-bit entries in the FAT (though only 28 bits are actually used for cluster numbers).
    - **Limitations:** Maximum file size is 4 GiB minus 1 byte. Maximum volume size is theoretically large (many TBs), but Windows tools often limit creation to 32 GiB. Still lacks features like journaling, permissions, encryption found in NTFS.
- **Compatibility:** Excellent compatibility across various operating systems (Windows, macOS, Linux, embedded systems, cameras, etc.), making it suitable for removable media like [[USB_Drive|USB drives]] and [[SD_Card|SD cards]] where interoperability is key.
- **No Journaling/Permissions:** Lacks robustness features like [[Journaling]] (making it more susceptible to corruption on unexpected shutdown) and file-level security permissions ([[Access_Control_List|ACLs]]).
- **[[Fragmentation]]:** Prone to file fragmentation over time as files are created, deleted, and modified, which can impact performance.

## Successors

- [[NTFS]]: Standard filesystem on modern Windows.
- [[exFAT]]: Developed by Microsoft as an improvement over FAT32, primarily for flash media. Supports larger files and volumes than FAT32, while retaining better cross-platform compatibility than NTFS.

## Related Concepts
- [[File_System]]
- [[NTFS]], [[exFAT]] (Other Microsoft filesystems)
- [[Cluster]] (Allocation unit)
- [[Fragmentation]] (Common issue)
- [[USB_Drive]], [[SD_Card]] (Common use cases)
- Long Filenames (VFAT extension)

---
**Source:** Worksheet WS1

# FAT (File Allocation Table) - FAT16 & FAT32

## Definition

**FAT (File Allocation Table)** is a family of relatively simple, legacy [[File_System|file systems]] originally developed for MS-DOS and widely used in earlier versions of Windows and on removable media. The name comes from its core data structure: a table (the File Allocation Table) stored on the volume that acts as a map, indicating which allocation units (**[[Cluster|clusters]]**) on the disk are used by which files. The most common variants are **FAT16** and **FAT32**.

## Key Aspects / Characteristics

- **Simplicity:** Relatively simple design compared to more modern filesystems like [[NTFS]] or ext4.
- **File Allocation Table (FAT):** The central structure. It's an array where each entry corresponds to a cluster on the disk. Each entry contains either:
    - The index of the *next* cluster belonging to the file.
    - A special marker indicating the end of the file's cluster chain.
    - A marker indicating the cluster is bad/unusable.
    - A marker indicating the cluster is free.
    Files are stored as linked lists of clusters via this table.
- **Clusters:** Disk space is allocated in fixed-size units called clusters (or allocation units). Cluster size varies depending on volume size and FAT type.
- **Directory Entries:** Store basic file metadata (name - 8.3 format for FAT16, long filenames supported via VFAT extension often used with FAT32, attributes, start cluster, size, timestamps). Stored within special directory files.
- **FAT16:**
    - Uses 16-bit entries in the FAT.
    - **Limitations:** Maximum volume size typically 2 GiB (sometimes 4 GiB with larger clusters), maximum file size 2 GiB (or 4 GiB), limited number of root directory entries. Prone to wasted space (slack space) on larger volumes due to large cluster sizes.
- **FAT32:**
    - Uses 32-bit entries in the FAT (though only 28 bits are actually used for cluster numbers).
    - **Limitations:** Maximum file size is 4 GiB minus 1 byte. Maximum volume size is theoretically large (many TBs), but Windows tools often limit creation to 32 GiB. Still lacks features like journaling, permissions, encryption found in NTFS.
- **Compatibility:** Excellent compatibility across various operating systems (Windows, macOS, Linux, embedded systems, cameras, etc.), making it suitable for removable media like [[USB_Drive|USB drives]] and [[SD_Card|SD cards]] where interoperability is key.
- **No Journaling/Permissions:** Lacks robustness features like [[Journaling]] (making it more susceptible to corruption on unexpected shutdown) and file-level security permissions ([[Access_Control_List|ACLs]]).
- **[[Fragmentation]]:** Prone to file fragmentation over time as files are created, deleted, and modified, which can impact performance.

## Successors

- [[NTFS]]: Standard filesystem on modern Windows.
- [[exFAT]]: Developed by Microsoft as an improvement over FAT32, primarily for flash media. Supports larger files and volumes than FAT32, while retaining better cross-platform compatibility than NTFS.

## Related Concepts
- [[File_System]]
- [[NTFS]], [[exFAT]] (Other Microsoft filesystems)
- [[Cluster]] (Allocation unit)
- [[Fragmentation]] (Common issue)
- [[USB_Drive]], [[SD_Card]] (Common use cases)
- Long Filenames (VFAT extension)

---
**Source:** Worksheet WS1