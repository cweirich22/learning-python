import subprocess, sys # loads the subprocess and sys module
from pathlib import Path # loads the Path class from pathlib module

HERE = Path(__file__).parent # pulls the directory of the current file
SCRIPT = HERE / "label_parser_cli.py" # joins the HERE filepath with the string file label_parser_cli.py

def run_cli(args): # creates a function called run_cli with a parameter called args
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True) # start Python, have it run label_parser_cli.py with whatever args were passed in, capture what it prints, use text=True so we get strings instead of bytes, and return the receipt (the CompletedProcess)

def test_no_args_exits_2(): # creates a function called test_no_args_exits_2 with no parameters
    result = run_cli([]) # runs the cli with no arguments and saves the receipt in result
    assert result.returncode == 2 # makes sure the returncode of result is equal to 2
    assert "usage" in result.stderr.lower() # lowercases the child's error output, then checks that "usage" appears in it

def test_missing_file_exits_1(tmp_path): # creates a function called test_missing_file_exits_1 with a parameter called tmp_path
    result = run_cli(["nope.txt", str(tmp_path / "out.csv")]) # runs the cli with two arguments: nope.txt and tmp_path joined with out.csv
    assert result.returncode == 1 # makes sure the returncode of result is equal to 1
    assert result.stderr != "" # checks to see if the stderr is blank as it must not be blank

def test_messy_file_exits_3(tmp_path): # creates a function called test_messy_file_exits_3 with an parameter called tmp_path
    out_csv = tmp_path / "out.csv" # joins the tmp_path with out.csv
    result = run_cli([str(HERE / "labels_messy.txt"), str(out_csv)]) # uses run_cli function with two arguments: HERE apth joined with labels_messy.txt and out_csv
    assert result.returncode == 3 # checks to see if result returncode is equal to 3
    bad = [line for line in result.stderr.splitlines() if line.strip()] # creates an empty list then goes through result.stderr one line at a time, if the line isn't blank after removing spaces then keep it
    assert len(bad) == 3 # length of bad must be equal to 3
    assert out_csv.exists() # out_csv must exist 

def test_clean_file_exits_0(tmp_path): # creates a function called test_clean_file_exits_0 with a parameter called tmp_path
    out_csv = tmp_path / "out.csv" # joins the tmp_path with out.csv
    result = run_cli([str(HERE / "labels_clean.txt"), str(out_csv)]) # runs the test on a joined filepath as the input then out_csv as the output
    assert result.returncode == 0 # returncode must be equal to 0
    assert result.stderr == "" # stderr must be blank
    assert out_csv.exists() # out_csv must exist

# PREDICTIONS
# input: python -m pytest drills/test_label_parser_cli.py -v
# output: drills/test_label_parser_cli.py::test_no_args_exits_2 PASSED  
# output: drills/test_label_parser_cli.py::test_missing_file_exits_1 FAILED
# output: drills/test_label_parser_cli.py::test_messy_file_exits_3 PASSED
# output: drills/test_label_parser_cli.py::test_clean_file_exits_0 PASSED

# CORRECTIONS
# output: drills/test_label_parser_cli.py::test_missing_file_exits_1 PASSED
# Both asserts were True. FileNotFound has a returncode of 1 and the file not found text is sent through stderr so its not blank


# How it works:
# You run `python -m pytest drills/test_label_parser_cli.py -v`
# pytest opens the file and finds every function whose name starts with `test_`. It ignores everything else, so `run_cli` is never treated as a test.
# It calls each test function. If every `assert` is True, the test **PASSED**. If any `assert` is False, or anything crashes, it FAILED, and pytest shows which line failed.
# With `-v`, you get one line per test, like `test_file.py::test_name PASSED`. At the end there's a summary line counting how many passed or failed.
