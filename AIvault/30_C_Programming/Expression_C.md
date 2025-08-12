---
tags: [c, concept, syntax]
aliases: [C Expression]
related:
  - "[[Operator_C]]"
  - "[[Variable_Definition_C]]"
  - "[[Function_C]]"
  - "[[Sequence_Point_C]]"
  - "[[Statement_C]]"
worksheet: [C_WS1]
date_created: 2025-04-21
date_created: 2025-04-12
---
# Expression (C)

## Definition

In C, an **Expression** is a sequence of [[Operator_C|operators]] and operands (variables, constants, function calls) that specifies a computation. Evaluating an expression produces a value and may potentially cause side effects (like modifying a variable or performing I/O).

## Key Aspects / Characteristics

- **Computes a Value:** Every expression evaluates to a value of a specific [[Data_Types_C|data type]].
- **Operators and Operands:** Composed of operators (e.g., `+`, `-`, `*`, `/`, `=`, `==`, `&&`, `()`) and operands (e.g., `x`, `10`, `calculate_sum(a, b)`).
- **Side Effects:** Some expressions modify the state of the program (e.g., `x = 5`, `++count`, `printf("Hello")`).
- **Used in Statements:** Expressions form the core components of many C [[Statement_C|statements]] (e.g., assignment statements, `if` conditions, `return` values).
- **Precedence and Associativity:** The order of evaluation within complex expressions is determined by [[Operator_Precedence_C]] and associativity rules.
- **Sequence Points:** [[Sequence_Point_C|Sequence points]] define specific points during expression evaluation where all side effects of previous evaluations must be complete.

## Examples / Use Cases

```c
int a = 5;
int b = 10;
int c;
int result;

// Simple expressions:
5          // Constant expression, value is 5
a          // Variable expression, value is 5
b + 3      // Arithmetic expression, value is 13

// Assignment expression (also has a value, which is the assigned value):
c = a + b  // Value of expression is 15, side effect: c becomes 15

// Relational expression:
a < b      // Value is 1 (true)

// Logical expression:
(a < b) && (c == 15) // Value is 1 (true)

// Function call expression:
result = printf("Value of c: %d\n", c); // Value is number of chars printed, side effect: prints output

// Complex expression:
result = (a * b) + (c / 2) - 1; // Evaluated based on precedence rules
```

## Related Concepts

- [[Operator_C]] (Symbols performing operations within expressions)
- [[Operator_Precedence_C]] (Rules governing evaluation order)
- [[Sequence_Point_C]] (Guarantees about side effect completion)
- [[Statement_C]] (Expressions are often part of statements)
- [[Function_C]] (Function calls are expressions)
- [[Side_Effect_C]] (Actions performed during expression evaluation - to be created)

## Questions / Further Study

> [!question] What is the difference between "Expression" and "Statement"? (WS18 - Python context, but relevant here)  
> An **[[Expression_C|expression]]** is something that evaluates to a value (e.g., 2 + 2, x * 5, is_valid(input)). A **[[Statement_C|statement]]** is a complete unit of execution that performs an action (e.g., x = 5;, if (y > 10) { ... }, while (i < 0) { ... }, return 0;). Expressions are often part of statements (e.g., the x = 5 expression is part of the assignment statement x = 5;). A simple expression followed by a semicolon (e.g., x + 1;) is also a valid statement (an "expression statement"), though often only useful if the expression has side effects (like printf("Hi"); or i++;).

---

**Source:** Worksheet C_WS1, WS18 (Python)