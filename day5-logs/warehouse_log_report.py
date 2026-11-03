import csv
import os
import re
import sys
from collections import Counter

LINE_RE = re.compile(r"(\S+ \S+) (INFO|ERROR) \[(\w+)\] (.+)")
SCAN_RE = re.compile(r"Scanned (SKU-\d+) qty=(\d+)")

def parse_line(line):
    # Why: one function = easy to test later
    match = LINE_RE.fullmatch(line.strip())
    if not match:
        return None
    timestamp, level, station, message = match.groups()
    return {"timestamp": timestamp, "level": level, "station": station, "message": message}

def build_reports(path):
    errors = Counter()
    sku_totals = Counter()
    skipped = 0
    with open(path) as f:
        for line in f:
            row = parse_line(line)
            if row is None:
                skipped += 1
                continue
            if row["level"] == "ERROR":
                errors[row["station"]] += 1
            scan = SCAN_RE.search(row["message"])
            if scan:
                sku, qty = scan.groups()
                sku_totals[sku] += int(qty)
    return errors, sku_totals, skipped

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    if len(sys.argv) != 2:
        print("Usage: python warehouse_log_report.py <logfile>", file=sys.stderr)
        sys.exit(1)
    log_path = sys.argv[1]
    if not os.path.exists(log_path):
        print(f"Error: {log_path}  not found", file=sys.stderr)
        sys.exit(1)
        
    errors, sku_totals, skipped = build_reports(log_path)
    out_dir = os.path.dirname(os.path.abspath(__file__))

    write_csv(os.path.join(out_dir, "error_report.csv"),
                ["station", "error_count"],
                [{"station": s, "error_count": c} for s, c in errors.most_common()])
    write_csv(os.path.join(out_dir, "sku_totals.csv"),
                ["sku", "total_qty"],
                [{"sku": s, "total_qty": c} for s, c in sku_totals.most_common()])

    print(f"Done. Skipped {skipped} bad lines.")

if __name__ == "__main__":
    main()


    