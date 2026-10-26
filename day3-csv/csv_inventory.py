import csv
import os
import sys

def csv_inventory(folder, output_path):
    rows = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        rows.append({"filename": name, "size_bytes": os.path.getsize(path)})

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "size_bytes"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(script_dir, "inventory.csv")
    csv_inventory(folder, out)