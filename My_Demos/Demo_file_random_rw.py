#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO open, close, read and write
# Randomly to a file using the .seek() and .tell() methods

"""
  Docstring
"""

SOF = 0 # Start of file
CUR = 1 # Current position
EOF = 2 # End of FIle
# Open file handle for Reading in text mode
with open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF (0 to start from start)
    text = fh_in.read(30) 
    print(f"text at position {fh_in.tell() - len(text)} = {text}")
    
    fh_in.seek(135, SOF) # Seek forwards 135 chars from SOF
    text = fh_in.read(30) # read next 30 chars
    print(f"text at position {fh_in.tell() - len(text)} = {text}")
    # after this point fh_in is flushed

print("-" * 60)

# Open file handle for Reading in BINARY mode
with open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="rb") as fh_data:
    fh_data.seek(-90, EOF) # Seek backwards 90 chars from EOF (end of file)
    text = fh_data.read(30) 
    print(f"text at position {fh_data.tell() - len(text)} = {text}")
    
    fh_data.seek(-60, CUR) # Seek backwards 60 bytes from current position
    text = fh_data.read(30) # read next 30 chars
    print(f"text at position {fh_data.tell() - len(text)} = {text}")
    # after this point fh_data is flushed