import json, sys

REQUIRED = ["clarifying_questions","assumptions","formula","explanation","warnings","alternatives","confidence"]

def validate_output(o):
    errs=[]
    for k in REQUIRED:
        if k not in o: errs.append(f"Missing {k}")
    if "formula" in o:
        if not isinstance(o["formula"], dict): errs.append("formula must be object")
        else:
            if "excel" not in o["formula"]: errs.append("formula.excel missing")
            if o["formula"].get("google_sheets", None) is not None: errs.append("formula.google_sheets must be null in v1")
    if "confidence" in o and not isinstance(o["confidence"], (int,float)): errs.append("confidence must be number")
    return errs

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path,"r",encoding="utf-8") as f:
        for i,line in enumerate(f, start=1):
            ex = json.loads(line)
            if "input" not in ex or "output" not in ex:
                print(f"Line {i}: must have input and output keys"); sys.exit(1)
            errs = validate_output(ex["output"])
            if errs:
                print(f"Line {i} errors:")
                for e in errs: print(" -", e)
                sys.exit(1)
    print("OK")