---
tags: [c, function, stdio, io, file, stream, position]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[fseek]]"
  - "[[rewind_C]]"
  - "[[fgetpos_C]]"
  - "[[File_Handling_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` ftell() `

## Purpose

The `ftell()` function obtains the current value of the file position indicator for the specified stream ([[FILE_pointer_C]]). For binary streams, this value represents the number of bytes from the beginning of the file. For text streams, the value might not directly correspond to byte counts due to potential line ending translations or encoding issues, but it can still be reliably used with [[fseek]] to return to the position from which the `ftell` value was obtained.

## Signature

```c
#include <stdio.h>
long int ftell(FILE *stream);
```

## Parameters

-   `stream`: The `FILE *` pointer identifying the stream.

## Return Value

-   On **success**, returns the current value of the file position indicator (as a `long int`).
-   On **failure**, returns `-1L` (a long int -1) and sets the global `errno` variable to indicate the error (e.g., if the stream is associated with a non-seekable device like a terminal).

## Key Aspects

-   **Get Current Position:** Reports the offset (usually in bytes for binary streams) from the beginning of the file where the next read or write operation will occur.
-   **Use with `fseek`:** Values returned by `ftell` can be stored and later used with [[fseek]](`stream, offset, SEEK_SET`) to return to that exact position in the file.
-   **File Size:** A common technique to find the size of a file is to `fseek(fp, 0, SEEK_END)` to go to the end and then call `ftell(fp)` to get the position (which equals the size in bytes for binary files). Remember to seek back if you need to perform further operations from a different position.
-   **Text Streams:** The value returned for text streams might not be a simple byte count. However, the standard guarantees that `fseek(stream, ftell(stream), SEEK_SET)` will work correctly, and `fseek(stream, 0L, SEEK_SET)` corresponds to the beginning.
-   **Error Checking:** Check the return value against `-1L` to detect errors.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("data.txt", "w+");
    if (fp == NULL) {
        perror("fopen failed");
        return 1;
    }

    long pos1, pos2, file_size;

    // Get position at the beginning
    pos1 = ftell(fp);
    if (pos1 == -1L) perror("ftell failed");
    else printf("Position at start: %ld\n", pos1); // Output: 0

    // Write some data
    fprintf(fp, "Hello");

    // Get position after writing
    pos2 = ftell(fp);
     if (pos2 == -1L) perror("ftell failed");
    else printf("Position after writing 'Hello': %ld\n", pos2); // Output: 5

    // Find file size
    if (fseek(fp, 0, SEEK_END) != 0) {
        perror("fseek to end failed");
    } else {
        file_size = ftell(fp);
        if (file_size == -1L) perror("ftell at end failed");
        else printf("File size: %ld\n", file_size); // Output: 5
    }

    // Seek back to pos2 using the stored value
    if (fseek(fp, pos2, SEEK_SET) != 0) {
         perror("fseek back to pos2 failed");
    } else {
        printf("Seeked back to position %ld.\n", pos2);
        // Write more data
        fprintf(fp, " World!");
    }

    fclose(fp);
    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The stream to query)
- [[fseek]] (Sets the file position; uses values from `ftell`)
- [[rewind_C]] (Resets position to the beginning)
- [[fgetpos_C]] (Alternative function to get position, potentially handles larger files better)
- [[File_Handling_C]], Random Access
- `errno` (Used for error reporting on failure)

---
**Source:** Worksheet C_WS5