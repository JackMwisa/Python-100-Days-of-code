
# for x in range(1, 101, 2):
#     # print(x)
#     if x % 2 != 0:
#         print(x)

row1 = ["😆", "😆", "😆"]
row2 = ["😭", "😭", "😭"]
row3 = ["😣", "😣", "😣"]

map = [row1,row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure? ")


row = int(position[0]) - 1
col = int(position[1]) - 1

map[row][col] = "X"

print(f"{row1}\n{row2}\n{row3}")
