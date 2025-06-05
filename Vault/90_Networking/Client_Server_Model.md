---
tags:
  - networking
  - concept
  - architecture
  - model
aliases:
  - Client-Server Architecture
related:
  - "[[Sockets]]"
  - "[[TCP]]"
  - "[[UDP]]"
  - "[[HTTP]]"
  - "[[DNS]]"
  - "[[Request_Response_Model]]"
  - "[[Peer_to_Peer_Model]]" # Contrast
worksheet: [WS26]
date_created: 2025-04-21
---
# Client-Server Model

## Definition

The **Client-Server Model** is a distributed application structure that partitions tasks or workloads between **servers** (providers of a resource or service) and **clients** (requesters of that service). Servers are typically powerful machines that host resources or services and wait for requests, while clients are usually user workstations or applications that initiate contact with servers to request services or data.

## Key Components & Interaction

1.  **Server:**
    -   A process or host that provides a specific service (e.g., web server, database server, file server, DNS server).
    -   Typically runs continuously, listening for incoming requests on a specific [[Port_(Networking)|port]].
    -   Manages resources and performs the requested service.
    -   Responds to client requests.
    -   Often handles multiple client requests concurrently.

2.  **Client:**
    -   A process or host that initiates communication with a server to request a service.
    -   Knows the address ([[ip]]) and port of the server it wants to contact.
    -   Sends a request message to the server.
    -   Waits for and processes the server's response.
    -   Typically interacts directly with the end-user (e.g., web browser, email client).

3.  **Network:**
    -   The underlying infrastructure ([[ip|IP network]], [[TCP]], [[UDP]], etc.) that allows clients and servers to communicate.

**Interaction Flow (Typical [[Request_Response_Model]]):**
1.  Server starts, binds to a port, and listens for connections ([[bind_function]], [[listen_function]]).
2.  Client initiates a connection to the server's IP and port ([[connect_function]]).
3.  Server accepts the connection ([[accept_function]]).
4.  Client sends a request message ([[send_function]]).
5.  Server processes the request.
6.  Server sends a response message back to the client ([[send_function]]).
7.  Client receives and processes the response ([[recv_function]]).
8.  Connection may be closed by either side.

## Characteristics

- **Centralized Resource:** Resources and services are managed centrally by the server(s).
- **Clear Roles:** Distinct roles for client (requester) and server (provider).
- **Request-Response:** Communication typically follows a request-response pattern.
- **Scalability:** Servers can often be scaled (vertically or horizontally) to handle more clients.
- **State:** Servers may be stateful (remembering client interactions across multiple requests) or stateless (treating each request independently).

## Examples

- **Web:** Web Browser (client) requests pages from a Web Server ([[HTTP]]).
- **Email:** Email Client (client) sends/receives mail via Mail Servers (SMTP, POP3/IMAP).
- **Database:** Application (client) queries a Database Server (SQL).
- **[[DNS]]:** DNS Resolver (client) queries a DNS Server.
- **File Sharing:** Client accesses files stored on a File Server (NFS, SMB).

## Contrast with Peer-to-Peer

- In a [[Peer_to_Peer_Model|Peer-to-Peer (P2P)]] model, participants (peers) act as both clients *and* servers, sharing resources directly with each other without necessarily relying on a central server.

## Related Concepts
- [[Sockets]], [[ip]], [[Port_(Networking)]] (Underlying mechanisms)
- [[TCP]], [[UDP]] (Transport protocols used)
- [[HTTP]], [[DNS]], [[FTP]], [[SMTP]] (Application protocols often using C-S model)
- [[Request_Response_Model]] (Common interaction pattern)
- [[Peer_to_Peer_Model]] (Alternative architecture)
- Server, Client, Network

---
**Source:** Worksheet WS26