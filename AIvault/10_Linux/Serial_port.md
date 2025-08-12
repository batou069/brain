---
tags:
  - linux
  - hardware
  - concept
  - interface
  - port
  - communication
  - networking
  - protocol
  - core
aliases:
  - Serial Port
  - COM Port
  - Internet Protocol
  - IP Address
related:
  - "[[Parallel_port]]"
  - "[[USB]]"
  - "[[RS-232]]"
  - "[[UART]]"
  - "[[Modem]]"
  - "[[Terminal]]"
  - "[[I/O_device]]"
  - "[[Networking_Protocols]]"
  - "[[TCP]]"
  - "[[UDP]]"
  - "[[OSI_Model]]"
  - "[[TCP_IP_Model]]"
  - "[[IP_Address_v4]]"
  - "[[IP_Address_v6]]"
  - "[[Subnet_Mask]]"
  - "[[Router]]"
  - "[[Packet]]"
worksheet:
  - WS1
  - WS26
date_created: 2025-04-21
---
# Serial Port

## Definition

A **Serial Port** is a serial communication interface through which information transfers in or out one [[bits|bit]] at a time (in contrast to a [[Parallel_port|parallel port]]). Throughout most of the history of personal computers, serial ports connected devices like terminals, modems, mice, and printers.

## Key Aspects / Characteristics

- **Serial Transmission:** Data bits are sent sequentially over a single data line (or pair of lines).
- **Asynchronous/Synchronous:** Can support both, but most common PC serial ports (using [[RS-232]]) are asynchronous, meaning no shared clock signal is used; timing is managed by start and stop bits added to each data byte.
- **[[RS-232]] Standard:** The most common standard defining the electrical characteristics, timing, signal meanings, and physical connectors (like DE-9 or DB-25) for serial ports on PCs.
- **[[UART]] (Universal Asynchronous Receiver/Transmitter):** The hardware chip that manages the conversion between the parallel data format inside the computer and the serial format used by the port.
- **COM Ports:** On IBM PC compatible systems (especially under DOS/Windows), serial ports are often referred to as COM ports (COM1, COM2, etc.).
- **Use Cases (Historical & Niche):**
    - Connecting external [[Modem|modems]].
    - Connecting serial mice (older).
    - Connecting some printers (older).
    - Console access for servers, routers, switches, and embedded systems (still common).
    - Interfacing with scientific instruments, industrial hardware, GPS receivers.
    - Debugging embedded systems.
- **Legacy Interface:** Largely replaced by [[USB]] for most consumer peripherals due to USB's higher speed, hot-plugging capability, and power delivery. However, still widely used in industrial, networking, and embedded contexts for its simplicity and robustness.

## Related Concepts
- [[Parallel_port]] (Contrast: transmits multiple bits simultaneously)
- [[USB]] (Modern successor for most peripherals)
- [[RS-232]] (Common standard for serial ports)
- [[UART]] (The hardware controller)
- Serial Communication
- [[Modem]]
- Console Port

---
**Source:** Worksheet WS1

# IP (Internet Protocol)

## Definition

The **Internet Protocol (IP)** is the principal communications protocol in the Internet protocol suite ([[TCP_IP_Model]]) for relaying datagrams (packets) across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet. IP defines addressing methods ([[IP_Address_v4]], [[IP_Address_v6]]) to identify hosts and delivers packets from a source host to a destination host based solely on the IP addresses in the packet headers.

## Key Aspects / Characteristics

- **Network Layer Protocol:** Operates at the Network Layer (Layer 3) of the [[OSI_Model]] and the Internet Layer of the [[TCP_IP_Model]].
- **Addressing:** Defines a logical addressing scheme ([[IP_Address_v4]], [[IP_Address_v6]]) that uniquely identifies devices (hosts) on a network.
- **Routing:** Responsible for moving data packets from their source to their destination across potentially multiple interconnected networks (internetworking), using [[Router|routers]] to make forwarding decisions based on destination IP addresses.
- **Packetization:** Data from higher layers (like [[TCP]] or [[UDP]]) is encapsulated into IP packets (datagrams), which include headers containing source/destination addresses and other control information.
- **Connectionless:** IP itself is a connectionless protocol. Each packet is treated independently, and there is no guarantee of delivery, order, or freedom from errors. It relies on routers making best-effort delivery decisions.
- **Unreliable:** IP does not guarantee that packets will arrive at the destination, arrive in the correct order, or arrive without errors or duplication. Reliability is typically handled by higher-level protocols like [[TCP]].
- **Versions:**
    - **[[IP_Address_v4|IPv4]]:** The original, widely deployed version using 32-bit addresses (e.g., `192.168.1.100`). Facing address exhaustion.
    - **[[IP_Address_v6|IPv6]]:** Newer version designed to replace IPv4, using 128-bit addresses (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`) providing a vastly larger address space and other improvements.

## Role in TCP/IP Suite

IP provides the host-to-host addressing and routing mechanism. It typically works in conjunction with:
- **Higher Layer Protocols:** [[TCP]] (provides reliable, connection-oriented transport) or [[UDP]] (provides unreliable, connectionless transport) run *on top* of IP.
- **Lower Layer Protocols:** IP runs *on top* of Data Link Layer protocols (like Ethernet, Wi-Fi) which handle data transfer within a single physical network segment.

## Related Concepts
- [[Networking_Protocols]], [[TCP_IP_Model]], [[OSI_Model]]
- [[TCP]], [[UDP]] (Transport layer protocols using IP)
- [[IP_Address_v4]], [[IP_Address_v6]], [[Subnet_Mask]] (Addressing)
- [[Router]] (Device making IP routing decisions)
- [[Packet]] / Datagram (Unit of data handled by IP)
- Connectionless Communication, Unreliable Delivery

---
**Source:** Worksheet WS1, WS26