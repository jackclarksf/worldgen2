__author__ = 'iamja_000'

from itertools import product, starmap
import random

#OBJECTIVES:
# CREATE A WORLD WITH A SPECIFIABLE AMOUNT OF WATER VERSUS LAND
# IF WATER OVER 50%, MAKE AN ISLAND. IF WATER UNDER 50%, MAKE LAKE


class World:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        total_squares = self.x * self.x
        water_level = random.randint(0, 10)
        print("World born with size: {} comprising of {} squares and a water level of {}".format(self.x, total_squares, water_level))
        self.water_list = self.water_list_generator(water_level)


    def water_return(self):
        return self.water_list

    def world_coordinates(self):
        w_coord = list(product(range(self.x), range(self.y)))
        return w_coord

    def get_neighbours(self, x_coord, y_coord):
        cells = starmap(lambda a,b: (x_coord+a, y_coord+b), product((0,-1,+1), (0,-1,+1)))
        return list(cells)[1:]

    def water_list_generator(self, water):
        if water > 4:
            list_to_return = self.water_world(water)
            return list_to_return
        elif water < 5:
            list_to_return = self.land_world(water)
            return list_to_return


    def water_world(self, w_level):
        water_list = []
        print("Creating an island world")
        our_coordinates = self.world_coordinates()
        for i in our_coordinates:
            a, b = i
            if a == 0:
                water_list.append(i)
            elif b == 0:
                water_list.append(i)
            elif a == self.x-1:
                water_list.append(i)
            elif b == self.x-1:
                water_list.append(i)
        remaining_list = [x for x in our_coordinates if x not in water_list]
        #print(remaining_list)
        extra_list = self.island_function(remaining_list)
        water_list = extra_list + water_list
        return water_list

    def island_function(self, island_list):
        additional_island_list = []
        for i in island_list:
            water_roll = random.randint(0, 10)
            a, b = i
            if a in range(1, self.x-1):
                if water_roll > 5:
                    additional_island_list.append(i)
        #print("Our extra list is {}".format(additional_island_list))
        return additional_island_list


    def land_world(self, w_level):
        water_list = []
        print("Creating a world with lakes and or rivers")
        our_coordinates = self.world_coordinates()
        return water_list

