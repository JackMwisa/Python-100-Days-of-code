# 2000 / 4 = 500
# 2000 / 100 = 20
# 2000 / 400 = 5


year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("Not a leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")