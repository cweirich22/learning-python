# Scanner Error Report

Supervisors need to know which scanner faults happen most so they can fix or replace equipment. 
This tool reads a scanner log and produces a ranked count of error types.

## Usage

```
python drills/scanner_error_report.py INPUT_LOG OUTPUT_CSV
```

## Exit codes
| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Input file not found |
| 2 | Incorrect number of arguments |

## Example

scanner.log (first 4 of 13 lines):
```
2026-11-17 08:00 SCN-01 INFO startup
2026-11-17 08:02 SCN-02 ERROR NO_READ
2026-11-17 08:03 SCN-01 ERROR JAM
2026-11-17 08:05 SCN-03 WARN LOW_BATTERY
```

Summary line printed:
```
Found 8 errors across 3 scanners.
```

scanner_errors.csv:
```
error,count
NO_READ,3
JAM,3
TIMEOUT,2
```

## How it works

Uses regex to filter each ERROR line then keeps counts of each scanner and error type.
The error type counts are then sorted from largest to smallest and put into the scanner_errors.csv.