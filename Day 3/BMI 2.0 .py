# BODY MASS INDEX CALCULATOR 2.0

# bmi weight / height ** 2

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

# bmi = "{:.2f}".format(bmi)

bmi = round(bmi, 2)

print(bmi)


if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")