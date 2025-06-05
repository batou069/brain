---
tags:
  - networking
  - concept
  - protocol
  - application_layer
  - web
aliases:
  - Hypertext Transfer Protocol
related:
  - "[[Networking_Protocols]]"
  - "[[Application_Layer]]"
  - "[[TCP_IP_Model]]"
  - "[[OSI_Model]]"
  - "[[World_Wide_Web]]"
  - "[[HTTPS]]"
  - "[[URL]]"
  - "[[Client_Server_Model]]"
  - "[[Request_Response_Model]]"
  - "[[HTTP_Request]]"
  - "[[HTTP_Response]]"
  - "[[HTTP_Methods]]"
  - "[[HTTP_Status_Codes]]"
  - "[[HTTP_Headers]]"
  - "[[TCP]]"
  - "[[Stateless_Protocol]]"
  - "[[Session]]"
  - "[[Cookies]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP (Hypertext Transfer Protocol)

## Definition

**HTTP (Hypertext Transfer Protocol)** is an [[Application_Layer|application-layer]] [[Networking_Protocols|protocol]] that forms the foundation of data communication for the [[World_Wide_Web]]. It defines how messages are formatted and transmitted, and what actions Web servers ([[Web_Server]]) and browsers ([[Web_Browser]]) should take in response to various commands. HTTP follows a [[Client_Server_Model|client-server]], [[Request_Response_Model|request-response]] paradigm.

## Key Aspects / Characteristics

- **Application Layer:** Operates at Layer 7 of the [[OSI_Model]] / Application Layer of [[TCP_IP_Model]].
- **Client-Server:** The client (e.g., web browser) sends an [[HTTP_Request]] message to a server. The server (e.g., web server hosting a website) processes the request and sends back an [[HTTP_Response]] message.
- **Request-Response:** Communication is driven by client requests followed by server responses.
- **Resource-Based:** Used primarily to request and transfer resources identified by [[URL|URLs]] (e.g., [[HTML]] documents, images, CSS files, JavaScript, data).
- **[[Stateless_Protocol|Stateless]]:** By default, HTTP is stateless. This means the server does not retain any information (state) about previous requests from the same client. Each request is treated independently. State management, if needed, must be handled using other mechanisms like [[Cookies]] or server-side [[Session|sessions]].
- **[[TCP]]-Based:** HTTP typically relies on [[TCP]] as its underlying [[Transport_Layer|transport layer]] protocol (usually on [[Port_(Networking)|port 80]]) to provide a reliable, connection-oriented data stream. [[UDP]] is generally not used for standard HTTP.
- **Message Structure:** Defines specific formats for [[HTTP_Request]] and [[HTTP_Response]] messages, including:
    - Start-line (Request line or Status line)
    - [[HTTP_Headers|Headers]] (Key-value pairs providing metadata)
    - An optional Message Body (containing data like submitted form data or the requested resource).
- **[[HTTP_Methods]]:** Defines standard request methods (verbs) indicating the desired action to be performed on the resource (e.g., [[HTTP_GET|GET]], [[HTTP_POST|POST]], [[HTTP_PUT|PUT]], [[HTTP_DELETE|DELETE]]).
- **[[HTTP_Status_Codes]]:** Standard codes returned in the response indicating the outcome of the request (e.g., `200 OK`, `404 Not Found`, `500 Internal Server Error`).
- **Extensible:** Can be extended with new methods, headers, and status codes.

## General Usage (WS26 Question 5)

HTTP is the primary protocol used for browsing the web. When you enter a URL in your browser:
1. The browser acts as an HTTP client.
2. It performs a [[DNS]] lookup to get the server's IP address.
3. It establishes a [[TCP]] connection to the server on port 80 (or 443 for [[HTTPS]]).
4. It sends an [[HTTP_Request]] (e.g., a `GET` request for the specified path) to the server.
5. The web server processes the request (e.g., retrieves the HTML file).
6. The server sends an [[HTTP_Response]] back to the browser, including status code, headers, and the requested resource (HTML) in the body.
7. The browser receives the response, parses the HTML, and may issue further HTTP requests for embedded resources (images, CSS, scripts).
8. The browser renders the page.
9. The TCP connection might be closed or kept alive for further requests (HTTP Keep-Alive).

## Versions (WS26 Question 2)

- **HTTP/0.9 (1991):** Very simple, one-line request (GET method only), response was just the HTML document. No headers, no status codes.
- **HTTP/1.0 (1996):** Introduced versioning, status codes, headers (like `Content-Type`), and more methods (POST, HEAD). Typically opened a new TCP connection for each request/response cycle (inefficient).
- **HTTP/1.1 (1997/1999):** Major improvements. Introduced persistent connections (Keep-Alive) allowing multiple requests/responses over a single TCP connection, pipelining (sending multiple requests before waiting for responses - though often problematic), chunked transfer encoding, host header (allowing multiple websites on one IP), caching mechanisms, more methods (PUT, DELETE, OPTIONS, TRACE, CONNECT). Still the most widely deployed version foundationally.
- **HTTP/2 (2015):** Major performance focus. Introduced binary framing (instead of plaintext), multiplexing (allowing multiple requests/responses concurrently over a single TCP connection without head-of-line blocking), header compression (HPACK), and server push. Aims to reduce latency. Requires TLS (effectively [[HTTPS]]) in most browser implementations.
- **HTTP/3 (Ongoing):** Uses QUIC (Quick UDP Internet Connections) as the transport layer protocol instead of TCP. Aims to further reduce latency, improve congestion control, and mitigate head-of-line blocking issues inherent even in HTTP/2's multiplexing over TCP. Built-in encryption (TLS 1.3).

## Related Concepts
- [[World_Wide_Web]], [[URL]]
- [[Client_Server_Model]], [[Request_Response_Model]]
- [[TCP]] (Underlying transport)
- [[HTTPS]] (Secure version using TLS/SSL)
- [[HTTP_Request]], [[HTTP_Response]], [[HTTP_Methods]], [[HTTP_Status_Codes]], [[HTTP_Headers]]
- [[Stateless_Protocol]], [[Session]], [[Cookies]] (State management)
- [[Web_Server]], [[Web_Browser]]

## Questions / Further Study
>[!question] Is HTTP TCP-based or UDP-based? (WS26)
> Standard HTTP (including versions 1.0, 1.1, and 2) is **[[TCP]]-based**. It relies on TCP for reliable, ordered delivery. HTTP/3 is the exception, using QUIC which runs over [[UDP]].

---
**Source:** Worksheet WS26, RFCs (e.g., 1945, 2616, 7540, 9110-9114), Research Links