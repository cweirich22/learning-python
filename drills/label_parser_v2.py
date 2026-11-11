# loads Python's regex module
import re
# loads Python's csv module for writing CSV files
import csv

# assigns a regex pattern to pattern that gets the SKU, Quantity, and PO
pattern = (r"(SKU-\d+) \| QTY: (\d+) \| (PO-\d+)")

# creates a function called parse_label that takes in one parameter called label
def parse_label(label):
    # result of searching through label using pattern
    match = re.search(pattern, label)
    # if the search found nothing (match is None)
    if not match:
        # stops this function and flags the line as bad
        raise ValueError("bad line")
    # the text captured by group 1 (the SKU)
    sku = match.group(1)
    # the text captured by group 2 (the QTY)
    qty = int(match.group(2))
    # the text captured by group 3 (the PO)
    po = match.group(3)
    # returns a dictionary with 'sku', 'qty', and 'po' as keys and sku, qty, and po as values
    return {"sku": sku, "qty": qty, "po":po}

# creates a function called main
def main():
    # assigns 0 to skipped which will be a running total
    skipped = 0
    # empty list that will hold one dict per good label
    records = []
    # opens labels_in.txt for reading as f; closes when the block ends
    with open("drills/labels_in.txt") as f:
        # loops through each line in f
        for line in f:
            # try to parse the line; if it raises ValueError, jump to except
            try:
                # runs parse_label on this line and stores the result in record
                record = parse_label(line)
                # appends the result of record into the records list
                records.append(record)
            # the line was bad, so skip the append and count it instead of crashing
            except ValueError:
                # adds one to skipped 
                skipped += 1
    # opens parsed_labels.csv as out in write mode which creates the file or clears an existing one
    with open("drills/parsed_labels.csv", "w", newline="") as out:
        # creates a csv writer for out which is assigned to writer
        writer = csv.writer(out)
        # writes the header to out
        writer.writerow(["sku", "qty", "po"])
        # loops through each record in records
        for record in records:
            # writes the value of sku, qty, and po from each record
            writer.writerow([record["sku"], record["qty"], record["po"]])
    # prints how many labels were parsed (dicts in records) and how many lines were skipped
    print(f"Parsed {len(records)} and skipped {skipped} lines.")

# only run main() when this file is run directly, not when it's imported
if __name__ == "__main__":
# calls main to start the program
    main()