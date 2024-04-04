import random

# Who is paying

name_string = input("Give me everybody's name separated by a comma. [,] \n")

name = name_string.split(", ")

print(name)


paying = name[random.randint(0,  len(name)-1)]  # Randomly select one of the names to pay

print(f"{paying} is going to buy the meal today!")