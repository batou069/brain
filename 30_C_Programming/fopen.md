---
tags: [c, function, stdio, io, file, stream]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[fclose]]"
  - "[[File_Handling_C]]"
  - "[[File_Modes_C]]"
  - "[[open_syscall_C]]"
worksheet: [C_WS5]
header_file: <stdio.h>
date_created: 2025-04-12
---
# ` fopen() `

## Purpose

The `fopen()` (file open) function opens a file specified by a filename and associates a **stream** ([[FILE_pointer_C]]) with it. It returns a pointer to a `FILE` object that can be used in subsequent standard I/O operations (like [[fread]], [[fwrite]], [[fprintf_C]], [[fscanf_C]], [[fgets]], etc.).

## Signature

```c
#include <stdio.h>
FILE *fopen(const char * restrict filename, const char * restrict mode);```

## Parameters

-   `filename`: A C string containing the name (and potentially path) of the file to be opened.
-   `mode`: A C string specifying the access mode in which the file should be opened. See [[File_Modes_C]]. Common modes include:
    -   `"r"`: Open for reading (file must exist).
    -   `"w"`: Open for writing (creates file if it doesn't exist, truncates to zero length if it does).
    -   `"a"`: Open for appending (writing at the end of the file; creates file if it doesn't exist).
    -   `"r+"`: Open for reading and writing (file must exist).
    -   `"w+"`: Open for reading and writing (creates/truncates file).
    -   `"a+"`: Open for reading and appending (creates file).
    -   Append `b` for binary mode (e.g., `"rb"`, `"wb"`). On POSIX systems, `b` is often ignored, but it's crucial on systems like Windows that differentiate text and binary files.

## Return Value

-   On **success**, returns a `FILE *` pointer associated with the opened stream.
-   On **failure** (e.g., file not found in `"r"` mode, permission denied), returns `NULL` and sets the global `errno` variable (from `<errno.h>`) to indicate the error. `perror()` or `strerror()` can be used to print a descriptive error message based on `errno`.

## Example Usage

```c
#include <stdio.h>
#include <stdlib.h> // For exit()
#include <errno.h>  // For errno

int main() {
    FILE *outfile = NULL;
    FILE *infile = NULL;

    // --- Open for writing ---
    outfile = fopen("mydata.txt", "w"); // Try to open/create for writing
    if (outfile == NULL) {
        perror("Error opening mydata.txt for writing"); // Print error based on errno
        exit(1);
    }
    printf("mydata.txt opened for writing.\n");
    fprintf(outfile, "Data line 1.\n");
    fclose(outfile); // Close the file
    outfile = NULL;
    printf("mydata.txt closed.\n");

    // --- Open for reading ---
    infile = fopen("mydata.txt", "r"); // Try to open for reading
    if (infile == NULL) {
        perror("Error opening mydata.txt for reading");
        exit(1);
    }
     printf("mydata.txt opened for reading.\n");
     // ... read from infile using fgets, fscanf, etc. ...
     fclose(infile);
     infile = NULL;
     printf("mydata.txt closed.\n");

     // --- Attempt to open non-existent file for reading ---
     infile = fopen("nonexistent.txt", "r");
     if (infile == NULL) {
         perror("Expected error opening nonexistent.txt"); // Should print "No such file or directory"
         // errno is set here
     } else {
         printf("Unexpectedly opened nonexistent file?\n");
         fclose(infile);
     }


    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file)
- [[FILE_pointer_C]] (The return type, represents the stream)
- [[fclose]] (Essential counterpart to close the file)
- [[File_Handling_C]] (General topic)
- [[File_Modes_C]] (The `mode` string options - *to be created*)
- `errno`, `perror()`, `strerror()` (Error handling mechanisms)
- [[open_syscall_C]] (Lower-level system call alternative - *to be created*)

## Notes
>[!warning] Error Checking
> **Always** check the return value of `fopen()` against `NULL`. Failure to open a file is common, and proceeding with a `NULL` file pointer will lead to crashes when passed to other stdio functions. Use `perror()` or `strerror(errno)` to get meaningful error messages.

>[!warning] Closing Files
> Files opened with `fopen()` **must** be closed with [[fclose]] to ensure data buffers are flushed to disk and system resources are released.

---
**Source:** Worksheet C_WS5