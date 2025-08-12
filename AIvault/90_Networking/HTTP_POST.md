---
tags:
  - networking
  - protocol
  - http
  - http_method
aliases:
  - POST Method
related:
  - "[[HTTP_Methods]]"
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[HTTP_Response]]"
  - "[[Idempotence]]" # POST is not idempotent
  - "[[HTML_Form]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP POST Method

## Definition

The **POST** method is one of the primary [[HTTP_Methods|HTTP methods]]. It is used to submit an entity (data) to the specified resource, often causing a change in state or side effects on the server. The specific action performed by POST is determined by the resource's own semantics.

## Characteristics

- **Submit Data / Trigger Action:** Used for various actions like:
    - Submitting [[HTML_Form|web form]] data.
    - Creating a new resource (e.g., adding a new user, posting a blog comment). The server often determines the URL of the newly created resource.
    - Uploading files.
    - Triggering a process or calculation on the server.
- **Has Request Body:** The data being submitted is typically included in the message body of the [[HTTP_Request]]. The `Content-Type` header indicates the format of the body (e.g., `application/x-www-form-urlencoded`, `multipart/form-data`, `application/json`).
- **Not [[Safety_(HTTP)|Safe]]:** POST requests usually cause side effects (data creation/modification).
- **Not [[Idempotence|Idempotent]]:** Sending the same POST request multiple times may result in multiple resources being created or the action being performed multiple times.
- **Not Typically Cacheable:** Responses to POST are generally not cacheable unless specific cache headers indicate otherwise.

## Example Request

```http
POST /api/articles HTTP/1.1
Host: myblog.com
Content-Type: application/json
Content-Length: 55

{"title": "New Post", "content": "This is the content."}
```

## Related Concepts
- [[HTTP_Methods]]
- [[Idempotence]] (POST is not)
- [[Safety_(HTTP)]] (POST is not)
- [[HTTP_Request]] (Body contains data)
- [[HTML_Form]] (Common use case)
- [[HTTP_PUT]] (Contrast: PUT is often for replacing/creating at a known URL and is idempotent)

---
**Source:** Worksheet WS26, RFC 9110