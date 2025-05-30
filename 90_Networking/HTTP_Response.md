---
tags:
  - networking
  - concept
  - protocol
  - http
  - web
aliases:
  - HTTP Response Message
related:
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[HTTP_Status_Codes]]"
  - "[[HTTP_Headers]]"
  - "[[MIME_type]]"
  - "[[Client_Server_Model]]"
  - "[[Request_Response_Model]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP Response

## Definition

An **HTTP Response** is a message sent by a server (e.g., a [[Web_Server]]) back to a client (e.g., a [[Web_Browser]]) in reply to an [[HTTP_Request]] it received. The response indicates the status of the request (success, failure, redirection) and typically includes the requested resource (if applicable), along with metadata in headers.

## Structure of an HTTP Response Message (WS26 Question 4)

An HTTP response message consists of the following parts, separated by CRLF (`\r\n`):

1.  **Status Line (Start Line):**
    -   Contains three parts, space-separated:
        -   **HTTP Version:** The version of the HTTP protocol being used (e.g., `HTTP/1.1`).
        -   **[[HTTP_Status_Codes|Status Code]]:** A 3-digit integer code indicating the result of the request (e.g., `200`, `404`, `500`).
        -   **Reason Phrase (Status Text):** A short, human-readable text description of the status code (e.g., `OK`, `Not Found`, `Internal Server Error`). The reason phrase is informational and not strictly parsed by clients.
    -   Example: `HTTP/1.1 200 OK`

2.  **[[HTTP_Headers|Headers]]:**
    -   Zero or more header lines, each consisting of a case-insensitive header field name, followed by a colon `:`, optional whitespace, and the field value.
    -   Provide metadata about the response, the server, or the resource being sent.
    -   Examples:
        -   `Date: Mon, 23 May 2023 22:38:34 GMT`
        -   `Server: Apache/2.4.1 (Unix)`
        -   `Content-Type: text/html; charset=UTF-8` (Specifies type of data in the response body - [[MIME_type]])
        -   `Content-Length: 1532` (Specifies size of response body in bytes)
        -   `Last-Modified: Tue, 15 Nov 2022 12:45:26 GMT`
        -   `Connection: close` or `keep-alive`
        -   `Location: /new/page.html` (Used with redirection status codes like 301/302)
        -   `Set-Cookie: sessionid=abc...` (Instructs client to store a cookie)

3.  **Empty Line (CRLF):**
    -   A single blank line (just CRLF) separates the headers from the message body. This line is always required, even if there is no body.

4.  **Message Body (Optional):**
    -   Contains the actual resource data requested (e.g., HTML content, image data, JSON payload) or information about an error.
    -   The presence and interpretation of the body depend on the request method and the response status code. Responses to `HEAD` requests and status codes like `204 No Content` or `304 Not Modified` do not have a body.

## Example Response

```http
HTTP/1.1 200 OK                     <-- Status Line
Date: Mon, 27 May 2024 10:00:00 GMT <-- Header
Server: nginx/1.18.0                <-- Header
Content-Type: text/html             <-- Header
Content-Length: 138                 <-- Header
Last-Modified: Sun, 26 May 2024 15:00:00 GMT <-- Header
Connection: keep-alive              <-- Header
                                    <-- Empty Line (CRLF)
<html>                              <-- Message Body Starts
<head><title>Example</title></head>
<body>Hello World!</body>
</html>                             <-- Message Body Ends
```

## Related Concepts
- [[HTTP]], [[Request_Response_Model]]
- [[HTTP_Request]] (The message the response replies to)
- [[HTTP_Status_Codes]] (Indicates outcome)
- [[HTTP_Headers]] (Provide metadata)
- [[MIME_type]] (Specified by `Content-Type` header)
- Message Body (Contains the resource/data)
- [[Client_Server_Model]] (Server sends response)

## Questions / Further Study
>[!question] In a successful HTTP response, which status code is returned, and which header field is used to indicate the size of the payload? (WS26)
> - **Status Code:** For a typical successful request (like a `GET` request that finds the resource), the status code returned is **`200 OK`**. Other success codes exist in the 2xx range (e.g., `201 Created`, `204 No Content`).
> - **Header Field for Size:** The **`Content-Length`** header field is used to indicate the size of the message body (payload) in bytes. (Alternatively, `Transfer-Encoding: chunked` might be used if the size is not known in advance).

---
**Source:** Worksheet WS26, RFC 9110/9112