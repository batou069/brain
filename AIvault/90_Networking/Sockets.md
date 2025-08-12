---
tags:
  - networking
  - concept
  - api
  - programming
  - transport_layer
aliases:
  - Network Socket
  - Socket API
related:
  - "[[ip]]"
  - "[[Port_Number]]"
  - "[[TCP]]"
  - "[[UDP]]"
  - "[[Client_Server_Model]]"
  - "[[TCP_IP_Model]]"
  - "[[socket_function]]"
  - "[[bind_function]]"
  - "[[connect_function]]"
  - "[[listen_function]]"
  - "[[accept_function]]"
  - "[[send_function]]"
  - "[[recv_function]]"
worksheet: [WS26, WS28]
date_created: 2025-04-21
---
# Sockets (Network Programming)

## Definition

In network programming, a **Socket** is one endpoint of a two-way communication link between two programs running on a network. It represents the combination of an [[ip|IP address]] and a [[Port_Number|port number]], providing a mechanism for a process to send and receive data across the network. The **Socket API** (Application Programming Interface), originally popularized by Berkeley Sockets (BSD Sockets), provides a standard set of functions for creating and using sockets.

## Key Concepts

- **Endpoint:** Represents one end of a network communication channel.
- **IP Address + Port Number:** A complete socket address uniquely identifies a specific application process on a specific host machine within the network.
    - IP Address: Identifies the host machine.
    - Port Number: Identifies the specific application/service process on that host.
- **Communication Types:** Sockets support different communication protocols, primarily:
    - **[[TCP]] Sockets (Stream Sockets):** Provide reliable, connection-oriented, stream-based communication (`SOCK_STREAM`).
    - **[[UDP]] Sockets (Datagram Sockets):** Provide unreliable, connectionless, message-based communication (`SOCK_DGRAM`).
- **Socket API:** A set of functions used to create, configure, and use sockets for network communication. Common functions (from BSD Sockets API, used in C, Python, etc.):
    - `[[socket_function|socket()]]`: Creates a new socket endpoint.
    - `[[bind_function|bind()]]`: Assigns a local IP address and port number to a socket (typically used by servers).
    - `[[listen_function|listen()]]`: Puts a TCP socket into listening mode, waiting for incoming client connections (server-side).
    - `[[accept_function|accept()]]`: Accepts an incoming connection request on a listening TCP socket, creating a *new* socket dedicated to communication with that specific client (server-side).
    - `[[connect_function|connect()]]`: Establishes a connection to a remote socket (typically used by TCP clients).
    - `[[send_function|send()]]` / `write()`: Sends data over a connected TCP socket or to a specific destination for UDP.
    - `[[recv_function|recv()]]` / `read()`: Receives data from a connected TCP socket or from any source for UDP.
    - `sendto()`, `recvfrom()`: Used specifically with UDP sockets to specify destination/source addresses for each datagram.
    - `close()` / `shutdown()`: Closes the socket connection.
- **[[Client_Server_Model]]:** Sockets are fundamental to implementing client-server applications. Servers typically `bind`, `listen`, and `accept`, while clients `connect`.

## Analogy

Think of network communication like a telephone system:
- **IP Address:** The phone number of a specific building (host).
- **Port Number:** The specific extension number within that building (application process).
- **Socket:** The complete phone endpoint (building number + extension).
- **`socket()`:** Getting a phone line installed.
- **`bind()`:** Assigning your specific extension number to your phone line (server).
- **`listen()`:** Turning on the ringer for incoming calls (server).
- **`connect()`:** Dialing someone else's number + extension (client).
- **`accept()`:** Answering an incoming call (server).
- **`send()`/`recv()`:** Talking/listening on the established call.
- **`close()`:** Hanging up the phone.

## Related Concepts
- [[ip]], [[Port_Number]] (Components of a socket address)
- [[TCP]], [[UDP]] (Protocols used by sockets)
- [[Client_Server_Model]] (Common architecture using sockets)
- [[TCP_IP_Model]], [[Transport_Layer]]
- Socket API Functions: [[socket_function]], [[bind_function]], [[connect_function]], [[listen_function]], [[accept_function]], [[send_function]], [[recv_function]], `sendto`, `recvfrom`, `close`, `shutdown`

---
**Source:** Worksheet WS26, WS28