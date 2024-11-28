#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will display postcodes in postcodes.txt file

"""
  Docstring
"""
import re

valid = 0
invalid = 0
infile = open(r"C:\Project\Python_Labs_Nov26\labs\postcodes.txt", mode="rt") # rt = read text mode

for postcode in infile:
    #qustion 1 solutions
    if postcode.isspace(): continue #remove blank lines and read next line
    postcode = postcode.upper()
    postcode = re.sub(r"\s+", r"", postcode) #remove all spaces
    postcode = re.sub("(\d[A-Z]{2})$", r" \1", postcode)


    #qustion 2 solutions
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}", postcode)
    if m:
        valid += 1
    else:
        invalid +=1

    print(postcode)
    


infile.close()
print(f"Valid postcodes: {valid}")
print(f"Invalid postcodes: {invalid}")