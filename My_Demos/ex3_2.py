import sys

var = input("Please enter an integer: ")

if not var.isdecimal():
    print("Wrong value entered")
    sys.exit(1)




if int(var) == 7:
    counter = 7
else:
    counter = 16

while counter >= 0:
    print(counter)
    counter -= 2