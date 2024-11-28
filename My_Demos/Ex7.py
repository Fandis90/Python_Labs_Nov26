#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will dmep

"""
  Docstring
"""
import sys
import os
import re

if sys.platform == "win32":
    #print(os.environ)
    path = f"C:\WINDOWS\system32\drivers\etc\services"
else:
        path = f"C:\WINNT\system32\drivers\etc\services"


all_ports = set(range(1,201))
used_ports = set()
pattern = re.compile(r"(\d+)/(tcp|udp)") #pre-compile PATTERN ONLY ONCE

with open(path, mode="rt") as fh_in:
    for line in fh_in:
        #print(line)
        m = pattern.search(line)
        if m:
            port = int(m.group(1))
            print(m.group(1)) # print a touple 
            if port <= 200:
                used_ports.add(port)

unused_ports = all_ports - used_ports
print(f"all ports {all_ports}")
print("used ports: ", used_ports)
print(f"unusued ports: {unused_ports}")
        


sys.exit(0)