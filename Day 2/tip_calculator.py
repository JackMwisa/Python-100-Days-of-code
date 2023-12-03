
print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
bill = float(bill)

percentage_tip = input("What percentage would you like to give? 10, 12, 0r 15 ?")


tip = (bill * int(percentage_tip)) / 100 

people = input("How many people will split the bill?")
people = int(people)

total_bill = (bill + tip)

amount_per_person = total_bill / people

# amount_per_person = round(amount_per_person, 2)

amount_per_person = "{:.2f}".format(amount_per_person)
 

print(f"Each person should pay: ${amount_per_person}")  

