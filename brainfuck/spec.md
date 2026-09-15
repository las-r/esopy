# Brainfuck
**Designed by:** Urban Müller\
**Paradigm:** cell-based, imperative\
**More:** [https://esolangs.org/wiki/Brainfuck](https://esolangs.org/wiki/Brainfuck)

## Overview
Brainfuck is arguably the most famous and well-known esolang, being Turing-complete with only 8 single-character instructions. 

Programs are executed left-to-right and halt when the source code ends. The cell tape is infinitely long in both directions and cell values have an 8-bit integer width.

## Instructions
| Symbol | Action |
|---|---|
| `>` | Move cell pointer right |
| `<` | Move cell pointer left |
| `+` | Increment cell at pointer |
| `-` | Decrement cell at pointer |
| `.` | Output UTF-8 character of cell at pointer |
| `,` | Input character and store in cell at pointer |
| `[` | Jump ahead of next `]` if cell at pointer is 0 |
| `]` | Jump back to last `[]` if cell at pointer is not 0 |
| *anything else* | Ignored, considered as comments |