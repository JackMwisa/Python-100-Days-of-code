def calculate_factorial(n):
    result = 1
    
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return result
    else:
        # Recursive multiplication
        result = n * calculate_factorial(n-1)
        return result

# Testing the Function
# result1 = calculate_factorial(5)
# result2 = calculate_factorial(0)
# result3 = calculate_factorial(3)

# Displaying Results and Explanation
print("Test 1: calculate_factorial(5) =", result1)
print("Test 2: calculate_factorial(0) =", result2)
print("Test 3: calculate_factorial(3) =", result3)
