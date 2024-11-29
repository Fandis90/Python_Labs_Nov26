#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO copy and optionally filter collections, using loops+conditions+expressions,
# The filter() built-in functions, lambda functions

"""
  Docstring
"""

students = ['winson', 'naoki', 'tom', 'chris', 'andrius', 'narla', 'aron', 'bobbin', 'grace', 'chris']

#ITERATE through the source list and copy and optionally filter 
#1. Using an ITERATOR for loop+collection, optional if (filtering), an expression.
wee_names = []
for name in students: # 1. Iterator Loop + source collection
    if len(name) <= 5: # 2. Optional condition (filtering)
        wee_names.append(name.upper()) # 3. Expression
print("1. short names =", wee_names)

# 2. Using iterator for loop+collection, user function (filtering), an expression
def filter_names(name):
    """Return True if name is less than 6 chars"""
    if len(name) <=5:
        return True
    else:
        return False
    
wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name.upper())
print("2. short names =", wee_names)


# 3. use built-in filter function+collection, user function (filtering)
wee_names = list(filter(filter_names, students))
print(f"3. short names =  {wee_names}")


# 4. use built-in filter function+collection, a lambda function (filtering)
# lambda INs:OUTs
wee_names = list(filter(lambda name:len(name) <=5, students))
print(f"4. short names =  {wee_names}")


# 5. use LIST COMPREHENSION = expression, ITERATOR loop+source collection, if condition does the filtering
wee_names = [ name.upper() for name in students if len(name) <=5 ]
print(f"5. short names =  {wee_names}")

# 5.1  use LIST COMPREHENSION = expression, ITERATOR loop+source collection, if condition does the filtering
# list of tuples
wee_names = [ (name.upper(), len(name))  for name in students if len(name) <=5 ]
print(f"5.1. short names =  {wee_names}")


# 5.2  use DICT COMPREHENSION = expression, ITERATOR loop+source collection, if condition does the filtering
# EXTRA filtering, duplicate keys have been removed
wee_names = { name.upper(): len(name)  for name in students if len(name) <=5 }
print(f"5.2. short names =  {wee_names}")

# 5.3  use SET COMPREHENSION = expression, ITERATOR loop+source collection, if condition does the filtering
# EXTRA filtering, duplicate values have been removed
wee_names = { name.upper() for name in students if len(name) <=5 }
#wee_names = sorted({ name.upper() for name in students if len(name) <=5 })
print(f"5.3. short names =  {wee_names}")