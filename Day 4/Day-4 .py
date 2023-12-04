import random
import my_module

random_integer = random.randint(0,10)

# random float
random_float = random.random() * 5


print(random_integer)
print(random_float)

print(my_module.pi)


love_score = random.randint(1,100)
print(f"Your love score is {love_score}")