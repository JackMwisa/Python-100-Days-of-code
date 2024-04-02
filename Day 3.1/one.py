print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

# if statements
if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7")
    elif 19 <= age <= 45:
        print("Please pay $12")
    else:
        print("Please pay $20")
    
else:
    print("Sorry, you have to grow taller before you can ride")