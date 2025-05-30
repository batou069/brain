---
tags:
  - linux
  - networking
  - protocol
  - concept
  - core
aliases:
  - Internet Protocol
  - IP Address
related:
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
date_created: 2025-04-20
---
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