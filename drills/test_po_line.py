# run as: python -m pytest drills/test_po_line.py -v

import pytest # loads the pytest module
from po_line import parse_po_line # loads the parse_po_line function from po_line

@pytest.mark.parametrize(
    "line, expected", # names of the two values each case provides
    [
        ("PO-55012,SKU-1042,ORDERED=12,RECEIVED=10", # the string will run through parse_po_line function and return a dictionary
         {'po': 'PO-55012', 'sku': 'SKU-1042', 'ordered': 12, 'received': 10, 'short': 2}), # this is the expected value which will match
        ("PO-55013,SKU-2210,ORDERED=5,RECEIVED=8",
         {'po': 'PO-55013', 'sku': 'SKU-2210', 'ordered': 5, 'received': 8, 'short': -3}),
        (" PO-55014,SKU-3301,ORDERED=20,RECEIVED=20\n",
         {'po': 'PO-55014', 'sku': 'SKU-3301', 'ordered': 20, 'received': 20, 'short': 0},),
    ],
)
def test_good_lines(line, expected): # pytest calls this once per case
    result = parse_po_line(line) # the line is passed into parse_po_line and the result is stored inside result
    assert result == expected # makes sure the result is equal to expected


@pytest.mark.parametrize(
    "line", # name of the single value each case provides
    [
        "PO-5501,SKU-1042,ORDERED=12,RECEIVED=10", # the string will run through parse_po_line function and raises a ValueError because PO has 4 digits
        "PO-55021,SKU-2210,ORDERED=twelve,RECEIVED=8", # the string will run through parse_po_line function and raises a ValueError because \d+ doesn't match any digits
        "", # the string will run through parse_po_line function and raises a ValueError because there is no match to the pattern
        "PO-55045,SKU-2210,ORDERED=5", # the string will run through parse_po_line function and raises a ValueError because received is completely missing
    ],
)
def test_bad_lines_raises_valueerror(line): # pytest calls this once per case 
    with pytest.raises(ValueError): # the test passes only if the indented code raises a ValueError, and fails if it returns normally
        parse_po_line(line) # calls parse_po_line on the bad line, which should raise

# PREDICT how many of the 7 pass:
# 7
# Which pass and which fail?
# PASS
# PASS
# PASS
# PASS
# PASS
# PASS
# PASS