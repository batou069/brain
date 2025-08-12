---
tags: [c, concept, function, parameter, main, execution, process]
aliases: [C main arguments, Command Line Arguments C]
related:
  - "[[main_Function_C]]"
  - "[[String_in_C]]"
  - "[[Array_C]]"
  - "[[Pointer_C]]"
  - "[[Process]]"
  - "[[Shell]]"
worksheet: [C_WS4]
date_created: 2025-04-12
---
# `argc` and `argv` (C `main` Arguments)

## Definition

`argc` (argument count) and `argv` (argument vector) are the conventional names for the parameters of the [[main_Function_C|`main` function]] when declared as `int main(int argc, char *argv[])`. They provide a standard mechanism for a C program to receive command-line arguments passed to it when it is executed by the [[Operating_System]] (often via a [[Shell]]).

## Key Aspects / Characteristics

-   **`int argc` (Argument Count):**
    -   An integer representing the total number of command-line arguments supplied to the program, *including* the name of the program itself.
    -   `argc` will always be at least 1 in a standard environment.

-   **`char *argv[]` (Argument Vector):**
    -   An array of character pointers ([[Pointer_C|pointers]] to [[String_in_C|C strings]]).
    -   `argv[0]`: Typically points to a string containing the name used to invoke the program (e.g., `./myprogram`).
    -   `argv[1]`: Points to the first command-line argument string.
    -   `argv[2]`: Points to the second command-line argument string.
    -   ...
    -   `argv[argc - 1]`: Points to the last command-line argument string.
    -   `argv[argc]`: Guaranteed by the C standard to be a null pointer (`NULL`). This provides an alternative way to iterate through the arguments without using `argc`.

-   **Parsing:** The shell or operating system is responsible for parsing the command line entered by the user (splitting it into words, handling quotes, etc.) and preparing the `argc` and `argv` values before calling the program's `main` function.
-   **Strings:** Each argument `argv[i]` is a null-terminated C string.

## Examples / Use Cases

**Program (`args_demo.c`):**
```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("argc = %d\n", argc);

    printf("argv contents (using index):\n");
    for (int i = 0; i < argc; ++i) {
        printf("  argv[%d] = %s\n", i, argv[i]);
    }

    printf("\nargv contents (using NULL terminator):\n");
    // Note: argv itself is the pointer to the first element (argv[0])
    for (char **arg_ptr = argv; *arg_ptr != NULL; ++arg_ptr) {
         printf("  Current arg: %s\n", *arg_ptr);
    }

    return 0;
}
```

**Compilation and Execution:**
```bash
gcc args_demo.c -o args_demo
./args_demo                 # No arguments
./args_demo first           # One argument
./args_demo hello world     # Two arguments
./args_demo "Argument with spaces" # One argument containing spaces
```

**Output for `./args_demo hello world`:**
```
argc = 3
argv contents (using index):
  argv[0] = ./args_demo
  argv[1] = hello
  argv[2] = world

argv contents (using NULL terminator):
  Current arg: ./args_demo
  Current arg: hello
  Current arg: world
```

## Related Concepts
- [[main_Function_C]] (Where `argc` and `argv` are parameters)
- [[String_in_C]], [[Array_C]], [[Pointer_C]] (The types involved)
- [[Process]] (Command-line arguments are passed during process creation)
- [[Shell]] (Typically parses the command line and provides `argc`/`argv`)
- [[envp_C]] (Optional third argument for environment variables)

---
**Source:** Worksheet C_WS4