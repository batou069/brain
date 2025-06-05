---
tags: [c, concept, syntax]
aliases: [C Operators]
related:
  - "[[Expression_C]]"
  - "[[Operator_Precedence_C]]"
  - "[[Data_Types_C]]"
  - "[[Pointer_C]]"
  - "[[bits]]"
worksheet: [C_WS1, C_WS3]
date_created: 2025-04-12
---
# Operator (C)

## Definition

In C, an **Operator** is a symbol that tells the [[Compiler_C|compiler]] to perform specific mathematical, relational, logical, bitwise, assignment, or other operations on one, two, or three operands (values or variables).

## Key Aspects / Characteristics


- **Symbolic Representation:** Uses symbols like +, -, *, /, %, ++, --, =,` ==, !=, <, >, <=, >=, &&, ||, !, &, |, ^, ~, <<, >>, sizeof, * (dereference), & (address-of), ->, ., ?: (ternary).
- **Arity:** Operators act on a specific number of operands:
    - *Unary:* One operand (e.g., !flag, ++count, -x, *ptr, &var, sizeof x).
    - *Binary:* Two operands (e.g., a + b, x = y, p -> member).
    - *Ternary:* Three operands (e.g., condition ? value_if_true : value_if_false).

- **Precedence & Associativity:** [[Operator_Precedence_C]] rules determine the order in which operators are evaluated in a complex [[Expression_C]]. Associativity rules determine the order for operators of the same precedence (e.g., left-to-right for +, -; right-to-left for assignment =).
- **Overloading (Not in C):** Unlike C++, C does not allow operator overloading (defining custom behavior for operators with user-defined types like structs).

## Categories of Operators

- **Arithmetic:** +, -, *, /, % (modulus)
- **Increment/Decrement:** ++, -- (prefix and postfix)
- **Relational:** `==, !=, >, <, >=, <=
- **Logical:** && (AND), || (OR), ! (NOT)
- **Bitwise:** & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
- **Assignment:** =, +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=
- **Pointer Operators:** * (dereference), & (address-of)
- **Structure/Union Member Access:** . (direct), -> (indirect via pointer)
- **Conditional (Ternary):** ?:
- **sizeof Operator:** [[sizeof_operator_C]] (returns size in bytes)
- **Comma Operator:** , (evaluates left operand, discards result, evaluates right operand, result is value of right operand)
- **Type Cast Operator:** (type_name)

## Related Concepts
- [[Expression_C]] (Operators are used within expressions)
- [[Operator_Precedence_C]] (Governs evaluation order)
- [[Data_Types_C]] (Operators work on specific data types)
- [[Pointer_C]] (Specific operators for pointers)
- [[bits]] (Bitwise operators manipulate bits)
- [[sizeof_operator_C]]

---
**Source:** Worksheet C_WS1, C_WS3
