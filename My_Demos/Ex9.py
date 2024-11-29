

def frange(start, end, step=0.25):
    if step == 0:
        step = 0.25
    value = start - step

    while value < end:
        value += step
        yield value

for z in frange(1.1,3):
    print (z)


print(list(frange(1.1,3)))