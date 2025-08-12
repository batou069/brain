---
tags: [c, function, stdio, string, output, variadic]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[printf]]"
  - "[[snprintf_C]]"
  - "[[fprintf_C]]"
  - "[[String_in_C]]"
  - "[[Format_Specifiers_C]]"
  - "[[Variable_Length_Parameter_List_C]]"
  - "[[stdarg_macros_C]]"
  - "[[Buffer_Overflow_C]]"
worksheet: [C_WS3]
header_file: <stdio.h>
date_created: 2025-04-11
---
# ` sprintf() `

## Purpose

The `sprintf()` (string print formatted) function works like [[printf]], but instead of writing the output to `stdout`, it writes the formatted output to a character array ([[String_in_C|string buffer]]) provided by the caller.

## Signature

```c
#include <stdio.h>
int sprintf(char * restrict str, const char * restrict format, ...);
```

## Parameters

-   `str`: A pointer (`char*`) to a character array (buffer) where the resulting formatted string will be stored. **This buffer must be large enough** to hold the entire generated string, including the automatically appended null terminator (`\0`).
-   `format`: A C string containing the text and [[Format_Specifiers_C|format specifiers]], identical in function to the `format` string used in [[printf]].
-   `...`: (Ellipsis) [[Variable_Length_Parameter_List_C|Variable arguments]] corresponding to the format specifiers in the `format` string.

## Return Value

-   On **success**, returns the total number of characters written to the buffer `str`, *excluding* the null terminator.
-   On **failure** (e.g., an encoding error occurs), returns a negative value. (Note: It does *not* typically return an error for buffer overflows, which is why it's dangerous).

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h> // For exit()

int main() {
    char buffer[100]; // Destination buffer
    char filename[50];
    int user_id = 123;
    int file_number = 5;
    int chars_written;

    // Format a string into the buffer
    chars_written = sprintf(buffer, "User ID: %d logged in.", user_id);

    // Check for potential errors (though sprintf doesn't report overflow)
    if (chars_written < 0) {
        perror("sprintf failed");
        exit(1);
    }

    printf("Buffer content: \"%s\"\n", buffer);
    printf("Characters written (excluding null): %d\n", chars_written);

    // Create a filename dynamically
    sprintf(filename, "data_%03d.txt", file_number); // e.g., "data_005.txt"
    printf("Generated filename: %s\n", filename);

    // Example of potential overflow (DANGEROUS)
    char small_buffer[10];
    // This will write past the end of small_buffer!
    // sprintf(small_buffer, "This is a very long string %d", 12345);
    // printf("Small buffer content (BAD): %s\n", small_buffer); // Undefined Behavior

    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file required)
- [[printf]] (Prints to stdout)
- [[snprintf_C]] (Safer version that prevents buffer overflows by limiting output size)
- [[fprintf_C]] (Prints to a file stream)
- [[String_in_C]] (Operates on C strings)
- [[Format_Specifiers_C]] (Controls formatting)
- [[Variable_Length_Parameter_List_C]], [[stdarg_macros_C]] (Handles variable arguments)
- [[Buffer_Overflow_C]] (Major risk associated with `sprintf`)

## Notes
>[!danger] Buffer Overflow Risk
> `sprintf` is notoriously unsafe because it performs **no bounds checking**. If the formatted output string (including the null terminator) is longer than the destination buffer `str` can hold, `sprintf` will write past the end of the buffer, causing a [[Buffer_Overflow_C|buffer overflow]]. This can overwrite adjacent memory, leading to crashes, incorrect behavior, and serious security vulnerabilities.
> **Use [[snprintf_C]] instead whenever possible.** `snprintf` takes an additional argument specifying the maximum number of bytes (including the null terminator) to write to the buffer, preventing overflows.

---
**Source:** Worksheet C_WS3