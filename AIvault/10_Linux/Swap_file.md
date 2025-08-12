---
tags:
  - linux
  - concept
  - os
  - memory
  - storage
  - virtual_memory
aliases:
  - Linux Swap File
related:
  - "[[Swap_Space]]"
  - "[[Swap_Partition]]"
  - "[[Virtual_memory]]"
  - "[[Paging]]"
  - "[[RAM]]"
  - "[[Operating_System]]"
  - "[[mkswap]]"
  - "[[swapon]]"
  - "[[swapoff]]"
worksheet:
  - WS1
  - WS12
date_created: 2025-04-20
---
# Swap File (Linux)

## Definition

A **Swap File** in Linux is a regular file residing on an existing filesystem (like ext4, XFS) that is designated by the [[Operating_System]] to be used as **[[Swap_Space]]**. It serves as an extension to the physical [[RAM]] (part of the [[Virtual_memory]] system), allowing the OS to move inactive memory pages from RAM to the swap file on disk when physical memory pressure is high.

## Key Aspects / Characteristics

- **File-Based:** Exists as a standard file within a filesystem hierarchy (e.g., `/swapfile`).
- **Flexibility:** Easier to create, resize, or remove compared to a dedicated [[Swap_Partition]]. The size can often be adjusted without repartitioning the disk.
- **Setup:** Requires specific steps:
    1.  Create an empty file of the desired size (e.g., using `fallocate` or `dd`).
    2.  Set appropriate permissions (usually readable/writable only by root).
    3.  Format the file for use as swap space using the `mkswap` command.
    4.  Activate the swap file using the `swapon` command.
    5.  (Optional) Add an entry to `/etc/fstab` to automatically activate the swap file on boot.
- **Performance:** Historically, swap files were sometimes considered slightly slower than swap partitions due to potential filesystem overhead or fragmentation. However, on modern systems (especially with SSDs and modern filesystems), the performance difference is often negligible or non-existent. Some filesystems (like BTRFS prior to kernel 5.0) had limitations or performance issues with swap files.
- **Use Cases:** Suitable for most systems, especially when flexibility in swap size is desired, or when repartitioning is difficult or undesirable (e.g., cloud instances, systems with complex partitioning already).

## Swap File vs. Swap Partition

| Feature         | Swap File                     | [[Swap_Partition]]            |
| :-------------- | :---------------------------- | :---------------------------- |
| **Type**        | Regular file on filesystem    | Dedicated disk partition      |
| **Location**    | Within a filesystem (e.g. `/`)| Separate partition (`/dev/sdXN`)|
| **Flexibility** | High (easy to resize/remove)  | Low (requires repartitioning) |
| **Setup**       | `fallocate`/`dd`, `mkswap`, `swapon` | Partitioning tool, `mkswap`, `swapon` |
| **Performance** | Generally comparable (modern) | Potentially slightly faster (legacy/specific cases) |
| **Hibernation** | May have issues (depends on FS/setup) | Generally more reliable       |

## Related Concepts
- [[Swap_Space]] (The general concept of using disk for RAM overflow)
- [[Swap_Partition]] (Alternative implementation using a dedicated partition)
- [[Virtual_memory]], [[Paging]] (The OS mechanism using swap)
- [[mkswap]], [[swapon]], [[swapoff]] (Commands for managing swap)
- `/etc/fstab` (Configuration file for mounting filesystems and activating swap on boot)

## Questions / Further Study
>[!question] What is the difference between a swap file and a swap partition? Advantages/Disadvantages? When use each? (WS12)
> - **Difference:** A [[Swap_File]] is a regular file on an existing filesystem used as swap space. A [[Swap_Partition]] is a dedicated, raw disk partition used as swap space.
> - **Advantages/Disadvantages:**
>     - **Swap File:** **Adv:** High flexibility (easy resize/add/remove). **Disadv:** Historically minor performance overhead (less relevant now), potential hibernation issues on some setups.
>     - **Swap Partition:** **Adv:** Historically slightly better performance, potentially more reliable for hibernation. **Disadv:** Inflexible (resizing requires partition table changes), wastes disk space if overallocated.
> - **When to Use:**
>     - **Swap File:** Most common choice now due to flexibility. Ideal when unsure about required swap size, or on systems where repartitioning is difficult (cloud VMs, existing complex layouts).
>     - **Swap Partition:** Still viable. Sometimes preferred for hibernation reliability or on systems where dedicated performance was historically critical, or if adhering to older setup guides.

---
**Source:** Worksheet WS1, WS12