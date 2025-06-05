---
tags:
  - networking
  - protocol
  - http
  - http_method
  - rest
aliases:
  - PUT Method
related:
  - "[[HTTP_Methods]]"
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[Idempotence]]"
  - "[[RESTful_API]]"
  - "[[HTTP_POST]]" # Contrast
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP PUT Method

## Definition

The **PUT** method is one of the primary [[HTTP_Methods|HTTP methods]]. It requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the [[HTTP_Request|request message body]].

## Characteristics

- **Replace or Create:** Used to either:
    - **Replace** the entire current representation of the resource at the target [[URL]] with the request payload.
    - **Create** a new resource at the target URL if it does not already exist.
- **Requires Full Representation:** The request body should contain the complete representation of the resource being created or replaced, not just partial changes (for partial changes, [[HTTP_PATCH]] is often preferred).
- **[[Idempotence|Idempotent]]:** PUT requests are idempotent. Sending the same PUT request multiple times with the same payload should have the same effect on the server state as sending it once. The resource will end up in the same final state.
- **URL Identifies Resource:** The URL in the request line typically points directly to the specific resource being created or replaced (e.g., `/users/123`). This contrasts with [[HTTP_POST]] where the URL might be a collection or factory endpoint (e.g., `/users`).
- **Has Request Body:** The new representation of the resource is sent in the message body.

## Example Request

```http
PUT /api/users/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 35

{"name": "Alice Smith", "age": 31}
```
*(This request intends to replace the entire user resource at `/api/users/123` with the provided JSON data, or create it if it doesn't exist).*

## Related Concepts
- [[HTTP_Methods]]
- [[Idempotence]] (PUT is idempotent)
- [[HTTP_Request]] (Body contains full resource representation)
- [[HTTP_POST]] (Contrast: POST is often for creating resources where server assigns URL, and is not idempotent)
- [[HTTP_PATCH]] (Contrast: PATCH is for partial updates)
- [[RESTful_API]] (PUT is commonly used for updates in REST)

---
**Source:** Worksheet WS26, RFC 9110