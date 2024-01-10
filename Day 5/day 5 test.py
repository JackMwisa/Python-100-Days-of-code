# print("test")

# Function for countdown with liftoff message when reaching 0 or less
def liftoff_down(count):
    if count <= 0:
        print('Liftoff!')  # Print Liftoff message when count reaches 0 or negative
    else:
        print(count)  # Print current count
        liftoff_down(count - 1)  # Recursive call reducing count by 1

# Function for countup with liftoff message when reaching 0 or more
def liftoff_up(count):
    if count >= 0:
        print('Liftoff!')  # Print Liftoff message when count reaches 0 or positive
    else:
        print(count)  # Print current count
        liftoff_up(count + 1)  # Recursive call increasing count by 1

# Main function to handle user input and function calls
def main():
    user_input = int(input("Enter a number: "))  # Get user input

    if user_input > 0:
        liftoff_down(user_input)  # If input is positive, call liftoff_down
    elif user_input < 0:
        liftoff_up(user_input)  # If input is negative, call liftoff_up
    else:
        liftoff_up(user_input)  # If input is zero, call liftoff_up for consistency

if __name__ == "__main__":
    main()  # Call the main function when the script is executed




