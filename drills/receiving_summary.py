import csv

def parse_receipt(line): # creates a function called parse_receipt which has one parameter called line
    stripped = line.strip() # takes the line and strips it then assigns it to stripped
    parts = stripped.split(",") # splits stripped based on commas which is assigned to parts
    if len(parts) != 3: # checks that the line didn't split into exactly 3 pieces (po, sku, qty)
        raise ValueError("bad line") # raises ValueError("bad line") 
    po = parts[0].strip().upper() # parts index 0 is stripped of whitespace and put into uppercase which is assigned to po
    sku = parts[1].strip().upper() # parts index 1 is stripped of whitespace and put into uppercase which is assigned to sku
    qty_text = parts[2].strip() # parts index 2 is stripped of whitespace and assigned to qty_text
    if not qty_text.isdigit(): # checks if qty_text is not digits
        raise ValueError("bad line") # stops this function and flags the line as bad
    return {"po": po, "sku": sku, "qty": int(qty_text)} # returns a dict with po, sku, and qty converted to an int

def main(): # creates the main function
    skipped = 0 # assigns skipped a running total starting at zero
    records = [] # assigns records an empty list
    with open("drills/receiving.txt") as f: # opens receiving.txt for reading as f; it closes automatically when this block ends
        for line in f: # loops through each line in f
            try: # try to parse the line; if it raises ValueError, jump to except
                record = parse_receipt(line) # runs parse_receipt on this line and stores the returned dict in record
                records.append(record) # appends record to the records list
            except ValueError: # the line was bad, so skip the append and count it instead of crashing
                skipped += 1 # adds one to skipped
    totals = {} # assigns an empty dictionary to totals
    for record in records: # loops through each record in records
        totals[record["sku"]] = totals.get(record["sku"], 0) + record["qty"] # add this record's qty to the running total for its sku (0 if the sku isn't in totals yet)
    with open("drills/receiving_summary.csv", "w", newline="") as out: # opens receiving_summary.csv as out in write mode which creates the file or clears an existing one 
        writer = csv.writer(out) # creates a csv writer for out assigned to writer
        writer.writerow(["sku", "total_qty"]) # writes the header row: sku, total_qty
        for sku, qty in totals.items(): # loops through totals using items() to get the sku and qty
            writer.writerow([sku, qty]) # writes the sku and qty to the csv
    print(f"Read {len(records)} records, skipped {skipped} bad lines.") # f string saying how many record were read along with how many lines were skipped

if __name__ == "__main__": # only run main() when this file is run directly, not when it's imported
    main() # calls main to start the program