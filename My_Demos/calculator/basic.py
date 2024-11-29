#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This module defines a collection of calculator functions

"""
  Basic calculator functions includding add, sub, mul and div functions
"""
import sys

def add(*args): #any number of parameters
    """Return SUM of all arguments
    >>> add(4, 3)
    7
    >>> add(4, 3, 2)
    9
    """
    total = 0
    for num in args:
        total += num
    return total

def sub(x, z):
    """Return the result of x subtract z"""
    return x-z

def mul(*args):
    """Return PRODUCT of all the arguments
    >>> mul(4, 3)
    12
    >>> mul(4, 3, 2)
    24
    
    """
    total = 1
    for num in args:
        total *=num
    return total

def div(x, z):
    """Return quotient of x divided by z to 3 decimal places"""
    return round(x/z, 3)


if __name__ == "__main__":
    import doctest
    doctest.testmod()