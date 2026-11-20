# run as: python -m pytest drills/test_cycle_count_report.py -v
import csv # loads the csv module
import subprocess # loads the subprocess module
import sys # loads the sys module

import pytest # loads the pytest module

from cycle_count_report import parse_count_line # loads the parse_count_line function from cycle_count_report

SCRIPT = "drills/cycle_count_report.py" # filepath that tests will be run on


@pytest.mark.parametrize(
    "line, expected", # names of the two values each case provides
    [
        ("2026-11-18 08:01:10 CC BIN=A3-04 SKU=SKU-1042 EXPECTED=12 COUNTED=10", # the string will run though parse_count_line function and return a dictionary
         {"bin": "A3-04", "sku": "SKU-1042", "expected": 12, "counted": 10}), # this is the expected value which will be a match
        ("2026-11-18 08:02:00 CC BIN=B1-01 SKU=SKU-0077 EXPECTED=5 COUNTED=8", # the string will run though parse_count_line function and return a dictionary
         {"bin": "B1-01", "sku": "SKU-0077", "expected": 5, "counted": 8}), # this is the expected value which will be a match
        ("2026-11-18 08:09:02 CC BIN=B1-02 SKU=SKU-3301 EXPECTED=24 COUNTED=", None), # this will return None because counted is missing digits
        ("2026-11-18 08:18:44 CC BIN=C2-08 SKU-9999 EXPECTED=10 COUNTED=10", None), # this will return None because the string is missing "SKU="
        ("2026-11-18 08:20:00 CC BIN=A1-01 SKU=SKU-1 EXPECTED=ten COUNTED=10", None), # this will return None because SKU needs 4 digits and only has 1 and expected shows ten as a word rather than digits. Fails for either reason.
    ],
)
def test_parse_count_line(line, expected): # pytest calls this once per case
    result = parse_count_line(line) # the line is passed into the parse_count_line function and stored isnide result
    if expected is None: # checks if expected is None
        assert result is None # makes sure the result is equal to None
    else: # if expected isn't None then 
        for key in expected: # loops through each key in expected
            assert result[key] == expected[key] # checks that the value for each key in result matches the expected value


def test_cli_no_args_exits_2(): # running with no args should be a usage error
    r = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True) # run the CLI with no extra args
    assert r.returncode == 2 # usage error code


def test_cli_missing_file_exits_1(tmp_path): # running with a missing file should be a filenotfounderror
    out = tmp_path / "out.csv" # sets the out path to tmp_path joined with out.csv
    r = subprocess.run([sys.executable, SCRIPT, "no_such_file.log", str(out)], # runs the CLI with two args, input file is missing
                       capture_output=True, text=True)
    assert r.returncode == 1 # file is missing or doesn't exist error code


def test_cli_real_log_exits_3_and_writes_csv(tmp_path): # has bad lines but still parses the good lines to the csv
    out = tmp_path / "out.csv" # sets the out path to tmp_path joined with out.csv
    r = subprocess.run([sys.executable, SCRIPT, "drills/cycle_counts.log", str(out)], # runs the CLI with two args, input file is valid
                       capture_output=True, text=True)
    assert r.returncode == 3 # has bad lines but still parses the good lines to the csv
    with open(out, newline="") as f: # opens output path in default mode and uses the built in csv newline method then assigning this to f
        rows = list(csv.DictReader(f)) # creates a list of all the dictionaries inside f
    assert rows[0]["bin"] == "A3-04" # checks that the first row key bin is equal to the value "A3-04"
    assert rows[0]["variance"] == "-2" # checks that the first row key variance is equal to the value "-2"

# PREDICTIONS:
# Total tests: 8, 5 parametrize tests and 3 exit code tests
# Every test will pass
# parametrize tests line matches expected in every case
# test_cli_no_args_exits_2 exit code is 2 which matches since script needs exactly 2 args and got 0
# test_cli_missing_file_exits_1 exit code is 1 which matches since the input file is missing
# test_cli_real_log_exits_3_and_writes_csv exit code is 3 since theres two bad lines and the good lines are parsed to the csv and match the two checks
# $LASTEXITCODE will be 0 since every single test passed

# Break parametrize test on purpose and write what pytest showed:
# changing the counted to 11 in the first test failed the test because this no longer matched the expected value for counted. line was 11 while expected was 10.
# Updated the fix so it's no longer in the code