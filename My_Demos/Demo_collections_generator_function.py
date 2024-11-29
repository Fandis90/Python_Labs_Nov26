#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO generate a collection one object at a time using a generator function.

"""
  Docstring
"""

def get_number():
    """Return entire list of numbers"""
    numbers = []
    for x in range(0,10):
        numbers.append(x)
    return numbers


def generate_numbers():
    """Yield one object at a time from a collections of numbers"""
    print("Executing generator numbers...")
    for x in range(0,10):
        yield x


for z in generate_numbers():
    print(z)

#Alternatively we could use a while loop and the built-in next() function to get the next Yielded value
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

#Alternatively we could just get the next Yielded value manually
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print (num1, num2, num3)