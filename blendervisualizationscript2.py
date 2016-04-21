__author__ = 'iamja_000'

#import bpy
from itertools import product

positions = list(product(range(10), range(10)))

visual_map = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
['W', ' ', ' ', 'W', 'W', ' ', 'W', 'W', 'C', 'W'],
['W', ' ', ' ', ' ', 'W', ' ', 'W', 'R', 'C', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', 'W'],
['W', ' ', 'R', 'R', 'R', 'R', 'R', 'R', ' ', 'W'],
['W', ' ', 'C', 'X', 'X', 'X', ' ', 'C', ' ', 'W'],
['W', ' ', 'R', 'R', 'R', 'R', 'C', ' ', ' ', 'W'],
['W', ' ', 'X', 'W', ' ', 'W', ' ', 'W', ' ', 'W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]

xlist = []
ylist = []

print(positions)
print(positions[2][1])

def map_maker(coordinates, chosen_list, list_location):
    step = list_location
    for i in coordinates:
        chosen_list.append(i[step])
    return chosen_list

xcoord = map_maker(positions, xlist, 0)
ycoord = map_maker(positions, ylist, 1)

print("Who a lemon?")
newlocx = list(map(lambda x: x + x, xlist))
newlocy = list(map(lambda x: x + x, ylist))
print(newlocx)
print(newlocy)

new_list = []
for i in visual_map:
    new_list.extend(i)

print("Megalist")
print(new_list)

print(len(new_list))

i = 0
while i < len(new_list):
    print("Our coordinate is {}".format(positions[i]))
    print("Our character is {}".format(new_list[i]))
    x = positions[i][0]
    y = positions[i][1]
    z = 0
    our_object = new_list[i]
    if our_object == "W":
        (location=(x, y, z))
    elif our_object == "C":
        cubeobject(location=(x, y, z))
    i += 1
