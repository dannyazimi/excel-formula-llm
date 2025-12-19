import json
from pathlib import Path

payload = {
    "task": "Sum Revenue for East last month excluding Refund",
    "table_name": "Table1",
    "columns": ["Date", "Region", "Revenue", "Type"],
    "sample_rows": [
        {"Date": "2025-11-02", "Region": "East", "Revenue": 1200, "Type": "Sale"},
        {"Date": "2025-11-03", "Region": "East", "Revenue": -200, "Type": "Refund"},
        {"Date": "2025-11-04", "Region": "West", "Revenue": 900, "Type": "Sale"},
    ],
    "constraints": {"excel_version": "365", "locale": "en-US"},
}

system = Path("prompts/system.txt").read_text(encoding="utf-8")
user_tmpl = Path("prompts/user_template.txt").read_text(encoding="utf-8")

user = user_tmpl.format(
    task=payload["task"],
    table_name=payload["table_name"],
    columns=", ".join(payload["columns"]),
    sample_rows=json.dumps(payload["sample_rows"], indent=2),
    excel_version=payload["constraints"]["excel_version"],
    locale=payload["constraints"]["locale"],
)

print("=== SYSTEM ===")
print(system)
print("\n=== USER ===")
print(user)

print("\nNext: wire this to your chosen model (API or local) and print the JSON output.")