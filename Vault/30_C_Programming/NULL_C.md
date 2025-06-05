---
tags: [c, concept, pointer, value, macro, error]
aliases: [C NULL Pointer, Null Pointer Constant]
related:
  - "[[Pointer_C]]"
  - "[[malloc]]"
  - "[[free]]"
  - "[[Dynamic_Allocation_C]]"
  - "[[Dangling_Pointer_C]]"
  - "[[Conditional_Statements_C]]"
worksheet: [C_WS3]
header_file: <stddef.h>, <stdlib.h>, <stdio.h>, etc. (defines NULL)
date_created: 2025-04-11
---
# NULL (C)

## Definition

In C, `NULL` is a **null pointer constant**. It's a macro defined in several standard library headers (like `<stddef.h>`, `<stdlib.h>`, `<stdio.h>`, `<string.h>`, `<time.h>`, `<wchar.h>`) that represents a pointer value guaranteed *not* to point to any valid object or function in memory. It's commonly used to indicate the absence of a valid address, often signifying errors, termination conditions, or uninitialized pointer states.

## Key Aspects / Characteristics

- **Macro Definition:** `NULL` is typically defined as `((void*)0)`, `0`, or `0L` depending on the compiler and context (in C++, it's often just `0` or `nullptr`). Regardless of the specific definition, it represents the null pointer value.
- **Invalid Address:** Conceptually represents address zero, but the actual bit pattern might differ on some architectures. The key is that it's distinguishable from any valid pointer to data or functions.
- **Comparison:** Any pointer type can be compared for equality (`==`) or inequality (`!=`) with `NULL`.
- **Indicates Absence/Error:**
    - [[malloc]] and other allocation functions return `NULL` on failure.
    - Functions searching for data might return `NULL` if the item isn't found.
    - Pointers can be initialized to `NULL` to indicate they aren't pointing anywhere valid yet.
    - Linked list terminators often use `NULL`.
- **Dereferencing:** Dereferencing a `NULL` pointer (`*null_ptr`) results in [[Undefined_Behavior_C]], usually a program crash (segmentation fault). **Always check pointers against `NULL` before dereferencing if they might be invalid.**
- **`free()` Safety:** Passing `NULL` to [[free]] is explicitly defined as safe and results in no operation.

## Examples / Use Cases

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // For strchr

int main() {
    int *ptr = NULL; // Initialize pointer to NULL

    // Check before dereferencing
    if (ptr != NULL) {
        printf("Value: %d\n", *ptr); // This block won't execute
    } else {
        printf("Pointer is NULL.\n");
    }

    // Allocation check
    ptr = (int*)malloc(sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    *ptr = 42;
    printf("Allocated pointer is not NULL. Value: %d\n", *ptr);

    // Freeing NULL is safe
    free(NULL);

    // Freeing the allocated memory
    free(ptr);
    ptr = NULL; // Good practice

    // Example: strchr returns NULL if character not found
    char *str = "Hello World";
    char *found = strchr(str, 'z'); // Search for 'z'
    if (found == NULL) {
        printf("Character 'z' not found in \"%s\".\n", str);
    }

    return 0;
}
```

## Related Concepts
- [[Pointer_C]] (NULL is a special pointer value)
- [[Dynamic_Allocation_C]], [[malloc]] (Return NULL on failure)
- [[free]] (Safely handles NULL input)
- [[Dangling_Pointer_C]] (Setting freed pointers to NULL helps prevent dangling pointer issues)
- [[Undefined_Behavior_C]] (Result of dereferencing NULL)
- [[Conditional_Statements_C]] (`if (ptr != NULL)` is common)
- [[void_pointer_C]] (NULL is often defined as `(void*)0`)

---
**Source:** Worksheet C_WS3