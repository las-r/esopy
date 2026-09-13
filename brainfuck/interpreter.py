import sys

# Brainfuck
# Interpreter by las-r

def run(code: str) -> None:
    i = 0
    tape = [0]
    ptr = 0
    
    while i < len(code):
        char = code[i]
        
        match char:
            case ">":
                ptr += 1
                if ptr >= len(tape):
                    tape.append(0)
            case "<":
                ptr -= 1
                if ptr < 0:
                    ptr = 0
                    tape.insert(0, 0)
            case "+": tape[ptr] = (tape[ptr] + 1) % 256
            case "-": tape[ptr] = (tape[ptr] - 1) % 256
            case ".": print(chr(tape[ptr]), end="", flush=True)
            case ",": 
                uin = sys.stdin.read(1)
                tape[ptr] = ord(uin) if uin else 0
            case "[":
                if tape[ptr] == 0:
                    depth = 1
                    while depth > 0:
                        i += 1
                        if i >= len(code):
                            break
                        if code[i] == "[":
                            depth += 1
                        elif code[i] == "]":
                            depth -= 1
            case "]":
                if tape[ptr] != 0:
                    depth = 1
                    while depth > 0:
                        i -= 1
                        if i < 0:
                            break
                        if code[i] == "]":
                            depth += 1
                        elif code[i] == "[":
                            depth -= 1
    
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        print("FALLBACK PROGRAM: Hello World")
        code = "+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+."

    run(code)