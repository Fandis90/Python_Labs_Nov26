#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO create, and grow, and shrink and
# combine sets using SET operators (Remember VENN diagrams)

"""
  Docstring
"""

marvel_fans = {'donald', 'naoki', 'chris', 'isla', 'grace'}
dc_fans = set() #create an empty set

#grow a set... one at the time
dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

#change a set
#dc_fans.pop() #can not specify a key, because sets do not have keys - Randomly remove a value
comic_fans = dc_fans.copy() # Copy a set
comic_fans.clear() # Empty a set

print(f"Fans of Marvel {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

print("-" * 60)

# COMBINE Sets using SET methods (Remember VEN diagrams)
#Combine - return all but get rids of duplicates
#intersection - return what is comon to both

print(f"Fans of either Marvel or DC = {marvel_fans.union(dc_fans)}")
print("-" * 60)
print(f"fans of both: {marvel_fans.intersection(dc_fans)}")
print("-" * 60)
print(f"fans of only marvel: {marvel_fans.difference(dc_fans)}")
print("-" * 60)
print(f"fans of only Marvel or DC {marvel_fans.symmetric_difference(dc_fans)}")

# COMBINE Sets using SET operators (Remember VEN diagrams)
print(f"Fans of either Marvel or DC = {marvel_fans | dc_fans}")
print("-" * 60)
print(f"fans of both: {marvel_fans & dc_fans}")
print("-" * 60)
print(f"fans of only marvel: {marvel_fans - dc_fans}")
print("-" * 60)
print(f"fans of only Marvel or DC {marvel_fans ^ dc_fans}")
