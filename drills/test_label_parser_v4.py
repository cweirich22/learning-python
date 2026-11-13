# Goal: prove parse_label handles clean, lowercase, and bad labels.

import pytest # loads the pytest module
from label_parser_v4 import parse_label # imports parse_label function from lavel_parser_v4 file

def test_clean_label_returns_expected_dict(): # creates a function called test_clean_label_returns_expected_dict with no parameter
    result = parse_label("SKU-2210 | QTY:3 | PO-55013") # stores the result of running the string through parse_label function
    assert result == {"sku": "SKU-2210", "qty": 3, "po": "PO-55013"} # checks that `result` equals this expected dictionary

def test_lowercase_label_is_uppercased(): # creates a function called test_lowercase_label_is_uppercased with no parameter
    result = parse_label("sku-2210 | qty:3 | po-55013") # stores the result of running the string through parse_label function
    assert result["sku"] == "SKU-2210" # checks that the sku the function returned equals the expected value
    assert result["po"] == "PO-55013" # checks that the po the function returned equals the expected value

def test_qty_is_an_int(): # creates a function called test_qty_is_an_int with no parameter
    result = parse_label("SKU-2210 | QTY:3 | PO-55013") # stores the result of running the string through parse_label function
    assert isinstance(result["qty"], int) # checks if the qty is an integer

@pytest.mark.parametrize("text", [ # tells pytest to run the test once for each item in the list, instead of once total. The first argument, `"text"`, is the parameter name. It has to match the `text` in `def test_bad_label_raises_valueerror(text):`.
    "SKU-2210 | PO-55013", # Each string in the list is an argument that gets passed into `text` on one of those runs.
    "SKU-1042 | QTY: 12 | PO-550123",
    "XSKU-1042 | QTY: 12 | PO-55012",
])
def test_bad_label_raises_valueerror(text):
    with pytest.raises(ValueError):
        parse_label(text)

def test_padded_line_still_parses(): # creates a function called test_padded_line_still_parses with no parameter
    result = parse_label("  SKU-4410 | QTY: 8 | PO-55016  \n") # stores the result of running parse_label with the string
    assert result == {"sku": "SKU-4410", "qty": 8, "po": "PO-55016"} # checks that `result` equals this expected dictionary

# PREDICTION:
# test_clean_label_returns_expected_dict will match the dictionary provided
# test_lowercase_label_is_uppercased both of these will pass
# test_qty_is_an_int this will pass because it turns every quantity into an integer
# test_missing_qty_raises_valueerror will pass a ValueError
# test_six_digit_po_raises_valueerror will not pass a ValueError since we use re.search
# test_prefix_junk_raises_valueerror will not pass a ValueError since we are using re.search
# test_padded_line_still_parses passes as the result will equal to the output