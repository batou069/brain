---
tags:
  - networking
  - concept
  - protocol
  - application_layer
  - security
  - encryption
  - remote_access
aliases:
  - Secure Shell
  - Secure Socket Shell
related:
  - "[[Networking_Protocols]]"
  - "[[Application_Layer]]"
  - "[[TCP]]"
  - "[[Port_(Networking)]]" # Port 22
  - "[[Encryption]]"
  - "[[Authentication]]" # Placeholder
  - "[[Public_Key_Cryptography]]" # Placeholder
  - "[[Telnet]]" # Insecure predecessor
  - "[[scp]]" # Secure copy, often uses SSH
  - "[[sftp]]" # Secure FTP, often uses SSH
  - "[[Client_Server_Model]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# SSH (Secure Shell)

## Definition

**SSH (Secure Shell)** is a cryptographic network protocol used for operating network services securely over an unsecured network. Its most notable applications are **remote login** (providing a secure command-line interface to a remote machine) and **secure file transfer**. SSH provides confidentiality and integrity of data using strong [[Encryption]], as well as server and client [[Authentication]].

## Key Features

- **Secure Remote Access:** Allows users to log into and execute commands on a remote computer securely, replacing insecure protocols like [[Telnet]].
- **[[Encryption]]:** Encrypts the entire session, including passwords, commands, and output, preventing eavesdropping. Uses symmetric encryption for bulk data transfer and asymmetric (public-key) cryptography for key exchange and authentication.
- **[[Authentication]]:** Provides mechanisms for authenticating both the server (to prevent man-in-the-middle attacks, usually via host keys) and the user (typically via passwords or, more securely, public-key authentication using SSH keys).
- **Data Integrity:** Ensures that data transmitted cannot be tampered with undetected using cryptographic message authentication codes (MACs).
- **Tunneling / Port Forwarding:** Can securely tunnel other network protocols (e.g., forwarding X11 graphical sessions, forwarding arbitrary TCP ports).
- **Secure File Transfer:** The SSH protocol itself underlies secure file transfer protocols like [[scp]] and [[sftp]].
- **[[Client_Server_Model|Client-Server Architecture]]:** An SSH client application connects to an SSH server application running on the remote host.
- **[[TCP]]-Based:** Runs over [[TCP]], typically using [[Port_(Networking)|port 22]].

## Common Use Cases

- Logging into remote Linux/Unix servers, routers, or other devices to manage them via the command line.
- Securely transferring files using `scp` or `sftp`.
- Tunneling other network traffic securely.
- Securely managing [[Git]] repositories (using SSH URLs for `clone`, `push`, `pull`).

## Authentication Methods

- **Password Authentication:** User provides username and password (encrypted during transit). Simple but vulnerable to brute-force attacks if passwords are weak.
- **Public Key Authentication:** More secure. User generates a public/private key pair. The public key is placed on the server (e.g., in `~/.ssh/authorized_keys`). The client proves possession of the corresponding private key during login without sending the private key itself. Often protected by a passphrase on the private key.
- **Host-Based Authentication:** Based on trusting specific client host keys.
- **Keyboard-Interactive:** Generic challenge-response mechanism, can be used for multi-factor authentication.

## Related Concepts
- [[Networking_Protocols]], [[Application_Layer]]
- [[Security]], [[Encryption]], [[Authentication]], [[Public_Key_Cryptography]]
- [[TCP]], [[Port_(Networking)]] (Port 22)
- [[Telnet]] (Insecure predecessor for remote login)
- [[scp]], [[sftp]] (File transfer protocols using SSH)
- [[Client_Server_Model]]
- SSH Keys, Host Keys

---
**Source:** Worksheet WS26