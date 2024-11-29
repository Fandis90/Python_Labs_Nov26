#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This module defines advanced functions for a calculator app

"""
  Advanced functions for calculator app, including modulus, power and sqrt
"""
import sys

def mod(x, z):
    """Return the remainder after x modulus z"""
    return x % z


def power(x, z):
    """Return the power of x to z as float"""
    return float(x**z)


def sqrt(x):
    """Return square root of x as a float"""
    return round(x**0.5, 2)



sys.exit(0)