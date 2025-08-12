---
tags: [c, function, stdio, io, output, variadic]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[scanf]]"
  - "[[sprintf]]"
  - "[[fprintf_C]]"
  - "[[stdout_stdout_stderr_C]]"
  - "[[Format_Specifiers_C]]"
  - "[[Variable_Length_Parameter_List_C]]"
  - "[[stdarg_macros_C]]"
worksheet: [C_WS3]
header_file: <stdio.h>
date_created: 2025-04-11
---
# ` printf() `

## Purpose

The `printf()` (print formatted) function sends formatted output to the standard output stream ([[stdout_stdout_stderr_C|`stdout`]]), which is typically the console or terminal window. It allows printing text mixed with the values of variables or expressions, formatted according to specified conversion specifiers.

## Signature

```c
#include <stdio.h>
int printf(const char * restrict format, ...);
```

## Parameters

-   `format`: A [[String_in_C|C string]] (null-terminated character array) that contains the text to be written to `stdout`. It can optionally contain embedded **format specifiers** (e.g., `%d`, `%f`, `%s`, `%c`, `%p`) which are replaced by the values specified in subsequent additional arguments and formatted as requested.
-   `...`: (Ellipsis) Indicates that the function takes a [[Variable_Length_Parameter_List_C|variable number of arguments]]. These arguments correspond to the format specifiers in the `format` string, in order. The number and type of these arguments *must* match the format specifiers.

## Return Value

-   On **success**, returns the total number of characters written to `stdout`.
-   On **failure** (e.g., an output error occurs), returns a negative value.

## Format Specifiers (Common)

See [[Format_Specifiers_C]] for more details.
-   `%d` or `%i`: Signed decimal integer (`int`).
-   `%u`: Unsigned decimal integer (`unsigned int`).
-   `%f`: Decimal floating-point (`double`). Default precision is 6 decimal places.
-   `%e`, `%E`: Scientific notation (`double`).
-   `%g`, `%G`: Use `%f` or `%e` depending on value/precision (`double`).
-   `%c`: Single character (`int` promoted from `char`).
-   `%s`: String ([[String_in_C|null-terminated `char*`]]).
-   `%p`: Pointer address (`void*`), implementation-defined representation.
-   `%x`, `%X`: Unsigned hexadecimal integer (`unsigned int`).
-   `%o`: Unsigned octal integer (`unsigned int`).
-   `%%`: A literal percent sign (`%`).
-   **Modifiers:** Length (e.g., `%ld` for `long int`, `%lf` for `double` - though often optional for `double` in `printf`), width, precision, flags (e.g., `-` for left-justify, `+` for sign, `0` for zero-padding).

## Example Usage

```c
#include <stdio.h>

int main() {
    int age = 30;
    double height = 1.75;
    char initial = 'J';
    char *name = "John Doe";
    int chars_written;

    // Basic usage
    printf("Hello, World!\n");

    // Printing variables
    printf("Name: %s\n", name);
    printf("Initial: %c\n", initial);
    printf("Age: %d years\n", age);
    printf("Height: %f meters\n", height); // Default precision
    printf("Height (2dp): %.2f meters\n", height); // 2 decimal places

    // Printing pointer address
    printf("Address of age: %p\n", (void*)&age);

    // Printing multiple variables and capturing return value
    chars_written = printf("User: %s, Age: %d\n", name, age);
    printf("(Previous line wrote %d characters)\n", chars_written);

    // Printing hex and octal
    printf("Age in Hex: %X\n", age); // Output: 1E
    printf("Age in Octal: %o\n", age); // Output: 36

    // Printing a literal % sign
    printf("Discount: 10%%\n"); // Output: Discount: 10%

    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file required)
- [[stdout_stdout_stderr_C]] (The default output stream)
- [[Format_Specifiers_C]] (Controls output formatting)
- [[Variable_Length_Parameter_List_C]], [[stdarg_macros_C]] (How `printf` handles variable arguments internally)
- [[scanf]] (Formatted input function)
- [[sprintf]] (Prints formatted output to a string buffer)
- [[fprintf_C]] (Prints formatted output to a specified file stream)
- [[Escape_Characters_C]] (Used within the format string, e.g., `\n`, `\t`)

## Notes
>[!warning] Type Mismatch
> Providing arguments of a type different from what the corresponding format specifier expects leads to [[Undefined_Behavior_C]]. For example, `printf("%d", 3.14);` or `printf("%s", 10);` are incorrect and can cause crashes or garbage output.

---
**Source:** Worksheet C_WS3