# run as: python -m pytest drills/test_top_n.py -v

import pytest # loads the pytest module
from top_n import top_n # loads top_n from top_n.py

PICKS = {"SKU-2210": 7, "SKU-1042": 12, "SKU-4410": 7, "SKU-3301": 3} # assigns a dictionary to PICKS

@pytest.mark.parametrize(
    "counts, n, expected", # names of the three values each case provides
    [
        (PICKS, 3, [('SKU-1042', 12), ('SKU-2210', 7), ('SKU-4410', 7)]), # counts and n will run through top_n function and return a list of sorted tuples
        (PICKS, 10, [('SKU-1042', 12), ('SKU-2210', 7), ('SKU-4410', 7), ('SKU-3301', 3)]),
        ({}, 5, []), # empty dictionary and n will run through top_n function and return an empty list
    ],
)
def test_top_n_cases(counts, n, expected): # pytest calls this once per case
    result = top_n(counts, n) # counts and n is passed into top_n function and stored inside result
    assert result == expected # makes sure the result is equal to expected

def test_negative_n_raises(): # running with a negative n should raise ValueError
    with pytest.raises(ValueError): # the test passes only if the indented code raises a ValueError, and fails if it returns normally
        top_n(PICKS, -3) # calls top_n with n=-3, which hits the n < 0 check and raises

# How many tests will pass?
# 4
# Which tests will pass/ fail?
# PASS
# PASS
# PASS
# PASS