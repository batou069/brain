---
tags:
  - networking
  - protocol
  - http
  - http_method
  - rest
aliases:
  - DELETE Method
related:
  - "[[HTTP_Methods]]"
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[Idempotence]]"
  - "[[RESTful_API]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP DELETE Method

## Definition

The **DELETE** method is one of the primary [[HTTP_Methods|HTTP methods]]. It requests that the server **delete** the resource identified by the request [[URL]].

## Characteristics

- **Delete Resource:** Used to remove a specific resource from the server.
- **[[Idempotence|Idempotent]]:** DELETE requests are idempotent. Deleting a resource multiple times should result in the same final state (the resource is gone). The [[HTTP_Status_Codes|status code]] might differ between the first successful deletion (e.g., `200 OK` or `204 No Content`) and subsequent attempts (e.g., `404 Not Found`), but the server state regarding that resource remains "deleted".
- **No Request Body (Typically):** DELETE requests usually do not have a message body, as the resource to be deleted is identified by the URL.
- **[[Safety_(HTTP)|Not Safe]]:** DELETE operations clearly change the server state.

## Example Request

```http
DELETE /api/users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
```
*(This request asks the server to delete the user resource located at `/api/users/123`)*

## Related Concepts
- [[HTTP_Methods]]
- [[Idempotence]] (DELETE is idempotent)
- [[Safety_(HTTP)]] (DELETE is not safe)
- [[HTTP_Request]] (Usually no body)
- [[RESTful_API]] (DELETE is commonly used for removing resources in REST)
- [[HTTP_Status_Codes]] (Common responses: 200, 204, 404)

---
**Source:** Worksheet WS26, RFC 9110