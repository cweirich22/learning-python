# Label Parser

Reads shipping labels that come in during receiving which are in a text file. Each one is 
checked with specific format rules to separate the good labels from the bad. Valid labels 
are written into a CSV file with `sku`, `qty`, and `po` as the columns. These valid labels 
are ready for receiving while the bad labels are put into bad_labels.txt for a clerk to review. 
This prevents bad labels from being received against the wrong purchase order.

## Input

A text file, `labels_messy.txt`, with one label per line:

```
SKU-1042 | QTY: 12 | PO-55012
```

## Output

- `parsed_labels_v4.csv`: one row per valid label (`sku,qty,po`)
- `bad_labels.txt`: each rejected line with its line number, for example
  `line 5: damaged pallet, no label`
- prints Parsed 4 labels, skipped 3 bad lines.

## How to run

From the repo root:

```
python drills/label_parser_v4.py
```

## How to run the tests

```
python -m pip install pytest
python -m pytest drills -v
```

## Rules

- The whole line must match the format. Extra characters before or after are rejected.
- Leading and trailing spaces are stripped before checking.
- A SKU is `SKU-` followed by digits.
- A quantity must be a whole number.
- A PO is `PO-` followed by exactly 5 digits.
- Matching is case-insensitive; SKU and PO are saved in uppercase.
- Bad lines go to `bad_labels.txt` with their line numbers.

