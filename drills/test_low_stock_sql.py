# run as: python -m pytest drills/test_low_stock_sql.py -v
import subprocess # loads the subprocess module
import sys # loads the sys module

SCRIPT = "drills/low_stock_sql.py" # assigns low_stock_sql path to SCRIPT
HEADER = "sku,bin,on_hand,reorder_point\n" # assigns a string to HEADER


def run_script(*args): # creates a function called run_script with a parameter called *args which collects any number of arguments. capture=True saves stdout and stderr, and text=True makes them strings instead of bytes
    return subprocess.run( # runs the subprocess on the script and captures the output then returns it 
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        text=True,
    )


def test_low_rows_sorted(tmp_path): # creates a function called test_low_rows_sorted with a parameter called tmp_path
    csv_path = tmp_path / "low_rows.csv" # joins tmp path  to the other string then assigns it to csv_path
    csv_path.write_text( # writes a csv file to csv.path which has the header and three rows 
        HEADER
        + "SKU-1042,A3-04,10,15\n"
        + "SKU-4410,B1-03,0,8\n"
        + "SKU-2210,A3-05,40,20\n"
    )
    r = run_script(str(csv_path)) # converts csv_path to a string then runs it as a parameter in run_script function then assigns the result to r
    lines = r.stdout.splitlines() # splits stdout into a list of strings, one per line
    assert r.returncode == 0 # returncode must equal 0
    assert lines[0] == "SKU BIN ON_HAND REORDER_POINT" # checks if the first line equals the string
    assert lines[1] == "SKU-4410 B1-03 0 8" # checks if the second line equals the string
    assert lines[2] == "SKU-1042 A3-04 10 15" # checks if the third line equals the string
    assert lines[-1] == "2 of 3 SKUs below reorder point." # checks if the last line equals the string


def test_equal_not_low(tmp_path): # creates a function called test_equal_not_low with a parameter called tmp_path
    csv_path = tmp_path / "equal_point.csv" # joins tmp path to the other string then assigns it to csv_path
    csv_path.write_text(HEADER + "SKU-5120,C2-01,25,25\n") # writes the header and first row to the csv_path
    r = run_script(str(csv_path)) # pushes the csv_path as a string as a parameter in run_script function then stores the result in r
    assert r.returncode == 0 # checks if returncode is equal to 0
    assert "SKU-5120" not in r.stdout # checks if the string is not in stdout
    assert r.stdout.splitlines()[-1] == "0 of 1 SKUs below reorder point." # checks the last line if it matches the string


def test_tiebreak_by_sku(tmp_path): # creates a function called test_tiebreak_by_sku with a parameter called tmp_path
    csv_path = tmp_path / "tiebreak.csv" # joins tmp path to the other string then assigns it to csv_path
    csv_path.write_text( # writes a csv file to csv.path which has the header and two rows 
        HEADER
        + "SKU-9000,D1-01,2,10\n"
        + "SKU-1000,D1-02,2,10\n"
    )
    r = run_script(str(csv_path)) # pushes the csv_path as a string as a parameter in run_script function then stores the result in r
    lines = r.stdout.splitlines() # gets the result of r in stdout and splits the lines then assigns it to lines
    assert lines[1].startswith("SKU-1000") # checks the second starts with the string
    assert lines[2].startswith("SKU-9000") # checks the third row starts with the string


def test_no_args(): # creates a function called test_no_args 
    r = run_script() # run_script without any args then store the result in r 
    assert r.returncode == 2 # check if r returncode is equal to 2
    assert "usage" in r.stderr # checks that usage appears in stderr


def test_missing_file(tmp_path): # creates a function called test_missing_files with a parameter called tmp_path
    r = run_script(str(tmp_path / "nope.csv")) # converts tmp_path into a string then joins the string which is then ran through run_script function with the result being stored inside r
    assert r.returncode == 1 # checks r returncode is matching 1
    assert r.stderr != "" # checks r stderr to make sure it isn't empty

# PREDICT (pass or fail for each test, and why):
# test_low_rows_sorted(tmp_path)
# FAIL - the header is not in all capitals
# CORRECTION:
# PASS - lines was what is printed to stdout so look at the line: print("SKU BIN ON_HAND REORDER_POINT")

# test_equal_not_low(tmp_path)
# PASS

# test_tiebreak_by_sku(tmp_path)
# PASS

# test_no_args()
# PASS

# test_missing_file(tmp_path)
# PASS
