print("Welcome to the rollercoaster")
# Ask the user for their height in centimeters
height = int(input("What is your height in cm? "))
bill = 0  # Initialize the bill variable to keep track of the total cost

# Check if the user's height is greater than or equal to 120 cm
if height >= 120:
    # If the height requirement is met, print a message allowing the user to ride
    print("You can ride the rollercoaster!")
    
    # Ask the user for their age
    age = int(input("What is your age? "))
    
    # Determine the cost based on the user's age
    if age <= 18:
        bill = 7
        print("Please pay $7")
    elif 19 <= age <= 45:
        bill = 12
        print("Please pay $12")
    else:
        bill = 20
        print("Please pay $20")

    # Ask the user if they want a photo
    photo = input("Do you want a photo? Y or N: ")   
    
    # If the user wants a photo, add $3 to the bill
    if photo.upper() == 'Y':
        bill += 3
        print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")