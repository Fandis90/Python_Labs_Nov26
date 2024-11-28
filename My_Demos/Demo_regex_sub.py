#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO match and SUBSTITUTE regex patterns
# using the re.sub() and re.subn() functions.

"""
  Docstring
"""
import re

# Sample line from /etc/passwd on Linux for he root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# ANd I want to modify the line str objects! IMMUTABLE!
line = re.sub(r"[sS]uper [uU]ser", r"Administartor", line) #Returns modified str
(line, num) = re.subn(r"ksh$", r"bash", line) #Returns a TUPLE (modified str, num changes)

print(f"Modified line = {line} with {num} changes")