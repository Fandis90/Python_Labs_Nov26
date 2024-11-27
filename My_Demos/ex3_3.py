
years = [1984, 1904, 2000, 1981, 1900, 2010]


for year in years:
    if (year/400) == (year//400):
        print(year, "is a leap year")
    elif (year/4) == (year//4) and not (year/100) == (year//100):
        print(year, "is a leap year")
    else:
        print(year, "is NOT a leap year")


for year in years:
    if year % 400 == 0:
        print(year, "is a leap year")
    elif (year/4) == (year//4) and not (year/100) == (year//100):
        print(year, "is a leap year")
    else:
        print(year, "is NOT a leap year")