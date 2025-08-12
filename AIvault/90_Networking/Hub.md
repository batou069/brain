---
tags:
  - networking
  - concept
  - hardware
  - physical_layer
  - legacy
aliases:
  - Network Hub
  - Ethernet Hub
  - Repeater Hub
related:
  - "[[Physical_Layer]]"
  - "[[OSI_Model]]"
  - "[[Switch]]"
  - "[[Router]]"
  - "[[Collision_Domain]]"
  - "[[Broadcast_Domain]]"
  - "[[Ethernet]]" # Placeholder
  - "[[LAN]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# Hub (Network)

## Definition

A **Network Hub** (or Ethernet Hub, Repeater Hub) is a simple, legacy networking device that operates at the **[[Physical_Layer|Physical Layer]]** (Layer 1) of the [[OSI_Model]]. It serves as a central connection point for multiple devices in a network segment (typically a [[LAN]]), but lacks any intelligence for directing traffic.

## Key Functions & Characteristics

- **Central Connection Point:** Provides multiple ports (usually Ethernet) to connect devices.
- **Signal Repeater:** When an electrical signal (representing data bits) arrives on one port, the hub simply regenerates (amplifies) the signal and **broadcasts it out all other ports**, regardless of the intended destination.
- **No Addressing Awareness:** Operates purely at the electrical signal level. It does not examine [[MAC_Address|MAC addresses]] (Layer 2) or [[ip|IP addresses]] (Layer 3).
- **Single Collision Domain:** All devices connected to a hub share the same **[[Collision_Domain]]**. If two devices transmit simultaneously, their signals collide, corrupting the data. Devices must use an access method like CSMA/CD (Carrier Sense Multiple Access with Collision Detection) to listen before transmitting and detect/recover from collisions. This severely limits performance, especially as more devices are added or traffic increases.
- **Single Broadcast Domain:** All devices connected to a hub are part of the same [[Broadcast_Domain]]. Broadcast frames sent by one device are repeated to all other devices.
- **Half-Duplex Operation:** Because of the shared collision domain, devices connected to a hub typically operate in half-duplex mode (they can either send or receive at any given moment, but not both simultaneously).
- **Obsolete:** Hubs have been almost entirely replaced by [[Switch|network switches]] in modern networks because switches offer significantly better performance and efficiency by creating separate collision domains per port and forwarding traffic intelligently based on MAC addresses.

## Hub vs. Switch vs. Router

- **Hub:** Layer 1. Repeats signals out all ports. Single collision domain. Single broadcast domain. Dumb device.
- **[[Switch]]:** Layer 2. Forwards based on MAC addresses. Separate collision domain per port. Single broadcast domain (by default). Intelligent Layer 2 device.
- **[[Router]]:** Layer 3. Forwards based on IP addresses between different networks. Separates broadcast domains. Intelligent Layer 3 device.

## Related Concepts
- [[Physical_Layer]], [[OSI_Model]]
- [[Switch]], [[Router]] (More advanced devices)
- [[Collision_Domain]], [[Broadcast_Domain]]
- [[Ethernet]] (Common protocol used with hubs/switches)
- [[LAN]] (Hubs were used in early LANs)
- Repeater (Hubs function as multi-port repeaters)

---
**Source:** Worksheet WS26