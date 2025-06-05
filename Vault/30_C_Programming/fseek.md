---
tags: [c, function, stdio, io, file, stream, position]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[ftell]]"
  - "[[rewind_C]]"
  - "[[fgetpos_C]]"
  - "[[fsetpos_C]]"
  - "[[File_Handling_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fseek() `

## Purpose

The `fseek()` function sets the file position indicator for the specified stream ([[FILE_pointer_C]]). This allows you to move to a specific location within the file before the next read or write operation (random access).

## Signature

```c
#include <stdio.h>
int fseek(FILE *stream, long int offset, int whence);
```

## Parameters

-   `stream`: The `FILE *` pointer identifying the stream.
-   `offset`: A `long int` value representing the number of bytes to offset the file position indicator. Can be positive (move forward) or negative (move backward).
-   `whence`: An integer specifying the position from which the `offset` is calculated. It must be one of the following macros (defined in `<stdio.h>`):
    -   `SEEK_SET`: Beginning of the file. The new position is `offset` bytes from the start. `offset` must be non-negative.
    -   `SEEK_CUR`: Current file position. The new position is the current position plus `offset` bytes.
    -   `SEEK_END`: End of the file. The new position is the end-of-file position plus `offset` bytes. `offset` is usually negative or zero when using `SEEK_END`.

## Return Value

-   Returns `0` on success.
-   Returns a non-zero value on failure (e.g., attempting to seek on a non-seekable device like a terminal, or seeking beyond file boundaries in some cases).

## Key Aspects

-   **Random Access:** Enables non-sequential access to file contents.
-   **Positioning:** Sets the location for the *next* read or write operation.
-   **Clears EOF:** A successful call to `fseek()` clears the end-of-file indicator (`feof()`) for the stream.
-   **Mode Interaction:** If the stream was opened in append mode (`"a"` or `"a+"`), subsequent writes will still occur at the end of the file, regardless of `fseek` calls. However, `fseek` can still position for reads in `"a+"` mode.
-   **Binary vs. Text Streams:** While `fseek` works on both, its behavior with `SEEK_END` or non-zero offsets relative to `SEEK_CUR` or `SEEK_END` might be unreliable or non-portable on text streams due to potential character encoding or line ending translations. It's generally safer and more predictable on binary streams (`"rb"`, `"wb"`, etc.). For text streams, using `fseek(stream, 0, SEEK_SET)` (rewind), `fseek(stream, 0, SEEK_END)` (go to end, usually for finding size with `ftell`), or offsets previously obtained from `ftell` with `SEEK_SET` are the most portable uses.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("test.txt", "w+"); // Open for reading and writing, create/truncate
    if (fp == NULL) {
        perror("fopen failed");
        return 1;
    }

    // Write some data
    fprintf(fp, "Line 1\nLine 2\nLine 3\n");
    long pos_after_write = ftell(fp); // Get current position
    printf("Position after writing: %ld\n", pos_after_write);

    // --- Using fseek ---

    // 1. Go back to the beginning (SEEK_SET)
    if (fseek(fp, 0, SEEK_SET) != 0) {
        perror("fseek to SEEK_SET failed");
    } else {
        printf("Seeked to beginning.\n");
        // Read the first character
        int c = fgetc(fp);
        printf("First char: %c\n", (char)c);
    }

    // 2. Go to a specific offset from the beginning
    long offset = 7; // Position after "Line 1\n"
    if (fseek(fp, offset, SEEK_SET) != 0) {
         perror("fseek to offset failed");
    } else {
        printf("Seeked to offset %ld from beginning.\n", offset);
        // Read the next character (should be 'L' of Line 2)
        int c = fgetc(fp);
        printf("Char at offset %ld: %c\n", offset, (char)c);
    }

    // 3. Go back 5 characters from the current position (SEEK_CUR)
    if (fseek(fp, -5, SEEK_CUR) != 0) { // Current pos is 8, move to 3
         perror("fseek with SEEK_CUR failed");
    } else {
        long current_pos = ftell(fp);
        printf("Seeked back 5 chars. Current pos: %ld\n", current_pos); // Should be 3
        int c = fgetc(fp);
        printf("Char at new pos: %c\n", (char)c); // Should be 'e' of "Line 1"
    }

    // 4. Go to the end of the file (SEEK_END)
     if (fseek(fp, 0, SEEK_END) != 0) {
         perror("fseek to SEEK_END failed");
    } else {
        long end_pos = ftell(fp); // Get file size
        printf("Seeked to end. File size: %ld\n", end_pos);
        // Trying to read here would result in EOF
    }

    fclose(fp);
    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The stream to operate on)
- [[ftell]] (Gets the current file position)
- [[rewind_C]] (Equivalent to `fseek(stream, 0L, SEEK_SET)` plus error clearing - *to be created*)
- [[fgetpos_C]], [[fsetpos_C]] (Alternative functions for getting/setting position, handle larger files better - *to be created*)
- [[File_Handling_C]], Random Access
- `SEEK_SET`, `SEEK_CUR`, `SEEK_END` (Macros for `whence`)

---
**Source:** Worksheet C_WS5