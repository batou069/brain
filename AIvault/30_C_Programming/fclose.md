---
tags: [c, function, stdio, io, file, stream]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[File_Handling_C]]"
  - "[[fflush]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fclose() `

## Purpose

The `fclose()` function disassociates the named stream (specified by the [[FILE_pointer_C|`FILE *` pointer]]) from its underlying file or device. It flushes any unwritten buffered data for output streams, discards any unread buffered input, and releases system resources associated with the stream.

## Signature

```c
#include <stdio.h>
int fclose(FILE *stream);
```

## Parameters

-   `stream`: A `FILE *` pointer to the stream to be closed. This pointer must have been obtained from a previous successful call to [[fopen]] (or functions like `freopen`, `fdopen`).

## Return Value

-   On **success**, returns `0`.
-   On **failure**, returns `EOF` (a macro defined in `<stdio.h>`, usually -1) and may set `errno` to indicate the error (e.g., if a final write operation during buffer flushing fails).

## Key Aspects

-   **Resource Release:** Frees memory used for buffering and releases operating system resources (like file descriptors) associated with the stream.
-   **Buffer Flushing:** For output streams, `fclose()` ensures that any data remaining in the standard I/O buffer is written to the underlying file or device before closing. This is crucial to prevent data loss.
-   **Mandatory Call:** Every stream opened with [[fopen]] should eventually be closed with `fclose()` to prevent resource leaks and potential data loss.
-   **Closing Standard Streams:** While possible (`fclose(stdout)`), closing the standard streams ([[stdin_stdout_stderr_C]]) is generally not recommended unless you have a specific reason and understand the consequences for subsequent I/O operations in your program. The operating system typically closes them automatically on program exit.
-   **Pointer Invalidation:** After `fclose(stream)` returns successfully, the `stream` pointer is no longer valid and should not be used with any other stdio functions. It's good practice to set the pointer variable to `NULL` after closing.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("data.tmp", "w"); // Open for writing

    if (fp == NULL) {
        perror("fopen failed");
        return 1;
    }

    fprintf(fp, "Writing some data...\n");
    // Data might still be in the buffer here

    printf("Closing file...\n");
    int result = fclose(fp); // Flushes buffer and closes file

    if (result == EOF) { // Check return value for errors
        perror("fclose failed");
        // Data might be lost if flushing failed
    } else {
        printf("File closed successfully.\n");
    }

    fp = NULL; // Set pointer to NULL

    // fclose(fp); // Calling fclose on NULL is technically undefined behavior,
                 // unlike free(NULL) which is safe. Avoid this.

    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The stream handle to close)
- [[fopen]] (The function that opens the stream)
- [[File_Handling_C]] (General topic)
- [[fflush]] (Can be used to flush buffers without closing the stream)
- Resource Management, [[Memory_Leak_C]] (Closing prevents leaks)

---
**Source:** Worksheet C_WS5