__author__ = 'iamja_000'

from itertools import product, starmap
import random
from entities import City, Scout

#OBJECTIVES:
#write a city function that scans for neighbours and converts to same origin if connected

class World:
    def __init__(self, x, y):
        self.cities = []
        self.scouts = []
        self.x = int(x)
        self.y = int(y)
        total_squares = self.x * self.x
        water_level = random.randint(0, 10)
        print("World born with size: {} comprising of {} squares and a water level of {}".format(self.x, total_squares, water_level))
        self.water_list = self.actual_water_world(water_level)
        self.city_generator()
        self.scout_generator()

    def water_return(self):
        return self.water_list

    def world_coordinates(self):
        w_coord = list(product(range(self.x), range(self.y)))
        return w_coord

    def city_return(self):
        city_locs = []
        for i in self.cities:
            loc = i.get_location()
            city_locs.append(loc)
        return city_locs


    def get_neighbours_specifiable(self, x_coord, y_coord, radius):
        r_list = []
        for i in range(-radius, radius+1):
            r_list.append(i)
        cells = starmap(lambda a,b: (x_coord+a, y_coord+b), product((r_list), (r_list)))
        return list(cells)[1:]

    def water_world(self, w_level):
        water_list = []
        return water_list

    def actual_water_world(self, w_level):
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
        free = [x for x in self.world_coordinates() if x not in self.water_return()]
        city_number = round(self.x/3)
        city_quantity = 0
        #THIS LOOP CAN DEFINITELY BE NEATENED UP...
        while city_quantity < city_number:
            city_coord = random.choice(free)
            a, b = city_coord
            while self.neighbour_type_check_boolean(a, b, 1, 2, self.water_return()):
                city_coord = random.choice(free)
                a, b = city_coord
            while self.neighbour_type_check_boolean(a, b, 2, 0, self.city_return()):
                city_coord = random.choice(free)
                a, b = city_coord

            self.cities.append(City(a, b, a, b))
            city_quantity += 1
        print("Our cities: {}".format(self.city_return()))

    def is_city_and_water_ok(self, a, b):
        false = 0
        if self.neighbour_type_check_boolean(a, b, 2, 0, self.city_return()):
            false += 1
        if self.neighbour_type_check_boolean(a, b, 1, 2, self.water_list):
            false += 1
        print("Value for coord {} {} is {}".format(a, b, false))


    def city_growth(self):
        for i in self.cities:
            if i.growth > 10:
                a, b = i.get_location()
                c, d = i.x0, i.y0
                pos_locs = self.neighbour_move_options_basic(a, b, 1)
                print("City at {} {} with origin {} {} has growth of {} \n potential moves = {} ".format(a, b, c, d, i.growth, pos_locs))
                our_move = random.choice(pos_locs)
                x, y = our_move
                self.scouts.append(Scout(x, y, c, d))
                i.growth = 0
            elif i.growth > 0:
                if i.growth < 11:
                    i.add_growth()


###################################
######## ^^ SCOUT STUFF ^^#########
###################################

    def scout_generator(self):
        for i in self.cities:
            a, b = i.get_location()
            x0, y0 = i.x0, i.y0
            combined_loc = a, b
            our_neighbours = self.get_neighbours_specifiable(a, b, 1)
            free_neighbours = [x for x in our_neighbours if x not in self.water_return()]
            free_neighbours.remove(combined_loc)
            free_neighbours = self.take_out_negative_and_overweight_neighbours(free_neighbours)
            if len(free_neighbours) > 0:
                candidate_loc = random.choice(free_neighbours)
                c, d = candidate_loc
                self.scouts.append(Scout(c, d, x0, y0))
            else:
                print("Looks like we don't have any spare neighbours.")
        for i in self.scouts:
            i.paths_taken.append(i.get_location())

    #SUPER HACKY, BUT GOOD IN PRINCIPLE, NOW JUST NEED TO REFACTOR
    def scout_movement(self):
        for i in self.scouts:
            a, b = i.get_location()
            path_so_far = i.return_paths()
            pos_moves = self.neighbour_move_options(a, b, 1)
            pos_moves = self.take_out_negative_and_overweight_neighbours(pos_moves)
            #print("Our cleaned moves: {}".format(pos_moves))
            other_cities = []
            other_cities.extend(self.city_return())
            i_origin = i.x0, i.y0
            other_cities.remove(i_origin)
            if self.neighbour_type_check(a, b, 1, other_cities) > 0:
                pos_locations = self.neighbour_type_check_return(a, b, 1, other_cities)
                our_decision = random.choice(pos_locations)
                print("Scout at ab {} {} is gonna join with city at {}".format(a, b, our_decision))
                c, d = our_decision
                self.scouts.remove(i)
                self.cities.append(City(a, b, c, d))
                for i in self.cities:
                    q, w = i.get_location()
                    e = c, d
                    r = q, w
                    if e == r:
                        i.add_growth()

            elif len(pos_moves) > 0:
                our_hits = i.hit_rate()
                if our_hits > 10:
                    #print("Taking extreme measures")
                    if self.neighbour_type_check(a, b, 3, other_cities) > 0:
                        locations = self.neighbour_type_check_return(a, b, 3, other_cities)
                        chosen_location = random.choice(locations)
                        c, d = chosen_location
                        for l in pos_moves:
                            e, f = l
                            if c > e:
                                if e > a:
                                    pos_moves.remove(l)
                            elif d > f:
                                if f > b:
                                    pos_moves.remove(l)
                        print("Our pos moves w/ radius 3 are now: {}".format(pos_moves))

                if self.neighbour_type_check(a, b, 2, other_cities) > 0:
                    locations = self.neighbour_type_check_return(a, b, 2, other_cities)
                    chosen_location = random.choice(locations)
                    c, d = chosen_location
                    for l in pos_moves:
                        e, f = l
                        #print("Checking city {} {} against move {} {} with scout at position: {} {}".format(c, d, e, f, a, b))
                        if c > e:
                            if e > a:
                                pos_moves.remove(l)
                        elif d > f:
                            if f > b:
                                pos_moves.remove(l)
                    print("Our pos moves are now: {}".format(pos_moves))
                else:
                    i.add_hit_rate()


                move = random.choice(pos_moves)
                print("Should move scout {} {} with hits {} to move {}".format(a, b, our_hits, move))
                c, d = move
                i.x = c
                i.y = d
                i.paths_taken.append(move)

            else:
                print("Out of moves!")
                i.more_lonely()
                if i.lonely > 10:
                    print("Too lonely, killing scout at position {} {}".format(a, b))
                    self.scouts.remove(i)




###################################
#### ^^ NEIGHBOURS AND CHUMS ^^####
###################################

    def take_out_negative_and_overweight_neighbours(self, input_list):
        temp_list = []
        for i in input_list:
            a, b = i
            if a < 0:
                temp_list.append(i)
            elif b < 0:
                temp_list.append(i)
            elif a >= self.x:
                temp_list.append(i)
            elif b >= self.x:
                temp_list.append(i)
        output_list = [x for x in input_list if x not in temp_list]
        return output_list


    def neighbour_move_options(self, x, y, distance_to_check):
        water_list = self.water_return()
        our_neighbours = self.get_neighbours_specifiable(x, y, distance_to_check)
        city_locations = self.city_return()
        scout_locations = []
        for i in self.scouts:
            i.get_location()
            scout_locations.append(i)

        pos_moves = [x for x in our_neighbours if x not in water_list]
        pos_moves_2 = [x for x in pos_moves if x not in scout_locations]
        final_moves = [x for x in pos_moves_2 if x not in city_locations]
        for i in final_moves:
            a, b = i
            if a < 0:
                #print("Looks like a {} of i {} is less than 0".format(a, i))
                final_moves.remove(i)
            elif b < 0:
                #print("Looks like b {} of i {} is less than 0".format(b, i))
                final_moves.remove(i)

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
        #print("Our entity at {} {} has {} neighbours".format(x, y, entity_count))
        if entity_count > number_to_check:
            return True
        else:
            return False

    def neighbour_move_options_basic(self, x, y, distance_to_check):
        water_list = self.water_return()
        our_neighbours = self.get_neighbours_specifiable(x, y, distance_to_check)
        city_locations = []
        for i in self.cities:
            i.get_location()
            city_locations.append(i)
        scout_locations = []
        for i in self.scouts:
            i.get_location()
            scout_locations.append(i)

        pos_moves = [x for x in our_neighbours if x not in water_list]
        pos_moves_2 = [x for x in pos_moves if x not in scout_locations]
        final_moves = [x for x in pos_moves_2 if x not in city_locations]
        return final_moves




#THIS IS HACKY AND WEIRD
    def scout_return(self):
        scouts_loc_loc = []
        for i in self.scouts:
            loca, locb = i.get_location()
            loc = loca, locb
            scouts_loc_loc.append(loc)

        return scouts_loc_loc

    def path_return(self):
        our_path_list = []
        for i in self.scouts:
            path_so_far = i.return_paths()
            our_path_list.extend(path_so_far)

        return our_path_list


#######################
##############tick funk


#####################################
#####################################
#####################################
#####################################


    def land_world(self, w_level):
        water_list = []
        print("Creating a world with lakes and or rivers")
        our_coordinates = self.world_coordinates()
        return water_list