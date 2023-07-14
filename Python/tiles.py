"""
How many tiles are needed?

You buy 17 packages of tiles containing 6 tiles each.

How many tiles will be left over?

In this quiz you're going to do some calculations
for a tiles. Two parts of a
floor need tiling. One part is 9 tiles wide by 7
tiles long, the other is 5 tiles
wide by 7 tiles long. Tiles come in packages of 6.

"""

tiles = 17 * 6
floor_1 = 9 * 7
floor_2 = 5 * 7
left_over_tiles = tiles - (floor_1 + floor_2)

print(left_over_tiles)





