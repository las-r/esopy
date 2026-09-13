import sys

# Tact
# Interpreter by las-r

def run(code: str) -> None:
    i = 0
    stk = []
    
    while i < len(code):
        char = code[i]
        
        match char:
            case char if char.isdigit(): stk.append(int(char))
            case "*": stk.append(stk.pop() * 10)
            case "+": stk.append(stk.pop() + stk.pop())
            case "-": stk.append((lambda a, b: b - a)(stk.pop(), stk.pop()))
            case "d": stk.append(stk[-1])
            case "x": stk.pop()
            case "s": stk[-1], stk[-2] = stk[-2], stk[-1]
            case "o": stk.append(stk[-2])
            case "j": i = stk.pop() - 1
            case ">": i += 0 if stk.pop() > 0 else 1
            case "<": i += 0 if stk.pop() < 0 else 1
            case "i": stk.append(int(input("Value input: ")))
            case "p": print(stk[-1])
            case _: raise Exception(f"Unknown character: {char}")
        
        #print(f"{i} ({char}), {stk}")
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        print("FALLBACK PROGRAM: Nth Triangular Number")
        code = "0iso+s1-d2s>jxxp"

    run(code)