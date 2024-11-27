#! /usr/bin/env/ python 3
# Author: ASlunka
# Description: How to iterate through a 
# Sequence (str/tuple/list/dict/set) using an Iterator for loop

heroes = ['iron man', 'deadpool', 'batman', 'hulk', 'wonder woman']

#iterate through hereos List using iterator Loop...
for hero in heroes:
    print(hero, end=", ") # default end="\n"

# ITERATE through LIST and modify the values using an ITERATOR loop 
# plus an index counter
idx = 0
for hero in heroes:
    print(hero.upper())
    heroes[idx] = hero.upper()
    idx +=1
print("Heroes=", heroes)

# ITERATE through LIST and modify the values using an ITERATOR loop 
# plus built-in enumerate() function
for (idx, hero) in enumerate(heroes, start =0): #enumerate retuns a tuple (index, value)
    print(hero.title())
    heroes[idx] = hero.title()
    idx +=1
print("Heroes Title=", heroes)