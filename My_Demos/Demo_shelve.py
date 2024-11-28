#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo

"""
  Docstring
"""

import shelve

movies = {
    'chris': ['Die Hard', 'Trainspotting', 'Barbie'],
    'tom': ['12 Strong', 'Forest Gump', 'The Matrix'],
    'andrius': ['Gladiator', 'The Boondock Saints', 'Con Air'],
    'winson': ['Top Gun', 'Terminator', 'Pretty Woman']
}

tv_series = { 'Chris': ['walking dead', 'yellowstone'],
             'tom': ['breaking bad', 'the boys'],
             'andrius': ['outlander', 'dads army']
}

books = {'andrius': 'dummys guide to python',
         'winson': 'extreme ironing'}

with shelve.open(r"C:\Project\Python_Labs_Nov26\My_Demos\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"C:\Project\Python_Labs_Nov26\My_Demos\media") as db:
    print(f"chris's favourite movies are {db['movies']['chris']}")
    print(f"tom's favourite tv_series is {db['tv_series']['tom'][0]}")
    print(f"winson's favourite book is {db['books']['winson']}")