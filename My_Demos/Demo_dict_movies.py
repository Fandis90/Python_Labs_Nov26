#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO create, grow and shrink and access
# keys and values in a dictionary (Unordered collection with unique keys)
# Py3.6 onwards, keys are INSERTION order!

"""
  Docstring
"""
import pprint #pretty print
#Create a multi-dimensional list
movies = {
    'chris': ['Die Hard', 'Trainspotting', 'Barbie'],
    'tom': ['12 Strong', 'Forest Gump', 'The Matrix'],
    'andrius': ['Gladiator', 'The Boondock Saints', 'Con Air'],
    'winson': ['Top Gun', 'Terminator', 'Pretty Woman']
}

#Grow dictionary
movies['naoki'] = ['Titanic', 'Star Wars', 'Spiderman']
movies['donald'] = ['seven samurai', 'battle royal', 'last samurai']

#referencing example
print(movies['chris'][0][0])

#access a dictionary
print(f"chris's favourite movies are: {movies['chris']}")
print(f"tom's ultimate movie is: {movies['chris'][0]}")
print(f"andrius best movies are: {movies.get('andrius')}") #another wat to access

#shrink a dictionary
films = movies.copy() # Shallow Copy Dict
films.clear() # Empty dict
movies.pop('winson') #pop/remove key ('winson') and value
pprint.pprint(movies) #display sorted keys + values in human pretty format
pprint.pprint( movies, sort_dicts=False) #unsorted display

movies.popitem() #removes LAST INSERTED key+value
pprint.pprint(movies)

# Accessing a dict it's keys and values
# 1. Using an iterator loop plus the keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}") 
print ('-' * 60)
# 2. Using an iterator loops plus the values() method
for films in movies.values():
    print (f'good films: {films}')
print ('-' * 60)

# 3. using an interator keys+values using items() method:
for (name, films) in movies.items():
    print(f'{name} loves the films: {films}')