__author__ = 'iamja_000'

from itertools import product, starmap
import collections
import random
from entities import City, Scout, Road, MetaRoad, Vegetation

############3LINUX TEST!!!!! ^ ____ ^

#OBJECTIVES:
#write a city function that scans for neighbours and converts to same origin if connected
#probably implement by adding age to city. The oldest city propagates origin to others connected to it.

class World:
    def __init__(self, x, y):
        self.cities = []
        self.scouts = []
        self.roads = []
        self.vegetation = []
        self.x = int(x)
        self.y = int(y)
        total_squares = self.x * self.x
        water_level = random.randint(0, 10)
        print("World born with size: {} comprising of {} squares and a water level of {}".format(self.x, total_squares, water_level))
        self.water_list = self.actual_water_world(water_level)
        self.land_generator()
        self.city_generator()
        self.scout_generator()
        self.tile_pop_dict = self.main_dictionary()
        print(self.tile_pop_dict)

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
        return water_list

    def actual_water_world(self, w_level):
        water_list = []
        our_coordinates = self.world_coordinates()
        remaining_list = [x for x in our_coordinates if x not in water_list]
        extra_list = self.island_function(remaining_list)
        water_list = extra_list + water_list
        sug_frequency = round(self.x)/3
        self.space_creator_length((round(self.x/3))*2, round(self.y/2), sug_frequency, water_list)
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

    def space_creator(self, coordinate_a, coordinate_b, list_of_entities):
        rad_to_check = round((self.x/3)/2)
        #print("cHECKING RADIUS AT A: {} B{} WITH RADIUS {}".format(coordinate_a, coordinate_b, rad_to_check))
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
######## ^^ LAND STUFF ^^##########
###################################
    def land_generator(self):
        land = [x for x in self.world_coordinates() if x not in self.water_return()]
        for i in land:
            a, b = i
            self.vegetation.append(Vegetation(a, b))


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
            while len(self.neighbour_type_check_return(a, b, 1, self.water_return())) > 1:
               #PRETTY SURE THIS ISN'T WORKING PROPERLY. NEED BETTER/DIFFERENT TELEMETRY
                city_coord = random.choice(free)
                a, b = city_coord
            while len(self.neighbour_type_check_return(a, b, 2, self.city_return())) > 0:
                city_coord = random.choice(free)
                a, b = city_coord

            self.cities.append(City(a, b, a, b))
            city_quantity += 1
        print("Our cities: {}".format(self.city_return()))

    def city_growth(self):
        for i in self.cities:
            a, b = i.get_location()
            c, d = i.x0, i.y0
            if i.growth > 10:
                pos_locs = self.neighbour_move_options(a, b, 1)
                if len(pos_locs) > 0:
                    #print("City at {} {} with origin {} {} has growth of {} \n potential moves = {} ".format(a, b, c, d, i.growth, pos_locs))
                    our_move = random.choice(pos_locs)
                    x, y = our_move
                    self.scouts.append(Scout(x, y, c, d))
                    i.growth = 0
            elif i.growth > 0:
                if i.growth < 11:
                    i.add_growth()
            i.add_age()
            if i.age % 40 == 0:
                pos_locs = self.neighbour_move_options(a, b, 1)
                if len(pos_locs) > 0:
                    #print("City at {} {} with origin {} {} has growth of {} \n potential moves = {} ".format(a, b, c, d, i.growth, pos_locs))
                    our_move = random.choice(pos_locs)
                    x, y = our_move
                    self.scouts.append(Scout(x, y, c, d))
                else:
                    print("City is crowded!")

    def city_origin_rationalizer(self):
        city_origin_dict = dict()
        for i in self.cities:
            city_origin_dict[i.get_location()] = i.return_city_origin()
        #print("Our cities & origin: {}".format(city_origin_dict))

    def road_rationalizer2(self):
        our_length = len(self.roads)
        our_length_range = list(range(our_length))
        catchall_road = dict()
        if our_length > 1:
            print("Roads = {} with range {}".format(our_length, our_length_range))
            for i in our_length_range:
                the_route = self.roads[i].get_route()
                print("The route: {}".format(the_route))
                catchall_road[i] = the_route
                if i < our_length-1:
                    adjacent_route = self.roads[i+1].get_route()
                    print("Adjacent route: {}".format(adjacent_route))
                    similarity_checker = set(the_route).intersection(adjacent_route)
                    print("Our similarity: {}".format(similarity_checker))
                    if len(similarity_checker) > 0:
                        print("Something similar, we should do something here.")
                        self.roads.remove(self.roads[i+1])
                        self.roads.remove(self.roads[i])
                        combined_list = []
                        combined_list.extend(the_route)
                        combined_list.extend(adjacent_route)
                        print("Our combined list we're trying to extend is: {}".format(combined_list))
        print(catchall_road)
        #####RIGHT SORTA IDEA BUT WRONG IMPLEMENTATION. DO WE NEED TO USE A RECURSIVE FUNCTION?

    def road_rationalizer3(self):
        our_length = len(self.roads)
        our_length_range = list(range(our_length))
        catchall_road = dict()
        catchall_city = dict()
        count = 0
        print("Catchall road")
        for i in self.roads:
            catchall_road[count] = i.return_end()
            count += 1
        print(catchall_road)

        c_count = 0
        for j in self.cities:
            catchall_city[c_count] = j.return_city_origin()
            c_count += 1
        print(catchall_city)

    def road_rationalizer(self):
        meta_road_list = []
        count = 0
        for i in self.roads:
            our_city = i.city_orig()
            our_end = i.return_end()
            city_and_end = our_city + our_end
            if city_and_end in meta_road_list:
                #print("looks like we have a double for {}!".format(city_and_end))
                shared_road_index = meta_road_list.index(city_and_end)
                print(shared_road_index)
                transplant_route = i.get_route()
                #print("Trying to transplant route {} into road {}".format(transplant_route, self.roads[shared_road_index]))
                #print("Current route: {}".format(self.roads[shared_road_index].road_route))
                self.roads[shared_road_index].road_route.extend(transplant_route)
                #print("Route now: {}".format(self.roads[shared_road_index].road_route))
                #print("Zapping road! ROad number currently: {}".format(len(self.roads)))
                self.roads.remove(i)
                #print("Zapped. Roads now: {}".format(len(self.roads)))

            #meta_road_list.append(count)
            meta_road_list.append(city_and_end)
            count += 1
            #print("Our roads and cities: {}".format(meta_road_list))

    def road_route_rationalizer(self):
        for i in self.roads:
            our_route = i.get_route()
            duplicate_list = [item for item, count in collections.Counter(our_route).items() if count > 1]
            if len(duplicate_list) > 0:
                for i in duplicate_list:
                    our_route.remove(i)










###################################
######## ^^ SCOUT STUFF ^^#########
###################################

    def scout_generator(self):
        for i in self.cities:
            a, b = i.get_location()
            x0, y0 = i.x0, i.y0
            combined_loc = a, b
            free_neighbours = self.take_out_negative_and_overweight_neighbours([x for x in self.get_neighbours_specifiable(a, b, 1) if x not in self.water_return()])
            free_neighbours.remove(combined_loc)

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
            our_hits = i.hit_rate()
            scout_origa, scout_origb = i.return_origin()
            scout_orig = i.return_origin()
            pos_moves = self.neighbour_move_options(a, b, 1)
            other_cities = self.origin_cleaner(self.cities, scout_orig)

            if len(self.neighbour_type_check_return(a, b, 1, other_cities)) > 0:
                our_decision = random.choice(self.neighbour_type_check_return(a, b, 1, other_cities))
                #print("Scout at ab {} {} with origination {} {} is gonna join with city at {}".format(a, b, scout_origa, scout_origb, our_decision))
                self.scouts.remove(i)
                for i in self.cities:
                    r = i.get_location()
                    if our_decision == r:
                        origina, originb = i.return_city_origin()
                        print("This city at {} has origin {} {}".format(r, origina, originb))
                        self.cities.append(City(a, b, origina, originb))
                        i.add_growth()
                        #THIS IS THE POINT WHERE WE NEED TO ADD THE ORIGIN
                        self.road_constructor(a, b, scout_origa, scout_origb, origina, originb)
                        #THIS IS WHERE WE CALL THE ROAD CREATOR FUNCTION

            elif our_hits > 50:
                #print("We've been talking aimless for too long with our {} hits".format(our_hits))
                print("Too aimless, killing scout at position {} {}".format(a, b))
                self.scouts.remove(i)

#THIS MOVEMENT LOOP IS A BIT FUCKED I THINK
            elif len(pos_moves) > 0:
#                our_hits = i.hit_rate()
                if our_hits > 10:
                    if len(self.neighbour_type_check_return(a, b, 3, other_cities)) > 0:
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
                        #print("Our pos moves w/ radius 3 are now: {}".format(pos_moves))

                if len(self.neighbour_type_check_return(a, b, 2, other_cities)) > 0:
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
                    #print("Our pos moves are now: {}".format(pos_moves))
                else:
                    i.add_hit_rate()

                move = random.choice(pos_moves)
                #print("Should move scout {} {} with hits {} to move {}".format(a, b, our_hits, move))
                c, d = move
                i.x = c
                i.y = d
                i.paths_taken.append(move)

            else:
                print("Out of moves!")
                #DEBATABLE AS TO WHETHER WE NEED THIS RATHER THAN JUST A STRAIGHT KILL FUNCTION
                i.more_lonely()
                if i.lonely > 10:
                    print("Too lonely, killing scout at position {} {}".format(a, b))
                    self.scouts.remove(i)

#################^^^^ THERE'S SOME PRETTY UGLY STUFF GOING ON IN THIS LOOP

###################################
#########ROADBUILDING#######
###################################
#function that takes in a city and a scout origin
#works out a line between them that skirts around water


    def road_constructor(self, city_coord_a, city_coord_b, origin_coord_a, origin_coord_b, city_origin_a, city_origin_b,):
        road_path = []
        #print("Attempting to draw road between {} {} and origin {} {}".format(city_coord_a, city_coord_b, origin_coord_a, origin_coord_b))
        dummy_city_a = city_coord_a
        dummy_city_b = city_coord_b
        dummy_origin_a = origin_coord_a
        dummy_origin_b = origin_coord_b
        a_diff = dummy_city_a - dummy_origin_a
        b_diff = dummy_city_b - dummy_origin_b
        #print("Our diffs are X {} and Y {}".format(a_diff, b_diff))
        abs_a_diff = abs(dummy_city_a - dummy_origin_a)
        abs_b_diff = abs(dummy_city_b - dummy_origin_b)
        while abs_a_diff > 0:
            calc_options = [-1, 1]
            dummy_city_a += random.choice(calc_options)
            new_diff = abs(dummy_city_a - dummy_origin_a)
            if new_diff < abs_a_diff:
                combined_a = dummy_city_a, dummy_city_b
                road_path.append(combined_a)
                abs_a_diff = new_diff

        while abs_b_diff > 0:
            calc_options = [-1, 1]
            dummy_city_b += random.choice(calc_options)
            new_diff = abs(dummy_city_b - dummy_origin_b)
            if new_diff < abs_b_diff:
                combined_b = dummy_city_a, dummy_city_b
                road_path.append(combined_b)
                abs_b_diff = new_diff

        #print("R path: {}".format(road_path))
        seeker_coordinate = origin_coord_a, origin_coord_b
        city_coordinate = city_coord_a, city_coord_b
        city_origin_coordinate = city_origin_a, city_origin_b
        if seeker_coordinate in road_path:
            road_path.remove(seeker_coordinate)

            #THINK WE NEED TO APPEND ORIGIN COORD
            print("Creating a road at {} with origin {} and scout origin {}".format(city_coordinate, city_origin_coordinate, seeker_coordinate))
            self.roads.append(Road(city_coordinate, seeker_coordinate, road_path, city_origin_coordinate))


###################################
#####NEIGHBOURS AND CHUMS#####
###################################

                ####THIS WHOLE SECTION CAN BE SLIMMED DOWN, I THINK ###

    def take_out_negative_and_overweight_neighbours(self, input_list):
        """
        This function takes in a list and then removes coordinates that are out of bounds
        """
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
        final_moves = self.take_out_negative_and_overweight_neighbours(final_moves)

        return final_moves

    def neighbour_type_check_return(self, x, y, distance_to_check, entity_coordinates):
        neighbour_list = [x for x in self.get_neighbours_specifiable(x, y, distance_to_check) if x in entity_coordinates]
        return neighbour_list

    def origin_cleaner(self, input_list, origin_to_clean):
        orig_list = []
        for i in input_list:
            i_origin = i.return_city_origin()
            if i_origin != origin_to_clean:
                orig_list.append(i_origin)
        return orig_list


#THIS IS HACKY AND WEIRD
    def scout_return(self):
        scouts_loc_loc = []
        for i in self.scouts:
            loc = i.get_location()
            scouts_loc_loc.append(loc)

        return scouts_loc_loc

    def path_return(self):
        our_path_list = []
        for i in self.scouts:
            path_so_far = i.return_paths()
            our_path_list.extend(path_so_far)

        return our_path_list

    def city_return(self):
        city_locs = []
        for i in self.cities:
            loc = i.get_location()
            city_locs.append(loc)
        return city_locs

    def vegetation_return(self):
        our_veggies = []
        for i in self.vegetation:
            loc = i.return_location()
            our_veggies.append(loc)
        return our_veggies

    def water_return(self):
        return self.water_list

    def roads_return(self):
        roads_to_return = []
        for i in self.roads:
            r_path = i.get_route()
            roads_to_return.extend(r_path)
        return roads_to_return

######################################
#########TELEMETRY OUTPUT#############
######################################

    def coordinate_telemetry(self, tick_number):
        our_cities = self.city_return()
        our_paths = self.path_return()
        our_scouts = self.scout_return()
        our_water = self.water_return()
        print("At tick number: {} \n Water: {} \n Scouts: {} \n Paths: {} \n Cities: {}".format(tick_number, our_water, our_scouts, our_paths, our_cities))
        self.update_dictionary(our_paths, our_scouts)
        #print("Dictionary now: {}".format(self.tile_pop_dict))
        city_dictionary = self.city_dictionary()
        #print("Our cities are now: {}".format(city_dictionary))
        #NEXT STEP: WRITE THIS OUT TO A TEXT FILE


    #FUNCTION COUNTS INSTANCES OF SCOUTS, PATHS, IN SPECIFIC COORDINATE. INCREMENTS BY 1 IF PRESENT.


    #THIS FUNCTION UPDATES A DICTIONARY OF CITIES AND INCREMENTS THEIR AGE

    def city_age(self):
        for i in self.cities:
            i.add_age()

    def city_dictionary(self):
        city_dict = dict()
        for i in self.cities:
            location = i.get_location()
            #i.add_age()
            city_dict[location] = i.age
        return city_dict

    def update_dictionary(self, paths, scouts):
        for i in self.tile_pop_dict:
            if i in paths:
                self.tile_pop_dict[i] += 1
            elif i in scouts:
                self.tile_pop_dict[i] += 1

    def main_dictionary(self):
        main_dict = dict()
        for i in self.world_coordinates():
            main_dict[i] = 0
        return main_dict

#####################################

    def land_world(self, w_level):
        water_list = []
        print("Creating a world with lakes and or rivers")
        our_coordinates = self.world_coordinates()
        return water_list