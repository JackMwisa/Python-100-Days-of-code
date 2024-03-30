height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# bmi = weight / height ** 2

bmi = int(weight) / float(height) ** 2

int_bmi = int(bmi)

print(f'Your bmi is {int_bmi}')
