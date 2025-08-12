---
tags: [c, concept, syntax, function, execution]
aliases: [C Function Invocation]
related:
  - "[[Function_C]]"
  - "[[Function_Declaration_C]]"
  - "[[Function_Definition_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Return_Value_C]]"
  - "[[Stack_Memory_C]]"
  - "[[Expression_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Function Call (C)

## Definition

A **Function Call** in C is an [[Expression_C]] that invokes (executes) a previously declared and defined [[Function_C]]. It transfers program control to the first statement inside the function's body, passes arguments (if any) to the function's parameters, and potentially receives a [[Return_Value_C|return value]] back when the function completes.

## Key Aspects / Characteristics

- **Syntax:** `function_name(argument_list)`
    - `function_name`: The identifier of the function to be called.
    - `argument_list`: A comma-separated list of expressions (arguments) whose values are passed to the function's corresponding parameters. The list is empty `()` if the function takes no arguments.
- **Control Transfer:** Execution jumps from the point of the call to the beginning of the function's definition.
- **Argument Passing:** Values of the arguments in the call are copied to the function's parameters. By default, C uses [[Pass_by_Value_C]]. To modify original variables, [[Pass_by_Address_C]] (passing pointers) is used.
- **Stack Frame:** Typically, a function call involves creating a new stack frame on the [[Stack_Memory_C|call stack]] to hold the function's parameters, local variables, and return address.
- **Return:** When the function executes a `return` statement or reaches the end of its body (for `void` functions), control returns to the point immediately following the function call expression.
- **Return Value Usage:** If the function returns a value (is not `void`), the function call expression itself evaluates to that return value, which can be used in assignments, further calculations, etc. The return value is ignored if not used.
- **Requires Declaration:** The function must be declared (via a prototype or its definition) before it can be called, so the compiler knows how to handle the arguments and return value.

## Examples / Use Cases

```c
#include <stdio.h>
#include <math.h> // For sqrt()

// Assume these functions are declared/defined elsewhere:
int multiply(int a, int b);
void display(int result);

int main() {
    int x = 5, y = 3;
    int product;
    double root;

    // Call 'multiply', assign return value to 'product'
    product = multiply(x, y);

    // Call 'display', passing 'product' as argument (return value ignored)
    display(product);

    // Call 'sqrt' from math library, use return value directly in printf
    root = sqrt(9.0); // Argument is 9.0, return value is 3.0
    printf("Square root of 9.0 is %f\n", root);

    // Function call as part of a larger expression
    product = multiply(multiply(2, 3), 4); // Calls multiply twice
    printf("Nested call result: %d\n", product); // Output: 24

    return 0;
}

// Example definitions for completeness
int multiply(int a, int b) {
    return a * b;
}

void display(int result) {
    printf("The result is: %d\n", result);
}
```

## Related Concepts
- [[Function_C]] (The entity being called)
- [[Function_Declaration_C]] (Required before call)
- [[Function_Definition_C]] (The code executed by the call)
- [[Function_Parameters_C]] & Arguments (Input mechanism)
- [[Return_Value_C]] (Output mechanism)
- [[Pass_by_Value_C]], [[Pass_by_Address_C]] (How arguments relate to parameters)
- [[Stack_Memory_C]] (Used for function call execution)
- [[Expression_C]] (A function call is an expression)

---
**Source:** Worksheet C_WS3