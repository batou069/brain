---
tags:
  - c
  - concept
  - os
  - process
  - execution
aliases:
  - C Environment Variables
related:
  - "[[Process]]"
  - "[[Operating_System]]"
  - "[[Shell]]"
  - "[[main_Function_C]]"
  - "[[envp_C]]"
  - "[[getenv_C]]"
  - "[[setenv_C]]"
  - "[[putenv_C]]"
worksheet:
  - C_WS4
date_created: 2025-04-12
---
# Environment Variables (C Access)

## Definition

**Environment Variables** are a set of dynamic named values, maintained by the [[Operating_System]], that can affect the way running [[Process|processes]] behave. They are part of the environment inherited by a child process from its parent ([[Shell]] or another program). C programs can access these variables to get configuration information, paths, user settings, etc.

## Key Aspects / Characteristics

- **Key-Value Pairs:** Consist of a name (string) and a value (string), e.g., `PATH=/usr/bin:/bin`, `HOME=/home/user`.
- **Inheritance:** Child processes usually inherit a copy of the environment variables from their parent process.
- **OS Managed:** Set and managed by the operating system shell or through system settings.
- **Configuration:** Often used to configure program behavior without changing code (e.g., setting `TEMP` directory, `LANG` for locale, `PATH` for finding executables).
- **Access in C:**
    - **`getenv()` (`<stdlib.h>`):** The standard and portable way to *read* the value of a specific environment variable. Returns a pointer to the value string, or `NULL` if the variable is not defined. See [[getenv_C]].
    - **`main`'s `envp` parameter:** A non-standard but common extension (especially on POSIX systems) allows `main` to be declared as `int main(int argc, char *argv[], char *envp[])`. `envp` is a NULL-terminated array of strings, where each string is of the form `"NAME=value"`. See [[envp_C]]. This provides access to the *initial* environment when the program started.
    - **`extern char **environ;`:** POSIX systems also typically provide an external global variable `environ` (declared via `<unistd.h>`) which points to the NULL-terminated array of environment strings. This pointer can change if the environment is modified during runtime (e.g., via `putenv`/`setenv`).
- **Modification in C (Use with Caution):**
    - **`putenv()` (`<stdlib.h>`):** Adds or changes an environment variable. Takes a string argument of the form `"NAME=value"`. *Caution:* The string passed becomes part of the environment; it should not be modified or deallocated afterwards if it was dynamically allocated. See [[putenv_C]].
    - **`setenv()` (`<stdlib.h>` - POSIX):** Adds or changes an environment variable. Takes separate name and value strings, and an overwrite flag. Generally safer than `putenv` as it copies the strings. See [[setenv_C]].
    - **`unsetenv()` (`<stdlib.h>` - POSIX):** Removes an environment variable.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h> // For getenv, setenv, putenv (setenv/putenv might need _POSIX_C_SOURCE)
#include <string.h> // For demonstration only (putenv)

// To access environ, uncomment the next line (POSIX)
// #include <unistd.h>
// extern char **environ;

// Using optional third argument envp (Common extension)
int main(int argc, char *argv[], char *envp[]) {
    // 1. Using getenv (Recommended way to read)
    char *path_var = getenv("PATH");
    if (path_var != NULL) {
        printf("PATH using getenv:\n%s\n\n", path_var);
    } else {
        printf("PATH environment variable not found.\n");
    }

    char *user_var = getenv("USER"); // Or "USERNAME" on Windows
     if (user_var != NULL) {
        printf("USER using getenv: %s\n\n", user_var);
    }

    // 2. Using envp (Access initial environment)
    printf("Environment variables from envp:\n");
    for (int i = 0; envp[i] != NULL; ++i) {
        // Print first few variables for brevity
        if (i < 5) {
             printf("  %s\n", envp[i]);
        } else if (i == 5) {
             printf("  ...\n");
        }
    }
    printf("\n");

    /* // 3. Using extern environ (POSIX)
    printf("Environment variables from environ:\n");
    for (char **env = environ; *env != NULL; ++env) {
        // Print first few variables for brevity
        static int count = 0;
        if (count < 5) {
             printf("  %s\n", *env);
        } else if (count == 5) {
             printf("  ...\n");
        }
        count++;
    }
    printf("\n");
    */

    // 4. Modifying environment (Example - affects child processes)
    // Using setenv (safer, POSIX)
    if (setenv("MY_VAR", "my_value", 1) == 0) { // Name, Value, Overwrite=1
         printf("Set MY_VAR=my_value using setenv.\n");
         printf("MY_VAR is now: %s\n", getenv("MY_VAR"));
    } else {
         perror("setenv failed");
    }

    // Using putenv (less safe)
    // Need a string that persists - static or allocated
    static char putenv_str[] = "ANOTHER_VAR=another_value";
    if (putenv(putenv_str) == 0) {
         printf("Set ANOTHER_VAR using putenv.\n");
         printf("ANOTHER_VAR is now: %s\n", getenv("ANOTHER_VAR"));
    } else {
         perror("putenv failed");
    }


    return 0;
}
```

## Related Concepts
- [[Process]] (Environment is associated with a process)
- [[Operating_System]], [[Shell]] (Manage and set environment variables)
- [[main_Function_C]] (Can receive `envp`)
- [[envp_C]] (The `main` argument)
- [[getenv_C]], [[setenv_C]], [[putenv_C]], `unsetenv` (Library functions)
- Configuration Management

---
**Source:** Worksheet C_WS4