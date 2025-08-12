---
tags:
  - networking
  - concept
  - web
  - api
  - architecture
  - style
aliases:
  - REST API
  - Representational State Transfer
  - REST
related:
  - "[[Web_API]]"
  - "[[HTTP]]"
  - "[[HTTP_Methods]]"
  - "[[HTTP_Status_Codes]]"
  - "[[URL]]"
  - "[[REST_Resource]]"
  - "[[JSON]]"
  - "[[XML]]"
  - "[[Stateless_Protocol]]"
  - "[[Client_Server_Model]]"
  - "[[Idempotence]]"
  - "[[CRUD]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# RESTful API (Representational State Transfer)

## Definition

**Representational State Transfer (REST)** is an **architectural style** for designing networked applications, particularly [[Web_API|web APIs]]. It relies on a **[[Stateless_Protocol|stateless]]**, [[Client_Server_Model|client-server]], cacheable communications protocol – typically [[HTTP]]. An API that adheres to the principles of REST is often referred to as a **RESTful API**. REST is not a standard or protocol itself, but rather a set of architectural constraints.

## Key Constraints/Principles of REST

1.  **Client-Server:** Clear separation between the client (request initiator) and the server (resource provider).
2.  **Stateless:** Each request from a client to the server must contain all the information needed to understand and complete the request. The server does not store any client context (session state) between requests. State management (like login status) is the client's responsibility (often using tokens/cookies sent with each request).
3.  **Cacheable:** Responses must implicitly or explicitly define themselves as cacheable or non-cacheable to prevent clients from reusing stale data and improve performance/scalability.
4.  **Uniform Interface:** This is a core constraint simplifying and decoupling the architecture. It consists of:
    -   *Identification of [[REST_Resource|Resources]]:* Resources (e.g., a user, an order, a product) are identified using stable identifiers, typically [[URL|URLs]] (e.g., `/users/123`, `/orders`).
    -   *Manipulation of Resources Through Representations:* Clients interact with resources via their representations (e.g., [[JSON]] or [[XML]] documents). The representation sent/received captures the current or intended state of the resource.
    -   *Self-descriptive Messages:* Each message (request/response) includes enough information to describe how to process it (e.g., [[HTTP_Methods|HTTP method]], [[HTTP_Headers|headers]] like `Content-Type` specifying the [[MIME_type]] of the representation).
    -   *Hypermedia as the Engine of Application State (HATEOAS):* (Often considered the most mature level of REST). Responses should include links ([[URL|URLs]]) to related resources or possible next actions, allowing clients to dynamically discover and navigate the API.
5.  **Layered System:** Clients generally cannot tell whether they are connected directly to the end server or to an intermediary (like a load balancer, cache, or proxy). Intermediaries can improve scalability, security, etc.
6.  **Code on Demand (Optional):** Servers can temporarily extend or customize client functionality by transferring executable code (e.g., JavaScript).

## REST and HTTP

REST is most commonly implemented using HTTP. The uniform interface constraints map well to HTTP features:
- **Resources:** Identified by [[URL|URLs]].
- **Actions:** Performed using standard [[HTTP_Methods]]:
    - `GET`: Retrieve a resource representation.
    - `POST`: Create a new resource (often within a collection) or trigger an action.
    - `PUT`: Replace/update an existing resource (or create at a known URL).
    - `DELETE`: Remove a resource.
    - `PATCH`: Partially update a resource.
- **Representations:** Exchanged in the message body, with format specified by `Content-Type` header (e.g., `application/json`).
- **Status:** Communicated using [[HTTP_Status_Codes]].

## Related Concepts
- [[Web_API]] (REST is a style for web APIs)
- [[HTTP]], [[HTTP_Methods]], [[HTTP_Status_Codes]], [[URL]], [[HTTP_Headers]], [[MIME_type]] (Technologies used)
- [[REST_Resource]] (The core abstraction)
- [[JSON]], [[XML]] (Common representation formats)
- [[Stateless_Protocol]], [[Client_Server_Model]], [[Cacheable]], [[Layered_System]], HATEOAS (Architectural constraints)
- [[Idempotence]] (Property of PUT, DELETE, GET)
- [[CRUD]] (Create, Read, Update, Delete operations often map to POST, GET, PUT/PATCH, DELETE)

## Questions / Further Study
>[!question] Describe REST in relation to HTTP methods and URIs. (WS26)
> REST uses [[URL|URIs (Uniform Resource Identifiers, typically URLs)]] to identify **[[REST_Resource|resources]]** (e.g., `/users/123` identifies user 123). It uses standard **[[HTTP_Methods]]** to define the **action** to be performed on that resource:
> - `GET /users/123`: Retrieve user 123.
> - `PUT /users/123`: Replace/update user 123 with data in the request body.
> - `DELETE /users/123`: Delete user 123.
> - `POST /users`: Create a new user (data in body), server determines the new URI (e.g., `/users/456`).
> - `GET /users`: Retrieve a list of users.
> This mapping of verbs (HTTP methods) to nouns (resources identified by URIs) is central to RESTful design over HTTP.

>[!question] How are parameters and data payload passed using REST? (WS26)
> - **Parameters in URI:**
>     - *Path Parameters:* Identify specific resources (e.g., `/users/{userId}`). The `userId` is part of the path.
>     - *[[HTTP_Query_String|Query Parameters]]:* Used primarily with `GET` requests for filtering, sorting, pagination (e.g., `/users?role=admin&sort=name`).
> - **Data Payload in Request Body:**
>     - Used primarily with `POST`, `PUT`, `PATCH` methods to send the representation of the resource (or partial updates).
>     - The format is specified by the `Content-Type` header (commonly `application/json`).

>[!question] Describe how a new user would be added to a remote server system over REST. (WS26)
> A common RESTful approach:
> 1.  **Client Action:** User fills out a registration form.
> 2.  **HTTP Request:** The client application sends an **[[HTTP_POST|POST]]** request to a collection URI, typically representing the type of resource being created (e.g., `/api/users`).
> 3.  **Request Body:** The body of the POST request contains the data for the new user, usually formatted as [[JSON]] (or form data). Example: `{"username": "newuser", "email": "new@example.com", "password": "..."}`. The `Content-Type` header would be set accordingly (e.g., `application/json`).
> 4.  **Server Action:** The server receives the POST request, validates the data, creates a new user record in its database (assigning a unique ID, e.g., 456), and potentially performs other actions (like hashing the password).
> 5.  **HTTP Response:** The server sends back an HTTP response:
>     - **Status Code:** Typically `201 Created` to indicate success and resource creation.
>     - **`Location` Header:** Contains the URL of the newly created user resource (e.g., `Location: /api/users/456`).
>     - **Response Body (Optional):** Might contain a representation of the newly created user resource.

>[!question] What are generally considered the best practices and guidelines for designing a good REST API? (WS26)
> Some common best practices include:
> - **Use Nouns for URIs:** URIs should identify resources (nouns), not actions (verbs). E.g., `/users`, `/users/123`, `/orders`.
> - **Use HTTP Methods for Actions:** Use `GET` (retrieve), `POST` (create/action), `PUT` (replace/create at known URI), `DELETE` (remove), `PATCH` (partial update) appropriately.
> - **Use Plural Nouns for Collections:** `/users` instead of `/user`.
> - **Use HTTP Status Codes Correctly:** Return appropriate codes (2xx for success, 4xx for client errors, 5xx for server errors). E.g., `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`.
> - **Provide Meaningful Error Responses:** Include informative JSON/XML bodies with error details for 4xx/5xx responses.
> - **Support Filtering, Sorting, Pagination:** Use query parameters for GET requests on collections (e.g., `/users?sort=-name&limit=20&offset=40`).
> - **Versioning:** Plan for API evolution (e.g., `/api/v1/users`, `/api/v2/users`, or via `Accept` headers).
> - **Use JSON:** Prefer JSON as the primary data format for request/response bodies.
> - **Statelessness:** Ensure server does not store client session state between requests.
> - **Security:** Use HTTPS, implement proper authentication/authorization.
> - **HATEOAS (Hypermedia):** Include links in responses to guide clients to related resources or possible next actions (more advanced REST maturity).
> - **Documentation:** Provide clear, comprehensive API documentation (e.g., using OpenAPI/Swagger).

---
**Source:** Worksheet WS26, Roy Fielding's Dissertation, General REST best practices