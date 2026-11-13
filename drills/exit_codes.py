import sys  # gives us argv, exit, stderr

if len(sys.argv) < 2:  # no word typed after the script name
    print("usage: exit_codes.py ok|fail|crash|msg", file=sys.stderr)  # error message goes to stderr
    sys.exit(2)  # 2 = script used wrong

word = sys.argv[1]  # the word typed after the script name

if word == "ok":
    print("all good")  # normal output goes to stdout
    sys.exit(0)  # 0 = success

if word == "fail":
    print("count mismatch", file=sys.stderr)  # error message goes to stderr
    sys.exit(1)  # 1 = something went wrong

if word == "crash":
    raise ValueError("bad pallet")  # uncaught error, not handled with try/except

if word == "msg":
    sys.exit("bad input")  # text instead of a number

print(f"unknown word: {word!r}", file=sys.stderr)  # anything not handled above
sys.exit(2)  # 2 = used wrong


# Terminal Inputs and Outputs:
# python drills/exit_codes.py ok
# all good
# $LASTEXITCODE
# 0

# python drills/exit_codes.py fail
# count mismatch
# $LASTEXITCODE
# 1

# python drills/exit_codes.py crash
# bad pallet
# $LASTEXITCODE
# 1

# python drills/exit_codes.py msg
# ValueError: bad input
# $LASTEXITCODE
# 1

# python drills/exit_codes.py 
# usage: exit_codes.py ok|fail|crash|msg
# $LASTEXITCODE
# 2

# python drills/exit_codes.py banana
# unknown word: 'banana'
# $LASTEXITCODE
# 2