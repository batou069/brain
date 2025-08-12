---
tags:
  - linux
  - hardware
  - concept
  - boot
  - storage
  - partition
  - legacy
aliases:
  - MBR
related:
  - "[[BIOS]]"
  - "[[Boot_loader]]"
  - "[[Disk_partition]]"
  - "[[GPT]]"
  - "[[Hard_disk]]"
  - "[[Boot_Process_C]]"
  - "[[LILO]]"
  - "[[GRUB]]"
worksheet:
  - WS1
  - WS13
date_created: 2025-04-20
---
# Master Boot Record (MBR)

## Definition

The **Master Boot Record (MBR)** is a special type of boot sector located at the very beginning (the first 512 bytes) of a partitioned computer mass storage device, such as a [[Hard_disk]]. It serves two main functions in legacy [[BIOS]]-based systems:

1.  **Contains Boot Code:** Holds a small amount of executable code (the first stage of the [[Boot_loader]]) loaded by the [[BIOS]] firmware. This code's job is usually to find the active partition, load its boot sector (Volume Boot Record - VBR), and transfer control to it.
2.  **Holds Partition Table:** Contains the primary partition table describing the disk's layout into logical [[Disk_partition|partitions]].

## Structure (512 Bytes Total)

1.  **Boot Code (Bootstrap Code):** First ~440-446 bytes. Contains the initial instructions executed after BIOS loads the MBR.
2.  **Disk Signature (Optional):** 4-byte unique identifier (sometimes).
3.  **Partition Table:** 64 bytes. Defines up to four **primary partitions**. Each entry (16 bytes) specifies:
    -   Bootable flag (indicates the active partition for booting).
    -   Starting and ending Cylinder-Head-Sector (CHS) address (legacy).
    -   Partition type code (e.g., indicating FAT32, NTFS, Linux swap, Linux native, Extended).
    -   Starting Logical Block Address (LBA).
    -   Number of sectors in the partition.
4.  **Boot Signature (Magic Number):** Last 2 bytes. Must be `0x55AA`. BIOS checks for this signature to validate the MBR as a bootable sector.

## Limitations

- **Disk Size Limit:** Using 32-bit LBA addresses in the partition table limits the maximum addressable disk size to 2 TiB (2<sup>32</sup> sectors * 512 bytes/sector).
- **Partition Limit:** Only allows a maximum of **four primary partitions**. To overcome this, one primary partition can be designated as an **[[Extended_Partition|extended partition]]**, which acts as a container for multiple **[[Logical_Partition|logical partitions]]** defined within it using a chain of Extended Boot Records (EBRs). This is complex and still has limitations.
- **No Redundancy/Checksum:** The partition table data is stored only once and has no checksum, making it vulnerable to corruption.

## Successor

- The MBR partitioning scheme and boot method have been largely superseded by the combination of [[UEFI]] firmware and the [[GPT]] (GUID Partition Table) scheme on modern systems, which overcome these limitations.

## Related Concepts
- [[BIOS]] (Loads and executes the MBR boot code)
- [[Boot_loader]] (MBR contains the first stage)
- [[Disk_partition]], [[Primary_Partition]], [[Extended_Partition]], [[Logical_Partition]]
- [[GPT]] (Modern replacement for MBR partitioning)
- [[Boot_Sector]] (MBR is the first sector)
- [[Boot_Process_C]] (MBR is key in legacy boot)

---
**Source:** Worksheet WS1, WS13