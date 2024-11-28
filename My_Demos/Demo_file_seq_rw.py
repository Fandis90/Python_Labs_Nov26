#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO open and read, write and append and close a text file

"""
  Docstring
"""
import sys
movies = {
    'chris': ['Die Hard', 'Trainspotting', 'Barbie'],
    'tom': ['12 Strong', 'Forest Gump', 'The Matrix'],
    'andrius': ['Gladiator', 'The Boondock Saints', 'Con Air'],
    'winson': ['Top Gun', 'Terminator', 'Pretty Woman']
}

# Open file handle for WRITING in text mode
fh_out = open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="wt")

# ITERATE through movies dictionary and WRITE movie info to file handle
for name in movies.keys(): #names are keys
    #print(name, movies[name], file=sys.stdout) #lookup movies by using a key[name]
    print(name, movies[name], file=fh_out) #alternative write method using print
    fh_out.write(f"{name} {str(movies[name])}\n")

fh_out.close()  # FLush buffers and close file.

print("-" * 60)

# Open file handle for READING in text mode
fh_in = open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="rt")

#text = fh_in.read() # Read ntire file into one string object. Be careful of huge files!
#text = fh_in.read(30) # Read first 30 chars 
lines = fh_in.readlines() # Read entire file into a list object. Be careful of huge files!
print(lines[-1]) #index a list to get a specific lines
fh_in.close()

print("-" * 60)

#ITERATE through the file one line at a time
#Using an ITERATOR LOOP plus ITERATOR object (iter/next method built in the object)
fh_in = open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.txt", mode="rt")

for line in fh_in:
    print(line, end="")
fh_in.close()