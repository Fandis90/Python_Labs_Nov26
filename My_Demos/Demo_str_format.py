#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo how to format strings in several ways
# using str concatenation and escape chars, str justification methods,
# the str format() method and f-strings!

"""
  Docstring
"""

planets = {'Mercury': 57.91, 
           'Venus': 108.2, 
           'Earth': 149.597870, 
           'Mars': 227.94
           }

# Iterate through the keys in the planets dict and display info
# Using str concatenation and  escape characters - UGLY SOLUTION!!!!
for planet in planets.keys():
    print("\t\t" + planet + ": " +str(planets[planet]) + "Gm \t" + str(hex(0xff)))

print(10 * 2)
print("-" * 60) #Repetitions

# Using str justification methods - OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm " + str(hex(0xff).rjust(6)))


print("-" * 60) #Repetitions

# Using str.format() method - GOOD!
for planet in planets.keys():
    print("{0} {1} {2} ".format(planet, planets[planet], 0xff)) #{} can be empty

print("-" * 60) #Repetitions

# Using str.format() method - GOOD! (formated)
for planet in planets.keys():
    print("{0:>12s} {1:.^12.3f} Gm {2:>#6x} ".format(planet, planets[planet], 0xff)) #{} can be empty
    # > right justified, ^ centre justified, < left justified

print("-" * 60) #Repetitions

# Using f-strings (Python 3.5 anwards) - GREAT!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.^12.3f} Gm {0xff:>#6x} ") #{} can be empty
    # > right justified, ^ centre justified, < left justified