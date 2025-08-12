---
tags:
  - networking
  - concept
  - standard
  - web
  - http
  - email
aliases:
  - MIME Type
  - Media Type
  - Content Type
related:
  - "[[HTTP]]"
  - "[[HTTP_Headers]]" # Content-Type header
  - "[[HTTP_Response]]"
  - "[[HTTP_Request]]" # For POST/PUT body
  - "[[Email]]" # Originally developed for email
  - "[[JSON]]"
  - "[[HTML]]"
  - "[[CSS]]" # Placeholder
  - "[[JavaScript]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# MIME Type (Media Type)

## Definition

A **MIME (Multipurpose Internet Mail Extensions) Type**, now more formally known as a **Media Type** (or sometimes Content Type), is a standardized two-part identifier used to indicate the nature and format of a document, file, or assortment of bytes. It allows software (like web browsers, email clients) to understand how to process or display the data correctly.

## Structure

A MIME type consists of a **type** and a **subtype**, separated by a slash (`/`). It can also optionally include parameters (like character set).

`type/subtype[; parameter=value]`

- **Type:** Represents the general category of the data. Common top-level types include:
    - `text` (e.g., `text/plain`, `text/html`, `text/css`)
    - `image` (e.g., `image/jpeg`, `image/png`, `image/gif`)
    - `audio` (e.g., `audio/mpeg`, `audio/ogg`)
    - `video` (e.g., `video/mp4`, `video/quicktime`)
    - `application` (For binary data, specific application formats, or data not fitting other categories; e.g., `application/octet-stream`, `application/pdf`, `application/json`, `application/xml`, `application/javascript`)
    - `multipart` (For messages containing multiple parts, e.g., `multipart/form-data` used in [[HTML_Form|form submissions]])
- **Subtype:** Specifies the exact kind of data within the top-level type.
- **Parameters (Optional):** Provide additional details, most commonly `charset` to specify the character encoding (e.g., `text/html; charset=UTF-8`).

## Usage in HTTP

- **`Content-Type` Header:** The most crucial use in [[HTTP]]. This header field in both [[HTTP_Request|requests]] (for POST/PUT bodies) and [[HTTP_Response|responses]] specifies the MIME type of the **message body**.
    - *Response:* Tells the browser how to interpret the received data (e.g., render as HTML, display as image, offer download for `application/octet-stream`).
    - *Request:* Tells the server how to interpret the data submitted in the request body (e.g., parse as JSON, process as form data).
- **`Accept` Header:** In an HTTP Request, the `Accept` header tells the server which MIME type(s) the client *prefers* or is capable of understanding for the response. This allows for [[Content_Negotiation]].

## Examples

- `text/html`: An [[HTML]] document.
- `text/plain`: Plain text, no special formatting.
- `image/jpeg`: A JPEG image.
- `image/png`: A PNG image.
- `application/pdf`: A PDF document.
- `application/json`: [[JSON]] formatted data.
- `application/xml`: XML formatted data.
- `application/octet-stream`: Arbitrary binary data (often triggers a download prompt).
- `multipart/form-data`: Used when submitting HTML forms that include file uploads.

## Related Concepts
- [[HTTP]], [[HTTP_Headers]] (`Content-Type`, `Accept`)
- [[HTTP_Request]], [[HTTP_Response]] (Where MIME types are specified)
- [[Email]] (Original context for MIME standard)
- File Formats ([[HTML]], [[JSON]], XML, JPEG, PNG, PDF, etc.)
- [[Content_Negotiation]] (Using `Accept` header)

## Questions / Further Study
>[!question] What is the MIME type for JSON? (WS26)
> The standard MIME type for [[JSON]] is **`application/json`**.

---
**Source:** Worksheet WS26, RFC 2046, MDN Web Docs