import bpy
from itertools import product

positions = list(product(range(10), range(10)))

visual_map = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
['W', ' ', 'W', 'W', ' ', 'W', 'W', 'S', 'W', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', 'R', 'C', ' ', 'W'],
['W', ' ', ' ', 'C', 'R', 'R', 'R', ' ', ' ', 'W'],
['W', ' ', 'C', 'C', 'R', 'R', 'R', ' ', ' ', 'W'],
['W', 'S', 'R', 'R', 'R', 'C', 'C', ' ', ' ', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'W'],
['W', 'W', ' ', ' ', ' ', 'W', ' ', 'W', 'W', 'W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]

xlist = []
ylist = []

print(positions)
print(positions[2][1])

cubeobject = bpy.ops.mesh.primitive_cube_add
cylobject = bpy.ops.mesh.primitive_cone_add
tubeobject = bpy.ops.mesh.primitive_cylinder_add

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

def distance_spanner(x_print, y_print, our_goal, our_distance):
    while our_distance != our_goal:
        cubeobject(location=(x_print, y_print, our_distance))
        our_distance -= 1

i = 0
while i < len(new_list):
    print("Our coordinate is {}".format(positions[i]))
    print("Our character is {}".format(new_list[i]))
    x = newlocx[i]
    y = newlocy[i]
    z = 0
    our_object = new_list[i]
    if our_object == "W":
        cubeobject(location=(x, y, -3))
    elif our_object == "C":
        cubeobject(location=(x, y, z))
        distance_spanner(x, y, -4, 0)
    elif our_object == "R":
        cubeobject(location=(x, y, -1))
        distance_spanner(x, y, -4, -1)
    elif our_object == " ":
        cubeobject(location=(x, y, -2))
        distance_spanner(x, y, -4, -2)
    elif our_object == "S":
        cubeobject(location=(x, y, z))
        distance_spanner(x, y, -4, 0)
    i += 1
