print("Welcome to the tip Calculator.")

bill = input("what is your bill? $")


tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip_sel = float(bill) * (int(tip) / 100)

people = int(input("How many people have to split the bill? "))
total_pays = float(bill) + tip_sel


each_should_pay = round(total_pays / people, 2)
print(f"Each person should pay ${each_should_pay}")