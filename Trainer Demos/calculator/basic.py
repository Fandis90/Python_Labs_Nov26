#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines a collection of calculator functions
"""
  Basic Calcualtor functions including add, sub, mul and div functions.
"""

def add(*args):
    """ Return SUM of all arguments """
    total = 0
    for num in args:
        total += num
    return total

def sub(x, z):
    """ Retuen result of x subtract z """
    return x-z

def mul(*args):
    """ Return PRODUCT of all the arguments """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)
