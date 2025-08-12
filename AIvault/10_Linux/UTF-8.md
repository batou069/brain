---
tags:
  - 10_linux
  - concept
aliases:
  - Unicode Transformation Format - 8-bit
related:
  - "[[Unicode]]"
  - "[[ASCII]]"
  - "[[wchar]]"
  - "[[bytes]]"
  - "[[Text_file]]"
  - "[[String_in_C]]"
worksheet:
  - WS<% tp.file.cursor(1) %>
date_created: 2025-04-10
---
# UTF-8

## Definition

**UTF-8 (Unicode Transformation Format - 8-bit)** is a variable-width character encoding used for electronic communication. It is capable of encoding all 1,112,064 valid character code points in [[Unicode]] using one to four 8-bit [[bytes]]. UTF-8 is designed for backward compatibility with [[ASCII]] and has become the dominant character encoding for the World Wide Web.

## Key Aspects / Characteristics

- **Unicode Encoding:** Represents [[Unicode]] code points as byte sequences.
- **Variable Width:** Characters are encoded using 1, 2, 3, or 4 bytes:
    - 1 byte: Standard [[ASCII]] characters (U+0000 to U+007F).
    - 2 bytes: Most Latin-script alphabets with diacritics, Greek, Cyrillic, Coptic, Armenian, Hebrew, Arabic (U+0080 to U+07FF).
    - 3 bytes: Most other common characters, including many East Asian characters (U+0800 to U+FFFF).
    - 4 bytes: Less common characters, historical scripts, mathematical symbols, emojis (U+10000 to U+10FFFF).
- **ASCII Compatibility:** Any valid ASCII text is also valid UTF-8 text with the same meaning. This was a major factor in its adoption.
- **Self-Synchronizing:** Easy to find the start of the next character after an error or random access, as the number of bytes in a sequence is determined by the leading bits of the first byte.
- **No Byte Order Mark (BOM) Needed:** Unlike UTF-16/UTF-32, UTF-8 does not have byte order issues, although a BOM (U+FEFF encoded as EF BB BF) is sometimes used (often unnecessarily) to indicate UTF-8 encoding.
- **Efficiency:** Space-efficient for text dominated by ASCII characters (common in programming languages, configuration files, English text).

## Examples / Use Cases

- The default character encoding for HTML5.
- Widely used in configuration files, source code, and text files on Linux and macOS.
- Standard encoding for JSON.
- Used in many internet protocols.

## Related Concepts
- [[Unicode]] (The character set standard that UTF-8 encodes)
- [[ASCII]] (UTF-8 is backward-compatible with ASCII)
- [[bytes]] (UTF-8 represents characters as sequences of bytes)
- [[wchar]] (C type sometimes used for Unicode, but UTF-8 is often handled using standard `char*` strings)
- [[Text_file]] (Commonly encoded using UTF-8)

## Questions / Further Study
>[!question] Why is UTF-8 so popular, especially on the web and in Unix-like systems?
> 1.  **[[ASCII]] Compatibility:** Existing tools and text files using ASCII often work correctly with UTF-8 without modification.
> 2.  **Universality:** Can represent any [[Unicode]] character.
> 3.  **Efficiency:** For English and code, it's as compact as ASCII (1 byte per character).
> 4.  **Robustness:** Self-synchronizing nature makes it resilient to some errors.
> 5.  **No Byte Order Issues:** Avoids the endianness problems of UTF-16/UTF-32.

---
**Source:** Worksheet WS1, C_WS1