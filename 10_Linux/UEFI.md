---
tags:
  - linux
  - hardware
  - concept
  - firmware
  - boot
  - standard
aliases:
  - Unified Extensible Firmware Interface
related:
  - "[[Firmware]]"
  - "[[BIOS]]"
  - "[[Motherboard]]"
  - "[[Boot_Process_C]]"
  - "[[Boot_loader]]"
  - "[[GPT]]"
  - "[[Master_boot_record]]"
  - "[[Secure_Boot]]"
  - "[[ESP_EFI_System_Partition]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# UEFI (Unified Extensible Firmware Interface)

## Definition

**UEFI (Unified Extensible Firmware Interface)** is a modern specification that defines a software interface between an operating system and platform [[Firmware]]. It serves as a replacement for the legacy [[BIOS]], providing enhanced features, improved security, faster boot times, and support for modern hardware.

## Key Features and Advantages over BIOS

- **Graphical User Interface:** Often provides richer, mouse-driven setup menus compared to text-based BIOS setup.
- **[[GPT]] (GUID Partition Table) Support:** Natively supports GPT partitioning, overcoming the disk size limitations (~2TB) and partition limits of the legacy [[Master_boot_record|MBR]] scheme used by BIOS.
- **Faster Boot Times:** Can initialize hardware in parallel and directly load OS boot loaders without relying on legacy MBR code execution.
- **CPU-Independent Architecture & Drivers:** Designed to be architecture-independent and can include its own drivers for hardware, allowing access to devices like network cards during the pre-boot environment.
- **[[Secure_Boot]]:** An optional security feature that helps prevent unauthorized boot loaders or malware from running during the boot process by verifying digital signatures.
- **Networking Capabilities:** Can include built-in networking support in the pre-boot environment (e.g., for network boot, remote diagnostics).
- **Extensibility:** Provides a more modular and extensible environment with support for EFI applications (including [[Boot_loader|boot loaders]]) stored on a dedicated [[ESP_EFI_System_Partition|EFI System Partition (ESP)]].
- **No 16-bit Limitations:** Operates in 32-bit or 64-bit mode, allowing access to more system RAM during boot.

## Boot Process with UEFI

1.  System powers on, UEFI firmware initializes.
2.  Performs hardware initialization (similar to [[POST]], but potentially faster/more parallel).
3.  Loads UEFI drivers from firmware or [[ESP_EFI_System_Partition|ESP]].
4.  Checks [[Secure_Boot]] configuration (if enabled).
5.  Loads the OS [[Boot_loader]] (an EFI application, e.g., `bootmgfw.efi` for Windows, `grubx64.efi` or `shimx64.efi` for Linux) directly from the [[ESP_EFI_System_Partition|ESP]] based on boot entries stored in NVRAM.
6.  Transfers control to the OS boot loader, which then loads the OS [[Kernel]].

## Related Concepts
- [[Firmware]] (UEFI is system firmware)
- [[BIOS]] (Legacy system UEFI replaces)
- [[Boot_Process_C]] (UEFI defines the modern boot process)
- [[Boot_loader]] (Loaded by UEFI as EFI applications)
- [[GPT]] (Partitioning scheme supported by UEFI)
- [[Master_boot_record]] (Legacy scheme replaced by GPT/UEFI booting)
- [[Secure_Boot]] (UEFI security feature)
- [[ESP_EFI_System_Partition]] (Dedicated partition for EFI boot files)

---
**Source:** Worksheet WS1