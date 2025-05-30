---
tags:
  - linux
  - hardware
  - concept
  - interface
  - storage
  - standard
  - legacy
aliases:
  - AT Attachment Packet Interface
  - ATA Packet Interface
related:
  - "[[ATA]]"
  - "[[SATA]]"
  - "[[IDE]]"
  - "[[SCSI]]"
  - "[[CD-ROM_Drive]]"
  - "[[DVD_Drive]]"
  - "[[Tape_Drive]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# ATAPI (AT Attachment Packet Interface)

## Definition

**ATAPI (AT Attachment Packet Interface)** is a protocol that extends the [[ATA]] (Advanced Technology Attachment, also known as [[IDE]]) interface standard, allowing devices other than hard disk drives to connect to a standard ATA/IDE controller. It achieves this by using ATA commands to transport [[SCSI]]-like command packets to the device.

## Key Aspects / Characteristics

- **Extension of ATA/IDE:** Builds upon the existing ATA interface used primarily for hard drives.
- **Packet Interface:** Uses a "Packet" command within the ATA command set. This command allows sending command packets (similar in structure to SCSI commands) to the ATAPI device.
- **Enables Non-HDD Devices:** Allowed devices like [[CD-ROM_Drive|CD-ROM drives]], [[DVD_Drive|DVD drives]], [[Tape_Drive|tape drives]], and large-capacity floppy drives (like Zip drives) to use the common and inexpensive ATA/IDE interface found on PC motherboards, rather than requiring a separate, more expensive [[SCSI]] controller.
- **SCSI Command Set (Subset):** The command packets sent via ATAPI often use commands based on the SCSI command set, allowing device manufacturers to leverage existing SCSI firmware logic.
- **Integration:** Allowed seamless integration of optical drives and other peripherals into the PC ecosystem using the standard IDE channels.
- **Legacy:** While the concept of packet interfaces persists, the specific ATAPI protocol over the parallel ATA (PATA/IDE) interface is largely legacy, superseded by [[SATA]] for internal drives and [[USB]]/[[FireWire]] for external devices. SATA uses the ATA Command Set (ACS), which incorporates and standardizes the packet command features originally introduced by ATAPI.

## Related Concepts
- [[ATA]] / [[IDE]] (The underlying interface standard)
- [[SATA]] (Serial ATA, the modern successor)
- [[SCSI]] (Alternative interface; ATAPI borrowed SCSI command concepts)
- [[CD-ROM_Drive]], [[DVD_Drive]], [[Tape_Drive]] (Devices commonly using ATAPI)
- Command Packets

---
**Source:** Worksheet WS1