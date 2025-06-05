---
tags:
  - networking
  - concept
  - hardware
  - data_link_layer
aliases:
  - Network Switch
  - Ethernet Switch
related:
  - "[[Data_Link_Layer]]"
  - "[[OSI_Model]]"
  - "[[MAC_Address]]" # Placeholder
  - "[[Ethernet_Frame]]" # Placeholder
  - "[[Router]]"
  - "[[Hub]]"
  - "[[Collision_Domain]]" # Placeholder
  - "[[Broadcast_Domain]]" # Placeholder
  - "[[LAN]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# Switch (Network)

## Definition

A **Network Switch** (or Ethernet Switch) is a networking hardware device that operates primarily at the **[[Data_Link_Layer|Data Link Layer]]** (Layer 2) of the [[OSI_Model]]. It connects multiple devices (like computers, printers, servers) together on a computer network (typically a Local Area Network - [[LAN]]) and uses [[MAC_Address|MAC addresses]] to intelligently forward data packets (specifically, [[Ethernet_Frame|Ethernet frames]]) only to the port connected to the intended recipient device.

## Key Functions

- **Connects Devices:** Provides multiple physical ports (usually Ethernet) to connect network devices.
- **MAC Address Learning:** Learns the MAC addresses of devices connected to each of its ports by examining the source MAC address of incoming frames. It stores this information in a MAC address table (also called CAM table or forwarding table).
- **Intelligent Frame Forwarding:** When a frame arrives, the switch looks up the destination MAC address in its table:
    - If the destination MAC is found and associated with a specific port, the switch forwards the frame *only* out that port.
    - If the destination MAC is unknown (or is a broadcast/multicast address), the switch **floods** the frame out all ports *except* the one it arrived on.
- **Collision Domain Segmentation:** Each port on a switch represents a separate **[[Collision_Domain]]**. This means devices connected to different ports can transmit simultaneously without causing collisions (unlike a [[Hub]]), significantly improving network efficiency, especially under load.
- **Full-Duplex Operation:** Most modern switches support full-duplex communication, allowing devices to send and receive data simultaneously on a port without collisions.

## Switch vs. Router vs. Hub

- **[[Hub]]:** Layer 1. Repeats signals out all ports. Single collision domain. Single broadcast domain.
- **Switch:** Layer 2. Forwards based on MAC addresses. Separate collision domain per port. Single broadcast domain (by default).
- **[[Router]]:** Layer 3. Forwards based on IP addresses between different networks. Separates broadcast domains. Separates collision domains (as each interface connects to a separate network/switch).

*(Note: Multi-layer switches exist that can perform some Layer 3 (routing) functions).*

## Related Concepts
- [[Data_Link_Layer]], [[OSI_Model]]
- [[MAC_Address]], [[Ethernet_Frame]]
- [[Router]], [[Hub]] (Contrasting devices)
- [[Collision_Domain]], [[Broadcast_Domain]]
- [[LAN]] (Switches are core components of LANs)
- MAC Address Table / CAM Table

---
**Source:** Worksheet WS26