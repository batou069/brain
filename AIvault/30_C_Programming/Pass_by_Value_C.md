---
tags: [c, concept, function, parameter, memory]
aliases: [C Pass by Copy]
related:
  - "[[Function_C]]"
  - "[[Function_Parameters_C]]"
  - "[[Function_Call_C]]"
  - "[[Pass_by_Address_C]]"
  - "[[Stack_Memory_C]]"
worksheet: [C_WS3]
date_created: 2025-04-11
---
# Pass by Value (C)

## Definition

**Pass by Value** is the default mechanism in C for passing arguments during a [[Function_Call_C]]. When an argument is passed by value, a **copy** of the argument's value is created and assigned to the corresponding [[Function_Parameters_C|function parameter]]. The function then works with this local copy.

## Key Aspects / Characteristics

- **Copying:** The value of the argument variable in the caller's scope is copied.
- **Isolation:** The function parameter is a distinct variable in memory (typically on the function's [[Stack_Memory_C|stack frame]]), separate from the original argument variable.
- **Caller's Variable Unchanged:** Modifications made to the parameter *inside* the function do **not** affect the original argument variable in the calling function's scope.
- **Default Behavior:** This is the standard way arguments are passed for fundamental types (like `int`, `float`, `char`, `double`) and structures (`struct`).

## Examples / Use Cases

```c
#include <stdio.h>

// Function takes an integer parameter 'param' by value
void try_modify(int param) {
    printf("  Inside try_modify: param before modification = %d\n", param);
    param = param * 10; // Modify the local copy 'param'
    printf("  Inside try_modify: param after modification = %d\n", param);
}

int main() {
    int original_arg = 5;

    printf("In main: original_arg before call = %d\n", original_arg);

    // Call try_modify, passing original_arg by value
    try_modify(original_arg); // A copy of the value 5 is passed to 'param'

    printf("In main: original_arg after call = %d\n", original_arg); // Value remains unchanged

    return 0;
}
```
**Output:**
```
In main: original_arg before call = 5
  Inside try_modify: param before modification = 5
  Inside try_modify: param after modification = 50
In main: original_arg after call = 5
```

## Related Concepts
- [[Function_C]], [[Function_Parameters_C]], [[Function_Call_C]]
- [[Pass_by_Address_C]] (Alternative mechanism using pointers to allow modification of caller's variables)
- [[Stack_Memory_C]] (Where the copies of parameters are typically stored)
- [[Scope_C]] (Parameters have local scope within the function)

## Questions / Further Study
>[!question] If C uses pass-by-value, how can functions like `scanf` change variables in the caller?
> Functions like [[scanf]] achieve this by using [[Pass_by_Address_C]]. Instead of passing the variable itself, you pass its memory address (using the [[Address_Operator_C|`&` operator]]). The function parameter is then a [[Pointer_C]] which receives this address. Inside the function, it uses the [[Dereference_Operator_C|`*` operator]] to access and modify the value *at the original address* in the caller's scope. So, while the pointer itself is passed by value (a copy of the address is made), this copied address still points to the original variable's location.

---
**Source:** Worksheet C_WS3