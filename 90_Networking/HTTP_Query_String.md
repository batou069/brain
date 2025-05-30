---
tags:
  - networking
  - concept
  - protocol
  - http
  - web
  - url
aliases:
  - Query String
  - URL Query Parameters
related:
  - "[[HTTP]]"
  - "[[HTTP_Request]]"
  - "[[URL]]"
  - "[[HTTP_GET]]"
  - "[[HTML_Form]]" # GET method forms use query strings
  - "[[RESTful_API]]"
worksheet: [WS26]
date_created: 2025-04-21
---
# HTTP Query String

## Definition

An **HTTP Query String** is the part of a [[URL]] that contains data to be passed to web applications or server-side scripts. It begins after a question mark (`?`) and typically consists of one or more **key-value pairs** (parameters), with pairs usually separated by an ampersand (`&`).

## Structure

`?key1=value1&key2=value2&key3=value3...`

- **Separator:** Starts with `?` separating it from the URL path.
- **Parameters:** Consists of key-value pairs.
- **Key-Value Separator:** The key is separated from its value by an equals sign `=`.
- **Pair Separator:** Multiple key-value pairs are separated by an ampersand `&`.
- **URL Encoding:** Keys and values should be URL-encoded (percent-encoded) to handle special characters (like spaces, `&`, `=`, `?`) safely. For example, a space becomes `%20`.

## Purpose & Usage (WS26 Question 13)

- **Passing Parameters with GET:** The primary way to send data to the server when using the [[HTTP_GET]] method, as GET requests typically don't have a message body.
- **Filtering/Searching:** Used to provide search terms, filter criteria, or sorting parameters (e.g., `/products?category=electronics&sort=price_asc`).
- **Pagination:** Indicating which page of results to display (e.g., `/articles?page=3&limit=10`).
- **State Information (Less Common):** Sometimes used to pass non-sensitive state information (though [[Cookies]] or server-side [[Session|sessions]] are generally preferred for state).
- **Tracking:** Used by analytics tools to track campaign sources, mediums, etc. (e.g., UTM parameters).

**When to use it:**
Use query strings primarily for parameters that **define the resource being requested** or modify how it's retrieved (filtering, sorting, pagination), especially with GET requests. Avoid putting sensitive information (like passwords) in query strings, as they are often logged by servers and visible in browser history and referrer headers. For submitting sensitive data or large amounts of data, [[HTTP_POST]] with a request body is preferred.

## Example

In the URL: `https://example.com/search?query=http+status+codes&lang=en`

- **Query String:** `query=http+status+codes&lang=en`
- **Parameter 1:** `key=query`, `value=http+status+codes` (space encoded as `+` or `%20`)
- **Parameter 2:** `key=lang`, `value=en`

The server-side application at `/search` would receive these parameters and use them to perform the search for "http status codes" in English.

## Related Concepts
- [[URL]] (Query string is a component)
- [[HTTP]], [[HTTP_Request]], [[HTTP_GET]]
- Key-Value Pairs
- URL Encoding (Percent Encoding)
- [[HTML_Form]] (GET method forms append data as query string)
- [[RESTful_API]] (Often used for filtering/pagination in GET requests)

---
**Source:** Worksheet WS26