import subprocess  # run the CLI as a child program
import sys  # sys.executable = the Python running pytest
import pytest  # the testing tool
# import parse_error_line the same way test_label_parser_cli.py imports from its script
from scanner_error_report import parse_error_line

@pytest.mark.parametrize("line, expected", [  # names of the two values each case provides
    ("2026-11-17 08:02 SCN-02 ERROR NO_READ", ("SCN-02", "NO_READ")), # the string will run through parse_error_line function and return a tuple
    ("2026-11-17 08:00 SCN-01 INFO startup", None), # the string will return None when ran through parse_error_line function
    ("2026-11-17 08:05 SCN-03 WARN LOW_BATTERY", None), # the string will return None when ran through parse_error_line function
    ("corrupted entry ###", None), # the string will return None when ran through parse_error_line function
    ("", None) # the string will return None when ran through parse_error_line function
])
def test_parse_error_line(line, expected):  # pytest calls this once per case
    assert parse_error_line(line) == expected  # does the function return what we expect?

# PREDICTION:
# All tests will pass and show 4 tests since balnk line isnt part of scanner.log
# CORRECTION:
# 5 collected, every tuple in the list is it's own test

def test_no_args_exits_2():  # running with no arguments should be a usage error
    r = subprocess.run([sys.executable, "drills/scanner_error_report.py"],  # run the CLI with no extra args
                       capture_output=True, text=True)  # capture stdout/stderr as text
    assert r.returncode == 2  # usage error code

def test_missing_file_exits_1(tmp_path): # running with a missing file should be a filenotfound error
    r = subprocess.run([sys.executable, "drills/scanner_error_report.py", "drills/nope.log", str(tmp_path / "out.csv")], # runs the CLI with two extra args
                       capture_output=True, text=True) # capture stdout/stderr as text
    assert r.returncode == 1 # file missing or doesn't exist error code

def test_real_log_exits_0(tmp_path): # running the log should be successful 
    out = tmp_path / "out.csv" # assigns the output file path by joining the two together
    r = subprocess.run([sys.executable, "drills/scanner_error_report.py", "drills/scanner.log", str(out)], # runs the CLI with two extra args
                       capture_output=True, text=True) # capture stdout/stderr as text
    assert r.returncode == 0 # success
    lines = out.read_text().splitlines()  # read the whole CSV as one string, then split it into a list of lines
    assert lines[1] == "NO_READ,3"  # index 0 is the header "error,count"; index 1 is the first data row

# PREDICTIONS:
# How many tests will pytest collect? 8
# How many tests will pass? 8