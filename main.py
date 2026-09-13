import argparse
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).parent

def run(lang, filep):
    langd = ROOT / lang
    interpf = langd / "interpreter.py"
    if not interpf.exists():
        print(f"Error: Language '{lang}' not found.", file=sys.stderr)
        sys.exit(1)
    if not filep.is_file():
        print(f"Error: Source file '{filep}' not found.", file=sys.stderr)
        sys.exit(1)
    code = filep.read_text(encoding="utf-8")
    module = importlib.import_module(f"{lang}.interpreter")
    if hasattr(module, "run"):
        module.run(code)
    else:
        print(f"Error: '{lang}/interpreter.py' has no run() function.", file=sys.stderr)
        sys.exit(1)
        
def spec(lang):
    specf = ROOT / lang / "spec.md"
    if not specf.exists():
        print(f"Error: No spec.md found for '{lang}'.", file=sys.stderr)
        sys.exit(1)
    print(specf.read_text("utf-8"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="esopy runner")
    subparsers = parser.add_subparsers(dest="command", required=True)
    runp = subparsers.add_parser("run", help="Run esolang script")
    runp.add_argument("lang", help="Directory name of the language")
    runp.add_argument("file", type=Path, help="Path to code file")
    infop = subparsers.add_parser("spec", help="View language spec")
    infop.add_argument("lang", help="Directory name of the language")

    args = parser.parse_args()
    if args.command == "run":
        run(args.lang, args.file)
    elif args.command == "spec":
        spec(args.lang)