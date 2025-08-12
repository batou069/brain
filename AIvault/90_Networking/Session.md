---
tags:
  - networking
  - concept
  - web
  - state_management
aliases:
  - Network Session
  - Web Session
related:
  - "[[HTTP]]"
  - "[[Stateless_Protocol]]"
  - "[[Cookies]]"
  - "[[Session_ID]]" # Placeholder
  - "[[Session_Layer]]" # OSI Model Layer
  - "[[TCP]]" # Connection provides a session context
  - "[[Stateful_vs_Stateless]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# Session (Networking / Web Context)

## Definition

In networking and web development, a **Session** refers to a persistent logical connection or a sequence of related interactions between two communicating endpoints (typically a client and a server) over a period of time. While protocols like [[TCP]] provide a connection-level session, the term is often used at the application layer (especially in web development) to refer to a mechanism for maintaining **state** across multiple [[HTTP]] requests from the same client, overcoming HTTP's inherent [[Stateless_Protocol|statelessness]].

## Application Layer Sessions (Web Context)

Since [[HTTP]] is stateless (each request is independent), web applications need a way to track user activity and maintain user-specific data across multiple requests (e.g., login status, shopping cart contents). This is typically achieved using **web sessions**:

1.  **Session Initiation:** When a user first interacts (e.g., logs in), the server creates a unique **[[Session_ID|Session Identifier (Session ID)]]**.
2.  **Session ID Storage (Server-Side):** The server stores session-specific data (e.g., user ID, preferences, cart items) associated with that Session ID, typically in memory, a database, or a dedicated session store.
3.  **Session ID Transmission (Client-Side):** The server sends the Session ID back to the client's browser. The most common mechanism is via **[[Cookies|HTTP Cookies]]**. The browser automatically includes this cookie (containing the Session ID) in subsequent requests to the same server. Alternatives include URL rewriting (embedding the ID in URLs - less secure) or hidden form fields.
4.  **Session Identification:** On subsequent requests, the server extracts the Session ID from the cookie (or other mechanism), looks up the corresponding session data in its store, and can thus identify the user and retrieve their state.
5.  **Session Termination:** Sessions typically expire after a period of inactivity (timeout) or when the user explicitly logs out. The server then invalidates the Session ID and removes the associated data.

## Key Aspects

- **State Management:** Provides a way to maintain state for stateless protocols like HTTP.
- **Session ID:** A unique token used to link multiple requests from the same client.
- **Server-Side Storage:** Session data is primarily stored on the server.
- **Client-Side Identifier:** The client only needs to store and send the Session ID (usually via cookies).
- **Security Considerations:** Session IDs must be unpredictable and transmitted securely ([[HTTPS]]) to prevent session hijacking. Session fixation and cross-site request forgery (CSRF) are related vulnerabilities.

## OSI Model Context

- The [[Session_Layer|OSI Model's Session Layer (Layer 5)]] is theoretically responsible for establishing, managing, and terminating sessions, including dialogue control and synchronization. However, in the [[TCP_IP_Model]], these functions are often handled implicitly by the transport layer ([[TCP]]) or explicitly by the application layer (like the web session mechanism described above).

## Related Concepts
- [[HTTP]], [[Stateless_Protocol]]
- [[Stateful_vs_Stateless]]
- [[Cookies]], [[Session_ID]]
- [[Authentication]], [[Authorization]] (Sessions often store login status)
- [[Session_Layer]] (OSI Layer 5)
- [[TCP]] (Provides connection-level session)

## Questions / Further Study
>[!question] Why is HTTP considered stateless, and how is the state kept in an HTTP session? (WS26)
> - **Why Stateless:** [[HTTP]] is considered stateless because each request from a client to a server is treated as an independent transaction. The server does not inherently remember anything about previous requests from the same client. This simplifies server design (no need to store ongoing conversation state for every client) and improves scalability.
> - **How State is Kept:** State is maintained *despite* HTTP's statelessness using **application-level session management**. The server generates a unique [[Session_ID]] for a user, stores user-specific data associated with that ID on the server-side, and sends the Session ID to the client (usually via a [[Cookies|Cookie]]). The client sends the Session ID back with each subsequent request, allowing the server to retrieve the user's session data and maintain the illusion of a continuous stateful session.

---
**Source:** Worksheet WS26