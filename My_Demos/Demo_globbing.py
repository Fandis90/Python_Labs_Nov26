#! /usr/bin/env Python3
#Author: ASlunka
# Description: This script will demo how to ITERATE through files
# and the file system using an ITERATOR for loop plus the glob module
# Globbing (globally expand) in linux is same as wild cards

import glob
import sys
import os

if sys.platform == "win32":
    #print(os.environ)
    if os.environ["USERPROFILE"]:
        home = os.environ["USERPROFILE"]
    else:
        home = r"C:\Users\aslunka"
    pattern = home + r"\*"
else:
    home = os.environ["HOME"] #Unix / Linux home path
    pattern = home + r"/*"

print(pattern)
for file in glob.glob(pattern):
    if os.path.isfile(file):
        print(file, os.path.getsize(file))