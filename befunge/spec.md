# Befunge-93
**Designed by:** Chris Pressey\
**Paradigm:** two-dimensional, stack-based, imperative\
**More:** [https://esolangs.org/wiki/Befunge](https://esolangs.org/wiki/Befunge)

## Overview
Befunge-93 is a two-dimensional esolang designed with the goal of being as difficult to compile as possible.

Programs are laid out on a fixed 80x25 grid. Execution starts at the top-left moving right, controlled by an instruction pointer (IP) that can change direction dynamically. Data is stored on a single standard LIFO stack, and non-instruction characters push their ASCII values to the stack.

## Instructions
| Symbol | Action |
| --- | --- |
| `0`-`9` | Push this number onto the stack |
| `+` | Addition: Pop *a* and *b*, push *a* + *b* |
| `-` | Subtraction: Pop *a* and *b*, push *b* - *a* |
| `*` | Multiplication: Pop *a* and *b*, push *a* * *b* |
| `/` | Integer division: Pop *a* and *b*, push *b* / *a* |
| `%` | Modulo: Pop *a* and *b*, push *b* mod *a* |
| `!` | Logical NOT: Pop a value; push 1 if 0, else 0 |
| `` ` `` | Greater than: Pop *a* and *b*, push 1 if *b* > *a*, else 0 |
| `>` | Move right |
| `<` | Move left |
| `^` | Move up |
| `v` | Move down |
| `?` | Move in a random direction |
| `_` | Horizontal IF: Pop a value; move right if 0, else left |
| `\|` | Vertical IF: Pop a value; move down if 0, else up |
| `"` | Toggle String mode: Push ASCII values of characters until next `"` |
| `:` | Duplicate value on top of stack |
| `\` | Swap top two values on stack |
| `$` | Pop value from stack and discard it |
| `.` | Pop value and output as integer |
| `,` | Pop value and output as ASCII character |
| `#` | Trampoline: Skip next cell |
| `g` | Get: Pop *y* and *x*, push ASCII value of character at (*x*, *y*) in grid |
| `p` | Put: Pop *y*, *x*, and *v*, change character at (*x*, *y*) in grid to ASCII value *v* |
| `&` | Input integer and push onto stack |
| `~` | Input character and push ASCII value onto stack |
| `@` | End program |
| *space* | No-op, execution continues in current direction |