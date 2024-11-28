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

#POOR example
"""for line in fh_in:
    #example of string testing
    if line.startswith("Y") and line.endswith("n\n"): # \n required because lines end with new line
        print(line, end="")"""

"""for line in fh_in:
    # \n strip all the lines that starts with new line and then search for end with "n" and contains "town"
    if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line: 
        print(line, end="")

print("-" * 60)"""

for line in fh_in:
    # m = re.search("town", line) # Returns NoneType Object if match not found (False), else returns REmatch object (True) (m for match_)
    # m = re.search("^town", line) # Match line STARTING WITH "town"
    # m = re.search("town$", line) # Match line STARTING WITH "town"
    # m = re.search("^[A-Z]", line) # Match line that begins with CAPITAL
    # m = re.search("^.ing$", line) # Match lines with only one char followed bt "ing"
    # m = re.search("^[adrp]ing$", line) # Match lines with only containing [adrp] and followed by "ing"
    # m = re.search("^...................$", line) # Match lines with exactly 19 chars
    # m = re.search("^.{19}$", line) # MATCH LINES WITH EXACTLY 19 CHARS
    # m = re.search("[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive vowels
    # m = re.search("[aeiou]{3}", line) # Match lines with 3 consecutive vowels
    # m = re.search("[aeiou]{5,}", line) Match line with at leats 5 consecutive vowels
    # m = re.search("[0-9][0-9]", line) # Match lines with 2 consecutive digits
    # m = re.search("\.", line) # Match lines with a Dot (Alternative [.]) (backslash compatible with other platforms)
    # m = re.search("^[A-Z].*[A-Z]$", line) # Lines that starts and ends with a CAPITAL
    m = re.search("^[A-Z].{3}[A-Z]$", line) # Match lines of 5 chars that starts and ends with a CAPITAL
    if m:
        print(line, end="")        

fh_in.close() # close file after handle 

