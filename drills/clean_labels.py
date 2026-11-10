import csv

def clean_label(text): # creates a function called clean_label which takes in the text parameter
    line = text.strip() # strips whitespace from both ends of the text and assigns it to line
    parts = line.split(",") # splits line on each comma into a list
    if len(parts) != 2: # checks if parts does NOT have exactly 2 pieces.
        raise ValueError("bad line") # stops the function and signals a bad line so main can skip it
    sku = parts[0].strip().upper() # parts[0] is the sku which is stripped of whitespace and put into uppercase and assigned to sku
    qty_text = parts[1].strip() # strips the whitespace off parts[1], the qty, and saves it as qty_text (still text)
    if not (sku[:4] == "SKU-" and len(sku) == 7 and sku[4:].isdigit()) or not qty_text.isdigit(): # checks if the sku is equal to SKU- and the length is equal to 7 and the last three characters are digits and also checks if the quantity is only digits
        raise ValueError("bad line") # stops the function and signals a bad line so main can skip it
    return sku, int(qty_text) # returns sku and the qty converted to an int

def main(): # creates a main function
    skipped = 0 # assigns zero integer to skipped
    rows = [] # assigns an empty list to rows
    with open("drills/labels.txt") as f: # opens the labels.txt file as f
        for line in f: # loops through each line
            try: # attempt to clean this line
                sku, qty = clean_label(line) # sends the line to clean_label and unpacks the returned sku and qty
                rows.append([sku, qty]) # adds [sku, qty] as one list to rows
            except ValueError: # if clean_label rejected the line, handle it here instead of crashing
                skipped += 1 # adds 1 to the skipped total
    with open("drills/clean_labels.csv", "w", newline="") as out: # creates an empty csv or wipes out an existing one using write mode as out
        writer = csv.writer(out) # creates a writer for out
        writer.writerow(["SKU", "QTY"]) # writes the header with SKU and QTY split by a comma
        writer.writerows(rows) # each row is a list, so it writes one row per inner list
    print(f"Skipped {skipped} bad lines.") # f string with the total count of skipped 

if __name__ == "__main__": # only run main when this file is run directly, not imported
    main() # run the program