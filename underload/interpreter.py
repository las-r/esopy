import sys

# Underload
# Interpreter by las-r

def run(code: str, stk: list = []) -> None:
    i = 0
    pstr = ""
    
    while i < len(code):
        char = code[i]
        
        if char == "(":
            depth = 1
            pstr = ""
            i += 1
            while i < len(code) and depth > 0:
                if code[i] == "(":
                    depth += 1
                elif code[i] == ")":
                    depth -= 1
                if depth > 0:
                    pstr += code[i]
                    i += 1
            stk.append(pstr)
        else:
            match char:
                case "~": stk[-1], stk[-2] = stk[-2], stk[-1]
                case ":": stk.append(stk[-1])
                case "!": stk.pop()
                case "*":
                    a, b = stk.pop(), stk.pop()
                    stk.append(b + a)
                case "a": stk.append(f"({stk.pop()})")
                case "^": run(stk.pop(), stk)
                case "S":
                    sys.stdout.write(stk.pop())
                    sys.stdout.flush()
            i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        print("FALLBACK PROGRAM: Fibonacci Numbers")
        code = "(()(*))(~:^:S*a~^a~!~*~:(/)S^):^"

    run(code)