---
tags: [c, concept, syntax, structure, core]
aliases: [C Function, C Subroutine, C Procedure]
related:
  - "[[Function_Declaration_C]]"
  - "[[Function_Definition_C]]"
  - "[[Function_Call_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Return_Value_C]]"
  - "[[Scope_C]]"
  - "[[Stack_Memory_C]]"
  - "[[main_Function_C]]"
  - "[[Static_Function_C]]"
  - "[[extern_Function_C]]"
  - "[[Function_Pointer_C]]"
worksheet: [C_WS3, C_WS6]
date_created: 2025-04-11
---
# Function (C)

## Definition

A **Function** in C is a self-contained block of code that performs a specific task. Functions allow code to be organized into reusable modules, improving structure, readability, and maintainability. A function typically takes input values ([[Function_Parameters_C|parameters]]), performs operations, and optionally returns a result ([[Return_Value_C|return value]]).

## Key Aspects / Characteristics

- **Modularity & Reusability:** Break down complex problems into smaller, manageable, reusable pieces.
- **Structure:** Every C program consists of one or more functions. Execution begins in the [[main_Function_C|`main` function]].
- **Declaration (Prototype):** A [[Function_Declaration_C]] tells the compiler the function's name, return type, and the types of its parameters. This allows the function to be called before its definition appears. Often placed in [[Header_file_C|header files]].
- **Definition:** The [[Function_Definition_C]] provides the actual code (the function body) that is executed when the function is called. A function must be defined exactly once in a program.
- **Call:** A [[Function_Call_C]] invokes the function, passing actual arguments and transferring control to the function's body.
- **Parameters:** [[Function_Parameters_C]] are variables declared in the function definition that receive input values (arguments) when the function is called. C uses [[Pass_by_Value_C]] by default. [[Pass_by_Address_C]] can be simulated using pointers.
- **Return Value:** A function can return a single value to the caller using the `return` statement. The type of the returned value must match the function's declared return type. Functions declared `void` do not return a value.
- **Scope:** Variables declared inside a function ([[Local_Variable_C]]) are typically local to that function and exist only during its execution (on the [[Stack_Memory_C|stack]]).
- **Linkage:** Functions can have external linkage (visible across files, default) or internal linkage ([[Static_Function_C|static functions]], visible only within the defining file).

## Examples / Use Cases

```c
#include <stdio.h>

// Function Declaration (Prototype)
int add(int x, int y);
void print_message(const char *message);

// Function Definition: add
int add(int x, int y) {
    int sum = x + y;
    return sum; // Return statement
}

// Function Definition: print_message (void return type)
void print_message(const char *message) {
    printf("Message: %s\n", message);
    // No return value needed for void functions (or use 'return;' optionally)
}

// The main function - program execution starts here
int main() {
    int num1 = 10, num2 = 5;
    int result;

    // Function Call: add
    result = add(num1, num2);
    printf("%d + %d = %d\n", num1, num2, result);

    // Function Call: print_message
    print_message("Functions are useful!");

    return 0; // Return value from main indicates exit status
}
```

## Related Concepts
- [[Function_Declaration_C]] (Prototype)
- [[Function_Definition_C]] (Implementation)
- [[Function_Call_C]] (Invoking the function)
- [[Function_Parameters_C]] (Inputs)
- [[Return_Value_C]] (Output)
- [[Pass_by_Value_C]], [[Pass_by_Address_C]] (Argument passing mechanisms)
- [[Scope_C]], [[Local_Variable_C]], [[Stack_Memory_C]] (Function execution context)
- [[main_Function_C]] (Program entry point)
- [[Static_Function_C]], [[extern_Function_C]] (Linkage)
- [[Variable_Length_Parameter_List_C]] (`...` syntax - *to be created*)
- [[Recursion_C]] (Function calling itself - *to be created*)

---
**Source:** Worksheet C_WS3, C_WS6