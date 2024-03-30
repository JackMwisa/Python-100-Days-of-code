

age = input("what is your current age? ")

remaining_years = 90 - int(age) 

days  = int(remaining_years * 365.2421897) # days
weeks = int(remaining_years * 52)
months = int(remaining_years * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# you have  x days x weeks x months left if you lived until 90