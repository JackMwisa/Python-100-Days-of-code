import math

def hypotenuse(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    sum_of_squares = a_squared + b_squared
    hypotenuse_length = math.sqrt(sum_of_squares)
    return hypotenuse_length

print(hypotenuse(3, 4))  # Expected output: 5.0