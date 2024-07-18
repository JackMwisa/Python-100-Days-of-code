def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(6))  # Expected output: 720
print(calculate_factorial(7))  # Expected output: 5040
