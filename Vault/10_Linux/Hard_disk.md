---
tags:
  - 10_linux
  - concept
  - hardware
  - storage
aliases:
  - HDD
  - Hard Disk Drive
related:
  - "[[SSD]]"
  - "[[File_System]]"
  - "[[Operating_System]]"
  - "[[RAM]]"
  - "[[inode]]"
  - "[[Disk_partition]]"
  - "[[Block_device]]"
  - "[[Mounting]]"
  - "[[SATA]]"
  - "[[ATAPI]]"
  - "[[MTBF]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# Hard Disk Drive (HDD)

## Definition

A **Hard Disk Drive (HDD)** is an electro-mechanical data storage device that uses magnetic storage to store and retrieve digital data using one or more rigid rapidly rotating platters coated with magnetic material. Data is accessed in a random-access manner, meaning individual blocks of data can be stored and retrieved in any order. It is a form of non-volatile storage, retaining data even when powered off.

## Key Aspects / Characteristics

- **Non-Volatile:** Retains data without power.
- **Magnetic Storage:** Uses rotating platters and read/write heads.
- **Mechanical:** Contains moving parts (platters, actuator arm, heads), making it susceptible to physical shock and slower than solid-state alternatives.
- **Capacity:** Generally offers high storage capacity at a lower cost per gigabyte compared to [[SSD|SSDs]].
- **Speed:** Access times are limited by the mechanical movement (seek time, rotational latency), making it significantly slower than [[RAM]] and [[SSD|SSDs]] for random access. Sequential access speeds can still be reasonable.
- **Block Device:** Accessed by the [[Operating_System]] as a [[Block_device]].

## Examples / Use Cases

- Storing the [[Operating_System]], applications, and user data in desktops and servers.
- Large-capacity storage for backups or archives.
- Network Attached Storage (NAS) devices.

## Related Concepts
- [[SSD]] (Solid State Drive - faster, no moving parts)
- [[File_System]] (Organizes data stored on the HDD)
- [[Disk_partition]] (Dividing the HDD into logical sections)
- [[Block_device]] (How the OS views the drive)
- [[Mounting]] (Making the file system on the drive accessible)
- [[SATA]] / [[ATAPI]] (Interfaces used to connect HDDs)
- [[RAM]] (Faster, volatile memory)
- [[MTBF]] (Mean Time Between Failures - a reliability metric)

## Questions / Further Study
>[!question] What is the main difference between HDD and SSD?
> The primary difference is the technology used. [[HDD|HDDs]] use spinning magnetic platters and moving read/write heads (mechanical). [[SSD|SSDs]] use flash memory chips (solid-state, no moving parts). This makes SSDs much faster, more durable, quieter, and energy-efficient, but typically more expensive per gigabyte than HDDs.

---
**Source:** Worksheet WS1, WS12