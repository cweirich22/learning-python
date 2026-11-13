import pytest
from valid_sku import is_valid_sku

@pytest.mark.parametrize("text, expected", [
    ("SKU-0042", True),
    ("sku-0042", False),
    ("SKU-99", False),
    ("ASKU-9900", False),
    ("SKU-", False),
    ("AKU-4009", False),
    (" SKU-1234  ", True),
    (" SKU-0042 \n", True),
])
def test_is_valid_sku(text, expected):
    assert is_valid_sku(text) == expected