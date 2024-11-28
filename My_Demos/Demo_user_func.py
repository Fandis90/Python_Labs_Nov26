#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO define name, call and optionally pass parameters in
# and optionally return data from a user function.

"""
  Docstring
"""
def say_helo(greeting:str="Labas", recipient:str="draugai")->None: #str and None are just annotations in this line
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_helo("hello", "my friends") # Example of positional parameter passing
say_helo("konichiwa", "tomodachi")
say_helo("bonjour", "mes amis")