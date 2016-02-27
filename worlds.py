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
        if water >= 0:
            list_to_return = self.water_world(water)
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
        extra_list = self.island_function(remaining_list)
        water_list = extra_list + water_list
        self.space_creator_length(round(self.x/2), round(self.y/2), 5, water_list)
        #self.space_creator(round(self.x/2), round(self.y/2), water_list)
        return water_list

    def space_creator_length(self, roota, rootb, frequency, check_list):
        coordinates_to_check = []
        a = roota, rootb
        coordinates_to_check.append(a)
        count = 0
        while count < frequency:
            roota -= 1
            a = roota, rootb
            coordinates_to_check.append(a)
            count += 1
        print("Coordinates: {}".format(coordinates_to_check))
        for i in coordinates_to_check:
            a, b = i
            self.space_creator(a, b, check_list)

#some really weird shit is happening here

    def space_creator(self, coordinate_a, coordinate_b, list_of_entities):
        #print("Checking {} {}".format(coordinate_a, coordinate_b))
        nearby = self.get_neighbours(coordinate_a, coordinate_b)
        for i in nearby:
            if i in list_of_entities:
                #print("Collision between i {} and entity list {}".format(i, list_of_entities))
                list_of_entities.remove(i)

    def island_function(self, island_list):
        additional_island_list = []
        middle_point = abs(1 - self.x-1)
        #print("OK, we're checking numbers between {} and {} with midpoint {}".format(1, self.x-1, middle_point))
        for i in island_list:
            water_roll = random.randint(0, 10)
            a, b = i
            if a in range(1, self.x-1):
                self.island_smart_scatter(a, b, i, water_roll, additional_island_list)
        return additional_island_list
        #print("Our extra list is {}".format(additional_island_list))

    def island_smart_scatter(self, inputa, inputb, inputi, water_stat, add_list):
        mid_point = round(abs(1 - self.x-1) / 2)
        low_quarter = round(mid_point - (mid_point/2))
        up_quarter = round(mid_point + (mid_point/2))
        #print("OK, our points are middle {} low {} and high {} and A is {} and B is {}".format(mid_point, low_quarter, up_quarter, inputa, inputb))
        if inputa and inputb < low_quarter:
            if water_stat > 3:
                add_list.append(inputi)
        elif inputa and inputb > up_quarter:
            if water_stat > 3:
                add_list.append(inputi)
        elif inputa and inputb >= low_quarter:
            if inputa and inputb <= up_quarter:
                if water_stat > 7:
                    add_list.append(inputi)

    def land_world(self, w_level):
        water_list = []
        print("Creating a world with lakes and or rivers")
        our_coordinates = self.world_coordinates()
        return water_list

