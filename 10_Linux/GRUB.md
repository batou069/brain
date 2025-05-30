---
tags:
  - linux
  - software
  - boot
  - boot_loader
aliases:
  - GRUB
  - GRand Unified Bootloader
related:
  - "[[Boot_loader]]"
  - "[[LILO]]"
  - "[[Linux_Boot_Process]]"
  - "[[Kernel]]"
  - "[[initrd]]"
  - "[[Multiboot]]"
  - "[[BIOS]]"
  - "[[UEFI]]"
  - "[[Master_boot_record]]"
  - "[[ESP_EFI_System_Partition]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# GRUB (GRand Unified Bootloader)

## Definition

**GRUB (GRand Unified Bootloader)** is a popular and powerful [[Boot_loader]] package from the GNU Project. It is the default boot loader for most major Linux distributions. GRUB is responsible for loading the Linux [[Kernel]] (and an optional [[initrd|initial RAM disk]]) into memory and then transferring execution control to the kernel.

## Key Features

- **Multiboot Support:** Can boot multiple different operating systems installed on the same machine (e.g., Linux, Windows, macOS via chainloading). Presents a menu at startup allowing the user to choose which OS or kernel version to boot.
- **Filesystem Awareness:** Can read various filesystems (like ext2/3/4, FAT, NTFS, BTRFS, XFS), allowing it to load kernels and configuration files directly by filename and path, rather than relying on fixed disk block locations like older bootloaders ([[LILO]]).
- **Configuration File:** Uses a configuration file (typically `/boot/grub/grub.cfg` or `/boot/grub2/grub.cfg`) to define menu entries, kernel parameters, timeouts, themes, etc. This file is usually generated automatically by tools like `update-grub` or `grub2-mkconfig` based on system settings and detected kernels/OSes.
- **Command-Line Interface:** Provides an interactive command line at boot time (accessed by pressing 'c' or 'e' in the menu) for advanced users to manually specify boot commands, modify parameters, or troubleshoot boot issues.
- **Modular Design:** Consists of multiple stages and loadable modules for different filesystems, video modes, etc.
- **[[BIOS]] and [[UEFI]] Support:** Supports booting on both legacy BIOS systems (installing parts to the [[Master_boot_record|MBR]] and subsequent sectors) and modern [[UEFI]] systems (installing as an EFI application on the [[ESP_EFI_System_Partition|ESP]]).
- **Network Boot:** Supports booting kernels over a network (PXE).
- **Scripting:** The configuration file format allows for basic scripting logic.

## Versions

- **GRUB Legacy (GRUB 1):** Older version, configuration file typically `/boot/grub/menu.lst`. Less common now.
- **GRUB 2:** Current version, more modular, powerful configuration system (`grub.cfg`), improved hardware support. This is what most modern distributions use.

## Related Concepts
- [[Boot_loader]] (GRUB is an implementation)
- [[LILO]] (Older Linux boot loader alternative)
- [[Linux_Boot_Process]] (GRUB is a key stage)
- [[Kernel]], [[initrd]] (Loaded by GRUB)
- [[Multiboot]] (Feature provided by GRUB)
- [[BIOS]], [[UEFI]] (Firmware environments GRUB runs under)
- [[Master_boot_record]], [[ESP_EFI_System_Partition]] (Installation locations)

---
**Source:** Worksheet WS1