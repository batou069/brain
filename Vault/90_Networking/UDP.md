---
tags:
  - linux
  - networking
  - protocol
  - concept
  - transport_layer
aliases:
  - User Datagram Protocol
related:
  - "[[Networking_Protocols]]"
  - "[[IP]]"
  - "[[TCP]]"
  - "[[OSI_Model]]"
  - "[[TCP_IP_Model]]"
  - "[[Sockets]]"
  - "[[Port_Number]]"
  - "[[Datagram]]"
  - "[[DNS]]"
  - "[[DHCP]]"
  - "[[VoIP]]"
  - "[[Streaming]]"
worksheet:
  - WS1
  - WS26
date_created: 2025-04-20
---
# UDP (User Datagram Protocol)

## Definition

**User Datagram Protocol (UDP)** is one of the core members of the Internet protocol suite ([[TCP_IP_Model]]). It operates at the Transport Layer (Layer 4 of [[OSI_Model]]), providing a simple, **connectionless**, and **unreliable** datagram service. Unlike [[TCP]], UDP does not guarantee delivery, order, or duplicate protection for messages (datagrams).

## Key Aspects / Characteristics

- **Connectionless:** No handshake or connection setup is required before sending data. Each datagram is sent independently.
- **Unreliable:** Provides "best-effort" delivery. There's no acknowledgment of receipt, no retransmission of lost datagrams, and no guarantee datagrams will arrive. Reliability must be handled by the application layer if needed.
- **Unordered Delivery:** Datagrams may arrive at the destination in a different order than they were sent. The receiving application must reorder them if necessary.
- **Datagram-Oriented:** Treats data in discrete chunks called datagrams. Each datagram sent by the application is typically delivered as a single unit (if delivered at all). Application needs to handle message boundaries.
- **Minimal Overhead:** Has a very small header (8 bytes) compared to TCP (>= 20 bytes), resulting in lower overhead and potentially faster transmission.
- **No Flow Control / Congestion Control:** UDP does not regulate sending speed based on receiver capacity or network congestion. Applications using UDP must implement these mechanisms themselves if required, or risk overwhelming the receiver or network.
- **Port Numbers:** Uses [[Port_Number|port numbers]] along with IP addresses ([[Sockets]]) to direct datagrams to the correct application process on the destination host.
- **Checksum:** Includes an optional (in IPv4, mandatory in IPv6) checksum for basic error detection within the UDP header and data. Corrupted datagrams are typically discarded silently.

## Common Applications Using UDP

UDP is suitable for applications where speed and low overhead are more critical than guaranteed delivery, or where occasional data loss is acceptable or handled by the application itself:
- **[[DNS]] (Domain Name System):** Fast lookups are prioritized. Reliability handled by application retries if needed.
- **[[DHCP]] (Dynamic Host Configuration Protocol):** Used for assigning IP addresses.
- **[[VoIP]] (Voice over IP) & Video [[Streaming]]:** Timeliness is crucial; retransmitting old audio/video packets is often useless. Application layer might handle some loss concealment.
- **Online Gaming:** Fast updates are needed; minor packet loss might be tolerated or compensated for.
- **TFTP (Trivial File Transfer Protocol):** Simple file transfer where reliability is less critical or handled by application logic.
- **NTP (Network Time Protocol)**
- **SNMP (Simple Network Management Protocol)**

## TCP vs. UDP

| Feature          | [[TCP]]                              | UDP                                  |
| :--------------- | :----------------------------------- | :----------------------------------- |
| **Connection**   | Connection-Oriented                  | Connectionless                       |
| **Reliability**  | Reliable (ACKs, Retransmissions)     | Unreliable (Best-Effort)             |
| **Ordering**     | Ordered Delivery                     | Unordered Delivery                   |
| **Error Checking**| Yes (Checksum, ACKs)                 | Yes (Checksum - optional in IPv4)    |
| **Flow Control** | Yes                                  | No                                   |
| **Congestion Ctrl**| Yes                                  | No                                   |
| **Header Size**  | Larger (>= 20 bytes)                 | Smaller (8 bytes)                    |
| **Speed**        | Slower (due to overhead)             | Faster (less overhead)               |
| **Use Cases**    | Web, Email, File Transfer, SSH       | DNS, DHCP, VoIP, Online Gaming, Streaming |

## Related Concepts
- [[Networking_Protocols]], [[TCP_IP_Model]], [[OSI_Model]]
- [[IP]] (UDP runs on top of IP)
- [[TCP]] (Alternative transport protocol)
- [[Sockets]], [[Port_Number]] (Addressing applications)
- [[Datagram]] (Unit of data)
- Connectionless Communication, Unreliable Delivery

## Questions / Further Study
>[!question] What are the differences between TCP and UDP? (WS26)
> See the comparison table above. Key differences are: TCP is connection-oriented, reliable, ordered, and has flow/congestion control, making it slower but dependable. UDP is connectionless, unreliable, unordered, and faster due to less overhead, suitable for applications where speed matters more than guaranteed delivery (like streaming or DNS).

---
**Source:** Worksheet WS1, WS26