---
tags:
  - networking
  - concept
  - web
  - api
  - interface
aliases:
  - Web API
  - Web Service API
related:
  - "[[API_C]]" # General API concept
  - "[[HTTP]]"
  - "[[RESTful_API]]"
  - "[[SOAP]]" # Placeholder
  - "[[GraphQL]]" # Placeholder
  - "[[JSON]]"
  - "[[XML]]"
  - "[[Client_Server_Model]]"
  - "[[Microservices]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# Web API

## Definition

A **Web API (Application Programming Interface)** is an [[API_C|API]] specifically designed to be accessed over a network, typically using the [[HTTP]] protocol. It defines a set of rules, protocols, and tools for building software applications, allowing different software systems (often running on different machines or platforms) to communicate and exchange data or functionality with each other over the web.

## Key Aspects / Characteristics

- **Network Accessible:** Designed to be called across network boundaries.
- **HTTP-Based (Usually):** The vast majority of modern web APIs use [[HTTP]] (or [[HTTPS]]) as the communication protocol.
- **Interface Definition:** Specifies endpoints ([[URL|URLs]]), allowed [[HTTP_Methods]], request/response formats ([[JSON]], [[XML]]), [[HTTP_Status_Codes]], authentication methods, etc.
- **Client-Server:** Follows the [[Client_Server_Model]], where a client application makes requests to an API endpoint hosted by a server.
- **Data Exchange:** Used primarily for exchanging data between systems (e.g., a mobile app getting data from a backend server).
- **Functionality Exposure:** Can also expose specific functionalities or services (e.g., triggering a payment process, sending a notification).
- **Styles/Architectures:** Various architectural styles exist for designing web APIs:
    - **[[RESTful_API|REST (Representational State Transfer)]]:** Currently the most popular style, emphasizing statelessness, resource identification via URLs, and standard HTTP methods.
    - **[[SOAP|SOAP (Simple Object Access Protocol)]]:** An older, more rigid protocol standard often using XML over HTTP, defining its own envelope and processing rules.
    - **[[GraphQL]]:** A query language for APIs, allowing clients to request exactly the data they need.
    - RPC (Remote Procedure Call) styles (like gRPC, XML-RPC, JSON-RPC).

## Purpose & Use Cases

- **Enable Communication:** Allow different software applications (web frontends, mobile apps, backend services, third-party systems) to interact.
- **Decoupling:** Decouple client applications from backend implementations. Clients only need to know the API contract.
- **[[Microservices]]:** APIs are the primary way microservices communicate with each other.
- **Third-Party Integration:** Allow external developers to integrate with a platform or service (e.g., Twitter API, Google Maps API).
- **Single Page Applications (SPAs):** SPAs heavily rely on web APIs to fetch data dynamically without full page reloads.

## Related Concepts
- [[API_C]] (General concept)
- [[HTTP]], [[HTTPS]] (Communication protocol)
- Architectural Styles: [[RESTful_API]], [[SOAP]], [[GraphQL]], RPC
- Data Formats: [[JSON]], [[XML]]
- [[Client_Server_Model]], [[Microservices]]
- [[URL]], [[HTTP_Methods]], [[HTTP_Status_Codes]] (API definition components)

## Questions / Further Study
>[!question] To implement a web API, what other options / alternatives to REST exist? (WS26)
> Besides [[RESTful_API|REST]], major alternatives include:
> - **[[SOAP]]:** A protocol standard using XML messages, often over HTTP. More rigid, defines envelope, encoding rules, and processing model. Was popular for enterprise services.
> - **[[GraphQL]]:** A query language for APIs. Allows clients to specify exactly the data structure they need, preventing over-fetching or under-fetching. Often uses HTTP POST.
> - **gRPC:** A high-performance RPC (Remote Procedure Call) framework developed by Google. Uses Protocol Buffers for serialization and typically HTTP/2 for transport. Efficient, good for internal microservice communication.
> - **XML-RPC / JSON-RPC:** Simpler RPC protocols using XML or JSON over HTTP POST.

---
**Source:** Worksheet WS26