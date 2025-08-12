---
tags:
  - networking
  - concept
  - addressing
  - transport_layer
aliases:
  - Port Numbers
  - Network Port
  - Transport Layer Port
related:
  - "[[Sockets]]"
  - "[[ip]]"
  - "[[TCP]]"
  - "[[UDP]]"
  - "[[TCP_IP_Model]]"
  - "[[Transport_Layer]]"
  - "[[Well_Known_Ports]]"
  - "[[Registered_Ports]]"
  - "[[Ephemeral_Ports]]"
  - "[[Multiplexing]]"
  - "[[Demultiplexing]]"
worksheet: [WS26, WS28]
date_created: 2025-04-21
---
# Port (Networking)

## Definition

In [[TCP_IP_Model|TCP/IP networking]], a **Port** is a logical endpoint for communication associated with a specific process or service running on a host computer. It is represented by a 16-bit unsigned integer (**Port Number**, 0-65535) used by [[Transport_Layer|Transport Layer]] protocols ([[TCP]], [[UDP]]) to distinguish between different applications or conversations running on the same host identified by its [[ip|IP address]]. The combination of an IP address and a port number forms a [[Sockets|network socket]].

## How Ports Work

1.  **[[Multiplexing]] (Sending):** When an application wants to send data, it creates a [[Sockets|socket]] and specifies the destination IP address and destination port number. The transport protocol (TCP/UDP) adds the application's *source port number* (often an [[Ephemeral_Ports|ephemeral port]] chosen by the OS) and the destination port number to the segment/datagram header, along with the data. The [[ip|IP layer]] then adds source/destination IP addresses. This allows multiple applications on the source host to send data seemingly simultaneously over the same network interface.
2.  **[[Demultiplexing]] (Receiving):** When a host receives an IP packet, the IP layer passes the payload (TCP segment or UDP datagram) up to the transport layer. The transport layer examines the **destination port number** in the header. It uses this port number to identify which local application process the data is intended for (i.e., which application has a socket bound to or listening on that port). The data is then delivered to the correct application's socket buffer. This allows multiple applications on the receiving host to receive data concurrently.

## Purpose

- **Application Identification:** Distinguishes between multiple network applications running on the same host. Without ports, the OS wouldn't know whether an incoming web request should go to a web server process or an email process.
- **Service Identification:** Standard services are assigned [[Well_Known_Ports]] (e.g., HTTP on port 80, HTTPS on 443) so clients know which port to connect to by default.
- **Enabling Concurrent Connections:** Allows a single host to maintain multiple simultaneous network connections (e.g., multiple web browser tabs connecting to different or even the same web server). Each connection uses a different socket pair (often differing by the client's ephemeral source port).

## Port Number Ranges (IANA Categories)

The Internet Assigned Numbers Authority (IANA) categorizes port numbers:

1.  **[[Well_Known_Ports|Well-Known Ports (0-1023)]]:** Assigned to standard system services (e.g., 22:SSH, 53:DNS, 80:HTTP, 443:HTTPS).**** Require root/admin privileges to bind to.
2.  **[[Registered_Ports|Registered Ports (1024-49151)]]:** Assigned by IANA for specific applications (e.g., 3306:MySQL, 5432:PostgreSQL). Usually don't require special privileges.
3.  **[[Ephemeral_Ports|Dynamic/Private/Ephemeral Ports (49152-65535)]]:** Used for temporary client-side source ports.

## Related Concepts
- [[Sockets]] (IP Address + Port Number)
- [[ip]] (Host addressing)
- [[TCP]], [[UDP]] (Protocols using ports)
- [[Transport_Layer]], [[TCP_IP_Model]]
- Port Categories: [[Well_Known_Ports]], [[Registered_Ports]], [[Ephemeral_Ports]]
- [[Multiplexing]], [[Demultiplexing]] (Core functions enabled by ports)

---
**Source:** Worksheet WS26, WS28