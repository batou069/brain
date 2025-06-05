---
tags:
  - 10_linux
  - concept
  - encoding
  - text
  - c/keyword
aliases:
  - American Standard Code for Information Interchange
related:
  - "[[Unicode]]"
  - "[[UTF-8]]"
  - "[[wchar]]"
  - "[[Binary]]"
  - "[[Text_file]]"
date_created: 2025-04-10
---
# ASCII

## Definition

**ASCII (American Standard Code for Information Interchange)** is a character encoding standard for electronic communication. It represents text in computers, telecommunications equipment, and other devices. ASCII codes represent text using 7 [[bits]], allowing for 128 specified characters: the numbers 0-9, the lowercase letters a-z, the uppercase letters A-Z, basic punctuation symbols, control codes that originated with Teletype machines, and a space.

## Key Aspects / Characteristics

- **7-Bit Encoding:** Uses 7 bits per character, defining 128 code points (0-127).
- **Character Set:** Includes printable characters (letters, digits, punctuation) and non-printable control characters (e.g., newline, tab, carriage return).
- **Compatibility:** Forms the basis for many other character encodings, including [[Unicode]] (the first 128 Unicode code points are identical to ASCII).
- **Limitations:** Only suitable for English text, lacks characters for other languages, accents, symbols, etc.
- **Extended ASCII:** Various unofficial 8-bit extensions were created to add more characters (128-255), but these were often incompatible with each other.

## Examples / Use Cases

- Basic text files on many older systems.
- Command-line interfaces and configuration files often use ASCII or an ASCII-compatible encoding like [[UTF-8]].
- Early internet protocols (like HTTP, SMTP) were originally designed around ASCII.

## Related Concepts
- [[Unicode]] (A modern standard encompassing characters from almost all writing systems)
- [[UTF-8]] (A variable-width encoding for Unicode that is backward-compatible with ASCII)
- [[wchar]] (A C data type often used for wider characters than standard `char`, related to Unicode)
- [[Binary]] / [[bits]] / [[bytes]] (ASCII defines the binary representation of characters)
- [[Text_file]] (Often encoded in ASCII or a compatible format)

## Questions / Further Study
>[!question] Why was ASCII insufficient for modern computing?
> ASCII's 128 characters are only enough for basic English text and control codes. It cannot represent accented characters (like é, ü), characters from non-Latin alphabets (like Cyrillic, Greek, Arabic, Chinese, Japanese, Korean), or many common symbols (like €, ©, mathematical symbols). This limitation necessitated the development of broader standards like [[Unicode]].

---
**Source:** Worksheet WS1, C_WS1
