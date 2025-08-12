---
tags:
  - linux
  - hardware
  - concept
  - interface
  - port
  - bus
aliases:
  - Universal Serial Bus
related:
  - "[[Bus]]"
  - "[[Serial_port]]"
  - "[[Parallel_port]]"
  - "[[I/O_device]]"
  - "[[Plug_and_Play]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# USB (Universal Serial Bus)

## Definition

**USB (Universal Serial Bus)** is an industry standard that establishes specifications for cables, connectors, and protocols for connection, communication, and power supply (interfacing) between computers, peripherals, and other computers. It is designed to standardize the connection of various [[I/O_device|peripheral devices]] to computers, both to communicate and to supply electric power.

## Key Aspects / Characteristics

- **Standardization:** Replaced a variety of earlier interfaces like [[Serial_port|serial ports]], [[Parallel_port|parallel ports]], PS/2 ports, and game ports with a single, unified standard.
- **Serial Communication:** Transmits data bit-by-bit over a serial line (though modern versions use multiple lanes for higher speeds).
- **Hot-Pluggable:** Devices can be connected and disconnected while the computer is running without needing a reboot.
- **Plug and Play:** Supports automatic detection and configuration of devices by the [[Operating_System]].
- **Power Delivery:** Can supply power to connected devices, eliminating the need for separate power adapters for many peripherals (e.g., keyboards, mice, webcams, external drives, charging phones). Power delivery capabilities have increased significantly with newer standards (USB Power Delivery - USB PD).
- **Host-Controlled Bus:** A USB system has a single host controller (in the computer) that manages communication with multiple devices connected in a tiered-star topology (using hubs). Devices cannot typically communicate directly with each other without host involvement (except with USB On-The-Go - OTG).
- **Versions & Speeds:** Has evolved through several versions with increasing data transfer speeds:
    - USB 1.x (Low Speed 1.5 Mbps, Full Speed 12 Mbps)
    - USB 2.0 (High Speed 480 Mbps)
    - USB 3.x (SuperSpeed 5 Gbps, 10 Gbps, 20 Gbps)
    - USB4 (Up to 40 Gbps, based on Thunderbolt 3 protocol)
- **Connector Types:** Various physical connector types exist (Type-A, Type-B, Mini-USB, Micro-USB, Type-C). USB Type-C is becoming prevalent due to its reversibility and support for multiple protocols (including DisplayPort, Thunderbolt via alternate modes) and higher power delivery.

## Use Cases

- Connecting keyboards, mice, printers, scanners, webcams, external hard drives/SSDs, flash drives, digital cameras, smartphones, game controllers, network adapters, audio interfaces, etc.
- Charging devices.

## Related Concepts
- [[Bus]], [[Serial_port]], [[Parallel_port]] (Interfaces USB replaced)
- [[I/O_device]] (Devices connected via USB)
- [[Plug_and_Play]] (Feature supported by USB)
- Data Transfer Rates, Power Delivery

---
**Source:** Worksheet WS1