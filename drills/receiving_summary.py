import csv

# define parse_receipt that takes one line
def parse_receipt(line):
    # strip the line, then split it on ","
    stripped = line.strip()
    parts = stripped.split(",")
    # if there aren't exactly 3 parts, raise ValueError("bad line")
    if len(parts) != 3:
        raise ValueError("bad line")
    # strip each part; upper() the po and the sku
    po = parts[0].strip().upper()
    sku = parts[1].strip().upper()
    qty_text = parts[2].strip()
    # if qty isn't all digits, raise ValueError("bad line")
    if not qty_text.isdigit():
        raise ValueError("bad line")
    # return a dict with keys "po", "sku", and "qty" (qty as an int)
    return {"po": po, "sku": sku, "qty": int(qty_text)}

print(parse_receipt("PO-502,sku-101 , 8"))

# define main
def main():
    # set skipped to 0
    skipped = 0
    # make an empty list called records
    records = []
    # open "drills/receiving.txt" as f
    with open("drills/receiving.txt") as f:
        # loop over each line in f
        for line in f:
            # try: call parse_receipt(line), save it as record, append record to records
            try:
                record = parse_receipt(line)
                records.append(record)
            # except ValueError: add 1 to skipped
            except ValueError:
                skipped += 1
    # make an empty dict called totals
    totals = {}
    # loop over each record in records
    for record in records:
        # totals[record["sku"]] = totals.get(record["sku"], 0) + record["qty"]
        totals[record["sku"]] = totals.get(record["sku"], 0) + record["qty"]
    # open "drills/receiving_summary.csv" to write with newline="", as out
    with open("drills/receiving_summary.csv", "w", newline="") as out:
        # make a csv.writer
        writer = csv.writer(out)
        # write the header ["sku", "total_qty"]
        writer.writerow(["sku", "total_qty"])
        # loop over totals.items() and write each sku and total as a row
        for sku, qty in totals.items():
            writer.writerow([sku, qty])
    # print how many records were read and how many lines were skipped
        print(f"Read {len(records)} records, skipped {skipped} bad lines.")
# __main__ guard that calls main()
if __name__ == "__main__":
    main()