---
tags:
  - linux
  - hardware
  - concept
  - interface
  - storage
  - standard
aliases:
  - Serial ATA
  - Serial Advanced Technology Attachment
related:
  - "[[ATA]]"
  - "[[PATA]]"
  - "[[ATAPI]]"
  - "[[IDE]]"
  - "[[Hard_disk]]"
  - "[[SSD]]"
  - "[[Bus]]"
  - "[[NVMe]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# SATA (Serial ATA)

## Definition

**SATA (Serial Advanced Technology Attachment)** is a computer [[Bus|bus]] interface standard that connects host bus adapters (typically integrated into motherboards) to mass storage devices such as [[Hard_disk|hard disk drives (HDDs)]], [[SSD|solid-state drives (SSDs)]], and optical drives. SATA replaced the older Parallel ATA ([[PATA]], often referred to as [[IDE]]) standard.

## Key Aspects / Characteristics

- **Serial Communication:** Uses serial signaling (transmitting one bit at a time over a differential pair) instead of the parallel signaling used by PATA.
- **Advantages over PATA:**
    - **Higher Speeds:** Offers significantly higher data transfer rates (SATA 1.5 Gbit/s, 3 Gbit/s, 6 Gbit/s, with newer revisions potentially faster).
    - **Thinner, Longer Cables:** Uses much smaller, thinner cables (7-pin data, 15-pin power) compared to bulky PATA ribbon cables. Allows for longer cable lengths and improved airflow within computer cases.
    - **Simplified Connection:** Point-to-point connection between the device and the host controller (no master/slave/cable select jumpers like PATA).
    - **Hot-Plugging:** Supports connecting/disconnecting drives while the system is running (requires OS and controller support, often enabled via AHCI mode).
- **Command Set:** Uses the ATA Command Set (ACS), which includes features for both traditional hard drives and packet-based devices (incorporating [[ATAPI]] concepts).
- **AHCI (Advanced Host Controller Interface):** A hardware mechanism that allows software to communicate with SATA host controllers, enabling advanced features like hot-plugging and Native Command Queuing (NCQ) for improved performance (especially with HDDs).
- **Connectors:** Distinctive L-shaped data and power connectors.
- **eSATA (External SATA):** A variant for connecting external drives, offering similar speeds to internal SATA but using a different, more robust connector. Largely superseded by USB 3.x and Thunderbolt for external connections.
- **mSATA / M.2 SATA:** Form factors using the SATA protocol for smaller devices like SSDs in laptops and small form-factor PCs. (Note: M.2 slots can also support the much faster [[NVMe]] protocol over PCIe).

## Related Concepts
- [[ATA]] / [[PATA]] / [[IDE]] (The older parallel standard SATA replaced)
- [[ATAPI]] (Concepts integrated into the SATA command set)
- [[Hard_disk]], [[SSD]], Optical Drives (Devices connected via SATA)
- [[Bus]] (SATA is a bus interface)
- [[AHCI]] (Controller interface standard)
- [[NVMe]] (Newer interface standard for SSDs using PCIe, much faster than SATA)
- Data Transfer Rates

---
**Source:** Worksheet WS1