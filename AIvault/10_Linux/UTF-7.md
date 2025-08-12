---
tags:
  - linux
  - concept
  - encoding
  - text
  - legacy
  - unicode
aliases:
  - UTF-7
related:
  - "[[Unicode]]"
  - "[[UTF-8]]"
  - "[[ASCII]]"
  - "[[Base64]]"
  - "[[Email]]"
worksheet:
  - WS1
date_created: 2025-04-20
---
# UTF-7 (Unicode Transformation Format - 7-bit)

## Definition

**UTF-7** is a variable-length character encoding designed to represent [[Unicode]] text using only streams of 7-bit [[ASCII]] characters. It was primarily intended for use in environments that could not handle 8-bit data cleanly, most notably older [[Email|email systems]] (SMTP) that sometimes stripped the 8th bit or misinterpreted 8-bit characters.

## Key Aspects / Characteristics

- **7-Bit ASCII Compatibility:** Uses only standard 7-bit ASCII characters (code points 0-127).
- **Encoding Method:**
    - Most standard printable ASCII characters (letters, numbers, common punctuation) represent themselves directly.
    - Other Unicode characters (including some ASCII symbols like `+`, `~`, `\`) are encoded using a **modified [[Base64]]** scheme.
    - Encoded blocks start with a `+` character and end with a `-` character. Inside the block, Unicode characters (represented as UTF-16 big-endian) are encoded using Base64, but with `,` used instead of `/` for the 64th character.
    - The `+` character itself is encoded as `+-`.
- **Variable Length:** The number of ASCII characters used to represent a Unicode character varies.
- **Obsolete:** UTF-7 is **obsolete** and **should not be used**. Modern systems overwhelmingly support [[UTF-8]], which is far more efficient and standardized for representing Unicode. Email systems now generally support 8-bit data using MIME encoding.
- **Security Risks:** UTF-7 encoding can be exploited in cross-site scripting (XSS) attacks if web applications incorrectly interpret UTF-7 encoded data within contexts expecting plain ASCII or UTF-8. Many browsers have dropped support for auto-detecting UTF-7.

## Example (Conceptual)

The string "Hi Ω!" (Omega is U+03A9) might be encoded something like:
`Hi +CE8AhA-!`
- `Hi ` and `!` are direct ASCII.
- `Ω` (U+03A9) is represented in UTF-16BE as `03 A9`.
- This byte sequence is encoded using modified Base64 within `+...-`. (`CE8AhA` is a conceptual representation of the Base64 encoding).

## Related Concepts
- [[Unicode]] (The character set being encoded)
- [[UTF-8]] (The dominant, recommended Unicode encoding)
- [[ASCII]] (UTF-7 uses only ASCII characters)
- [[Base64]] (Encoding scheme adapted by UTF-7)
- [[Email]] (Original intended use case)
- Character Encoding

---
**Source:** Worksheet WS1, RFC 2152