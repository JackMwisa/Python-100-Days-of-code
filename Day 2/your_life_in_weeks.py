# time left program

age = input("What is your current age?")
age = int(age)

age_limit = 90

age_left = age_limit - age


# year = 365 days
# year = 12 months
# year = 52 weeks 

left_days = age_left * 365
left_months = age_left * 12
left_weeks = age_left * 52



print(f"you are {age} years old")
print(f"The age limit is {age_limit}")
print(f"You are remaining with {age_left} years old")
print(f"you have {left_days} days, {left_weeks} weeks, and {left_months} months left")