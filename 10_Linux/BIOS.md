---
tags:
  - linux
  - hardware
  - concept
  - firmware
  - boot
aliases:
  - Basic Input/Output System
related:
  - "[[Firmware]]"
  - "[[UEFI]]"
  - "[[Motherboard]]"
  - "[[Boot_Process_C]]"
  - "[[Boot_loader]]"
  - "[[POST]]"
  - "[[CMOS_Setup]]"
  - "[[ROM]]"
  - "[[EPROM]]"
  - "[[EEPROM]]"
  - "[[Flash_Memory]]"
  - "[[Master_boot_record]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# BIOS (Basic Input/Output System)

## Definition

**BIOS (Basic Input/Output System)** is [[Firmware]] stored on a chip (historically [[ROM]], [[EPROM]], [[EEPROM]], now typically [[Flash_Memory]]) on a computer's [[Motherboard]]. It is the first software run by a PC when powered on. Its primary functions are to initialize and test the system hardware ([[POST]]), and to load an operating system from a mass storage device ([[Boot_loader]]).

## Key Functions

1.  **[[POST]] (Power-On Self-Test):** Checks the basic hardware components (CPU, RAM, keyboard, video card) for functionality before loading the OS. Reports errors via beep codes or on-screen messages if critical failures occur.
2.  **Bootstrap Loader:** Locates the [[Boot_loader]] software on a storage device (like a hard drive's [[Master_boot_record|MBR]], floppy disk, CD/DVD, or USB drive) according to a configured boot order, loads it into [[RAM]], and transfers control to it.
3.  **Hardware Initialization:** Initializes basic hardware components required for booting.
4.  **[[CMOS_Setup|BIOS Setup Utility (CMOS Setup)]]:** Provides a basic user interface (accessed via a key press like DEL, F2, F10 during boot) allowing users to configure hardware settings (e.g., system time/date, boot order, CPU/RAM settings, enable/disable peripherals). These settings are typically stored in volatile CMOS memory powered by a small battery.
5.  **Basic Runtime Services (Legacy):** Historically provided a basic set of interrupt-driven routines for the operating system (especially DOS) to interact with hardware like the keyboard, display, and disk drives. Modern OSes generally bypass these, using their own drivers.

## Limitations & Successor

- **Legacy Design:** Based on architecture dating back to the original IBM PC.
- **MBR Booting:** Limited by the [[Master_boot_record]] partitioning scheme (e.g., disk size limits, limited number of primary partitions).
- **16-bit Execution:** Runs in 16-bit mode with limited memory access during boot.
- **Limited Hardware Support:** May lack built-in drivers for modern hardware (network cards, newer storage controllers) during the boot phase.
- **Security:** Less secure boot process compared to its successor.
- **Successor:** Largely replaced by [[UEFI]] (Unified Extensible Firmware Interface) on modern computers, which overcomes many of these limitations.

## Related Concepts
- [[Firmware]] (BIOS is system firmware)
- [[UEFI]] (Modern successor)
- [[Motherboard]] (Where the BIOS chip resides)
- [[Boot_Process_C]] (BIOS initiates the boot process)
- [[Boot_loader]] (Loaded by BIOS)
- [[POST]] (Hardware check performed by BIOS)
- [[CMOS_Setup]] (Configuration utility accessed via BIOS)
- [[ROM]], [[Flash_Memory]] (Storage medium for BIOS firmware)
- [[Master_boot_record]] (Boot sector used by legacy BIOS)

---
**Source:** Worksheet WS1