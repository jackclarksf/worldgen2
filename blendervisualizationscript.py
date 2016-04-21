__author__ = 'iamja_000'

import bpy
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



############
###OLD WORKING CODE
############
positions = list(product(range(10), range(10)))

cubeobject = bpy.ops.mesh.primitive_cube_add
cylobject = bpy.ops.mesh.primitive_cone_add
frequencies = [6,3,5,5,5,1,7,8,2,0]
frequencies1 = [[6,3,5,5,5,1,7,8,2,0],
[6,5,6,2,9,3,4,3,1,0],
[9,0,6,0,3,5,8,3,1,0],
[5,5,5,4,2,4,4,3,5,2],
[4,5,3,2,4,5,0,5,6,3],
[6,7,5,5,6,4,8,6,10,5],
[1,5,5,2,4,4,4,0,4,5],
[0,0,5,9,9,8,4,7,6,4],
[9,2,2,4,4,2,3,3,3,5],
[10,9,7,5,4,2,2,4,4,2]]

new_frequencies = sum(frequencies1, [])

xlist = []
ylist = []
#lemon = []

def map_maker(coordinates, chosen_list, list_location):
    step = list_location
    for i in coordinates:
        chosen_list.append(i[step])

xcoordinates = map_maker(positions, xlist, 0)
ycoordinates = map_maker(positions, ylist, 1)
#print(xlist)
#print(ylist)

newloc = list(map(lambda x: x + x, ylist))
newlocx = list(map(lambda x: x + x, xlist))
#print(newloc)



i = 0
step = 0

def depth_printer(x_print, y_print, list_input, list_step):
    temp_number = list_input[list_step]
    temp_list = [i for i in range(temp_number)]
    for i in temp_list:
        cubeobject(location=(x_print, y_print, i))


while i < 90:
    print("i is now: {}".format(i))
    x = newlocx[step]
    y = newloc[step]
    z = new_frequencies[step]
    cylobject(location=(x, y, z))
    depth_printer(x, y, new_frequencies, step)
    i += 1
    step += 1