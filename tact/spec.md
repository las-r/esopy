# Tact
**Designed by:** las-r\
**Paradigm:** stack-based, imperative

## Overview
Tact programs are a single string of characters executed left to right. The program halts when the pointer runs past the end of the source.

## Instructions
| Char | Name | Effect |
|---|---|---|
| `0`-`9` | Push digit | Pushes that digit onto the stack |
| `*` | Times ten | Pop `a`, push `a * 10` (used to build multi-digit numbers) |
| `+` | Add | Pop `a`, `b`, push `a + b` |
| `-` | Subtract | Pop `a`, `b`, push `b - a` (second-popped minus first-popped) |
| `d` | Duplicate | Push a copy of the top element |
| `x` | Discard | Pop and discard the top element |
| `s` | Swap | Swap the top two elements |
| `o` | Over | Push a copy of the second-from-top element |
| `j` | Jump | Pop `n`, set instruction pointer to index `n` |
| `>` | Skip-if-positive | Pop `n`; if `n > 0` continue normally, else skip the next instruction |
| `<` | Skip-if-negative | Pop `n`; if `n < 0` continue normally, else skip the next instruction |
| `i` | Input | Prompt user, read an integer, push it |
| `p` | Print | Print the top of stack (without popping) |

**Notes:**
- Any operation popping from an empty stack crashes the interpreter since there's no bounds checking.