# Underload
**Designed by:** User:ais523 on esolangs.org\
**Paradigm:** functional, concatenative\
**More:** [https://esolangs.org/wiki/Underload](https://esolangs.org/wiki/Underload)

## Overview
Underload is a stack-based esoteric programming language created by ais523 in 2006, influenced heavily by Muriel. Although not strictly functional, its evaluation operator `^` serves as its sole form of flow control, making programming functional in practice.

Data manipulation relies on Church-numeral-inspired constructs and code execution directly from the stack.

## Commands
| Symbol | Action | Stack Effect |
| --- | --- | --- |
| `~` | Swap the top two elements | `(x) (y) -> (y) (x)` |
| `:` | Duplicate top element | `(x) -> (x) (x)` |
| `!` | Discard top element | `(x) -> ` |
| `*` | Concatenate top element to end of second element | `(x) (y) -> (xy)` |
| `(x)` | Push string enclosed in matching parentheses | `-> (x)` |
| `a` | Enclose top element in parentheses | `(x) -> ((x))` |
| `^` | Execute top element as instructions immediately following `^` | `(x) -> x` |
| `S` | Output top element and pop it | `(x) -> ` |