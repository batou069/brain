---
tags:
  - c
  - concept
  - data_type
  - keyword
  - syntax
  - data_structure
aliases:
  - C Struct
  - Structure C
related:
  - "[[Data_Types_C]]"
  - "[[Member_Access_Operators_C]]"
  - "[[Pointer_C]]"
  - "[[typedef_C]]"
  - "[[50_Data_Structures/Memory_Management]]"
  - "[[Padding_C]]"
  - "[[Union_C]]"
worksheet:
  - C_WS5
date_created: 2025-04-12
---
# `struct` (Structure) (C)

## Definition

A **`struct` (structure)** in C is a user-defined composite data type that groups together one or more variables, potentially of different data types, under a single name. These variables within the struct are called **members** or **fields**. Structs allow you to represent more complex data entities.

## Key Aspects / Characteristics

- **Composite Type:** Groups multiple variables (members).
- **Heterogeneous Members:** Members can be of different data types (e.g., `int`, `char`, `double`, pointers, other structs, arrays).
- **Memory Layout:** Members are typically stored sequentially in memory in the order they are declared, although the compiler may insert padding bytes ([[Padding_C]]) between members for alignment purposes to improve access speed.
- **Declaration:**
    ```c
    struct TagName {
        type1 member1;
        type2 member2;
        // ...
    }; // Semicolon is important!
    ```
- **Variable Definition:**
    ```c
    struct TagName my_variable; // Defines a variable of the struct type
    ```
- **Member Access:** Members are accessed using the member access operators ([[Member_Access_Operators_C]]):
    - **`.` (Dot operator):** Used when accessing members directly via the struct variable itself (e.g., `my_variable.member1`).
    - **`->` (Arrow operator):** Used when accessing members via a pointer to the struct (e.g., `ptr_to_struct->member1`, which is shorthand for `(*ptr_to_struct).member1`).
- **`typedef`:** Often used with `struct` definitions to create a simpler alias for the type name (e.g., `typedef struct TagName TypeAlias;`).
- **Assignment & Passing:** Structs can be assigned (`struct1 = struct2;`), passed to functions by value ([[Pass_by_Value_C]]), and returned from functions by value. Passing large structs by value involves copying the entire structure, which can be inefficient; passing a pointer ([[Pass_by_Address_C]]) is often preferred.

## Syntax & Examples

```c
#include <stdio.h>
#include <string.h>

// Define a struct type named 'Point'
struct Point {
    int x;
    int y;
};

// Define a struct type 'Person' using typedef for convenience
typedef struct {
    char name[50];
    int age;
    struct Point location; // Struct can contain other structs
} Person;

// Function that takes a struct by value
void print_person_by_value(Person p) {
    printf("Value: Name=%s, Age=%d, Location=(%d, %d)\n",
           p.name, p.age, p.location.x, p.location.y);
}

// Function that takes a pointer to a struct
void print_person_by_pointer(const Person *p_ptr) {
    if (p_ptr == NULL) return;
    printf("Pointer: Name=%s, Age=%d, Location=(%d, %d)\n",
           p_ptr->name, p_ptr->age, p_ptr->location.x, p_ptr->location.y);
    // Equivalent using dot operator: (*p_ptr).name, (*p_ptr).age etc.
}


int main() {
    // Define and initialize a struct variable
    struct Point p1 = {10, 20}; // Using initializer list
    Person person1;

    // Access and assign members using dot operator
    p1.x = 15;
    strcpy(person1.name, "Alice");
    person1.age = 30;
    person1.location = p1; // Assign struct p1 to member location
    person1.location.y = 25; // Access nested struct member

    printf("P1: (%d, %d)\n", p1.x, p1.y);

    // Access using pointer and arrow operator
    Person *person_ptr = &person1;
    printf("Access via pointer: Age = %d\n", person_ptr->age);
    person_ptr->age = 31; // Modify via pointer

    // Pass struct to functions
    print_person_by_value(person1);
    print_person_by_pointer(&person1);

    return 0;
}
```

## Related Concepts
- [[Data_Types_C]] (Struct creates a new composite type)
- [[Member_Access_Operators_C]] (`.` and `->`)
- [[typedef_C]] (Often used to alias struct types)
- [[Pointer_C]] (Used to access structs via `->`, efficient passing)
- [[50_Data_Structures/Memory_Management]], [[Padding_C]] (How structs are laid out in memory)
- [[Union_C]] (Similar concept, but members share the same memory)
- [[Pass_by_Value_C]], [[Pass_by_Address_C]] (How structs are passed to functions)

---
**Source:** Worksheet C_WS5