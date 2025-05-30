---
tags: [c, concept, data_representation, math]
aliases: [Binary, Octal, Hexadecimal, Decimal, Base]
related:
  - "[[bits]]"
  - "[[bytes]]"
  - "[[Data_Types_C]]"
  - "[[Bitwise_Operator_C]]"
worksheet: [WS1, C_WS1]
date_created: 2025-04-12
---
# Number Systems (Binary, Octal, Decimal, Hexadecimal)

## Definition

Number systems are ways of representing numerical values. Computers fundamentally operate using **Binary** (base-2), but programmers often use **Decimal** (base-10), **Octal** (base-8), and **Hexadecimal** (base-16) for convenience, especially when dealing with [[bits]] and [[bytes]]. C allows integer constants to be written in decimal, octal, and hexadecimal formats.

## Key Aspects / Characteristics

-   **Base:** The number of unique digits used in the system.
    -   **Binary (Base-2):** Uses digits 0, 1. Directly represents the on/off states of [[bits]].
        -   *C Literal Prefix:* `0b` or `0B` (since C11, but widely supported before). Example: `0b1011` (decimal 11).
    -   **Octal (Base-8):** Uses digits 0-7. Each octal digit represents exactly 3 bits (`2^3 = 8`). Was more common when word sizes were multiples of 3 bits.
        -   *C Literal Prefix:* `0`. Example: `013` (decimal 11). *Caution: A leading zero means octal!*
    -   **Decimal (Base-10):** Uses digits 0-9. The standard system for human arithmetic.
        -   *C Literal Prefix:* None (or just not `0` or `0x`/`0X`). Example: `11`.
    -   **Hexadecimal (Base-16):** Uses digits 0-9 and letters A-F (or a-f) to represent values 10-15. Each hex digit represents exactly 4 bits (`2^4 = 16`), making it very convenient for representing [[bytes]].
        -   *C Literal Prefix:* `0x` or `0X`. Example: `0xB` (decimal 11), `0xFF` (decimal 255).

-   **Place Value:** The position of a digit determines its value (multiplied by the base raised to the power of the position).
    -   Binary `1011` = (1 * 2³) + (0 * 2²) + (1 * 2¹) + (1 * 2⁰) = 8 + 0 + 2 + 1 = 11 (decimal).
    -   Octal `013` = (1 * 8¹) + (3 * 8⁰) = 8 + 3 = 11 (decimal).
    -   Hex `0xB` = (11 * 16⁰) = 11 (decimal).
    -   Hex `0x1A` = (1 * 16¹) + (10 * 16⁰) = 16 + 10 = 26 (decimal).

## Examples / Use Cases

```c
#include <stdio.h>

int main() {
    int dec_val = 26;
    int oct_val = 032;   // Octal representation of 26 (3*8 + 2*1)
    int hex_val = 0x1A;  // Hexadecimal representation of 26 (1*16 + 10*1)
    int bin_val = 0b11010; // Binary representation of 26 (16 + 8 + 2) - C11+

    printf("Decimal: %d\n", dec_val);
    printf("Octal (032) as decimal: %d\n", oct_val);
    printf("Hex (0x1A) as decimal: %d\n", hex_val);
    printf("Binary (0b11010) as decimal: %d\n", bin_val);

    // Printing in different bases
    printf("Decimal 26 as Octal: %o\n", dec_val);   // Output: 32
    printf("Decimal 26 as Hex: %x\n", dec_val);     // Output: 1a
    printf("Decimal 26 as HEX: %X\n", dec_val);     // Output: 1A

    // Using different bases in code
    int permissions = 0755; // Octal common for Unix permissions
    int color = 0xFF0000;   // Hex common for RGB colors (Red)
    int flags = 0b00001010; // Binary useful for bit flags

    printf("Permissions (0755 octal): %d decimal\n", permissions); // Output: 493
    printf("Color (0xFF0000 hex): %d decimal\n", color);       // Output: 16711680
    printf("Flags (0b1010 binary): %d decimal\n", flags);       // Output: 10

    return 0;
}
```

## Related Concepts

- [[bits]], [[bytes]] (The underlying representation)
- [[Data_Types_C]] (How values are stored)
- [[Bitwise_Operator_C]] (Often used with hex or binary representations)
- [[printf]], [[scanf]] (Functions for formatted I/O using different bases)

---

**Source:** Worksheet WS1, C_WS1