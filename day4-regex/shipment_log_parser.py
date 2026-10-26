import csv
import os
import re
import sys

PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) "
    r"(RECEIVED|SHIPPED|ADJUST) (SKU-\d+) QTY (-?\d+) LOC (\S+)$"
)

def parse_line(line):
    match = PATTERN.fullmatch(line.strip())
    if not match:
        return None
    date, time, action, sku, qty, loc = match.groups()
    return {
        "date": date,
        "time": time,
        "action": action,
        "sku": sku,
        "qty": int(qty),
        "location": loc,
    }

def parse_file(input_path, output_path):
    rows = []
    skipped = 0
    with open(input_path) as f:
        for line in f:
            if not line.strip():
                continue
            row = parse_line(line)
            if row is None:
                skipped += 1
            else: 
                rows.append(row)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["date", "time", "action", "sku", "qty", "location"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f'Wrote {len(rows)} rows, skipped {skipped}')

def main():
    if len(sys.argv) != 3:
        print("Usage: python shipment_log_parser.py <input_log> <output_csv>")
        sys.exit(1)
    input_path, output_path = sys.argv[1], sys.argv[2]
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        sys.exit(1)
    parse_file(input_path, output_path)

if __name__ == "__main__":
    main()