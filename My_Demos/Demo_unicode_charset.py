#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo how to display entire unicode charset

"""
  Docstring
"""
import sys

#Iterate through all CHAR postitions in Unicod charset
for pos in range(0,65535):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print("")



sys.exit(0)