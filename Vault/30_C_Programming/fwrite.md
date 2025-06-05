---
tags: [c, function, stdio, io, file, stream, output, binary]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[fclose]]"
  - "[[fread]]"
  - "[[fseek]]"
  - "[[File_Handling_C]]"
  - "[[sizeof_operator_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fwrite() `

## Purpose

The `fwrite()` (file write) function writes blocks of binary data from a buffer in memory to a given output stream ([[FILE_pointer_C]]). It is designed for writing a specified number of items, each of a specified size.

## Signature

```c
#include <stdio.h>
size_t fwrite(const void * restrict ptr, size_t size, size_t nmemb, FILE * restrict stream);
```

## Parameters

-   `ptr`: A pointer (`const void*`) to the block of memory (buffer) containing the data to be written.
-   `size`: The size, in bytes, of each individual element to be written. Often calculated using [[sizeof_operator_C]].
-   `nmemb`: The number of elements (each of size `size`) to write to the stream. The total number of bytes written will be `(size * nmemb)`.
-   `stream`: The `FILE *` pointer identifying the output stream to write to (previously opened with [[fopen]] in a write or append mode, e.g., `"w"`, `"wb"`, `"a"`, `"ab"`).

## Return Value

-   Returns the **number of elements** (`nmemb`) successfully written.
-   This value may be less than `nmemb` only if a write error occurs.
-   If `size` or `nmemb` is 0, `fwrite` returns 0 and the stream state remains unchanged.
-   If an error occurs, the error indicator for the stream is set, which can be checked using `ferror()`.

## Key Aspects

-   **Binary Data:** Primarily intended for writing binary data (like raw bytes, structs, arrays of numbers) rather than formatted text (for which [[fprintf_C]] or [[fputs]] are often better).
-   **Block Writing:** Writes data in chunks defined by `size` and `nmemb`.
-   **Buffer:** Requires the caller to provide the memory buffer (`ptr`) containing the data to write.
-   **File Position:** Writes data starting at the current file position indicator for the stream, and advances the indicator by the number of bytes successfully written.
-   **Error Handling:** The return value indicates the number of *full elements* written. Check `ferror()` to determine if a short write was caused by an error.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    double value;
} Record;

int main() {
    FILE *outfile = fopen("records.dat", "wb"); // Open in binary write mode
    if (outfile == NULL) {
        perror("Error opening records.dat");
        return 1;
    }

    Record records_to_write[3] = {
        {101, 12.34},
        {102, 56.78},
        {103, 90.12}
    };
    size_t num_records = 3;
    size_t records_written;

    // Attempt to write 3 records (each of size sizeof(Record))
    records_written = fwrite(records_to_write, sizeof(Record), num_records, outfile);

    printf("Attempted to write %zu records, successfully wrote: %zu\n", num_records, records_written);

    // Check for errors if not all records were written
    if (records_written < num_records) {
        if (ferror(outfile)) {
            perror("Error writing file");
        } else {
            // This case is less common for fwrite unless disk full etc.
            printf("Unexpected short write without error flag.\n");
        }
    }

    // It's crucial to close the file to ensure buffers are flushed
    if (fclose(outfile) != 0) {
        perror("Error closing file");
    } else {
        printf("File closed successfully.\n");
    }

    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The output stream)
- [[fread]] (The corresponding binary read function)
- [[fopen]], [[fclose]] (Opening and closing the stream)
- [[File_Handling_C]] (General topic)
- [[sizeof_operator_C]] (Used to determine element `size`)
- `ferror()` (Function to check stream error status)
- [[fprintf_C]], [[fputs]] (Alternatives for writing text)
- Binary vs Text Files

---
**Source:** Worksheet C_WS5