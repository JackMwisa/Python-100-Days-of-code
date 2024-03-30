height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# bmi = weight / height ** 2

bmi = int(weight) / int(height) ** 2

print(f'Your bmi is {bmi}')
