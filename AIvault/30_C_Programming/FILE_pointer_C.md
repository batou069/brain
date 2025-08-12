---
tags: [c, concept, io, stream, file, stdio, pointer, type]
aliases: [FILE*, C File Pointer, File Handle C, Stream Pointer C]
related:
  - "[[stdio_h_C]]"
  - "[[stdin_stdout_stderr_C]]"
  - "[[fopen]]"
  - "[[fclose]]"
  - "[[fread]]"
  - "[[fwrite]]"
  - "[[fprintf_C]]"
  - "[[fscanf_C]]"
  - "[[fgets]]"
  - "[[fputs]]"
  - "[[fseek]]"
  - "[[ftell]]"
  - "[[fflush]]"
  - "[[File_Handling_C]]"
worksheet: [C_WS5]
header_file: <stdio.h> (defines the FILE type)
date_created: 2025-04-12
---
# `FILE *` (File Pointer) (C)

## Definition

`FILE *` (pronounced "file pointer" or "file star") is a pointer type defined in `<stdio.h>`. A `FILE *` variable points to an object of type `FILE`, which is an opaque structure (its internal details are hidden) maintained by the C standard library. This `FILE` object holds all the necessary information to manage a **stream**, including its buffering details, current position, error indicators, end-of-file status, and connection to the actual file or device. It acts as a handle for performing buffered I/O operations.

## Key Aspects / Characteristics

- **Stream Handle:** Represents an open stream, which could be connected to a disk file, the console ([[stdin_stdout_stderr_C]]), a pipe, or another device.
- **Buffered I/O:** The standard I/O library (`<stdio.h>`) functions operating on `FILE *` streams typically perform buffered I/O for efficiency. Data is read/written in larger chunks to/from an internal buffer associated with the `FILE` object.
- **Obtained via `fopen`:** Typically obtained by calling [[fopen]] to open a file. `fopen` returns a `FILE *` on success or `NULL` on failure.
- **Standard Streams:** The standard streams [[stdin_stdout_stderr_C|`stdin`, `stdout`, and `stderr`]] are pre-defined macros of type `FILE *`.
- **Used by stdio Functions:** Passed as an argument to most functions in `<stdio.h>` to specify which stream to operate on (e.g., [[fprintf_C]], [[fscanf_C]], [[fgets]], [[fputs]], [[fread]], [[fwrite]], [[fseek]], [[ftell]], [[fclose]]).
- **Must Be Closed:** Streams opened with `fopen` **must** be closed using [[fclose]] when no longer needed. This flushes any remaining buffered data, releases system resources associated with the stream, and breaks the connection to the file. Failure to close files can lead to data loss or resource exhaustion.
- **Opaque Type:** The internal structure of `FILE` is implementation-defined and should not be accessed directly by user code. Interaction happens solely through the `FILE *` pointer and the standard library functions.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h> // For exit()

int main() {
    FILE *input_file = NULL; // Initialize FILE pointer to NULL
    FILE *output_file = NULL;
    char buffer[256];

    // --- Writing to a file ---
    // Open file for writing ("w" mode)
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        perror("Error opening output.txt for writing");
        return 1;
    }
    printf("output.txt opened successfully for writing.\n");

    // Write formatted data using fprintf
    fprintf(output_file, "This is line 1.\n");
    fprintf(output_file, "Value: %d\n", 42);

    // Close the output file (flushes buffer)
    if (fclose(output_file) != 0) {
        perror("Error closing output.txt");
        // Continue if possible, but log error
    }
    output_file = NULL; // Good practice
    printf("output.txt closed.\n");


    // --- Reading from a file ---
    // Open file for reading ("r" mode)
    input_file = fopen("output.txt", "r");
    if (input_file == NULL) {
        perror("Error opening output.txt for reading");
        return 1;
    }
     printf("\noutput.txt opened successfully for reading.\n");

    // Read line by line using fgets
    printf("Contents of output.txt:\n");
    while (fgets(buffer, sizeof(buffer), input_file) != NULL) {
        printf("  Read: %s", buffer); // fgets includes newline if it fits
    }

    // Check if loop ended due to error or EOF
    if (ferror(input_file)) {
        perror("Error reading from input file");
    } else if (feof(input_file)) {
        printf("End of file reached.\n");
    }

    // Close the input file
    if (fclose(input_file) != 0) {
         perror("Error closing input file");
    }
    input_file = NULL;
    printf("Input file closed.\n");

    return 0;
}
```

## Related Concepts
- [[stdio_h_C]] (Defines `FILE` type and related functions)
- [[File_Handling_C]] (Overall topic)
- Stream (The abstract concept represented by `FILE *`)
- [[fopen]], [[fclose]] (Functions to open/close streams)
- [[fread]], [[fwrite]], [[fprintf_C]], [[fscanf_C]], [[fgets]], [[fputs]], etc. (Functions operating on `FILE *`)
- [[stdin_stdout_stderr_C]] (Standard streams of type `FILE *`)
- Buffering (Key feature of stdio streams)
- File Descriptors (Lower-level OS concept, often wrapped by `FILE` structure)

## Questions / Further Study
>[!question] What is the difference between `fopen()` and `open()`? What is the difference between what they return? (WS5)
> - **`fopen()` (`<stdio.h>`):**
>     - Part of the C Standard Library (stdio).
>     - Operates on **streams** (buffered I/O).
>     - Returns a **`FILE *`** pointer (a pointer to the library's internal stream management structure) on success, or `NULL` on failure.
>     - Provides higher-level, portable, buffered file access. Easier to use for formatted I/O ([[fprintf_C]], [[fscanf_C]]).
> - **`open()` (`<fcntl.h>`, `<sys/stat.h>`, `<sys/types.h>` - POSIX/Unix):**
>     - A lower-level **system call** provided directly by the operating system (on POSIX-compliant systems).
>     - Operates on **file descriptors** (unbuffered I/O by default, unless managed manually).
>     - Returns an **`int`** (a small, non-negative integer representing the file descriptor) on success, or `-1` on failure (setting `errno`).
>     - Provides lower-level, often unbuffered, less portable access. Used when finer control over file flags, modes, or low-level I/O is needed (e.g., device control, non-blocking I/O). Functions like `read()`, `write()`, `close()` (note the different `close`) operate on file descriptors.

---
**Source:** Worksheet C_WS5