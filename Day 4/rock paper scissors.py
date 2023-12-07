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

random_cp = random.randint(0,2)

computer_choice = my_options[random_cp]
 
print(f"computer choice \n {computer_choice}")


if choice == 0 and random_cp == 1:
    print("You have failed")
elif choice == 1 and random_cp == 2:
    print("You have failed")
elif choice == 2 and random_cp == 0:
    print("You have failed")
elif choice == random_cp:
    print("No winner")
else:
    print("You have won")
    





# print(computer_choice)
# print(choice)


# print(rock, paper, scissors)