---
tags:
  - networking
  - concept
  - protocol
  - http
  - web
aliases:
  - HTTP Request Message
related:
  - "[[HTTP]]"
  - "[[HTTP_Response]]"
  - "[[HTTP_Methods]]"
  - "[[URL]]"
  - "[[HTTP_Headers]]"
  - "[[HTTP_Query_String]]"
  - "[[Client_Server_Model]]"
  - "[[Request_Response_Model]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP Request

## Definition

An **HTTP Request** is a message sent by a client (e.g., a [[Web_Browser]]) to a server (e.g., a [[Web_Server]]) to initiate an action on a resource. The request specifies the desired action ([[HTTP_Methods|HTTP method]]), the target resource ([[URL]]), the HTTP protocol version, optional metadata ([[HTTP_Headers|headers]]), and an optional message body containing data.

## Structure of an HTTP Request Message (WS26 Question 4)

An HTTP request message consists of the following parts, separated by CRLF (`\r\n`):

1.  **Request Line (Start Line):**
    -   Contains three parts, space-separated:
        -   **Method:** The HTTP method indicating the desired action (e.g., `GET`, `POST`, `PUT`, `DELETE`). See [[HTTP_Methods]].
        -   **Request Target (URI/Path):** Usually the path component of the [[URL]] (e.g., `/index.html`, `/api/users`) or sometimes the full URL (for proxies). Includes the [[HTTP_Query_String|query string]] if present.
        -   **HTTP Version:** The version of the HTTP protocol being used (e.g., `HTTP/1.1`, `HTTP/2`).
    -   Example: `GET /search?query=testing HTTP/1.1`

2.  **[[HTTP_Headers|Headers]]:**
    -   Zero or more header lines, each consisting of a case-insensitive header field name, followed by a colon `:`, optional whitespace, and the field value.
    -   Provide metadata about the request, the client, or the resource being requested.
    -   Examples:
        -   `Host: www.example.com` (Required in HTTP/1.1)
        -   `User-Agent: Mozilla/5.0 ...` (Client software information)
        -   `Accept: text/html,application/xhtml+xml` (Acceptable response media types)
        -   `Accept-Language: en-US`
        -   `Content-Type: application/json` (Specifies type of data in the request body)
        -   `Content-Length: 123` (Specifies size of request body in bytes)
        -   `Authorization: Bearer ...` (Authentication credentials)
        -   `Cookie: sessionid=xyz...`

3.  **Empty Line (CRLF):**
    -   A single blank line (just CRLF) separates the headers from the message body. This line is always required, even if there is no body.

4.  **Message Body (Optional):**
    -   Contains data associated with the request, typically used with methods like `POST` or `PUT` to send data to the server (e.g., submitted form data, JSON payload).
    -   The presence and interpretation of the body depend on the request method and the `Content-Type` / `Content-Length` headers. `GET` requests typically do not have a body.

## Example Request

```http
GET /index.html HTTP/1.1       <-- Request Line
Host: www.example.com          <-- Header
User-Agent: curl/7.68.0        <-- Header
Accept: */*                    <-- Header
                               <-- Empty Line (CRLF)
                               <-- No Message Body for GET
```

```http
POST /api/users HTTP/1.1       <-- Request Line
Host: api.example.com          <-- Header
Content-Type: application/json <-- Header
Content-Length: 27             <-- Header
                               <-- Empty Line (CRLF)
{"name": "Alice", "age": 30}   <-- Message Body
```

## Related Concepts
- [[HTTP]], [[Request_Response_Model]]
- [[HTTP_Response]] (The server's reply)
- [[HTTP_Methods]] (GET, POST, etc.)
- [[URL]] (Identifies the target resource)
- [[HTTP_Headers]] (Provide metadata)
- [[HTTP_Query_String]] (Part of the request target)
- Message Body (Optional data payload)
- [[Client_Server_Model]] (Client sends request)

---
**Source:** Worksheet WS26, RFC 9110/9112