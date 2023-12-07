def divide_numbers():
    try:
        # Prompt the user to enter two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Check if the denominator is zero
        if denominator == 0:
            # Raise a runtime error with a meaningful message
            raise ValueError("Error: Division by zero is not allowed.")
        
        # Perform the division operation
        result = numerator / denominator
        
        # Display the result
        print(f"Result of {numerator} / {denominator} is: {result}")

    except ValueError as ve:
        # Handle the specific ValueError (division by zero) and display an error message
        print(ve)

    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

# Call the function to perform the division
divide_numbers()
