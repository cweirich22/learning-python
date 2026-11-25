# run as: python drills/po_line.py
import re # loads the re module

PO_PATTERN = re.compile(r"(?P<po>PO-\d{5}),(?P<sku>SKU-\d{4}),ORDERED=(?P<ordered>\d+),RECEIVED=(?P<received>\d+)") # creates a regex pattern with named capture groups then saves the pattern


def parse_po_line(line): # creates a function called parse_po_line with a parameter called line
    m = PO_PATTERN.fullmatch(line.strip()) # checks for a complete match using PO_PATTERN on line after stripping 
    if m is None: # checks if m has no match
        raise ValueError(f"bad PO line: {line!r}") # if not match then raise ValueError with a f string comment using !r to show the string the way Python writes it (\n included)
    ordered = int(m.group("ordered")) # converts the group ordered into an integer then stores the result inside ordered
    received = int(m.group("received")) # converts the group received into an integer then stores the result inside received
    return { # returns a dictionary with keys along with the groups po and sku, then uses ordered and received for the other three key value pairs
        "po": m.group("po"),
        "sku": m.group("sku"),
        "ordered": ordered,
        "received": received,
        "short": ordered - received,
    }


if __name__ == "__main__": # only runs this block when the file is run directly
    print(parse_po_line("PO-55012,SKU-1042,ORDERED=12,RECEIVED=10")) # print the result of parse_po_line with the line passed
    print(parse_po_line("  PO-55013,SKU-2210,ORDERED=5,RECEIVED=8\n")) # print the result of parse_po_line with the line passed

# PREDICT (both printed lines):
# {'po': 'PO-55012', 'sku': 'SKU-1042', 'ordered': 12, 'received': 10, 'short': 2}
# {'po': 'PO-55013', 'sku': 'SKU-2210', 'ordered': 5, 'received': 8, 'short': -3}