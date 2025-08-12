---
tags: [c, concept, rule, evaluation, side_effect]
aliases: [C Sequence Points]
related:
  - "[[Expression_C]]"
  - "[[Operator_Precedence_C]]"
  - "[[Side_Effect_C]]"
  - "[[Undefined_Behavior_C]]"
worksheet: [C_WS1]
date_created: 2025-04-12
---
# Sequence Point (C)

## Definition

In C (and C++), a **Sequence Point** defines a specific point in the execution sequence of a program at which all side effects of previous evaluations are guaranteed to be complete, and no side effects of subsequent evaluations have yet occurred. They are crucial for understanding the behavior of expressions with [[Side_Effect_C|side effects]], especially when a variable is read and modified multiple times within the same expression without an intervening sequence point.

## Key Aspects / Characteristics

- **Side Effect Completion:** Guarantees that modifications to variables (e.g., via `++`, `--`, assignment `=`) are finished.
- **Order Guarantee:** Ensures a defined order between the completion of previous side effects and the start of subsequent evaluations.
- **Preventing Undefined Behavior:** Modifying an object more than once, or modifying it and reading its value for another purpose, between two sequence points results in [[Undefined_Behavior_C]]. Sequence points prevent this ambiguity.
- **Common Sequence Points:** Sequence points exist at:
    - The end of a full expression statement (at the semicolon `;`).
    - Between the evaluation of the left and right operands of the logical AND (`&&`), logical OR (`||`), and comma (`,`) operators.
    - Between the evaluation of the condition in `if`, `switch`, `while`, `do-while`, `for` statements and the execution of the associated sub-statement/block.
    - Between the evaluation of the first operand of the conditional operator (`?:`) and the evaluation of the second or third operand.
    - At the point of a function call, after the evaluation of all function arguments and the function designator itself, but before execution of the function body begins.
    - After the evaluation of the expression in a `return` statement.

## Examples / Use Cases

**Undefined Behavior (No Sequence Point):**
```c
int i = 5;
i = i++; // UNDEFINED BEHAVIOR: 'i' is modified twice without sequence point between modifications.
         // The compiler could increment i before or after assigning the original value.

int x = 1;
printf("%d %d\n", x++, x++); // UNDEFINED BEHAVIOR: Order of evaluation of arguments and side effects is unspecified.

int arr[5];
int j = 0;
arr[j] = j++; // UNDEFINED BEHAVIOR: 'j' is read (for index) and modified without sequence point.
```

**Defined Behavior (Sequence Points Present):**

```c
int i = 5;
i++;       // Sequence point at ';' - i becomes 6. 
int j = i; // Sequence point at ';' - j becomes 6.  

int a = 1, b = 2;
if (a++ && b++) { /* ... */ } // Sequence point after a++ evaluation (due to &&).                              // b++ is only evaluated if a++ was non-zero.  

int k = 0; 
k = (k++, k + 1); // Sequence point at ','. k becomes 1, expression value is 2. k is assigned 2.
```

## Related Concepts

- [[Expression_C]] (Sequence points occur during expression evaluation)
- [[Operator_Precedence_C]] (Determines grouping, but not necessarily full evaluation order regarding side effects)
- [[Side_Effect_C]] (Actions whose completion is guaranteed at sequence points)
- [[Undefined_Behavior_C]] (Result of violating sequence point rules)


---

**Source:** Worksheet C_WS1