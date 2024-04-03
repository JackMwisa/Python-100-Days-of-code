# pizza order program in python

print("--------------------------------------")
print("| Welcome to python Pizza deliveries! |")
print("--------------------------------------")
size = input("What size pizza do you want? S, M, or  L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
bill = 0

# small pizza = 15$
# medium pizza = 20$
# large pizza = 25$

# peperoni for small pizza +2$
# peperoni for medium or large pizza +2$

# Extra cheese +1$

# your final bill is ...$

if size.upper() == "S":
    bill += 15
    if add_pepperoni.upper() == "Y":
        bill += 2
    if extra_cheese.upper() == "Y":
        bill += 1
    
    print(f"Your final bill is ${bill}")
    
    
elif size.upper() == "M":
    bill += 20

    if add_pepperoni.upper() == "Y":
            bill += 3
    if extra_cheese.upper() == "Y":
            bill += 1
    
    print(f"Your final bill is ${bill}")

elif size.upper() == "L":
    bill += 25

    if add_pepperoni.upper() == "Y":
            bill += 3
    if extra_cheese.upper() == "Y":
            bill += 1
    
    print(f"Your final bill is ${bill}")

    
else:
    print("You picked the wrong size")