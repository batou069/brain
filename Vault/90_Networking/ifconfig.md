---
tags:
  - networking
  - tool
  - command
  - linux
  - troubleshooting
  - legacy
aliases:
  - ifconfig command
related:
  - "[[ip_command]]" # Modern replacement
  - "[[ip]]"
  - "[[MAC_Address]]"
  - "[[Network_Interface_Card]]" # Placeholder
  - "[[Troubleshooting_Network]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# ` ifconfig `

## Purpose

`ifconfig` (interface configuration) is a **legacy** command-line utility on Unix-like systems used to **configure, manage, and query network interface parameters**. It can display information about active network interfaces (like IP address, netmask, MAC address) and modify their settings.

## Status

**Deprecated:** `ifconfig` is considered deprecated on modern Linux systems and has been largely replaced by the more powerful and versatile `ip` command (from the `iproute2` package). While still available on many systems for backward compatibility or out of habit, using the `ip` command is generally recommended.

## Common Usage (Legacy)

```bash
# Display information about all active network interfaces
ifconfig

# Display information about a specific interface (e.g., eth0)
ifconfig eth0

# Bring an interface UP
ifconfig eth0 up

# Bring an interface DOWN
ifconfig eth0 down

# Assign an IP address and netmask to an interface (temporary)
ifconfig eth0 192.168.1.100 netmask 255.255.255.0

# Change the MAC address (requires interface down first sometimes)
ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF
```

## Information Displayed

When run without arguments, `ifconfig` typically shows for each active interface:
- Interface name (e.g., `eth0`, `wlan0`, `lo`)
- Hardware Address ([[MAC_Address]])
- [[ip|IP Address]] (inet addr)
- Broadcast Address (Bcast)
- [[Subnet_Mask|Subnet Mask]] (Mask)
- IPv6 Address (inet6 addr)
- MTU (Maximum Transmission Unit)
- Interface flags/status (UP, BROADCAST, RUNNING, MULTICAST, etc.)
- Statistics (RX/TX packets, errors, dropped, collisions)

## Modern Replacement (`ip` command)

Equivalent `ip` commands:
```bash
ip addr show # (or `ip a`): Replaces `ifconfig` (shows all interfaces).
ip link show # Shows link-layer information (MAC, MTU, state).
ip link set eth0 up # Replaces `ifconfig eth0 up`.
ip link set eth0 down # Replaces `ifconfig eth0 down`.
ip addr add 192.168.1.100/24 dev eth0 # Replaces `ifconfig eth0 ip netmask ...`.
ip link set dev eth0 address AA:BB:CC:DD:EE:FF # Replaces `ifconfig eth0 hw ether ...`.
```

## Related Concepts
- [[ip_command]] (Modern replacement)
- [[ip]], [[MAC_Address]], [[Subnet_Mask]] (Information displayed/configured)
- [[Network_Interface_Card]] (The hardware being configured)
- [[Troubleshooting_Network]]

---
**Source:** Worksheet WS26, `ifconfig` man page