

print("Welcome to the treasure Island!!!!!!!!!")
print("Your mission is to find  the treasure")


road = input(input("Choose left or right? "))
road = road.lower() 


if road == "left":
    lake= input("You have reached in front of a lake, choose swim or wait for a boat").lower()
    
    if lake == swim:
        print("You won")
    else:
        print("You're dead")
else:
    print("You have failed") 