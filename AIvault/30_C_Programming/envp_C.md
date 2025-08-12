---
tags: [c, concept, function, parameter, main, execution, process, environment_variables, non_standard]
aliases: [C main envp, Environment Pointer C]
related:
  - "[[main_Function_C]]"
  - "[[Environment_variables_C]]"
  - "[[String_in_C]]"
  - "[[Array_C]]"
  - "[[Pointer_C]]"
  - "[[Process]]"
  - "[[getenv_C]]"
worksheet: [C_WS4]
date_created: 2025-04-12
---
# `envp` (C `main` Argument)

## Definition

`envp` (environment pointer) is an optional, non-standard but widely supported third parameter to the [[main_Function_C|`main` function]] in C, particularly on POSIX-compliant systems (like Linux, macOS). When supported, the `main` function can be declared as `int main(int argc, char *argv[], char *envp[])`. `envp` provides access to the program's initial [[Environment_variables_C|environment variables]].

## Key Aspects / Characteristics

- **Non-Standard:** Unlike `argc` and `argv`, the `envp` parameter is not mandated by the C standard. Relying on it reduces portability compared to using [[getenv_C]] or `extern char **environ`.
- **Array of Strings:** Similar to `argv`, `envp` is a NULL-terminated array of character pointers (`char *[]`).
- **Format:** Each string in the `envp` array is of the form `"NAME=value"`, representing one environment variable.
- **Initial Environment:** `envp` typically reflects the environment variables as they were when the [[Process]] started. It might not reflect changes made later using functions like `setenv` or `putenv` (whereas `getenv` and `environ` usually do).
- **NULL Termination:** The end of the array is marked by a `NULL` pointer (`envp[last+1] == NULL`).

## Examples / Use Cases

```c
#include <stdio.h>

// Using the non-standard third argument envp
int main(int argc, char *argv[], char *envp[]) {
    printf("Listing environment variables using envp:\n");

    // Iterate until a NULL pointer is encountered
    for (int i = 0; envp[i] != NULL; ++i) {
        // Print only the first few for brevity
        if (i < 10) {
             printf("  envp[%d]: %s\n", i, envp[i]);
        } else if (i == 10) {
             printf("  ...\n");
        }
    }

    // Compare with getenv (which is standard)
    printf("\nGetting specific variable 'USER' using getenv: %s\n", getenv("USER"));

    return 0;
}
```

## Related Concepts
- [[main_Function_C]] (Where `envp` can be a parameter)
- [[Environment_variables_C]] (The data accessed via `envp`)
- [[String_in_C]], [[Array_C]], [[Pointer_C]] (The types involved)
- [[argc_argv_C]] (The standard `main` arguments)
- [[getenv_C]] (Standard, portable way to get environment variables)
- `extern char **environ` (Alternative POSIX way to access environment)

## Notes
>[!warning] Portability
> Since `envp` is not part of the C standard, its availability and behavior might vary across different compilers and operating systems. For portable code, using `getenv()` is the preferred method for accessing environment variables.

---
**Source:** Worksheet C_WS4