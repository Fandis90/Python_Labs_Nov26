#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo a SAFER way of managinf file handles using CONTEXT RESOURCE MANAGER (WITH)
# Simulating BLOCK scope

"""
  Docstring
"""

# Open file handle for READING in TEXT mode
movies = {
    'chris': ['Die Hard', 'Trainspotting', 'Barbie'],
    'tom': ['12 Strong', 'Forest Gump', 'The Matrix'],
    'andrius': ['Gladiator', 'The Boondock Saints', 'Con Air'],
    'winson': ['Top Gun', 'Terminator', 'Pretty Woman']
}

# Open file handle for WRITING in text mode
with open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="wt") as fh_out:
    # ITERATE through movies dictionary and WRITE movie info to file handle
    for name in movies.keys(): #names are keys
        print(f"{name}: {movies[name]}", end="\n")
        print(f"{name}: {movies[name]}", end="\n", file=fh_out)
        # End of Block, fh_out is closed and deleted automatically.

print("-" * 60)

# Open file handle for READING in text mode
with  open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
