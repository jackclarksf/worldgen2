__author__ = 'iamja_000'

from itertools import product, starmap
import random
from entities import City, Scout


#OBJECTIVES:
# CREATE A WORLD WITH A SPECIFIABLE AMOUNT OF WATER VERSUS LAND
# IF WATER OVER 50%, MAKE AN ISLAND. IF WATER UNDER 50%, MAKE LAKE


class World:
    def __init__(self, x, y):
        self.cities = []
        self.cities_loc = []
        self.scouts = []
        self.scouts_loc = []
        self.x = int(x)
        self.y = int(y)
        total_squares = self.x * self.x
        water_level = random.randint(0, 10)
        print("World born with size: {} comprising of {} squares and a water level of {}".format(self.x, total_squares, water_level))
        self.water_list = self.water_world(water_level)
        self.city_generator()
        self.scout_generator()

    def water_return(self):
        return self.water_list

    def world_coordinates(self):
        w_coord = list(product(range(self.x), range(self.y)))
        return w_coord

    def get_neighbours_specifiable(self, x_coord, y_coord, radius):
        r_list = []
        for i in range(-radius, radius+1):
            r_list.append(i)
        cells = starmap(lambda a,b: (x_coord+a, y_coord+b), product((r_list), (r_list)))
        return list(cells)[1:]

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
        sug_frequency = round(self.x)/3
        print("Our suggested frequency is {}".format(sug_frequency))
        self.space_creator_length(round(self.x/2), round(self.y/2), sug_frequency, water_list)
        return water_list

    def island_function(self, island_list):
        additional_island_list = []
        for i in island_list:
            water_roll = random.randint(0, 10)
            a, b = i
            if a in range(1, self.x-1):
                self.island_smart_scatter(a, b, i, water_roll, additional_island_list)
        return additional_island_list

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
        for i in coordinates_to_check:
            a, b = i
            self.space_creator(a, b, check_list)

    #NEXT STEP - MAKE RADIUS SCALE WITH SIZE
    def space_creator(self, coordinate_a, coordinate_b, list_of_entities):
        rad_to_check = round((self.x/3)/3)
        nearby = self.get_neighbours_specifiable(coordinate_a, coordinate_b, rad_to_check)
        for i in nearby:
            if i in list_of_entities:
                list_of_entities.remove(i)

    def island_smart_scatter(self, inputa, inputb, inputi, water_stat, add_list):
        mid_point = round(abs(1 - self.x-1) / 2)
        low_quarter = round(mid_point - (mid_point/2))
        up_quarter = round(mid_point + (mid_point/2))
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

###################################
######## ^^ CITY STUFF ^^##########
###################################

    def city_generator(self):
        global_co = self.world_coordinates()
        water_list = self.water_return()
        free = [x for x in global_co if x not in water_list]
        city_number = round(self.x/3)
        city_quantity = 0
        while city_quantity < city_number:
            city_coord = random.choice(free)
            a, b = city_coord
            print("Checking this coordinate w/duel function test? {}".format(city_coord))
            self.is_city_and_water_ok(a, b)

            while self.neighbour_type_check_boolean(a, b, 1, 2, water_list):
                city_coord = random.choice(free)
                a, b = city_coord
                print("Water triggered: How about this coordinate, then? {}".format(city_coord))
            while self.neighbour_type_check_boolean(a, b, 2, 0, self.cities_loc):
                city_coord = random.choice(free)
                a, b = city_coord
                print("City triggered: How about this coordinate, then? {}".format(city_coord))

#NOT FINDING CITIES CORRECTLY, DAGNABBIT

            self.cities.append(City(a, b, a, b))
            city_loc = self.cities[city_quantity].get_location()
            city_loc = a, b
            self.cities_loc.append(city_loc)
            print("Our cities: {}".format(self.cities_loc))
            city_quantity += 1

    def is_city_and_water_ok(self, a, b):
        false = 0
        if self.neighbour_type_check_boolean(a, b, 2, 0, self.cities_loc):
            false += 1
        if self.neighbour_type_check_boolean(a, b, 1, 2, self.water_list):
            false += 1
        print("Value for coord {} {} is {}".format(a, b, false))

###################################
######## ^^ SCOUT STUFF ^^#########
###################################

    def scout_generator(self):
        global_co = self.world_coordinates()
        water_list = self.water_return()
        free = [x for x in global_co if x not in water_list]
        for i in self.cities:
            a, b = i.get_location()
            combined_loc = a, b
            our_neighbours = self.get_neighbours_specifiable(a, b, 1)
            free_neighbours = [x for x in our_neighbours if x not in water_list]
            free_neighbours.remove(combined_loc)
            if len(free_neighbours) > 0:
                candidate_loc = random.choice(free_neighbours)
                c, d = candidate_loc
                self.scouts.append(Scout(c, d, a, b))
                self.scouts_loc.append(candidate_loc)
            else:
                print("Looks like we don't have any spare neighbours.")

    #SUPER HACKY, BUT GOOD IN PRINCIPLE, NOW JUST NEED TO REFACTOR
    def scout_movement(self):
        for i in self.scouts:
            a, b = i.get_location()
            path_so_far = i.return_paths()
            print("So far: {}".format(path_so_far))
            pos_moves = self.neighbour_move_options(a, b, 1)
            if len(pos_moves) > 0:
                print("Our moves: {}".format(pos_moves))
                if self.neighbour_type_check(a, b, 2, self.cities_loc) > 0:
                    print("Looks like we have a city nearby!")
                    i_origin = i.x0, i.y0
                    print("We originated at {}".format(i_origin))
                    print("Our city list is {}".format(self.cities_loc))
                    other_cities = self.cities_loc
                    other_cities.remove(i_origin)
                    print("Our other cities are: {}".format(other_cities))
                    if self.neighbour_type_check(a, b, 2, other_cities) > 0:
                        print("Definite collision!")
                        locations = self.neighbour_type_check_return(a, b, 2, other_cities)
                        print("Other city locations are: {}".format(locations))
                        for j in locations:
                            c, d = j
                            for l in pos_moves:
                                e, f = l
                                print("Checking city {} {} against move {} {} with scout at position: {} {}".format(c, d, e, f, a, b))

                move = random.choice(pos_moves)
                print("Should move scout {} {} to move {}".format(a, b, move))
                c, d = move
                i.x = c
                i.y = d
                self.scouts_loc.append(move)
                i.paths_taken.append(move)
            else:
                print("Out of moves!")




###################################
#### ^^ NEIGHBOURS AND CHUMS ^^####
###################################

    def neighbour_move_options(self, x, y, distance_to_check):
        water_list = self.water_return()
        our_neighbours = self.get_neighbours_specifiable(x, y, distance_to_check)
        city_locations = self.cities_loc

        pos_moves = [x for x in our_neighbours if x not in water_list]
        pos_moves_2 = [x for x in pos_moves if x not in self.scouts_loc]
        final_moves = [x for x in pos_moves_2 if x not in city_locations]
        return final_moves

    def neighbour_type_check(self, x, y, distance_to_check, water_coordinates):
        neighbours_to_check = self.get_neighbours_specifiable(x, y, distance_to_check)
        water_count = 0
        for i in neighbours_to_check:
            if i in water_coordinates:
                water_count += 1
        return water_count

    def neighbour_type_check_return(self, x, y, distance_to_check, water_coordinates):
        neighbours_to_check = self.get_neighbours_specifiable(x, y, distance_to_check)
        neighbour_list = []
        for i in neighbours_to_check:
            if i in water_coordinates:
                neighbour_list.append(i)
        return neighbour_list

    def neighbour_type_check_boolean(self, x, y, distance_to_check, number_to_check, coordinates_to_check):
        neighbours_to_check = self.get_neighbours_specifiable(x, y, distance_to_check)
        entity_count = 0
        for i in neighbours_to_check:
            if i in coordinates_to_check:
                entity_count += 1
        print("Our entity at {} {} has {} neighbours".format(x, y, entity_count))
        if entity_count > number_to_check:
            return True
        else:
            return False



    def city_return(self):
        return self.cities_loc

#THIS IS HACKY AND WEIRD
    def scout_return(self):
        scouts_loc_loc = []
        for i in self.scouts:
            loca, locb = i.get_location()
            loc = loca, locb
            scouts_loc_loc.append(loc)

        return scouts_loc_loc



#####################################
#####################################
#####################################
#####################################


    def land_world(self, w_level):
        water_list = []
        print("Creating a world with lakes and or rivers")
        our_coordinates = self.world_coordinates()
        return water_list