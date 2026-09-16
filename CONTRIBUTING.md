# Contributing
Thank you for wanting to contribute to EsoPy! Anyone is welcome to submit pull requests, report issues, or suggest new esolangs.

## Adding a New Esolang
When submitting a new language implementation, please place it in its own folder at the root of the repository:

```text
esopy/
    your_esolang_name/
        examples/        # Collection of example programs (Not required but highly recommended)
        interpreter.py   # Python implementation
        spec.md          # Language specification & instruction set

```

### Interpreter Template
Your `interpreter.py` must adhere to this standard execution layout so every language in the repository remains consistent:

```python
import sys
import whatever_other
import imports_you_need

# LanguageName
# Interpreter by your-github-username-or-whatever-you-go-by

def run(code: str) -> None:
    # PUT YOUR MAIN INTERPRETING CODE IN HERE.
    # YOU CAN USE ANY SPACE ABOVE FOR OOP OR HELPER FUNCTIONS.
    pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        print("FALLBACK PROGRAM: Simple Description For Fallback Program")
        code = "<fallback example code>"

    run(code)
```

### Language Spec Template
```md
# Language Name
**Designed by:** author-name
**Paradigm:** paradigm-type (e.g. stack-based, tape-based, 2D grid, imperative)
**More:** external.link-for-more.info (e.g. an esolangs.org page)

## Overview
A brief high-level description of how the language works, how code is read (e.g., left-to-right, 2D execution pointer), and the termination condition for programs.

<!-- And then you can do whatever you want! Try to be detailed to the point where someone else can be able to write their own interpreter from the ground up based on the spec alone. -->
```

## Modifying an Existing Esolang
If you are fixing a bug, refactoring, or optimizing an existing interpreter:
- **Preserve the CLI interface:** Ensure `run(code: str)` and the `sys.argv` fallback check remain unchanged.
- **Update `spec.md`:** If your change affects instruction behavior, syntax edge cases, or memory limits, update the corresponding `spec.md` file in that language's directory.
- **Test the fallback:** Verify that running `python <language>/interpreter.py` without arguments still executes the default test program cleanly.

If you are adding a new example to an existing language:
- **Give proper credit:** Check licenses and include the author's name at the top of the program, if the author is known. If the language doesn't support comments, then please add the file's name and author's name to the `credits.txt` in the examples folder. If there is no `credits.txt` file in the example folder, then feel free to create it.
- **Avoid duplicates:** Do not submit minified versions of existing code. Submissions must use a distinct algorithm or approach to be considered new.

## Other General Rules
- Please try to not run your autolinter on the entire repository, we want to keep our diffs neat.