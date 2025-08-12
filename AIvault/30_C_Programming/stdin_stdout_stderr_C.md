---
tags:
  - c
  - concept
  - io
  - stream
  - file
  - stdio
aliases:
  - Standard Streams C
  - stdin
  - stdout
  - stderr
related:
  - "[[stdio_h_C]]"
  - "[[FILE_pointer_C]]"
  - "[[printf]]"
  - "[[scanf]]"
  - "[[fprintf_C]]"
  - "[[fscanf_C]]"
  - "[[getchar_C]]"
  - "[[putchar_C]]"
  - "[[Operating_System]]"
  - "[[Shell]]"
  - "[[Redirection_C]]"
worksheet:
  - C_WS5
header_file: <stdio.h> (defines the macros)
date_created: 2025-04-12
---
# Standard Streams (`stdin`, `stdout`, `stderr`) (C)

## Definition

In C programming (and generally in Unix-like operating systems), **Standard Streams** are pre-connected input and output communication channels between a program and its environment (usually the terminal or [[Shell]] that launched it). The C standard library defines three standard streams, accessible via macros declared in `<stdio.h>`:

1.  **`stdin` (Standard Input):** The default source for input data for a program. By default, it's connected to the keyboard. Functions like [[scanf]], [[getchar_C]], [[fgets]] read from `stdin` by default or when passed `stdin`.
2.  **`stdout` (Standard Output):** The default destination for normal output data from a program. By default, it's connected to the terminal display. Functions like [[printf]], [[putchar_C]], [[puts_C]] write to `stdout` by default or when passed `stdout`.
3.  **`stderr` (Standard Error):** The default destination for error messages and diagnostic output from a program. By default, it's also connected to the terminal display, but it's a separate stream from `stdout`. This allows redirection of normal output (`stdout`) without hiding error messages (`stderr`). [[fprintf_C]] is often used to write specifically to `stderr`.

## Key Aspects / Characteristics

- **Pre-defined:** Available automatically when a C program starts; no need to open them explicitly.
- **`FILE *` Type:** `stdin`, `stdout`, and `stderr` are macros that expand to expressions of type `FILE *` ([[FILE_pointer_C]]). They can be used with any standard I/O function that accepts a `FILE *` argument (e.g., `fprintf(stdout, ...)` is equivalent to `printf(...)`).
- **Buffering:** `stdout` is typically *line-buffered* when connected to a terminal (output is sent when a newline `\n` is encountered or the buffer fills) and *fully buffered* when redirected to a file (output is sent only when the buffer fills). `stderr` is typically *unbuffered* or *line-buffered* to ensure error messages appear promptly, even if the program crashes. `stdin` is also typically buffered. [[fflush]] can be used to force writing of buffered output.
- **Redirection:** The [[Operating_System]] [[Shell]] allows users to redirect these streams when launching a program:
    - `< input.txt`: Redirects `stdin` to read from `input.txt`.
    - `> output.txt`: Redirects `stdout` to write to `output.txt` (overwriting).
    - `>> output.txt`: Redirects `stdout` to append to `output.txt`.
    - `2> error.log`: Redirects `stderr` (file descriptor 2) to `error.log`.
    - `&> combined.log`: Redirects both `stdout` and `stderr` (shell-specific).
- **Pipes:** Output of one command (`stdout`) can be piped (`|`) to the input (`stdin`) of another command.

## Examples / Use Cases

```c
#include <stdio.h>

int main() {
    int age;
    char name[50];

    // Reading from stdin (default for scanf)
    printf("Enter name: ");
    // Safer input reading than scanf("%s", name);
    if (fgets(name, sizeof(name), stdin) != NULL) {
         // Remove trailing newline if present
         name[strcspn(name, "\n")] = 0; // Needs <string.h>
    } else {
         fprintf(stderr, "Error reading name from stdin.\n");
         return 1;
    }


    printf("Enter age: ");
    if (scanf("%d", &age) != 1) {
        // Writing error message to stderr
        fprintf(stderr, "Invalid input for age.\n");
        return 1;
    }

    // Writing normal output to stdout (default for printf)
    printf("\n--- User Info ---\n");
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);

    // Explicitly writing to stdout and stderr using fprintf
    fprintf(stdout, "Processing complete.\n");
    // fprintf(stderr, "Warning: Low disk space (example error).\n");


    return 0;
}
```
**Shell Usage Examples:**
```bash
gcc main.c -o main
./main                 # Reads from keyboard, writes to terminal
./main < input.dat     # Reads name/age from input.dat, writes output/errors to terminal
./main > output.log    # Reads from keyboard, writes normal output to output.log, errors to terminal
./main 2> errors.log   # Reads from keyboard, writes normal output to terminal, errors to errors.log
./main < in.txt > out.log 2> err.log # Reads from in.txt, output to out.log, errors to err.log
```

## Related Concepts
- [[FILE_pointer_C]] (The type of `stdin`, `stdout`, `stderr`)
- [[stdio_h_C]] (Header defining the streams and I/O functions)
- [[printf]], [[scanf]], [[fgets]], [[fprintf_C]], etc. (Functions using the streams)
- [[Operating_System]], [[Shell]] (Manage streams and redirection)
- [[Redirection_C]], [[Pipe_C]] (Shell features manipulating streams - *to be created*)
- File Descriptors (Lower-level OS concept, `stdin`=0, `stdout`=1, `stderr`=2 on Unix-like systems)

---
**Source:** Worksheet C_WS5