#! /usr/bin/env python3
# Author: ASlunka
# Description: This script will demo how to repeat a block of
# command a specific number of times using a counter loop

#Traditional way
count = 0 # 1. initialise counter
while count < 10: # 2. test counter
    print(count)
    count += 1 # 3. increment counter


#Alternatively we could repeat block of comands using a
# for loop and the built in range() function (fucntion takes x3 parameters: start, stop, step)
for num in range(0, 10, 1): # 0 - start, 10 - stop, 1 - step. Can be without 3rd value, it defaults to 1. for example: range(0, 10)
    print(num)

for num in range(0, 10): # step default = 1
    print(num)

for num in range(10): # start default = 0 and step default = 1
    print(num)