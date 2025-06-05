---
tags: [c, concept, data_representation, data_type, encoding, text]
aliases: [wchar_t, Wide Character]
related:
  - "[[bits]]"
  - "[[bytes]]"
  - "[[char_C]]"
  - "[[Unicode]]"
  - "[[UTF-8]]"
  - "[[ASCII]]"
  - "[[String_in_C]]"
  - "[[Locale_C]]"
worksheet: [WS1, C_WS1]
date_created: 2025-04-12
---
# wchar_t (Wide Character)

## Definition

`wchar_t` is a fundamental data type in C (and C++) designed to hold characters from character sets wider than the standard `char` type can typically represent, such as those defined by [[Unicode]]. The actual size and encoding of `wchar_t` are implementation-defined (compiler/platform specific) and depend on the system's [[Locale_C|locale]] settings.

## Key Aspects / Characteristics

- **Wider than `char`:** Intended to store character codes that require more than the 8 [[bits]] usually allocated for `char`.
- **Implementation-Defined Size:** The size of `wchar_t` (e.g., 16 bits or 32 bits) varies across platforms and compilers. This lack of standardization is a major drawback.
    - On Windows, it's typically 16 bits (representing UTF-16 code units).
    - On many Linux/Unix systems, it's typically 32 bits (representing UTF-32/UCS-4 code points).
- **Locale Dependent:** The interpretation of `wchar_t` values often depends on the current program locale set using functions like `setlocale()`.
- **Wide String Literals:** Prefixed with `L`, e.g., `L"Hello World"`, `L'Ω'`.
- **Standard Library Functions:** A set of functions analogous to `<string.h>` and `<stdio.h>` exist in `<wchar.h>` for manipulating wide characters and strings (e.g., `wcslen`, `wcscpy`, `wprintf`, `fgetws`).

## Examples / Use Cases

```c
#include <wchar.h>
#include <stdio.h>
#include <locale.h>

int main() {
    // Set locale to allow system's default wide character handling
    setlocale(LC_ALL, "");

    wchar_t wc = L'Ω'; // Wide character literal (Omega)
    wchar_t wstr[] = L"你好世界"; // Wide string literal (Chinese: Hello World)

    // Note: wprintf is needed for wide strings
    wprintf(L"Wide char: %lc\n", wc);
    wprintf(L"Wide string: %ls\n", wstr);
    wprintf(L"Size of wchar_t on this system: %zu bytes\n", sizeof(wchar_t));

    return 0;
}
```

## Related Concepts

- [[char_C]] (Standard character type, usually 8 bits)
- [[Unicode]] (The character set wchar_t aims to represent)
- [[UTF-8]], UTF-16, UTF-32 (Encodings often used by wchar_t, depending on platform)
- [[bytes]], [[bits]] (Underlying storage units)
- [[String_in_C]] (Wide strings wchar_t* vs standard strings char*)
- [[Locale_C]] (Affects interpretation and I/O of wide characters)

## Questions / Further Study

> [!warning] Portability Issues  
> Because the size and encoding of wchar_t are not standardized across platforms, relying heavily on it can lead to significant portability problems. Modern C/C++ often favors using [[UTF-8]] encoded char strings and libraries designed to handle UTF-8 directly, or uses the more explicitly sized types like char16_t and char32_t introduced in C11/C++11.

---

**Source:** Worksheet WS1, C_WS1