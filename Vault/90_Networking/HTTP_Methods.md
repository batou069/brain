---
tags:
  - networking
  - concept
  - protocol
  - http
  - web
  - rest
aliases:
  - HTTP Verbs
  - HTTP Request Methods
related:
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[RESTful_API]]"
  - "[[Idempotence]]" # Placeholder
  - "[[Safety_(HTTP)]]" # Placeholder
  - "[[HTTP_GET]]"
  - "[[HTTP_POST]]"
  - "[[HTTP_PUT]]"
  - "[[HTTP_DELETE]]"
  - "[[HTTP_HEAD]]" # Placeholder
  - "[[HTTP_OPTIONS]]" # Placeholder
  - "[[HTTP_PATCH]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP Methods

## Definition

**HTTP Methods** (sometimes called HTTP Verbs) are specified in the [[HTTP_Request|request line]] of an HTTP request and indicate the desired **action** to be performed on the resource identified by the requested [[URL]]. They define the semantics of the client's request.

## Key Properties

Some methods have specific properties:

- **[[Safety_(HTTP)|Safe]]:** Safe methods are intended only for information retrieval and should not change the state of the server. Clients (and intermediaries like caches) should feel safe retrying safe methods automatically. `GET`, `HEAD`, `OPTIONS`, `TRACE` are generally considered safe.
- **[[Idempotence|Idempotent]]:** An operation is idempotent if making the same request multiple times produces the same result (has the same effect on the server state) as making it once. `GET`, `HEAD`, `OPTIONS`, `TRACE`, `PUT`, `DELETE` are typically idempotent. `POST` is generally *not* idempotent.

## Common HTTP Methods (WS26 List)

1.  **[[HTTP_GET|GET]]:**
    -   **Purpose:** Requests a representation of the specified resource. Should only retrieve data (safe).
    -   **Body:** Should not have a request body.
    -   **Idempotent:** Yes.
    -   **Use Case:** Retrieving web pages, images, data via APIs. Parameters often sent via [[HTTP_Query_String]].

2.  **[[HTTP_POST|POST]]:**
    -   **Purpose:** Submits data to be processed to the identified resource, often causing a change in state or side effects on the server (e.g., creating a new resource, submitting a form).
    -   **Body:** Typically contains the data being submitted (e.g., form data, JSON).
    -   **Idempotent:** No (usually). Sending the same POST request twice might create two resources or perform an action twice.
    -   **Use Case:** Submitting web forms, creating new resources via APIs, uploading files.

3.  **[[HTTP_PUT|PUT]]:**
    -   **Purpose:** Replaces the current representation of the target resource with the request payload. If the resource doesn't exist, it might create it.
    -   **Body:** Contains the complete new representation of the resource.
    -   **Idempotent:** Yes. Sending the same PUT request multiple times with the same payload should result in the same final state on the server.
    -   **Use Case:** Updating an existing resource completely, or creating a resource at a specific known URL.

4.  **[[HTTP_DELETE|DELETE]]:**
    -   **Purpose:** Deletes the specified resource.
    -   **Body:** Typically does not have a request body.
    -   **Idempotent:** Yes. Deleting something multiple times results in the same state (it's gone). The status code might differ between the first (e.g., `200 OK` or `204 No Content`) and subsequent calls (e.g., `404 Not Found`).
    -   **Use Case:** Removing a resource (e.g., deleting a user account, a file).

## Other Common Methods

- **HEAD:** Identical to GET, but the server must **not** return a message body in the response. Used to retrieve only the headers for a resource (e.g., to check `Last-Modified` or `Content-Length` before downloading). Safe, Idempotent.
- **OPTIONS:** Requests information about the communication options available for the target resource (e.g., which HTTP methods are supported). Safe, Idempotent. Used in CORS (Cross-Origin Resource Sharing) preflight requests.
- **PATCH:** Applies partial modifications to a resource. Contrast with PUT which replaces the entire resource. Idempotency depends on the patch format/semantics.
- **CONNECT:** Establishes a tunnel to the server identified by the target resource (used for HTTPS proxies).
- **TRACE:** Performs a message loop-back test along the path to the target resource (useful for debugging, but often disabled for security). Safe, Idempotent.

## Related Concepts
- [[HTTP]], [[HTTP_Request]]
- [[RESTful_API]] (Methods map closely to CRUD operations in REST)
- [[Idempotence]], [[Safety_(HTTP)]] (Properties of methods)
- [[HTTP_Status_Codes]] (Responses depend on method and outcome)

## Questions / Further Study
>[!question] For each of the HTTP methods (GET, POST, DELETE, PUT), where can you send additional Parameters / data? (WS26)
> - **[[HTTP_GET|GET]]:** Primarily via the **[[HTTP_Query_String]]** part of the URL (e.g., `/search?q=term&page=2`). GET requests should *not* have a request body.
> - **[[HTTP_POST|POST]]:** Primarily via the **message body** of the request. The format is specified by the `Content-Type` header (e.g., `application/x-www-form-urlencoded`, `multipart/form-data`, `application/json`). Query string parameters can also be used but are less common for the main payload.
> - **[[HTTP_PUT|PUT]]:** Primarily via the **message body**, which should contain the complete new representation of the resource being updated or created. Query string parameters can also be used in the URL identifying the resource.
> - **[[HTTP_DELETE|DELETE]]:** Typically does **not** send data in the message body. Parameters identifying the resource are usually in the **URL path** (e.g., `/users/123`). Query string parameters can also be used. Sending a body with DELETE is possible but less common and semantics might vary.

>[!question] When should you use the PUT and POST methods? (WS26)
> The choice depends on idempotence and the desired semantics:
> - Use **[[HTTP_POST|POST]]** when:
>     - Creating a *new* resource where the client doesn't know the final URL yet (e.g., submitting a form to `/orders`, server creates `/orders/123`).
>     - The operation is **not idempotent** (e.g., sending an instruction to "add item to cart" - doing it twice adds two items).
>     - Performing actions that don't neatly map to a specific resource (e.g., triggering a calculation).
> - Use **[[HTTP_PUT|PUT]]** when:
>     - **Replacing** an existing resource *entirely* with the data provided in the request body, or **creating** a resource at a *specific, client-known URL*.
>     - The operation **is idempotent**. Sending the same PUT request multiple times should have the same effect as sending it once (the resource ends up in the same state).

---
**Source:** Worksheet WS26, RFC 9110