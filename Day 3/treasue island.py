

print("Welcome to the treasure Island!!!!!!!!!")
print("Your mission is to find  the treasure")


road = input(input("Choose left or right? "))
road = road.lower() 


if road == "left":
        
    lake= input("You have reached infront of a lake, choose swim or wait for a boat")
    lake = lake.lower()

    if lake == swim:
        print("Yes")
        
    else:
        print("You're dead")
    
else:
    print("You have failed") 