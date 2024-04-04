


row1 = ["😆", "😆", "😆"]
row2 = ["😭", "😭", "😭"]
row3 = ["😣", "😣", "😣"]

map = [row1,row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure? ")


row = position[0]
col = position[1]

map[row][col] = "X"