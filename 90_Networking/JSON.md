---
tags:
  - networking
  - data_format
  - concept
  - web
  - api
aliases:
  - JavaScript Object Notation
related:
  - "[[Data_Format]]" # Placeholder
  - "[[XML]]" # Contrast
  - "[[Web_API]]"
  - "[[RESTful_API]]"
  - "[[JavaScript]]" # Origin
  - "[[MIME_type]]" # application/json
  - "[[Serialization]]" # Placeholder
worksheet: [WS26]
date_created: 2025-04-21
---
# JSON (JavaScript Object Notation)

## Definition

**JSON (JavaScript Object Notation)** is a lightweight, text-based, human-readable data interchange format. It was derived from the object literal syntax of the [[JavaScript]] programming language but is language-independent. JSON is commonly used for transmitting structured data, particularly between a server and web application (as an alternative to [[XML]]), in [[Web_API|web APIs]], and for configuration files.

## Structure & Syntax

JSON represents data using two main structures:

1.  **Objects:** An unordered collection of **key/value pairs**.
    -   Enclosed in curly braces `{}`.
    -   Keys must be **strings** (enclosed in double quotes `"`).
    -   Values can be strings, numbers, booleans (`true`/`false`), arrays, `null`, or other JSON objects.
    -   Key-value pairs are separated by commas `,`. The key is separated from the value by a colon `:`.
    -   Example: `{"name": "Alice", "age": 30, "isStudent": false, "courses": ["CS101", "MA203"]}`

2.  **Arrays:** An ordered sequence of **values**.
    -   Enclosed in square brackets `[]`.
    -   Values can be strings, numbers, booleans, arrays, `null`, or JSON objects.
    -   Values are separated by commas `,`.
    -   Example: `[10, "hello", true, null, {"id": 1}]`

**Data Types:**
- **String:** Sequence of Unicode characters enclosed in double quotes `"`. Backslash `\` is used for escaping special characters (e.g., `\"`, `\\`, `\n`, `\t`, `\uXXXX`).
- **Number:** Integer or floating-point numbers (no distinction like `int` vs `float`). Octal and hex formats are not used.
- **Boolean:** `true` or `false` (lowercase).
- **Array:** Ordered list `[...]`.
- **Object:** Unordered key-value pairs `{...}`.
- **`null`:** Represents an empty or null value (lowercase).

## Advantages

- **Human-Readable:** Relatively easy for humans to read and write compared to binary formats or even some XML.
- **Easy to Parse:** Simple syntax makes it easy and efficient for machines to parse and generate. Parsers are readily available in virtually all programming languages.
- **Lightweight:** Less verbose than [[XML]], resulting in smaller message sizes and faster transmission.
- **Widely Used:** The de facto standard for data exchange in modern web APIs ([[RESTful_API]]).
- **JavaScript Integration:** Maps directly to JavaScript object literals, making it trivial to work with in web browsers and Node.js.

## JSON vs. XML (WS26 Question 15)

| Feature         | JSON                                | XML                                       |
| :-------------- | :---------------------------------- | :---------------------------------------- |
| **Verbosity**   | Less verbose                        | More verbose (tags, attributes)           |
| **Readability** | Generally easier for humans       | Can be readable, but tags add clutter     |
| **Parsing**     | Simpler, faster (built-in JS eval)  | More complex (requires XML parser)        |
| **Data Types**  | String, Number, Boolean, Array, Object, null | Primarily text-based (types via schema) |
| **Extensibility**| Less formal (structure implies type)| Formal (Namespaces, Schemas - XSD)      |
| **Comments**    | No built-in support                 | Yes (`<!-- comment -->`)                 |
| **Arrays**      | Native array type `[]`              | Represented using repeated tags           |
| **Use Case**    | Web APIs, data interchange, config  | Documents, configuration, SOAP, legacy    |

**How JSON is simpler:** Less syntax overhead (no closing tags), native support for basic data types (especially arrays/lists), simpler parsing model.

## Related Concepts
- [[Data_Format]], [[Serialization]]
- [[XML]] (Alternative format)
- [[Web_API]], [[RESTful_API]] (Common use case)
- [[JavaScript]] (Origin of notation)
- [[MIME_type]] (`application/json`)
- Key-Value Pairs, Objects, Arrays

## Questions / Further Study
>[!question] What does JSON stand for? (WS26)
> **JavaScript Object Notation**.

>[!question] What is the MIME type for JSON? (WS26)
> **`application/json`**.

---
**Source:** Worksheet WS26, json.org