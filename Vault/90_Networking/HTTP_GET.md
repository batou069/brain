---
tags:
  - networking
  - protocol
  - http
  - http_method
aliases:
  - GET Method
related:
  - "[[HTTP_Methods]]"
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[HTTP_Query_String]]"
  - "[[Safety_(HTTP)]]"
  - "[[Idempotence]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP GET Method

## Definition

The **GET** method is one of the primary [[HTTP_Methods|HTTP methods]]. It requests a representation of the specified resource. Requests using GET should only retrieve data and should not have other effects (they should be **[[Safety_(HTTP)|safe]]**).

## Characteristics

- **Retrieve Data:** Used to fetch data or resources (HTML pages, images, JSON data, etc.).
- **Safe:** Should not cause any side effects or changes on the server (e.g., modifying data, making a purchase).
- **[[Idempotence|Idempotent]]:** Making the same GET request multiple times should yield the same result (assuming the resource itself hasn't changed).
- **No Request Body:** GET requests should not have a message body. Data/parameters are typically sent via the [[HTTP_Query_String]] in the URL.
- **Cacheable:** Responses to GET requests can often be cached by browsers and intermediaries.
- **Bookmarkable/Linkable:** URLs corresponding to GET requests can usually be bookmarked, shared, and reloaded easily.

## Example Request

```http
GET /users/123?fields=name,email HTTP/1.1
Host: api.example.com
Accept: application/json
```

## Related Concepts
- [[HTTP_Methods]]
- [[Safety_(HTTP)]]
- [[Idempotence]]
- [[HTTP_Query_String]]

---
**Source:** Worksheet WS26, RFC 9110