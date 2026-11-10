import re # loads Python's regex module
import csv # loads Python's csv module for writing CSV files

pattern = (r"(SKU-\d+) \| QTY: (\d+) \| (PO-\d+)") # assigns a regex pattern to pattern that gets the SKU, Quantity, and PO

def parse_label(label): # creates a function called parse_label that takes in one parameter called label
    match = re.search(pattern, label) # result of searching through label using pattern
    if not match: # if the search found nothing (match is None)
        raise ValueError("bad label") # stops this function and flags the line as bad
    sku = match.group(1) # the text captured by group 1 (the SKU)
    qty = int(match.group(2)) # the text captured by group 2 (the QTY)
    po = match.group(3) # the text captured by group 3 (the PO)
    return {"sku": sku, "qty": qty, "po": po} # returns a dictionary with 'sku', 'qty', and 'po' as keys and sku, qty, and po as values

def main(): # creates a function called main
    skipped = 0 # assigns 0 to skipped which will be a running total
    records = [] # empty list that will hold one dict per good label
    with open("drills/labels_in.txt") as f: # opens labels_in.txt for reading as f; closes when the block ends
        for line in f: # loops through each line in f
            try: # try to parse the line; if it raises ValueError, jump to except
                record = parse_label(line) # runs parse_label on this line and stores the result in record
                records.append(record) # appends the result of record into the records list
            except ValueError: # the line was bad, so skip the append and count it instead of crashing
                skipped += 1 # adds one to skipped 
    with open("drills/parsed_labels.csv", "w", newline="") as out: # opens parsed_labels.csv as out in write mode which creates the file or clears an existing one
        writer = csv.writer(out) # creates a csv writer for out which is assigned to writer
        writer.writerow(["sku", "qty", "po"]) # writes the header to out
        for record in records: # loops through each record in records
            writer.writerow([record["sku"], record["qty"], record["po"]]) # writes the value of sku, qty, and po from each record
    print(f"Parsed {len(records)} labels, skipped {skipped} bad lines.") # prints how many labels were parsed (dicts in records) and how many lines were skipped

if __name__ == "__main__": # only run main() when this file is run directly, not when it's imported
    main() # calls main to start the program