import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

my_options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 For Scissors.\n"))

my_choice = my_options[choice]

print(my_choice)

computer_choice = my_options[random.randint(0,2)]
 
print(f"computer choice \n {computer_choice}")


if 








# print(rock, paper, scissors)