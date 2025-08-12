---
tags: [c, concept, syntax, function]
aliases: [C Function Arguments, Formal Parameters C]
related:
  - "[[Function_C]]"
  - "[[Function_Declaration_C]]"
  - "[[Function_Definition_C]]"
  - "[[Function_Call_C]]"
  - "[[Pass_by_Value_C]]"
  - "[[Pass_by_Address_C]]"
  - "[[Scope_C]]"
  - "[[Local_Variable_C]]"
  - "[[Stack_Memory_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Function Parameters (C)

## Definition

**Function Parameters** (also called **formal parameters**) are variables declared in the header of a [[Function_Definition_C]]. They act as placeholders to receive input values, known as **arguments** (or **actual parameters**), that are passed during a [[Function_Call_C]]. Parameters define the type and name of the data the function expects to receive.

## Key Aspects / Characteristics

- **Declaration in Header:** Defined within the parentheses `()` following the function name in both the [[Function_Declaration_C|declaration (prototype)]] and the [[Function_Definition_C|definition]].
- **Type Specification:** Each parameter must have a specified data type (e.g., `int`, `double`, `char*`, `struct Point`).
- **Receiving Arguments:** When a function is called, the values of the arguments provided in the call are copied into the corresponding parameters.
- **Local Scope:** Parameters behave like [[Local_Variable_C|local variables]] within the function's body. They exist only during the function's execution and are typically stored on the [[Stack_Memory_C|stack frame]]. Their scope is limited to the function body.
- **Passing Mechanism:** By default, C uses [[Pass_by_Value_C]]. This means the function receives a *copy* of the argument's value, and modifications to the parameter inside the function do *not* affect the original argument variable in the caller. [[Pass_by_Address_C]] (passing pointers as arguments) is used to allow functions to modify the caller's variables.
- **`void` Parameter List:** `void` in the parameter list (e.g., `int func(void)`) explicitly indicates that the function takes no parameters. An empty list `int func()` is an older style meaning "takes an unspecified number of arguments" (generally discouraged in modern C).

## Examples / Use Cases

```c
#include <stdio.h>

// Function definition with parameters 'a' and 'b'
int sum(int a, int b) { // 'a' and 'b' are parameters
    a = a + 1; // Modifies the local copy 'a', not the original argument
    return a + b;
}

// Function definition with a pointer parameter 'ptr'
void increment(int *ptr) { // 'ptr' is a parameter (pointer to int)
    if (ptr != NULL) {
        (*ptr)++; // Modifies the value AT THE ADDRESS pointed to by ptr
    }
}

// Function taking no parameters
void print_hello(void) {
    printf("Hello!\n");
}

int main() {
    int x = 5, y = 10;
    int result;

    // Call 'sum', passing 'x' and 'y' as arguments
    result = sum(x, y); // x's value (5) copied to 'a', y's value (10) copied to 'b'
    printf("Sum result: %d\n", result); // Output: 16 (because 'a' became 6 inside sum)
    printf("Original x after sum call: %d\n", x); // Output: 5 (original x is unchanged)

    // Call 'increment', passing the address of 'x' as argument
    increment(&x); // Address of x copied to 'ptr'
    printf("Original x after increment call: %d\n", x); // Output: 6 (original x was modified)

    // Call 'print_hello'
    print_hello();

    return 0;
}
```

## Related Concepts
- [[Function_C]], [[Function_Declaration_C]], [[Function_Definition_C]], [[Function_Call_C]]
- Arguments (The values passed during the call)
- [[Pass_by_Value_C]] (Default mechanism)
- [[Pass_by_Address_C]] (Using pointers to modify caller's data)
- [[Scope_C]], [[Local_Variable_C]], [[Stack_Memory_C]] (Parameter lifetime and storage)
- [[Data_Types_C]] (Parameters have types)
- [[Variable_Length_Parameter_List_C]] (Functions like `printf` use `...`)

---
**Source:** Worksheet C_WS3