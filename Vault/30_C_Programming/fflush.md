---
tags: [c, function, stdio, io, file, stream, buffer]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[fclose]]"
  - "[[printf]]"
  - "[[fprintf_C]]"
  - "[[fwrite]]"
  - "[[stdout_stdout_stderr_C]]"
  - "[[Buffering_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fflush() `

## Purpose

The `fflush()` function forces a write of any buffered data for the specified output stream ([[FILE_pointer_C]]) to the underlying file or device. It is used to ensure that output becomes visible or is written to disk immediately, rather than waiting for the buffer to fill or the stream to be closed.

## Signature

```c
#include <stdio.h>
int fflush(FILE *stream);
```

## Parameters

-   `stream`: The `FILE *` pointer identifying the output stream or update stream (e.g., opened with `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`) whose buffer should be flushed.
    -   If `stream` is `NULL`, `fflush` attempts to flush the buffers of **all** open output streams.

## Return Value

-   Returns `0` on success.
-   Returns `EOF` (usually -1) on failure (e.g., a write error occurs while flushing) and sets the error indicator for the stream (`ferror()`).

## Key Aspects

-   **Buffer Flushing:** Explicitly forces the contents of the standard I/O output buffer associated with the `stream` to be written to the host environment (e.g., disk file, terminal).
-   **Output Streams Only (Standard C):** According to the C standard, the behavior of `fflush` on an *input* stream is undefined. However, some implementations (notably POSIX systems) extend `fflush` to discard buffered input when called on an input stream, but this is **not portable**.
-   **Use Cases:**
    -   Ensuring critical data (like logs or prompts) is written immediately, especially before a potential program crash or long delay.
    -   Ensuring output appears on the console before waiting for input when `stdout` is line-buffered or fully buffered (e.g., `printf("Enter value: "); fflush(stdout); scanf("%d", &val);`).
    -   Controlling interaction when output is piped to another program.
-   **`fclose` Implies Flush:** [[fclose]] automatically calls `fflush` before closing the stream.
-   **`stderr` Buffering:** [[stdout_stdout_stderr_C|`stderr`]] is often unbuffered or line-buffered, so `fflush(stderr)` is less commonly needed than `fflush(stdout)`.

## Example Usage

```c
#include <stdio.h>
#include <unistd.h> // For sleep() on POSIX systems

int main() {
    // Example 1: Flushing stdout before a delay or input
    printf("Processing step 1...");
    fflush(stdout); // Ensure this message appears immediately
    sleep(2);       // Simulate a delay
    printf(" Done.\n"); // This might appear later without the flush

    // Example 2: Flushing a file stream
    FILE *log_file = fopen("activity.log", "a"); // Append mode
    if (log_file == NULL) {
        perror("fopen failed");
        return 1;
    }

    fprintf(log_file, "Critical event started.\n");
    fflush(log_file); // Ensure log entry is written immediately to disk
    // ... potentially risky operation ...
    fprintf(log_file, "Critical event finished.\n");
    // fclose will flush again, but the explicit flush ensures the first message is saved
    // even if the program crashes during the risky operation.

    if (fclose(log_file) != 0) {
        perror("fclose failed");
    }

    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The stream to flush)
- [[Buffering_C]] (The mechanism `fflush` interacts with - *to be created*)
- [[fclose]] (Implicitly flushes)
- [[printf]], [[fprintf_C]], [[fwrite]], [[putchar_C]], [[puts_C]] (Functions whose output might be buffered)
- [[stdout_stdout_stderr_C]] (Common streams to flush)

---
**Source:** Worksheet C_WS5