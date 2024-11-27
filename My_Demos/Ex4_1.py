
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium.replace(",", ":"))

value = 0
counter = 0
fields = Belgium.split(",")
while counter < 2:
    for field in fields:
        if field.isdecimal():
            value += int(field)
            
print(value)

    