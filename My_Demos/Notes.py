name = "Andrius"

#check data type of an object
isinstance(name, str)

#return memory location of an object
id(name)

#check methods inside object
dir(name)


print("is it a string?", isinstance(name, str))
print("location", id(name))

#Variable naming convention --------- 
#taxrate - lower case
#TAXRATE - upper case
#TaxRate - Title case
#taxRate - cammel case
#tax_rate - snake case
#------------------------------------

#Python Enhancement Proposal (P.E.P)
#Style Guide for Python Code -  https://peps.python.org/pep-0008/

# _ before variable means local and private (a rule that we follow - do not access it, use internally)
# __ before variable means mangled - to avoid accidental access. These are also called "Dunders"


#Difference betwee Tuples and Lsits-------------------
# Tuple() is read only (immutable)
# List[] is read write (mutable)

#indexes = sequences

#dictionaries adds keys (unique) to the values (no duplicates)
#dictionaries are mutable
#insertion order (keys, but not indexes)

#sets are read write (mutable) and has unique values



#=========================== TUPLE EXAMPLE ==================
movies = 'Harry Potter', 'Dark Knight', 'Django', 'Black Hawk Down', 'Trainspotting'
"""
type(movies)
<class 'tuple'>
isinstance(movies, tuple)
True
hex(id(movies))
'0x17b133d8950'

len(movies)
5
min(movies)
'Black Hawk Down'
max(movies)
'Trainspotting'
movies[0]
'Harry Potter'
movies[-1]
'Trainspotting'
movies.count('Dark Knight')
1
movies.index('Dark Knight')
1


numbers = (45, -32, 31, 120, -99, 0, 348, 2000)
min(numbers)
-99
max(numbers)
2000
sum(numbers)
2413
"""

# ========= UNPACK TUPLE
"""
a, b, *c = 10, 20, 30, 40, 50, 60
a
10
b
20
c
[30, 40, 50, 60]"""


#======================== LIST EXAMPLES =================
"""
movies = list(movies)
type(movies)
<class 'list'>
isinstance(movies, list)
True
len(movies)
5
min(movies)
'Black Hawk Down'
max(movies)
'Trainspotting'
sorted(movies)
['Black Hawk Down', 'Dark Knight', 'Django', 'Harry Potter', 'Trainspotting']
sorted(movies, key=str, reverse=False)
['Black Hawk Down', 'Dark Knight', 'Django', 'Harry Potter', 'Trainspotting']
sorted(movies, key=str, reverse=True)
['Trainspotting', 'Harry Potter', 'Django', 'Dark Knight', 'Black Hawk Down']
sorted(movies, key=len, reverse=True)
['Black Hawk Down', 'Trainspotting', 'Harry Potter', 'Dark Knight', 'Django']
movies.pop() # will remove the last entry from the list (if adding index value, will remove specified)
"""