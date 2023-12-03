# pizza order program in python


print("Welcome to python Pizza deliveries!")
size = input("What size pizza do you want? S, M, or  L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")


# small pizza  = $15
# medium pizza  = $20
# large pizza  = $25

# peperoni for small pizza is $2
# peperoni for meduim and large pizza is $3

# Extra cheese for any size pizza is + 5

price = 0

if size == "s" or size == "S":
    price += 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 2
    else:
        print("Thank you")
elif size == "m" or size == "M":
    price += 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3
    else:
        print("Thank you")
elif size == "l" or size == "L":
    price += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3
    else:
        print("Thank you")

if extra_cheese == "Y" or "y":
    price +=5
    print(f"Your final bill is {price}")
else:
    print(f"Your final bill is {price}")

