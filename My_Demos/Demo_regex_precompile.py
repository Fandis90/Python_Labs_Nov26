#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO match text data using str testing
# and Regular Expressions / Regex and the re module.

"""
  Docstring
"""
import re

# Open file handle for READING in TEXT mode
fh_in = open(r"C:\Project\Python_Labs_Nov26\labs\words", mode="rt") #fh = file handle
# Iterate through the file handle one line at a time...


reobj = re.compile(r"^(.)(.).\2\1$") #pre-compile PATTERN ONLY ONCE
for line in fh_in:
    #m = re.search(r"^(.)(.).\2\1$", line) # Must 5 char palindromes
    m = reobj.search(line) # Use precompiled pattern! BETTER PERFORMANCE.
    if m:
        #print(line, end="") 
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
fh_in.close() # close file after handle 

