#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO spot and rejoin a string

"""
  Docstring
"""
import sys

#sample line form /etc/passwd on Linux for the root user account
line = r"root:x:0:0: The Super User :/root:/bin/ksh"

# ..and I want to modify parts of this string! IMMUTABLE! (read only)
fields = line.split(":") #Returns a list, which is MUTABLE!
fields[4] = "The Administartor"
fields[4] = "/bin/bash"

print(fields)
line = ":".join(fields) #Return a new string
print(line)

sys.exit(0)