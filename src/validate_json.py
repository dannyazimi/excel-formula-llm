import json
import sys

REQUIRED_KEYS = [
    "clarifying_questions", "assumptions", "formula", "explanation",
    "warnings", "alternatives", "confidence"
]

def validate(obj: dict) -> list[str]:
    errors = []
    for k in REQUIRED_KEYS:
        if k not in obj:
            errors.append(f"Missing key: {k}")
    if "formula" in obj:
        if not isinstance(obj["formula"], dict):
            errors.append("formula must be an object")
        else:
            if "excel" not in obj["formula"]:
                errors.append("formula.excel missing")
            if obj["formula"].get("google_sheets", None) is not None:
                errors.append("formula.google_sheets must be null for v1")
    if "confidence" in obj and not isinstance(obj["confidence"], (int, float)):
        errors.append("confidence must be a number")
    return errors

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            ex = json.loads(line)
            errs = validate(ex["output"])
            if errs:
                print(f"Line {i} errors:")
                for e in errs:
                    print("  -", e)
                sys.exit(1)
    print("OK: all outputs match basic schema.")