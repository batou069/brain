---
tags:
  - networking
  - concept
  - hardware
  - network_layer
aliases: []
related:
  - "[[ip]]"
  - "[[Network_Layer]]"
  - "[[OSI_Model]]"
  - "[[TCP_IP_Model]]"
  - "[[Routing]]" # Placeholder
  - "[[Routing_Table]]" # Placeholder
  - "[[Subnet]]"
  - "[[Switch]]"
  - "[[Hub]]"
  - "[[Gateway]]" # Often acts as default gateway
worksheet: [WS26]
date_created: 2025-04-21
---
# Router

## Definition

A **Router** is a networking device that operates at the **[[Network_Layer|Network Layer]]** (Layer 3) of the [[OSI_Model]]. Its primary function is to **forward data packets** ([[ip|IP packets]]) between different computer networks (or [[Subnet|subnets]]). Routers make decisions about the best path for packets to travel based on logical addresses ([[ip|IP addresses]]) and information stored in their [[Routing_Table|routing tables]].

## Key Functions

- **[[Routing|Routing]] / Path Determination:** Examines the destination IP address in an incoming packet's header and consults its internal routing table to determine the optimal next hop (the next router or the final destination network) to send the packet towards.
- **Packet Forwarding:** Moves packets between its different network interfaces (connected to different networks/subnets).
- **Connecting Networks:** Connects distinct IP networks or subnets together, enabling communication between them (internetworking). Home routers connect a local network (LAN) to the ISP's network (WAN/Internet). Core Internet routers connect large networks together.
- **Broadcast Containment:** Routers do **not** typically forward broadcast packets between the networks they connect. Each connected network interface is in a separate broadcast domain. This helps limit network congestion.
- **Network Address Translation (NAT):** Many home/office routers perform NAT, allowing multiple devices on a private internal network (using private IP addresses) to share a single public IP address for Internet access.
- **Other Functions (Often Integrated):** Modern routers, especially home/SOHO routers, often integrate other functions like:
    - [[Switch|Switching]] (built-in Ethernet switch ports)
    - Wireless Access Point (Wi-Fi)
    - [[DHCP]] Server (assigning IP addresses to local devices)
    - Firewall capabilities

## Router vs. Switch vs. Hub

- **[[Hub]]:** Layer 1 (Physical). Simple repeater. Receives signal on one port, regenerates and broadcasts it out *all* other ports. Creates a single collision domain. Inefficient and obsolete.
- **[[Switch]]:** Layer 2 (Data Link). Learns MAC addresses of connected devices. Forwards frames only out the specific port connected to the destination MAC address (or floods if unknown). Creates separate collision domains per port but a single broadcast domain by default.
- **Router:** Layer 3 (Network). Connects different networks/subnets. Makes forwarding decisions based on IP addresses using a routing table. Separates broadcast domains.

## Related Concepts
- [[ip]], [[Network_Layer]], [[OSI_Model]], [[TCP_IP_Model]]
- [[Routing]], [[Routing_Table]]
- [[Subnet]] (Routers connect subnets)
- [[Switch]], [[Hub]] (Lower-layer devices)
- [[Gateway]] (A router often serves as the default gateway for hosts on a LAN)
- Packet Forwarding, Internetworking
- NAT, DHCP, Firewall (Often integrated features)

---
**Source:** Worksheet WS26