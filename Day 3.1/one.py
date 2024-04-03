print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

# if statements
if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age? "))
    if age <= 18:
        bill = 7
        print("Please pay $7")
    elif 19 <= age <= 45:
        bill = 12
        print("Please pay $12")
    else:
        bill = 20
        print("Please pay $20")

    photo = input("Do you want a photo? Y or N: ")   
    if photo.upper() == 'Y':
        bill += 3
        print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")