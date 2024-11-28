#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will dmep

"""
  Docstring
"""
import re

def search_pattern(pattern=r"^.{19}", file=f"C:\Project\Python_Labs_Nov26\labs\words"):
    lines = 0
    with open(file, mode="rt") as fh_in:

        for line in fh_in:
            m = re.search(pattern, line) # Match pattern

            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.strip()} at {m.start()}-{m.end()}")
    return lines

num_lines = search_pattern()
print(f"Matched lines found: {num_lines}")