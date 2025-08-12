---
tags:
  - 10_linux
  - concept
  - os
  - boot
aliases: 
related:
  - "[[BIOS]]"
  - "[[UEFI]]"
  - "[[Master_boot_record]]"
  - "[[GRUB]]"
  - "[[LILO]]"
  - "[[Kernel]]"
  - "[[Operating_System]]"
  - "[[Linux_Boot_Process]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# Boot Loader

## Definition

A **Boot Loader** is a small program that loads the main [[Operating_System]] or runtime environment for the computer after completion of the self-tests performed by the firmware ([[BIOS]] or [[UEFI]]). It is responsible for finding the [[Kernel]] on the storage device, loading it into [[RAM]], and transferring control to it.

## Key Aspects / Characteristics

- **Initialization:** Takes over after the system firmware (BIOS/UEFI) initializes basic hardware.
- **Kernel Loading:** Locates the OS kernel image (e.g., `vmlinuz` in Linux) on a [[Hard_disk]], [[SSD]], or network.
- **Memory Transfer:** Loads the kernel and often an initial RAM disk (initrd/initramfs) into [[RAM]].
- **Parameter Passing:** Can pass boot parameters (e.g., root filesystem location, kernel options) to the kernel.
- **Multi-Boot:** Many boot loaders (like [[GRUB]]) can present a menu allowing the user to choose which OS or kernel version to boot if multiple are installed.
- **Location:** Traditionally stored in the [[Master_boot_record]] (MBR) for BIOS systems, or as an EFI application on a dedicated partition (ESP) for UEFI systems.

## Examples / Use Cases

- **[[GRUB]] (GRand Unified Bootloader):** Very common boot loader for Linux distributions.
- **[[LILO]] (LInux LOader):** An older Linux boot loader, less common now.
- **Windows Boot Manager:** The boot loader used by modern Windows versions.
- **systemd-boot (formerly gummiboot):** A simpler UEFI boot manager.
- **U-Boot:** Common in embedded systems.

## Related Concepts
- [[Linux_Boot_Process]] (The boot loader is a key stage)
- [[BIOS]] / [[UEFI]] (Firmware that starts the boot loader)
- [[Master_boot_record]] (Traditional location for BIOS boot loaders)
- [[Kernel]] (The program loaded by the boot loader)
- [[Operating_System]] (The ultimate goal of the boot process)
- [[GRUB]], [[LILO]] (Specific boot loader examples)
- Initial RAM Disk (initrd/initramfs) (Often loaded alongside the kernel)

## Questions / Further Study
>[!question] Describe the six stages of the Linux booting process. (WS13)
> While specifics can vary, a general overview includes:
> 1.  **[[BIOS]]/[[UEFI]] Initialization:** Hardware checks (POST), firmware loads.
> 2.  **[[Boot_loader]] Stage 1:** Firmware loads the first stage of the boot loader (e.g., from [[Master_boot_record|MBR]] or EFI partition). This stage is small and usually just loads the next stage.
> 3.  **[[Boot_loader]] Stage 2 ([[GRUB]], [[LILO]]):** The main boot loader code runs, presents a menu (if configured), locates the [[Kernel]] and initrd/initramfs.
> 4.  **[[Kernel]] Loading & Initialization:** The boot loader loads the kernel and initrd into [[RAM]] and transfers control. The kernel initializes itself, sets up core data structures, detects hardware.
> 5.  **Initramfs Execution:** The initial RAM filesystem is mounted. It contains necessary drivers and tools (e.g., for disk access) needed to mount the real root filesystem.
> 6.  **Init Process Start:** The kernel mounts the real root filesystem and starts the first user-space process, typically `init` or `systemd` (PID 1), which proceeds to bring up the rest of the system services and user environment (e.g., based on [[Run_levels]] or systemd targets).

---
**Source:** Worksheet WS1, WS13
