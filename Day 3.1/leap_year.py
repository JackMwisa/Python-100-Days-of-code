
year = int(input("Enter a year:"))

# 2000 / 4 = 500
# 2000 / 100 = 20
# 2000 / 400 = 5

# if year % 4 == 0:
    
#     if year % 100 == 0 and year % 400 == 0:
#         print("This is a leap year!")
#     else:
#         print("This is not a leap year!")
# else:
#     print("This is not a leap year!")
    

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")