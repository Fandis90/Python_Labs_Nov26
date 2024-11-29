#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo How to define and call a variadic user function

"""
  Program to search for regex patterns in text files
"""
import re

# Example of a VARIADIC function that allows variable num of parameters
def search_pattern(pattern=r"^.{19}", *files):
    """
    Search for regex pattern in multiple files and return num lines matched
    """
    lines = 0
    for file in files:
        with open(file, mode="rt") as fh_in:

            for line in fh_in:
                m = re.search(pattern, line) # Match pattern

                if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.strip()} at {m.start()}-{m.end()}")
    return lines

num_lines = search_pattern(r"^.{20}$", r"C:\Project\Python_Labs_Nov26\My_Demos\words", r"C:\Project\Python_Labs_Nov26\My_Demos\words2", 
                           r"C:\Project\Python_Labs_Nov26\My_Demos\words3")
print(f"Matched lines found: {num_lines}")