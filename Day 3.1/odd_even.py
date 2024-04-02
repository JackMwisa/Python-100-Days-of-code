print("--------------")
print("| ODD OR EVEN |")
print("--------------")
number = int(input("Enter your number: "))

if number == 0:
    print("This number is zero!")
elif number % 2 == 0:
    print("This is an even number!")
else:
    print("This number is odd!")