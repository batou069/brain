---
tags:
  - networking
  - concept
  - addressing
  - ip
aliases:
  - Subnetwork
related:
  - "[[ip]]"
  - "[[IP_Address_v4]]"
  - "[[IP_Address_v6]]"
  - "[[Subnet_Mask]]"
  - "[[CIDR]]"
  - "[[Router]]"
  - "[[Broadcast_Address]]"
  - "[[Network_Address]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# Subnet (Subnetwork)

## Definition

A **Subnet** (short for **subnetwork**) is a logical subdivision of a larger [[ip|IP network]]. The process of dividing a network into two or more smaller networks is called **subnetting**. This is achieved by using a portion of the host part of an IP address to identify the specific subnet, effectively extending the network portion of the address.

## Purpose

- **Network Management & Organization:** Breaks down large networks into smaller, more manageable segments (e.g., by department, building, floor).
- **Improved Performance:** Reduces network broadcast traffic. Broadcast messages (sent to all hosts on a network) are generally confined within their own subnet and are not forwarded by [[Router|routers]] to other subnets, reducing overall network congestion.
- **Enhanced Security:** Allows for the implementation of security policies between subnets using firewalls or Access Control Lists (ACLs) on routers. Traffic between subnets must pass through a router, providing points for control and monitoring.
- **Overcoming Distance Limitations:** Routers connecting subnets can overcome physical distance limitations of a single network segment (like Ethernet length limits).
- **Efficient Use of IP Addresses:** Allows more granular allocation of IP address ranges within an organization.

## How it Works ([[IP_Address_v4|IPv4]])

- **[[Subnet_Mask]]:** A 32-bit number that defines which part of an IP address represents the network (and subnet) portion and which part represents the host portion. It has '1's for the network/subnet bits and '0's for the host bits.
- **Borrowing Host Bits:** Subnetting involves "borrowing" bits from the host portion of the original IP address range and using them to create subnet identifiers.
- **Network & Broadcast Addresses:** Within each subnet, two addresses are reserved:
    - **[[Network_Address]]:** The first address in the range (all host bits are 0). Identifies the subnet itself.
    - **[[Broadcast_Address]]:** The last address in the range (all host bits are 1). Used to send messages to all hosts within that specific subnet.
- **Usable Host Addresses:** The addresses between the network and broadcast addresses are available for assignment to devices. The number of usable hosts depends on the number of bits allocated to the host portion.
- **[[CIDR]] (Classless Inter-Domain Routing):** Modern notation for representing subnets, using a slash followed by the number of bits in the network prefix (e.g., `192.168.1.0/24`). `/24` means the first 24 bits are the network portion (equivalent to subnet mask `255.255.255.0`).

## Example

- Network: `192.168.1.0` with mask `255.255.255.0` (or `/24`).
- Let's subnet this into smaller networks using mask `255.255.255.192` (or `/26`). This borrows 2 bits from the host portion (`192` = `11000000` in binary).
- Possible Subnets:
    - Subnet 1: `192.168.1.0/26` (Network Addr: `.0`, Host Range: `.1` to `.62`, Broadcast Addr: `.63`)
    - Subnet 2: `192.168.1.64/26` (Network Addr: `.64`, Host Range: `.65` to `.126`, Broadcast Addr: `.127`)
    - Subnet 3: `192.168.1.128/26` (Network Addr: `.128`, Host Range: `.129` to `.190`, Broadcast Addr: `.191`)
    - Subnet 4: `192.168.1.192/26` (Network Addr: `.192`, Host Range: `.193` to `.254`, Broadcast Addr: `.255`)
- Hosts within the same subnet can communicate directly (via a [[Switch]]). Hosts in different subnets must communicate via a [[Router]].

## Related Concepts
- [[ip]], [[IP_Address_v4]], [[IP_Address_v6]]
- [[Subnet_Mask]], [[CIDR]] (Define subnets)
- [[Router]] (Connects different subnets)
- [[Network_Address]], [[Broadcast_Address]] (Reserved addresses within a subnet)
- [[Switch]], [[Hub]] (Operate within a single subnet/broadcast domain)
- Network Segmentation

---
**Source:** Worksheet WS26