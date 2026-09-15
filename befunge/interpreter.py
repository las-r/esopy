import random
import sys
import textwrap

# Befunge-93 Interpreter
# Interpreter by las-r

def pop(stk: list) -> int:
    return stk.pop() if stk else 0

def run(code: str) -> None:
    pf = [[' '] * 80 for _ in range(25)]
    for y, line in enumerate(code.splitlines()[:25]):
        for x, char in enumerate(line[:80]):
            pf[y][x] = char

    stk = []
    pc = [0, 0]
    pcd = (1, 0)
    asciim = False
    
    while True:
        i = pf[pc[1]][pc[0]]
        
        if asciim:
            if i == '"':
                asciim = False
            else:
                stk.append(ord(i))
        else:
            match i:
                case i if i.isdigit(): stk.append(int(i))
                case "+": stk.append(pop(stk) + pop(stk))
                case "-":
                    a, b = pop(stk), pop(stk)
                    stk.append(b - a)
                case "*": stk.append(pop(stk) * pop(stk))
                case "/":
                    a, b = pop(stk), pop(stk)
                    if a == 0:
                        stk.append(int(input("Division by zero! Enter result: ")))
                    else:
                        stk.append(b // a)
                case "%":
                    a, b = pop(stk), pop(stk)
                    stk.append(0 if a == 0 else b % a)
                case "!": stk.append(1 if pop(stk) == 0 else 0)
                case "`":
                    a, b = pop(stk), pop(stk)
                    stk.append(1 if b > a else 0)
                case ">": pcd = (1, 0)
                case "<": pcd = (-1, 0)
                case "^": pcd = (0, -1)
                case "v": pcd = (0, 1)
                case "?": pcd = random.choice([(1, 0), (-1, 0), (0, -1), (0, 1)])
                case "_": pcd = (1, 0) if pop(stk) == 0 else (-1, 0)
                case "|": pcd = (0, 1) if pop(stk) == 0 else (0, -1)
                case '"': asciim = True
                case ":":
                    v = pop(stk)
                    stk.extend([v, v])
                case "\\":
                    a, b = pop(stk), pop(stk)
                    stk.extend([a, b])
                case "$": pop(stk)
                case ".": print(f"{pop(stk)}", end="", flush=True)
                case ",": print(chr(pop(stk)), end="", flush=True)
                case "#":
                    pc[0] = (pc[0] + pcd[0]) % 80
                    pc[1] = (pc[1] + pcd[1]) % 25
                case "g":
                    y, x = pop(stk), pop(stk)
                    if 0 <= y < 25 and 0 <= x < 80:
                        stk.append(ord(pf[y][x]))
                    else:
                        stk.append(0)
                case "p":
                    y, x, v = pop(stk), pop(stk), pop(stk)
                    if 0 <= y < 25 and 0 <= x < 80:
                        pf[y][x] = chr(v % 256)
                case "&": stk.append(int(input("Integer input: ")))
                case "~":
                    char = sys.stdin.read(1)
                    stk.append(ord(char) if char else -1)
                case "@": break

        pc[0] = (pc[0] + pcd[0]) % 80
        pc[1] = (pc[1] + pcd[1]) % 25

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        print("FALLBACK PROGRAM: Fibonacci Sequence")
        code = textwrap.dedent(r"""
            0:09p1>09g\:09p+:.84*,v
                  ^             <
        """).strip("\n")

    run(code)