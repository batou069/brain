---
tags: [c, function, stdio, io, input, variadic, pointer]
aliases: []
related:
  - "[[stdio_h_C]]"
  - "[[printf]]"
  - "[[sscanf_C]]"
  - "[[fscanf_C]]"
  - "[[stdin_stdout_stderr_C]]"
  - "[[Format_Specifiers_C]]"
  - "[[Variable_Length_Parameter_List_C]]"
  - "[[stdarg_macros_C]]"
  - "[[Pointer_C]]"
  - "[[Address_Operator_C]]"
  - "[[Pass_by_Address_C]]"
worksheet: [C_WS3]
header_file: <stdio.h>
date_created: 2025-04-11
---
# ` scanf() `

## Purpose

The `scanf()` (scan formatted) function reads formatted input from the standard input stream ([[stdin_stdout_stderr_C|`stdin`]]), which is typically the keyboard. It attempts to parse input according to specified format specifiers and stores the converted values into the memory locations pointed to by the additional arguments.

## Signature

```c
#include <stdio.h>
int scanf(const char * restrict format, ...);
```

## Parameters

-   `format`: A [[String_in_C|C string]] containing **format specifiers** (e.g., `%d`, `%lf`, `%s`, `%c`) that control how input characters are interpreted and converted. Whitespace characters in the format string generally match any amount of whitespace (including none) in the input. Other non-whitespace characters must match the input exactly.
-   `...`: (Ellipsis) Indicates a [[Variable_Length_Parameter_List_C|variable number of arguments]]. These arguments **must be pointers** to variables where the converted input values will be stored. The type of the pointer *must* match the corresponding format specifier (e.g., `%d` requires an `int*`, `%lf` requires a `double*`, `%s` requires a `char*` pointing to a sufficiently large buffer).

## Return Value

-   On **success**, returns the number of input items successfully matched and assigned. This can be fewer than the number of format specifiers if input ends or a matching failure occurs early.
-   Returns `EOF` (a macro defined in `<stdio.h>`, usually -1) if an input failure occurs *before* any successful conversion (e.g., end-of-file reached).
-   Returns `0` if the first input item fails to match the first format specifier.

## Format Specifiers (Common)

See [[Format_Specifiers_C]] for more details. Note differences from `printf` (e.g., `%f` vs `%lf`).
-   `%d`: Signed decimal integer (`int*` argument required).
-   `%ld`: Signed long integer (`long int*` argument required).
-   `%u`: Unsigned decimal integer (`unsigned int*` argument required).
-   `%f`: Floating-point number (`float*` argument required).
-   `%lf`: Double-precision floating-point number (`double*` argument required). **Note the `l` modifier for `double` with `scanf`!**
-   `%Lf`: Long double floating-point number (`long double*` argument required).
-   `%c`: Single character (`char*` argument required). Does *not* skip leading whitespace by default. Use `% c` to skip whitespace.
-   `%s`: Sequence of non-whitespace characters (string). Requires a `char*` argument pointing to a buffer large enough to hold the input string *plus* a null terminator, which `scanf` adds automatically. **Highly unsafe due to potential buffer overflows.** Use width specifiers (e.g., `%19s` for a 20-char buffer) or preferably use [[fgets]] instead.
-   `%[...]`: Scanset - matches a sequence of characters within the specified set.
-   `%*...`: Assignment suppression - reads input according to the specifier but does *not* assign it to any argument (e.g., `%*d` reads an integer but discards it).

## Example Usage

```c
#include <stdio.h>

int main() {
    int age;
    double weight;
    char initial;
    char name[50]; // Buffer for string input
    int items_read;

    printf("Enter age (int): ");
    items_read = scanf("%d", &age); // Pass ADDRESS of age
    if (items_read != 1) {
        printf("Failed to read age.\n");
        // Clear input buffer (simple example, may not be robust)
        while (getchar() != '\n');
    } else {
        printf("Age entered: %d\n", age);
    }


    printf("Enter weight (double): ");
    items_read = scanf("%lf", &weight); // Pass ADDRESS, use %lf for double
     if (items_read != 1) {
        printf("Failed to read weight.\n");
        while (getchar() != '\n');
    } else {
        printf("Weight entered: %f\n", weight);
    }

    printf("Enter initial (char): ");
    // Note the space before %c to consume any leftover newline from previous input
    items_read = scanf(" %c", &initial); // Pass ADDRESS
     if (items_read != 1) {
        printf("Failed to read initial.\n");
        while (getchar() != '\n');
    } else {
        printf("Initial entered: %c\n", initial);
    }

    printf("Enter name (string, max 49 chars): ");
    // Using width specifier for safety, but fgets is better
    items_read = scanf("%49s", name); // Pass array name (decays to pointer)
     if (items_read != 1) {
        printf("Failed to read name.\n");
    } else {
        printf("Name entered: %s\n", name);
    }

    printf("\nTotal items successfully read in last scanf: %d\n", items_read);


    return 0;
}
```

## Related Functions/Concepts
- [[stdio_h_C]] (Header file required)
- [[stdin_stdout_stderr_C]] (The default input stream)
- [[Format_Specifiers_C]] (Controls input parsing)
- [[Pointer_C]], [[Address_Operator_C]], [[Pass_by_Address_C]] (Arguments MUST be pointers)
- [[Variable_Length_Parameter_List_C]], [[stdarg_macros_C]] (How `scanf` handles variable arguments internally)
- [[printf]] (Formatted output function)
- [[sscanf_C]] (Reads formatted input from a string buffer)
- [[fscanf_C]] (Reads formatted input from a specified file stream)
- [[fgets]] (Safer alternative for reading strings)
- [[Buffer_Overflow_C]] (Risk when using `%s` without width limits - *to be created*)

## Notes
>[!danger] Buffer Overflow Risk
> Using `%s` without a width specifier (e.g., `%49s` for a 50-byte buffer) is extremely dangerous. If the user types more characters than the buffer can hold, `scanf` will write past the end of the buffer, causing a buffer overflow, which can lead to crashes and security vulnerabilities. **It is generally recommended to avoid `scanf` for reading strings and use `fgets` instead**, followed by parsing if necessary (e.g., with `sscanf`).

>[!warning] Input Buffer Issues
> `scanf` can leave characters (especially newline `\n`) in the input buffer, which can interfere with subsequent input operations (especially reading characters with `%c`). Careful handling of whitespace in the format string (e.g., `" %c"`) or explicitly consuming leftover characters (e.g., with a `getchar()` loop) is often necessary.

---
**Source:** Worksheet C_WS3