#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will dmep

"""
  Docstring
"""
import re
import sys

def search_pattern(pattern=r"^.{19}", file=r"C:\Project\Python_Labs_Nov26\labs\wrds"):
    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as e:
        print(f"Error={e.args[0]}, reason={e.args[1]}, file={e.filename}", file=sys.stderr)
    except PermissionError as e:
        print("error")
        sys.exit(66)
    except BaseException as e:
        print("Some other error occurred, Investigate")
        sys.exit(3)
    else:
        for line in fh_in:
            m = re.search(pattern, line) # Match pattern

            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.strip()} at {m.start()}-{m.end()}")
        return lines
    finally:
        print("And now for something else different")

def main():
    num_lines = search_pattern()
    print(f"Matched lines found: {num_lines}")
    return None

if __name__ == "__main__":
    main()
    sys.exit()