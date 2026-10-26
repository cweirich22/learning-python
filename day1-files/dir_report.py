import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(script_dir, "report.txt")

def dir_report(folder):
    total_kb = 0
    lines = []

    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        size_kb = os.path.getsize(path) / 1024
        total_kb += size_kb
        lines.append(f"{name}: {size_kb:.2f} KB")

    lines.append(f"TOTAL: {total_kb:.2f} KB")

    with open(report_path, "w") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    dir_report(folder)