

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age? "))
    
    if age <=18:
        print("Please pay $7")
    elif age <= 12:
        print("Pay 7") 
    else:
        print("You pay 18")
else:
    print("Sorry, you have to grow taller before you can ride")