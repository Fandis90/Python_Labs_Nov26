
for line in open('C:\Project\Python_Labs_Nov26\My_Demos\messier.txt', encoding='latin_1'): 
    if not line: break # The text is in the variable named 'line'
    if line.startswith("M"):
        print(line)