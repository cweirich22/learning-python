# Cycle Count

Cycle counts catch bins where the physical count doesn't match the system. This script converts a raw log file into a CSV of every bin's variance. Analyst's can then see which bins need a recount.

## Input

A log file, `cycle_counts.log`, with count lines that are mixed in with other log lines (INFO, WARN), which get skipped:
```
2026-11-18 07:58:40 INFO CC session start user=jlopez
2026-11-18 08:01:12 CC BIN=A3-04 SKU=SKU-1042 EXPECTED=12 COUNTED=10
2026-11-18 08:09:02 CC BIN=B1-02 SKU=SKU-3301 EXPECTED=24 COUNTED=
2026-11-18 08:14:30 WARN scanner battery low SCN-03
```

## Output

A CSV with columns bin, sku, expected, counted, variance (variance = counted - expected).
```
bin,sku,expected,counted,variance
A3-04,SKU-1042,12,10,-2
A3-05,SKU-2210,40,40,0
B1-01,SKU-0077,5,8,3
B1-03,SKU-1042,6,6,0
C2-07,SKU-5150,100,93,-7
```
(This summary is based on a log file with 10 lines)
Summary line: Parsed 5 counts, 3 with variance, 2 bad lines.
Two stderr examples that are reported on stderr:
```
2026-11-18 08:09:02 CC BIN=B1-02 SKU=SKU-3301 EXPECTED=24 COUNTED=
2026-11-18 08:18:44 CC BIN=C2-08 SKU-9999 EXPECTED=10 COUNTED=10
```

## How to run

```
python drills/cycle_count_report.py INPUT_LOG OUTPUT_CSV
```

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Input file not found |
| 2 | Invalid usage - needs 2 arguments |
| 3 | Contains bad lines |

## Rules

- Each line inside the log file must contain " CC BIN=" to be counted. Lines without it are skipped silently, not counted as bad.
- A good count line has a bin like `A3-04` (letter, digit, dash, two digits), a SKU like `SKU-1042`, and EXPECTED and COUNTED as whole numbers, with nothing else after COUNTED.
- To separate the good lines from the bad lines each line must fit this regex criteria: 
```
r"^\S+ \S+ CC BIN=(?P<bin>[A-Z]\d-\d{2}) SKU=(?P<sku>SKU-\d{4}) EXPECTED=(?P<expected>\d+) COUNTED=(?P<counted>\d+)$"
```
- A bin "has variance" when counted - expected is not 0.
- Matches to the regex criteria are counted as good lines and non-matches are counted as bad lines.
- Bad lines are printed to stderr with their line number.
- Good lines are counted and another count is made for lines with variance.

## How to run the tests

Run this command in the Terminal:
```
python -m pytest drills/test_cycle_count_report.py -v
```
8 tests, all passing: 5 parse cases (2 good lines, 3 bad lines that must return None) and 3 CLI tests checking exit codes 2 (no args), 1 (missing file), and 3 (real log with bad lines, CSV still written).