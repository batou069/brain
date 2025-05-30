---
tags: [c, concept, syntax, string, char]
aliases: [C Escape Sequences]
related:
  - "[[String_in_C]]"
  - "[[char_C]]"
  - "[[printf]]"
  - "[[ASCII]]"
worksheet: [C_WS1]
date_created: 2025-04-12
---
# Escape Characters (C)

## Definition

In C, **Escape Characters** (more accurately, **Escape Sequences**) are sequences of characters starting with a backslash (`\`) used within character (`' '`) and string (`" "`) literals. They represent characters that are difficult or impossible to type directly, such as non-printable control characters (like newline, tab) or characters that have special meaning within literals (like the backslash itself or quotation marks).

## Key Aspects / Characteristics

- **Backslash Prefix:** Always begin with `\`.
- **Represent Special Characters:** Allow embedding control codes or syntactically significant characters into literals.
- **Compile-Time Interpretation:** The compiler replaces the escape sequence with the single character value it represents.
- **Common Sequences:**
    - `\n`: Newline
    - `\t`: Horizontal Tab
    - `\r`: Carriage Return
    - `\b`: Backspace
    - `\\`: Backslash (`\`)
    - `\'`: Single quote (`'`)
    - `\"`: Double quote (`"`)
    - `\?`: Question mark (`?`) (useful for avoiding trigraphs, though less relevant now)
    - `\a`: Alert (Bell)
    - `\f`: Form Feed
    - `\v`: Vertical Tab
    - `\0`: Null character (very important for terminating C [[String_in_C|strings]])
    - `\ooo`: Character represented by octal value `ooo` (1 to 3 octal digits).
    - `\xhh`: Character represented by hexadecimal value `hh` (1 or more hex digits).
    - `\u`hhhh / `\U`hhhhhhhh: Universal character names (for [[Unicode]] code points, C99+).

## Examples / Use Cases

```c
#include <stdio.h>

int main() {
    // Using common escape sequences
    printf("Hello\tWorld!\n"); // Output: Hello   World! (newline at end)
    printf("This is a line.\rOverwrite\n"); // Output depends on terminal, often "Overwrite line."
    printf("Beep! \a\n"); // Might produce an audible beep

    // Escaping special characters
    printf("Path: C:\\Users\\Default\n"); // Output: Path: C:\Users\Default
    printf("She said, \"Hi!\"\n");      // Output: She said, "Hi!"
    printf("Character: \'\n");          // Output: Character: '

    // Using octal and hex escapes
    char newline_oct = '\012'; // Octal for newline (ASCII 10)
    char newline_hex = '\x0A'; // Hex for newline (ASCII 10)
    char null_char = '\0';     // The null terminator

    printf("Newline (oct): %d\n", newline_oct); // Output: 10
    printf("Newline (hex): %d\n", newline_hex); // Output: 10

    // Null terminator in strings
    char my_string[] = "Test\0Hidden"; // String is effectively "Test" due to \0
    printf("String: %s\n", my_string); // Output: Test

    return 0;
}
```

## Related Concepts

- [[String_in_C]] (Strings are terminated by the \0 escape sequence)
- [[char_C]] (Escape sequences represent single character values)
- [[printf]] (Uses escape sequences for formatting output)
- [[ASCII]] (Many escape sequences correspond to ASCII control codes)
- [[Unicode]] (\u and \U escapes relate to Unicode)


---

**Source:** Worksheet C_WS1