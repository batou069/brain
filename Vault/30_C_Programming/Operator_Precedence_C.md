---
tags: [c, concept, syntax, rule]
aliases: [C Operator Precedence, Order of Operations C]
related:
  - "[[Operator_C]]"
  - "[[Expression_C]]"
  - "[[Sequence_Point_C]]"
worksheet: [C_WS1]
date_created: 2025-04-21
---
# Operator Precedence (C)

## Definition

**Operator Precedence** in C determines the order in which different [[Operator_C|operators]] are evaluated when they appear together in an [[Expression_C]] without explicit parentheses `()`. Operators with higher precedence are evaluated before operators with lower precedence. **Associativity** rules determine the evaluation order for operators with the *same* precedence level.

## Key Aspects / Characteristics

- **Evaluation Order:** Controls how expressions like `a + b * c` are grouped (multiplication `*` has higher precedence than addition `+`, so it's `a + (b * c)`).
- **Precedence Levels:** C defines numerous precedence levels for its operators.
- **Associativity:**
    - *Left-to-Right:* Most binary operators (e.g., `+`, `-`, `*`, `/`, `%`, `<<`, `>>`, relational, logical AND/OR) group from left to right (e.g., `a - b + c` is `(a - b) + c`).
    - *Right-to-Left:* Assignment operators (=, +=, etc.), unary operators (`+`, `-`, `!`, `~`, `++`, `--`, `*` deref, `&` addr-of, `sizeof`), and the conditional operator (`?:`) group from right to left (e.g., `x = y = 5` is `x = (y = 5)`).
- **Parentheses Override:** Parentheses `()` can be used to explicitly control the order of evaluation, overriding the default precedence and associativity rules. Using parentheses often improves code readability even when not strictly necessary.

## Precedence Table (Simplified - Highest to Lowest)

>[!note] Simplified Precedence Table
> This is not exhaustive but covers common operators. Refer to a full C reference for complete details.

1.  **Postfix:** `()` (function call), `[]` (array subscript), `.` (member access), `->` (member access via ptr), `++` (postfix), `--` (postfix) - *Left-to-Right*
2.  **Unary:** `+` (unary plus), `-` (unary minus), `!` (logical NOT), `~` (bitwise NOT), `++` (prefix), `--` (prefix), `*` (dereference), `&` (address-of), `sizeof`, `(type)` (cast) - *Right-to-Left*
3.  **Multiplicative:** `*`, `/`, `%` - *Left-to-Right*
4.  **Additive:** `+`, `-` - *Left-to-Right*
5.  **Bitwise Shift:** `<<`, `>>` - *Left-to-Right*
6.  **Relational:** `<`, `<=`, `>`, `>=` - *Left-to-Right*
7.  **Equality:** `==, != - *Left-to-Right*
8.  **Bitwise AND:** `&` - *Left-to-Right*
9.  **Bitwise XOR:** `^` - *Left-to-Right*
10. **Bitwise OR:** `|` - *Left-to-Right*
11. **Logical AND:** `&&` - *Left-to-Right*
12. **Logical OR:** `||` - *Left-to-Right*
13. **Conditional (Ternary):** `?:` - *Right-to-Left*
14. **Assignment:** =, +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>= - *Right-to-Left*
15. **Comma:** `,` - *Left-to-Right*

## Examples

```c
int a = 2, b = 3, c = 4, d;

d = a + b * c;      // Equivalent to d = a + (b * c); -> d = 2 + 12; -> d = 14
d = (a + b) * c;    // Parentheses override: d = (2 + 3) * 4; -> d = 5 * 4; -> d = 20
d = a * b / c;      // Equivalent to d = (a * b) / c; -> d = 6 / 4; -> d = 1 (integer division)
d = c % a + b;      // Equivalent to d = (c % a) + b; -> d = (4 % 2) + 3; -> d = 0 + 3; -> d = 3
d = a < b && b < c; // Equivalent to d = (a < b) && (b < c); -> d = (1) && (1); -> d = 1 (true)

int x, y = 5, z = 10;
x = y = z;          // Right-to-left: x = (y = z); -> y becomes 10, x becomes 10    
```

## Related Concepts

- [[Operator_C]] (The symbols whose evaluation order is defined)
- [[Expression_C]] (Where precedence rules apply)
- [[Sequence_Point_C]] (Related concept about when side effects are complete)

---

**Source:** Worksheet C_WS1