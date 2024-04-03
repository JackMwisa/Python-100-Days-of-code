print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# Ask the user to choose left or right
direction = input("You're at a crossroad. Which direction do you want to go? Left or Right? ").lower()

if direction == "left":
    # If the user chooses left, prompt them to make another decision at the lake
    action = input("You've arrived at a lake. Do you want to 'swim' across or 'wait' for a boat? ").lower()
    
    if action == "wait":
        # If the user waits for the boat, they continue their journey
        print("You found a boat and crossed the lake safely.")
        
        # Now, they face another decision
        door = input("You've arrived at a house with three doors: Red, Blue, and Yellow. Which color do you choose? ").lower()
        
        if door == "yellow":
            # If they choose the yellow door, they find the treasure and win
            print("Congratulations! You found the treasure! You Win!")
        else:
            # Choosing any other door leads to a trap and they lose
            print("Oops! You opened a door to a room full of monsters. Game Over.")
    else:
        # If the user chooses to swim, they get attacked by crocodiles and lose
        print("Oh no! You were attacked by crocodiles while swimming. Game Over.")
else:
    # If the user chooses right, they fall into a hole and lose
    print("Oops! You fell into a hole. Game Over.")
