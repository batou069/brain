---
tags: [c, concept, data_representation, array, pointer]
aliases: [C Strings, Character Arrays C, Null-terminated Strings]
related:
  - "[[char_C]]"
  - "[[Array_C]]"
  - "[[Pointer_C]]"
  - "[[Escape_Characters_C]]"
  - "[[NULL_C]]"
  - "[[string_h_C]]"
  - "[[Memory_Segments_C]]"
worksheet: [C_WS3, C_WS4]
date_created: 2025-04-11
---
# String in C

## Definition

In C, a **string** is not a built-in fundamental data type like in some other languages. Instead, a string is represented by convention as a contiguous sequence (an [[Array_C]]) of characters ([[char_C]]) terminated by a special **null character** (`\0`). String manipulation is primarily done using [[Pointer_C|character pointers]] (`char *`) and standard library functions from `<string.h>`.

## Key Aspects / Characteristics

- **Character Array:** Fundamentally an array of `char`.
- **Null Termination:** The end of the string is marked by the null character `\0` (which has an [[ASCII]] value of 0). This terminator is crucial for standard library functions to know where the string ends. The memory allocated for a string must be large enough to hold all its characters *plus* the null terminator.
- **String Literals:** Written in double quotes (`" "`), e.g., `"Hello"`. The compiler automatically appends a null terminator `\0` to string literals when storing them (usually in a read-only part of the [[Memory_Segments_C|memory]]).
    - `"Hello"` is stored as `{'H', 'e', 'l', 'l', 'o', '\0'}`.
- **Representation:** Can be represented/manipulated as:
    - A `char` array initialized with a string literal: `char str[] = "Hello";` (size is 6).
    - A `char` array initialized element by element (must add `\0` manually): `char str[] = {'H', 'e', 'l', 'l', 'o', '\0'};`
    - A `char` pointer pointing to a string literal: `char *ptr = "Hello";` (`ptr` points to the first character 'H' of the literal, which is usually in read-only memory). Modifying through `ptr` is [[Undefined_Behavior_C]].
    - A `char` pointer pointing to a modifiable character array: `char str[] = "Hello"; char *ptr = str;`
- **Library Functions (`<string.h>`):** Since C has no built-in string operators, functions like `strlen`, `strcpy`, `strncpy`, `strcat`, `strcmp`, `strchr`, `strstr`, etc., are used for operations. See [[string_h_C]].

## Examples / Use Cases

```c
#include <stdio.h>
#include <string.h> // For string functions

int main() {
    // 1. String as an initialized character array (modifiable)
    char greeting[] = "Hello"; // Size is 6 (includes '\0')
    printf("Greeting: %s\n", greeting);
    printf("Length (strlen): %zu\n", strlen(greeting)); // Output: 5
    printf("Sizeof array: %zu\n", sizeof(greeting));   // Output: 6

    greeting[0] = 'J'; // Modifiable
    printf("Modified greeting: %s\n", greeting); // Output: Jello

    // 2. String as a pointer to a string literal (read-only)
    char *message = "World";
    printf("Message: %s\n", message);
    printf("Length (strlen): %zu\n", strlen(message)); // Output: 5
    printf("Sizeof pointer: %zu\n", sizeof(message));   // Output: size of a pointer (e.g., 4 or 8)

    // message[0] = 'B'; // UNDEFINED BEHAVIOR - Attempting to modify read-only memory

    // 3. Copying strings
    char buffer[20]; // Must be large enough
    // strcpy(buffer, "A long string that might overflow"); // Unsafe strcpy
    strncpy(buffer, message, sizeof(buffer) - 1); // Safer strncpy
    buffer[sizeof(buffer) - 1] = '\0'; // Ensure null termination
    printf("Copied string: %s\n", buffer);

    // 4. Concatenation
    strncat(greeting, message, sizeof(greeting) - strlen(greeting) - 1); // Append "World" to "Jello"
    printf("Concatenated: %s\n", greeting); // Output: JelloWorld (if greeting was large enough!)

    return 0;
}```

## Related Concepts
- [[char_C]] (The basic building block)
- [[Array_C]] (The underlying storage mechanism)
- [[Pointer_C]] (`char*` is commonly used to work with strings)
- [[Null_Character_C]] (`\0`) (The essential terminator - *to be created*)
- [[Escape_Characters_C]] (Used within string literals)
- [[string_h_C]] (Standard library for string functions)
- [[Memory_Segments_C]] (Where string literals vs. arrays are stored)
- [[Undefined_Behavior_C]] (Modifying string literals, buffer overflows)

## Questions / Further Study
>[!question] Given `char str[] = "welcome";`, what is `sizeof(str)` vs `strlen(str)`? (WS4)
> - `strlen(str)`: Calculates the length of the string *excluding* the null terminator. It counts characters until it finds `\0`. For `"welcome"`, `strlen` returns **7**. (Requires `#include <string.h>`)
> - `sizeof(str)`: Returns the total size *in bytes* allocated for the array `str`. Since `str` is initialized with `"welcome"`, the compiler allocates space for the 7 characters plus the automatically appended null terminator `\0`. Therefore, `sizeof(str)` returns **8**.

>[!question] Differences between `char* p = "lalala";` and `char arr[] = "lalala";`? (WS4)
> - **Allocation:**
>     - `char* p`: `p` is a pointer variable (typically stored on the stack or in static memory depending on where `p` is defined). It is initialized to point to the first character of the string literal `"lalala"`. The string literal itself is typically stored in a **read-only** section of memory.
>     - `char arr[]`: `arr` is an array of characters (allocated on the stack if local, or in static memory if global/static). The compiler determines its size (7 bytes: 6 for "lalala" + 1 for `\0`) and initializes the array's contents by *copying* the characters from the string literal into the array's allocated memory. This array is **modifiable**.
> - **`sizeof`:**
>     - `sizeof(p)`: Returns the size of a pointer variable (e.g., 4 or 8 bytes, depending on the architecture).
>     - `sizeof(arr)`: Returns the total size allocated for the array, which is 7 bytes in this case.
> - **Modifiability:**
>     - `p[0] = 's';` or `*p = 's';`: **Undefined Behavior**. Attempts to modify the read-only memory where the string literal is stored. Likely crashes the program.
>     - `arr[0] = 's';` or `*arr = 's';`: **Valid**. Modifies the first character of the array `arr` in its allocated (writable) memory.
> - **Assignment:**
>     - `p = "new string";`: **Valid**. Makes the pointer `p` point to a different string literal.
>     - `arr = "new string";`: **Invalid**. You cannot assign directly to an array name after its definition. You would need `strcpy` or similar to change its contents.
> - **Pointer Arithmetic:**
>     - `++p;`: **Valid**. Makes `p` point to the next character (`'a'`).
>     - `++arr;`: **Invalid**. An array name is (usually) a non-modifiable lvalue representing the address of the first element; you cannot change where the array itself starts.

---
**Source:** Worksheet C_WS3, C_WS4