# Goal: prove parse_label handles clean, lowercase, and bad labels.

import pytest # loads the pytest module
from label_parser_v3 import parse_label # imports parse_label function from lavel_parser_v3 file

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

def test_missing_qty_raises_valueerror(): # creates a function called test_missing_qty_raises_valueerror with no parameter
    with pytest.raises(ValueError): # checks to see if missing qty rasises a ValueError
        parse_label("SKU-2210 | PO-55013") # runs the parse_label function with the string

# PREDICTION:
# test_clean_label_returns_expected_dict will match the dictionary provided
# test_lowercase_label_is_uppercased both of these will pass
# test_qty_is_an_int this will pass because it turns every quantity into an integer
# test_missing_qty_raises_valueerror will pass a ValueError
# all four will pass