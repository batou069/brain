---
tags:
  - linux
  - software
  - boot
  - boot_loader
  - legacy
aliases:
  - LILO
  - LInux LOader
related:
  - "[[Boot_loader]]"
  - "[[GRUB]]"
  - "[[Linux_Boot_Process]]"
  - "[[Kernel]]"
  - "[[Master_boot_record]]"
  - "[[BIOS]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# LILO (LInux LOader)

## Definition

**LILO (LInux LOader)** is a legacy [[Boot_loader]] for Linux and other Unix-like operating systems. For many years, it was one of the most common boot loaders used, but it has largely been superseded by [[GRUB]] in most modern Linux distributions.

## Key Aspects / Characteristics

- **Simplicity:** Generally considered simpler in design and configuration compared to GRUB 2.
- **Configuration File:** Typically configured using `/etc/lilo.conf`.
- **MBR Installation:** Installs primarily to the [[Master_boot_record|Master Boot Record (MBR)]] or a partition boot sector.
- **No Filesystem Awareness (Mostly):** Unlike GRUB, LILO generally does *not* understand filesystems. It relies on storing the physical disk block locations (sector addresses) of the kernel image(s) it needs to load.
- **Requires Re-running `lilo`:** Because it stores block locations, **the `lilo` command must be re-run** every time a new kernel is installed or the configuration file (`/etc/lilo.conf`) is changed. This updates the boot sector with the correct block addresses. Forgetting this step is a common cause of boot failures with LILO.
- **Multiboot:** Can boot multiple Linux kernels and other operating systems (via chainloading).
- **Legacy:** Primarily used on older systems or systems with specific [[BIOS]] limitations. Not commonly used with [[UEFI]].

## LILO vs. GRUB

| Feature             | LILO                                   | GRUB (especially GRUB 2)              |
| :------------------ | :------------------------------------- | :------------------------------------ |
| Filesystem Aware?   | No (uses block lists)                  | Yes (reads filesystems)               |
| Config Update       | Requires re-running `lilo` command     | Config file read at boot time         |
| Config File         | `/etc/lilo.conf`                       | `/boot/grub/grub.cfg` (usually generated) |
| Boot Menu           | Basic text menu                        | More advanced, themable menu          |
| Boot CLI            | Limited                                | Powerful interactive command line     |
| UEFI Support        | Generally No                           | Yes                                   |
| Complexity          | Simpler                                | More complex, more features           |
| Current Usage       | Rare, legacy systems                   | Default on most modern distributions  |

## Related Concepts
- [[Boot_loader]] (LILO is an implementation)
- [[GRUB]] (Modern successor/alternative)
- [[Linux_Boot_Process]]
- [[Kernel]] (Loaded by LILO)
- [[Master_boot_record]] (Primary install location)
- [[BIOS]] (Firmware environment LILO runs under)

---
**Source:** Worksheet WS1