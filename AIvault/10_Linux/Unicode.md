---
tags:
  - 10_linux
  - concept
  - encoding
  - text
aliases: 
related:
  - "[[ASCII]]"
  - "[[UTF-8]]"
  - "[[UTF-7]]"
  - "[[wchar]]"
  - "[[Text_file]]"
  - "[[String_in_C]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# Unicode

## Definition

**Unicode** is an international character encoding standard that provides a unique number (a *code point*) for every character, no matter the platform, program, or language. It aims to cover all the characters for all the writing systems of the world, modern and ancient, plus technical symbols, emojis, and more.

## Key Aspects / Characteristics

- **Universal Character Set:** Defines a massive set of characters and assigns each a unique code point (e.g., U+0041 for 'A', U+03A9 for 'Ω', U+1F600 for '😀').
- **Standard, Not Encoding:** Unicode itself defines the code points. Separate *encoding forms* specify how these code points are represented in [[bytes]]. Common encodings include [[UTF-8]], UTF-16, and UTF-32.
- **Compatibility:** The first 128 code points (U+0000 to U+007F) match the [[ASCII]] standard.
- **Platform Independence:** Aims to provide a consistent way to represent text across different operating systems and applications.
- **Ongoing Development:** Managed by the Unicode Consortium, which regularly updates the standard to add new characters and scripts.

## Examples / Use Cases

- Modern operating systems (Linux, Windows, macOS, Android, iOS) use Unicode internally for text processing.
- Web pages typically use [[UTF-8]] encoding to display multilingual content.
- Modern programming languages often use Unicode for string representation.

## Related Concepts
- [[ASCII]] (Unicode is a superset, compatible for the first 128 characters)
- [[UTF-8]], [[UTF-7]], UTF-16, UTF-32 (Encodings that represent Unicode code points as byte sequences)
- [[wchar]] (C data type often used to hold Unicode characters, though size varies by platform)
- Code Point (The unique number assigned to a character by Unicode)
- Character Encoding (The method of representing code points in bytes)
- [[Text_file]] (Modern text files are often Unicode-encoded)

## Questions / Further Study
>[!question] What is the difference between Unicode and UTF-8?
> [[Unicode]] is the standard that assigns a unique number (code point) to each character (e.g., U+1F604 is assigned to the "Smiling Face With Open Mouth and Smiling Eyes" emoji 😄). [[UTF-8]] is an *encoding scheme* that specifies how to represent these Unicode code points using sequences of 1 to 4 [[bytes]]. UTF-8 is designed to be backward-compatible with [[ASCII]] (ASCII characters use only 1 byte in UTF-8) and is the dominant encoding on the web.

---
**Source:** Worksheet WS1, C_WS1