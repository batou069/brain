---
tags:
  - networking
  - tool
  - command
  - troubleshooting
  - protocol
  - application_layer
  - legacy
  - insecure
aliases:
  - telnet command
  - Teletype Network
related:
  - "[[TCP]]"
  - "[[Port_(Networking)]]"
  - "[[Client_Server_Model]]"
  - "[[SSH]]" # Secure replacement
  - "[[Troubleshooting_Network]]"
  - "[[netcat]]" # More versatile tool
worksheet: [WS26]
date_created: 2025-04-21
---
# ` telnet `

## Definition

**Telnet** is an early [[Application_Layer|application-layer]] network protocol and command-line utility based on the [[Client_Server_Model|client-server model]]. It provides a bidirectional, interactive, text-oriented communication facility using a virtual terminal connection over [[TCP]]. Historically, its primary use was for **remote login** to command-line interfaces on servers.

## Status

**Largely Obsolete and Insecure:** Telnet transmits **all data, including usernames and passwords, in plain text**, making it extremely vulnerable to eavesdropping. For remote login, it has been almost entirely replaced by the secure [[SSH]] protocol.

## Modern Uses (Limited & Cautious)

Despite its insecurity for remote login, the `telnet` *client* utility is sometimes still used by network administrators and developers for simple, manual **TCP port checking and troubleshooting**:

- **Checking Port Connectivity:** You can use `telnet <hostname_or_ip> <port_number>` to see if a TCP connection can be established to a specific port on a remote host.
    - If it connects (e.g., shows "Connected to..." or presents a blank screen), the port is open and listening for TCP connections.
    - If it fails immediately ("Connection refused"), the port is likely closed or no service is listening.
    - If it times out ("Unable to connect..."), a firewall might be blocking the connection, or the host might be unreachable.
- **Basic Protocol Interaction:** For some simple text-based protocols (like older SMTP or POP3, or sometimes HTTP for basic requests), you can manually type protocol commands after establishing a connection with `telnet` to observe the server's raw responses. This is useful for low-level debugging but requires knowing the protocol syntax.

## Syntax (Client Utility)

```bash
# Attempt to connect to a specific host and port
telnet <hostname_or_ip> <port_number>

# Example: Check if a web server is listening on port 80
telnet www.example.com 80
# (If successful, you might see 'Connected to...' then type 'GET / HTTP/1.0' and press Enter twice)

# Example: Check if an SMTP server is listening on port 25
telnet mail.example.com 25

# Exit telnet session (often Ctrl + ], then type 'quit')
```

## Security Warning

**Never use Telnet for logging into remote systems or transmitting sensitive data over untrusted networks.** Use [[SSH]] instead. The `telnet` client utility itself is generally safe for basic port checking, but the Telnet *protocol* for login is insecure.

## Related Concepts
- [[TCP]], [[Port_(Networking)]] (Telnet uses TCP and connects to specific ports)
- [[Client_Server_Model]]
- [[SSH]] (Secure replacement for Telnet login)
- [[Troubleshooting_Network]] (Limited use for port checking)
- [[netcat]] (`nc`) (A more modern and versatile command-line tool often preferred over telnet for network debugging and port checking)

---
**Source:** Worksheet WS26, `telnet` man page