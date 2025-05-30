---
tags: [c, concept, syntax, function, implementation]
aliases: [C Function Implementation]
related:
  - "[[Function_C]]"
  - "[[Function_Declaration_C]]"
  - "[[Function_Call_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Return_Value_C]]"
  - "[[Scope_C]]"
  - "[[Linker_C]]"
worksheet: [C_WS3, C_WS6]
date_created: 2025-04-11
---
# Function Definition (C)

## Definition

A **Function Definition** in C provides the actual implementation (the body) of a [[Function_C]]. It consists of the function header (return type, name, parameter list) followed by a compound statement (code enclosed in curly braces `{}`) containing the executable statements that perform the function's task. Every function that is called in a program must have exactly one definition within the entire program (One Definition Rule).

## Key Aspects / Characteristics

- **Provides Implementation:** Contains the actual code that runs when the function is called.
- **Syntax:**
  ```c
  return_type function_name(parameter_list) {
      // Declarations and statements (function body)
      // ...
      return return_value; // Optional, required if return_type is not void
  }
  ```
- **Function Header:** Matches the [[Function_Declaration_C|function declaration (prototype)]] in terms of return type, name, and parameter types. Parameter names *must* be present in the definition header.
- **Function Body:** Enclosed in curly braces `{}`. Contains local variable definitions and executable statements.
- **One Definition Rule (ODR):** A non-inline function can only be defined once across all source files linked together. Multiple definitions usually cause a [[Linker_C|linker]] error.
- **Location:** Function definitions are typically placed in source files (`.c` files), not header files (except for `inline` functions or sometimes `static` functions intended only for that file's use).

## Examples / Use Cases

```c
#include <stdio.h>

// Definition for a function declared elsewhere (e.g., in a header)
int calculate_sum(int a, int b) { // Function header
    // Function body starts here
    int result; // Local variable definition
    result = a + b;
    return result; // Return statement
    // Function body ends here
}

// Definition for a function that might only be declared implicitly (older C style - not recommended)
// or declared just before this definition
void print_greeting(const char *name) {
    if (name != NULL) {
        printf("Hello, %s!\n", name);
    } else {
        printf("Hello there!\n");
    }
    // Implicit return for void function at the end of the body
}

// Definition of the main function
int main(void) {
    int sum = calculate_sum(5, 7);
    print_greeting("Alice");
    return 0;
}
```

## Related Concepts
- [[Function_C]] (The overall concept)
- [[Function_Declaration_C]] (Specifies the interface)
- [[Function_Call_C]] (Invokes the defined code)
- [[Function_Parameters_C]], [[Return_Value_C]] (Part of the definition header and body)
- [[Scope_C]], [[Local_Variable_C]] (Defined within the function body)
- [[Linker_C]] (Connects calls to the single definition)
- [[Implementation_C]] (The definition provides the implementation)

## Questions / Further Study
>[!question] Do you ever include a .c file? (WS6)
> **Almost never.** Including a `.c` file (`#include "my_implementation.c"`) directly incorporates its entire content, including function and variable *definitions*, into the including file *before* compilation. If `my_implementation.c` is also compiled separately and linked, or if it's included in another `.c` file, this will lead to multiple definition errors from the [[Linker_C]]. Including `.c` files breaks the standard C compilation model (compile separately, link together) and is considered very bad practice. The correct approach is to put declarations in `.h` files and definitions in `.c` files, then `#include` the `.h` files where needed and link the compiled `.o` files together. (Rare exceptions might exist in highly specialized build systems or for generating monolithic code, but these are unconventional).

---
**Source:** Worksheet C_WS3, C_WS6