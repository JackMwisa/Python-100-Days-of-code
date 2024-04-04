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


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n  "))

my_choice = my_options[choice]
print(f"My choice is \n {my_choice}")

computer_choice = random.choice(my_options)
print(f"Computer Choses \n {computer_choice}")


# if choice > 2 or choice < 0:
#     print("Wrong choice! You lose")
if choice == 0 and computer_choice == scissors:
    print("You win")
elif choice == 1 and computer_choice == rock:
    print("You win")
elif choice == 2 and computer_choice == paper:
    print("You win")
elif my_choice == computer_choice:
    print("draw")
else:
    print("You lose")

