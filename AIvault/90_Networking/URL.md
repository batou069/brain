---
tags:
  - networking
  - concept
  - web
  - addressing
  - standard
aliases:
  - Uniform Resource Locator
related:
  - "[[URI]]" # Placeholder
  - "[[URN]]" # Placeholder
  - "[[HTTP]]"
  - "[[HTTPS]]"
  - "[[DNS]]"
  - "[[Domain_Name]]"
  - "[[ip]]"
  - "[[Port_(Networking)]]"
  - "[[HTTP_Query_String]]"
  - "[[Web_Browser]]"
  - "[[World_Wide_Web]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# URL (Uniform Resource Locator)

## Definition

A **URL (Uniform Resource Locator)**, colloquially termed a **web address**, is a reference to a web resource that specifies its **location** on a computer network and a mechanism for retrieving it. URLs are a specific type of Uniform Resource Identifier ([[URI]]), although the terms are often used interchangeably in casual web contexts. URLs are most commonly used to locate web pages ([[HTTP]], [[HTTPS]]) but are also used for file transfer ([[FTP]]), email ([[mailto]]), database access, and other applications.

## Structure (Common HTTP/HTTPS URL)

A typical HTTP/HTTPS URL has the following components:

`scheme://hostname[:port][/path][?query][#fragment]`

-   **`scheme`:** The protocol used to access the resource (e.g., `http`, `https`, `ftp`, `mailto`, `file`). Followed by `://`.
-   **`hostname`:** The [[Domain_Name|domain name]] (e.g., `www.example.com`) or [[ip|IP address]] (e.g., `192.168.1.1`) of the server hosting the resource. [[DNS]] is used to resolve domain names to IP addresses.
-   **`port` (Optional):** The [[Port_(Networking)|port number]] on the server to connect to. If omitted, defaults to the standard port for the scheme (e.g., 80 for `http`, 443 for `https`). Separated from the hostname by a colon `:`. Example: `http://example.com:8080`.
-   **`/path` (Optional):** Specifies the specific resource (e.g., file, directory, endpoint) being requested on the server. If omitted, often defaults to a root resource (`/`). Path segments are separated by forward slashes `/`. Example: `/products/search`.
-   **`?query` (Optional):** Contains additional data (often key-value pairs) passed to the server, typically used for filtering, searching, or parameters. Starts with a question mark `?`. Key-value pairs are usually separated by ampersands `&`. See [[HTTP_Query_String]]. Example: `?query=networking&page=2`.
-   **`#fragment` (Optional):** An anchor or fragment identifier pointing to a specific section *within* the resource (e.g., a specific heading on a web page). Starts with a hash `#`. This part is typically processed only by the client ([[Web_Browser]]) and is *not* sent to the server. Example: `#section-3`.

## Example URL Breakdown

`https://www.example.co.uk:443/blog/article?id=123#comments`

-   **Scheme:** `https`
-   **Hostname:** `www.example.co.uk`
-   **Port:** `443` (Default for HTTPS, often omitted)
-   **Path:** `/blog/article`
-   **Query:** `id=123`
-   **Fragment:** `comments`

## Related Concepts
- [[URI]] (URL is a type of URI), [[URN]] (Another type of URI)
- [[World_Wide_Web]], [[HTTP]], [[HTTPS]] (Primary context for URLs)
- [[DNS]], [[Domain_Name]], [[ip]], [[Port_(Networking)]] (Components used for location)
- [[HTTP_Query_String]], Fragment Identifier (#)
- [[Web_Browser]] (Parses and uses URLs)

---
**Source:** Worksheet WS26, RFC 3986