__author__ = 'iamja_000'

from itertools import product, starmap
import random
from entities import City, Scout

def get_neighbours_specifiable(x_coord, y_coord, radius):
    r_list = []
    for i in range(-radius, radius+1):
        r_list.append(i)
    cells = starmap(lambda a,b: (x_coord+a, y_coord+b), product((r_list), (r_list)))
    our_position = x_coord, y_coord
    nu_list = list(cells)
    nu_list.remove(our_position)
    return nu_list

our_neighbours = get_neighbours_specifiable(0, 0, 1)

water_list = [(1,0),(1,1)]
scout_locations = [(2,1)]
city_locations = [(0,1)]

print("our moves {}".format(our_neighbours))
pos_moves = [x for x in our_neighbours if x not in water_list]
pos_moves_2 = [x for x in pos_moves if x not in scout_locations]
print("Pos2: {}".format(pos_moves_2))
final_moves = [x for x in pos_moves_2 if x not in city_locations]
print("Final: {}".format(final_moves))