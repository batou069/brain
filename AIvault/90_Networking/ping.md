---
tags:
  - networking
  - tool
  - command
  - troubleshooting
  - icmp
aliases:
  - ping command
related:
  - "[[ICMP]]" # Placeholder
  - "[[ip]]"
  - "[[Network_Layer]]"
  - "[[Latency]]" # Placeholder
  - "[[Packet_Loss]]" # Placeholder
  - "[[Troubleshooting_Network]]"
  - "[[DNS]]" # Often used implicitly to resolve hostname
worksheet: [WS26]
date_created: 2025-04-21
---
# ` ping `

## Purpose

`ping` (Packet InterNet Groper) is a fundamental command-line network diagnostic tool used to test the **reachability** of a host on an [[ip|IP network]] and measure the **round-trip time** (latency) for messages sent from the originating host to a destination computer.

## How it Works

1.  `ping` sends **[[ICMP]] Echo Request** packets to the target host specified by its IP address or hostname. (If a hostname is given, [[DNS]] is used first to resolve it to an IP address).
2.  The target host, upon receiving an ICMP Echo Request, is expected (if not blocked by a firewall) to respond with an **ICMP Echo Reply** packet back to the source host.
3.  `ping` measures the time elapsed between sending the request and receiving the reply (the round-trip time, RTT, or latency), usually displayed in milliseconds (ms).
4.  It typically sends multiple Echo Requests (e.g., one per second by default on Linux) and displays the results for each, along with summary statistics (min/avg/max RTT, packet loss percentage) when terminated (usually via `Ctrl+C`).

## Common Usage

```bash
# Ping a host by hostname (DNS lookup happens first)
ping www.google.com

# Ping a host by IP address
ping 8.8.8.8

# Send only a specific number of pings (e.g., 5)
ping -c 5 www.google.com  # Linux/macOS
ping -n 5 www.google.com  # Windows

# Specify interval between pings (e.g., 0.5 seconds)
ping -i 0.5 www.google.com # Linux/macOS

# Specify packet size (e.g., 100 bytes payload)
ping -s 100 www.google.com # Linux/macOS
ping -l 100 www.google.com # Windows
```

## Interpreting Output

- **Successful Reply:** Lines like `64 bytes from ...: icmp_seq=1 ttl=... time=10.5 ms` indicate a successful reply was received.
    - `icmp_seq`: Sequence number of the packet.
    - `ttl`: Time To Live (indicates hops remaining, can hint at distance).
    - `time`: Round-trip time (latency). Lower is better.
- **Request Timed Out:** Indicates no Echo Reply was received within the timeout period. Could mean the host is down, network congestion, or (very commonly) a firewall is blocking ICMP requests or replies.
- **Destination Host Unreachable:** Indicates a router along the path could not find a route to the destination network or host.
- **Packet Loss:** The summary shows the percentage of packets for which no reply was received. High packet loss indicates network problems.
- **Latency (RTT):** The summary shows min/avg/max round-trip times. High or variable latency indicates network delays or congestion.

## Use Cases

- Checking basic network connectivity to a remote host.
- Verifying if a host is online ("up").
- Measuring network latency (ping time).
- Diagnosing packet loss issues.
- Basic [[DNS]] troubleshooting (if pinging by hostname works but accessing fails, DNS is likely okay).

## Related Concepts
- [[ICMP]] (The protocol used by ping - Echo Request/Reply)
- [[ip]], [[Network_Layer]]
- [[Latency]], [[Packet_Loss]] (Metrics measured/indicated by ping)
- [[Troubleshooting_Network]]
- [[Firewall]] (Often block ping requests/replies)
- [[DNS]] (Used to resolve hostnames before pinging)

---
**Source:** Worksheet WS26, `ping` man page