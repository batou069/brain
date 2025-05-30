---
tags:
  - networking
  - concept
  - protocol
  - http
  - web
  - status_code
aliases:
  - HTTP Status Codes
related:
  - "[[HTTP]]"
  - "[[HTTP_Response]]"
  - "[[HTTP_Request]]"
  - "[[RESTful_API]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP Status Codes

## Definition

**HTTP Status Codes** are three-digit integer codes included in the first line (Status Line) of an [[HTTP_Response]] message from a server. They indicate the outcome of the client's [[HTTP_Request]]. Each status code belongs to one of five classes, identified by the first digit, and provides a standardized way for servers to communicate results back to clients (like browsers or API consumers).

## Classes of Status Codes (WS26 Question 7)

1.  **1xx (Informational):** Request received, continuing process.
    -   *Examples:* `100 Continue` (Client should continue request or ignore if finished), `101 Switching Protocols` (Server agrees to switch protocols as requested).
    -   *Usage:* Relatively rare in general web browsing.

2.  **2xx (Successful):** The action requested by the client was received, understood, accepted, and processed successfully.
    -   *Examples:*
        -   `200 OK`: Standard response for successful HTTP requests (e.g., GET, PUT success).
        -   `201 Created`: Request succeeded, and a new resource was created as a result (often returned after POST or PUT).
        -   `202 Accepted`: Request accepted for processing, but processing is not complete.
        -   `204 No Content`: Server successfully processed the request but there is no content to return (often used for DELETE success).
    -   *Usage:* Indicates the request achieved its goal.

3.  **3xx (Redirection):** Further action needs to be taken by the client (user agent) to complete the request. Usually involves redirecting to a different [[URL]].
    -   *Examples:*
        -   `301 Moved Permanently`: The requested resource has permanently moved to a new URL (given in the `Location` header).
        -   `302 Found` (or `307 Temporary Redirect`): The resource is temporarily at a different URL. Client should use the original URL for future requests.
        -   `304 Not Modified`: Used for caching. Indicates the resource hasn't changed since the version specified by request headers (`If-Modified-Since` or `If-None-Match`), so the client can use its cached copy.
    -   *Usage:* Handles moved resources, caching, temporary redirects.

4.  **4xx (Client Error):** The request contains bad syntax or cannot be fulfilled by the server, likely due to an error on the client's side.
    -   *Examples:*
        -   `400 Bad Request`: Server cannot process the request due to a client error (e.g., malformed syntax).
        -   `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
        -   `403 Forbidden`: Server understood the request but refuses to authorize it (client lacks permission).
        -   `404 Not Found`: Server cannot find the requested resource.
        -   `405 Method Not Allowed`: The HTTP method used (e.g., POST) is not supported for the requested resource.
        -   `409 Conflict`: Request conflicts with the current state of the resource (e.g., edit conflict).
    -   *Usage:* Indicates problems with the client's request.

5.  **5xx (Server Error):** The server failed to fulfill an apparently valid request due to an error on the server's side.
    -   *Examples:*
        -   `500 Internal Server Error`: A generic error message when an unexpected condition was encountered and no more specific message is suitable.
        -   `501 Not Implemented`: Server does not support the functionality required to fulfill the request.
        -   `502 Bad Gateway`: Server, while acting as a gateway or proxy, received an invalid response from the upstream server.
        -   `503 Service Unavailable`: Server is currently unable to handle the request due to temporary overloading or maintenance.
        -   `504 Gateway Timeout`: Server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.
    -   *Usage:* Indicates problems on the server side.

## Related Concepts
- [[HTTP]], [[HTTP_Response]] (Status codes are part of the response)
- [[HTTP_Request]] (The request whose outcome is indicated)
- [[RESTful_API]] (Status codes are crucial for signaling API call results)

## Questions / Further Study
>[!question] What status code is returned for a resource which is not found on the server? (WS26)
> **`404 Not Found`**.

>[!question] In a successful HTTP response, which status code is returned...? (WS26)
> The most common status code for a generally successful request (like retrieving a resource with GET) is **`200 OK`**. Other success codes in the `2xx` range indicate specific types of success (e.g., `201 Created`, `204 No Content`).

---
**Source:** Worksheet WS26, RFC 9110