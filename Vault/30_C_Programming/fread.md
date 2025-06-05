---
tags: [c, function, stdio, io, file, stream, input, binary]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fopen]]"
  - "[[fclose]]"
  - "[[fwrite]]"
  - "[[fseek]]"
  - "[[File_Handling_C]]"
  - "[[sizeof_operator_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fread() `

## Purpose

The `fread()` (file read) function reads blocks of binary data from a given input stream ([[FILE_pointer_C]]) into a buffer in memory. It is designed for reading a specified number of items, each of a specified size.

## Signature

```c
#include <stdio.h>
size_t fread(void * restrict ptr, size_t size, size_t nmemb, FILE * restrict stream);
```

## Parameters

-   `ptr`: A pointer (`void*`) to a block of memory (buffer) large enough to hold the data being read. The buffer must have a size of at least `(size * nmemb)` bytes.
-   `size`: The size, in bytes, of each individual element to be read. Often calculated using [[sizeof_operator_C]].
-   `nmemb`: The maximum number of elements (each of size `size`) to read from the stream.
-   `stream`: The `FILE *` pointer identifying the input stream to read from (previously opened with [[fopen]] in a read mode, e.g., `"r"`, `"rb"`, `"r+"`).

## Return Value

-   Returns the **number of elements** (`nmemb`) successfully read.
-   This value may be less than `nmemb` if an end-of-file condition is reached or a read error occurs before `nmemb` elements could be read.
-   If `size` or `nmemb` is 0, `fread` returns 0 and the buffer content and stream state remain unchanged.
-   To distinguish between end-of-file and a read error after a short read (return value < `nmemb`), you must use `feof()` and `ferror()` on the `stream`.

## Key Aspects

-   **Binary Data:** Primarily intended for reading binary data (like raw bytes, structs, arrays of numbers) rather than text lines (for which [[fgets]] is often better).
-   **Block Reading:** Reads data in chunks defined by `size` and `nmemb`.
-   **Buffer:** Requires the caller to provide a sufficiently large memory buffer (`ptr`).
-   **File Position:** Reads data starting from the current file position indicator for the stream, and advances the indicator by the number of bytes successfully read.
-   **Error/EOF Handling:** The return value indicates the number of *full elements* read. Check `feof()` and `ferror()` to determine the cause of a short read.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    double value;
} Record;

int main() {
    FILE *infile = fopen("records.dat", "rb"); // Open in binary read mode
    if (infile == NULL) {
        perror("Error opening records.dat");
        return 1;
    }

    Record records_buffer[10]; // Buffer to hold up to 10 records
    size_t records_read;

    // Attempt to read 10 records (each of size sizeof(Record))
    records_read = fread(records_buffer, sizeof(Record), 10, infile);

    printf("Attempted to read 10 records, successfully read: %zu\n", records_read);

    // Process the records that were actually read
    for (size_t i = 0; i < records_read; ++i) {
        printf("Record %zu: ID=%d, Value=%.2f\n", i, records_buffer[i].id, records_buffer[i].value);
    }

    // Check for errors or EOF if not all records were read
    if (records_read < 10) {
        if (feof(infile)) {
            printf("End of file reached.\n");
        } else if (ferror(infile)) {
            perror("Error reading file");
        }
    }

    fclose(infile);

    return 0;
}
// Assumes records.dat was previously created (e.g., using fwrite)
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The input stream)
- [[fwrite]] (The corresponding binary write function)
- [[fopen]], [[fclose]] (Opening and closing the stream)
- [[File_Handling_C]] (General topic)
- [[sizeof_operator_C]] (Used to determine element `size`)
- `feof()`, `ferror()` (Functions to check stream status after read)
- [[fgets]] (Alternative for reading text lines)
- Binary vs Text Files

---
**Source:** Worksheet C_WS5