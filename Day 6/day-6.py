
import math

def hypotenuse(leg1, leg2):
    sum_of_squares = leg1**2 + leg2**2
    hypotenuse_length = math.sqrt(sum_of_squares)
    return hypotenuse_length

# Testing the Function
result1 = hypotenuse(3, 4)
result2 = hypotenuse(5, 12)
result3 = hypotenuse(8, 15)

# Displaying Results in Learning Journal
print("Test 1: hypotenuse(3, 4) =", result1)
print("Test 2: hypotenuse(5, 12) =", result2)
print("Test 3: hypotenuse(8, 15) =", result3)