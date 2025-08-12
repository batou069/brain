---
tags:
  - linux
  - networking
  - protocol
  - concept
  - transport_layer
aliases:
  - Transmission Control Protocol
related:
  - "[[Networking_Protocols]]"
  - "[[IP]]"
  - "[[UDP]]"
  - "[[OSI_Model]]"
  - "[[TCP_IP_Model]]"
  - "[[Sockets]]"
  - "[[Port_Number]]"
  - "[[Three-Way_Handshake]]"
  - "[[Flow_Control]]"
  - "[[Congestion_Control]]"
  - "[[HTTP]]"
  - "[[HTTPS]]"
  - "[[SSH]]"
  - "[[FTP]]"
  - "[[SMTP]]"
worksheet:
  - WS1
  - WS26
date_created: 2025-04-20
---
# TCP (Transmission Control Protocol)

## Definition

**Transmission Control Protocol (TCP)** is one of the main protocols of the Internet protocol suite ([[TCP_IP_Model]]). It operates at the Transport Layer (Layer 4 of [[OSI_Model]]), providing **reliable, ordered, and error-checked** delivery of a stream of bytes between applications running on hosts communicating over an [[IP|IP network]]. TCP is a **connection-oriented** protocol.

## Key Aspects / Characteristics

- **Connection-Oriented:** Requires a connection to be established between the two communicating applications before data transfer begins. This involves a [[Three-Way_Handshake]] (SYN, SYN-ACK, ACK). A connection teardown process also occurs.
- **Reliability:** Guarantees that data sent will arrive at the destination without corruption and in the correct order. It achieves this through:
    - **Sequence Numbers:** Each byte sent is numbered, allowing the receiver to reorder packets that arrive out of sequence.
    - **Acknowledgments (ACKs):** The receiver sends acknowledgments back to the sender confirming receipt of data segments.
    - **Retransmissions:** If the sender doesn't receive an ACK within a certain time (timeout), it retransmits the lost segment.
    - **Checksums:** Used to detect data corruption within TCP segments.
- **Ordered Delivery:** Ensures that data bytes are delivered to the receiving application in the same order they were sent by the sending application.
- **[[Flow_Control]]:** Prevents a fast sender from overwhelming a slow receiver. The receiver advertises its available buffer space (receive window), and the sender adjusts its sending rate accordingly.
- **[[Congestion_Control]]:** Aims to prevent network congestion by regulating the rate at which data is injected into the network, based on perceived network conditions (e.g., packet loss, delays).
- **Full-Duplex:** Allows data to flow in both directions simultaneously over a single connection.
- **Stream-Based:** Treats data as a continuous stream of bytes, rather than distinct messages (like [[UDP]]). Application layer protocols running over TCP must define their own message boundaries if needed.
- **Port Numbers:** Uses [[Port_Number|port numbers]] along with IP addresses ([[Sockets]]) to identify specific sending and receiving application processes on the hosts.

## Common Applications Using TCP

TCP is used for applications where reliability and order are critical:
- [[HTTP]] / [[HTTPS]] (Web browsing)
- [[FTP]] (File Transfer Protocol)
- [[SMTP]] (Simple Mail Transfer Protocol - sending email)
- POP3 / IMAP (Receiving email)
- [[SSH]] (Secure Shell)
- Telnet

## TCP vs. UDP

| Feature          | TCP                                  | [[UDP]]                              |
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
- [[IP]] (TCP runs on top of IP)
- [[UDP]] (Alternative transport protocol)
- [[Sockets]], [[Port_Number]] (Addressing applications)
- [[Three-Way_Handshake]] (Connection setup)
- [[Flow_Control]], [[Congestion_Control]], Sequence Numbers, Acknowledgments (Reliability mechanisms)

## Questions / Further Study
>[!question] What are the differences between TCP and UDP? (WS26)
> See the comparison table above. Key differences are: TCP is connection-oriented, reliable, ordered, and has flow/congestion control, making it slower but dependable. UDP is connectionless, unreliable, unordered, and faster due to less overhead, suitable for applications where speed matters more than guaranteed delivery (like streaming or DNS).

---
**Source:** Worksheet WS1, WS26