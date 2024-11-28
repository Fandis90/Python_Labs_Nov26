#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This script will demo HOW TO preserve one python object to a pickle file using the pickle module

"""
  Docstring
"""
import pickle
import pprint
import gzip # other compresion modules including bz2, tarfile, shutil

# Open file handle for READING in TEXT mode
movies = {
    'chris': ['Die Hard', 'Trainspotting', 'Barbie'],
    'tom': ['12 Strong', 'Forest Gump', 'The Matrix'],
    'andrius': ['Gladiator', 'The Boondock Saints', 'Con Air'],
    'winson': ['Top Gun', 'Terminator', 'Pretty Woman']
}

# Open file handle for WRITING in binary mode
#with open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.p", mode="wb") as fh_out:
with gzip.open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.pgz", mode="wb") as fh_out: #only in binary mode
    
    #pickle.dump(movies, fh_out, protocol=0) # pickle protocol goes from 0-5 (0=ASCII, 1-5=BINARY)
    #pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # Default = 4
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL) # Highest = 5
    # protocol 3 introduced with Python3 (every protocol is more efficient)

print("-" * 60)

# Open file handle for READING in BINARY mode
#with  open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.p", mode="rb") as fh_in:
with  gzip.open(r"C:\Project\Python_Labs_Nov26\My_Demos\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)