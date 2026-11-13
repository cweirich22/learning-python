# load re, csv, and os
import re
import csv
import os
# folder this script lives in: os.path.dirname(os.path.abspath(__file__))
folder = os.path.dirname(os.path.abspath(__file__))
# full paths for labels_messy.txt, parsed_labels_v4.csv, bad_labels.txt using os.path.join
labels_messy_path = os.path.join(folder, "labels_messy.txt")
parsed_labels_v4_path = os.path.join(folder, "parsed_labels_v4.csv")
bad_labels_path = os.path.join(folder, "bad_labels.txt")
# forgiving pattern: r"(SKU-\d+)\s*\|\s*QTY:?\s*(\d+)\s*\|\s*(PO-\d{5})"
forgiving_pattern = r"(SKU-\d+)\s*\|\s*QTY:?\s*(\d+)\s*\|\s*(PO-\d{5})"
# def parse_label(label):
def parse_label(label):
    # fullmatch label with the pattern, using flags=re.IGNORECASE
    label = label.strip()
    match = re.fullmatch(forgiving_pattern, label, flags=re.IGNORECASE)
    # if no match, raise ValueError
    if not match:
        raise ValueError(f"bad label: {label!r}")
    # return a dict with sku uppercased, qty as int, po uppercased
    return {"sku": match.group(1).upper(), "qty": int(match.group(2)), "po": match.group(3).upper()}

# def main():
def main():
    # empty records list, empty bad_lines list
    records = []
    bad_lines = []
    # open the input file
    with open(labels_messy_path) as f:
        # loop with: for line_num, line in enumerate(f, start=1):
        for line_num, line in enumerate(f, start=1):
            # try: parse, append the record
            try:
                record = parse_label(line)
                records.append(record)
            # except ValueError: append f"line {line_num}: {line.strip()}" to bad_lines
            except ValueError:
                bad_lines.append(f"line {line_num}: {line.strip()}")

    # open the CSV in "w" with newline=""
    with open(parsed_labels_v4_path, "w", newline="") as out:
        # writer = csv.DictWriter(out, fieldnames=["sku", "qty", "po"])
        writer = csv.DictWriter(out, fieldnames=["sku", "qty", "po"])
        # writer.writeheader()
        writer.writeheader()
        for record in records:
            # write each record with writer.writerow(record)
            writer.writerow(record)
    # open bad_labels.txt in "w"
    with open(bad_labels_path, "w") as out:
        # write each bad line followed by "\n"
        for line in bad_lines:
            out.write(line + "\n")
            
    # print f"Parsed {len(records)} labels, skipped {len(bad_lines)} bad lines."
    print(f"Parsed {len(records)} labels, skipped {len(bad_lines)} bad lines.")

# __main__ guard calling main()
if __name__ == "__main__":
    main()

# PREDICTIONS: 
# Which lines fail?
# Lines 4, 5, and 7.
# Exact contents of the CSV: 
# sku,qty,po
# SKU-1042,12,PO-55012
# SKU-2210,3,PO-55013
# SKU-3301,40,PO-55014
# SKU-4410,8,PO-55016  
# Exact contents of bad_labels.txt:
# line 4: SKU-77 | QTY: | PO-55015
# line 5: damaged pallet, no label
# line 7: SKU-5120 | QTY: 6 | PO-5501
