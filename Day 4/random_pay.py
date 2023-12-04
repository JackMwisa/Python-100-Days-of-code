
import random

name_string = input("Give me everybody's name, separated by a comma. ")

# Jack, Mark, Lily, Kevin, Sarah, Laura, Martin
name = name_string.split(", ")

payer = random.randint(0, len(name))

# print(len(name))

bill_payer = f"The one who will pay the bill is {name[payer]}"

print(bill_payer)