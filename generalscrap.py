__author__ = 'iamja_000'

__author__ = 'iamja_000'


s = int(input("Enter a number "))
r_list = []
for i in range(-s, s+1):
    print(i)
    r_list.append(i)

print(r_list)


from itertools import product, starmap
import random

roota = 4
rootb = 3
a = roota, rootb
coord = []
coord.append(a)
print(coord)
coord.append(product(roota-1, rootb-1))
print(coord)


def road_constructor(city_coord_a, city_coord_b, origin_coord_a, origin_coord_b):
    road_path = []
    print("Attempting to draw road between {} {} and origin {} {}".format(city_coord_a, city_coord_b, origin_coord_a, origin_coord_b))
    dummy_city_a = city_coord_a
    dummy_city_b = city_coord_b
    dummy_origin_a = origin_coord_a
    dummy_origin_b = origin_coord_b
    a_diff = dummy_city_a - dummy_origin_a
    b_diff = dummy_city_b - dummy_origin_b
    print("Our diffs are X {} and Y {}".format(a_diff, b_diff))

class World:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.terrain_a = []
        self.terrain_b = []
        self.terrain_list = [self.terrain_a, self.terrain_b]
        self.terrain_scatter()
        nu_list = self.terrain_eval()
        temp_list = self.return_dominant()
        nu_list = temp_list

        #self.terrain_clump()
        print("End test clump")





        print("World born with size: {} comprising of {} squares".format(self.x, self.x*self.x))

    def world_coordinates(self):
        w_coord = list(product(range(self.x), range(self.y)))
        return w_coord

    def get_neighbours(self, x_coord, y_coord):
        cells = starmap(lambda a,b: (x_coord+a, y_coord+b), product((0,-1,+1), (0,-1,+1)))
        return list(cells)[1:]

    def terrain_scatter(self):
        base_coords = self.world_coordinates()
        for i in base_coords:
            choice = random.randint(0, 10)
            if choice < 8:
                self.terrain_list[0].append(i)
            else:
                self.terrain_list[1].append(i)
            #self.terrain_list[choice].append(i)

    def get_neighbours_of_same_class(self, neighbour_list, class_list):
        i_count = 0
        for i in neighbour_list:
            if i in class_list:
                i_count +=1
        #print("Total neighbours: {}".format(i_count))
        return i_count

    def terrain_eval(self):
        max_list = list(self.return_dominant())
        min_list = list(self.return_submissive())
        print(max_list)
        for i, j in enumerate(max_list):
            i_count = 0
            a, b = j
            j_neighbours = self.get_neighbours(a, b)
            if self.get_neighbours_of_same_class(j_neighbours, max_list) < 1:
                print("Taking further action on value {} {}".format(a, b))
                c, d = random.choice(min_list)
                nu_value = c, d
                print("Our candidate coord now: {} {}".format(c, d))
                print("Max list i is {} w/overall {}".format(max_list[i], max_list))
                max_list[i] = nu_value
                print("Max list is now {} w/overall {}".format(max_list[i], max_list))
                dog = max(self.terrain_list, key=len)
                for i in self.terrain_list:
                    print(i)
                    print(len(i))
        return max_list


    def terrain_clump(self):
        max_list = list(self.return_dominant())
        abs_gap = []
        gap_count = 0
        for i, j in enumerate(max_list):
            if i == len(max_list)-1:
                continue
            else:
                a, b = j
                c, d = max_list[i+1]
                holder_list = []
                if a == c:
                    temp = abs(b-d)
                    if temp == 1:
                        gap_count += 1
                    abs_gap.append(temp)

                    print("AB {} {} and CD {} {} is and gap is {} and gap count is {}".format(a, b, c, d, temp, gap_count))

                #abs_gap.append(abs(b-d))
                #i += 1
        print(abs_gap)
        #INSTEAD SHOULT WORK THIS OUT FOR EACH LINE THEN CONCATE LISTS



    def return_dominant(self):
        return max(self.terrain_list, key=len)

    def return_submissive(self):
        return min(self.terrain_list, key=len)







class Forest(World):
    def __init__(self, x, y):
        World.__init__(self, x, y)
        print("Desert world born! size {} comprising of {} squares".format(self.x, self.x*self.x))




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

 def road_constructor_2(self, loc_a, loc_b, r_origin_a, r_origin_b, c_origin_a, c_origin_b):

        def abs_diff_checker(input_a, input_b, r_a, r_b):
            road_path = []
            distance_tuple = [input_a, input_b]
            target_distance = [0, 0]
            actual_distance = [r_a, r_b]
            while distance_tuple > target_distance:
                calc_options = [-1, 1]
                tuple_option = [0, 1]
                our_option = random.choice(tuple_option)
                distance_tuple[our_option] += random.choice(calc_options)
                new_distance = [0, 0]
                new_distance[0] = abs(distance_tuple[0] - actual_distance[0])
                new_distance[1] = abs(distance_tuple[1] - actual_distance[1])
                print("Our tuples are now new distance {} and distance tuple {}".format(new_distance, distance_tuple))
                if tuple(new_distance) < tuple(distance_tuple):
                    road_path.append(new_distance)
                    distance_tuple = new_distance
            return road_path

        abs_a_diff = abs(loc_a - r_origin_a)
        abs_b_diff = abs(loc_b - r_origin_b)

        candidate_path = abs_diff_checker(abs_a_diff, abs_b_diff, r_origin_a, r_origin_b)
        print("Our candidate path is: {}".format(candidate_path))
        seeker_coordinate = r_origin_a, r_origin_b
        city_coordinate = loc_a, loc_b
        city_origin_coordinate = c_origin_a, c_origin_b
        if seeker_coordinate in candidate_path:
            candidate_path.remove(seeker_coordinate)
            self.roads.append(Road(city_coordinate, seeker_coordinate, candidate_path, city_origin_coordinate))


            def location_manipulator(self, input_list, list_options, input_calculations):
        manipulation_entity = input_list
        choice = random.choice(list_options)
        manipulation_entity[choice] += random.choice(input_calculations)
        return manipulation_entity

    def road_constructor_3(self, loc_a, loc_b, r_origin_a, r_origin_b, c_origin_a, c_origin_b):
        road_path = []
        print("OK, here is our position {} {} and our origin {} {} and our city origin {} {}".format(loc_a, loc_b, r_origin_a, r_origin_b, c_origin_a, c_origin_b))
        #WHAT WE NEED IS TO BUILD A ROUTE BETWEEN OUR LOCATION (LOC) AND SCOUT ORIGIN (R_ORIG)
        our_current_distance_a = abs(loc_a - r_origin_a)
        our_current_distance_b = abs(loc_b - r_origin_b)
        combined_distance = [abs(loc_a - r_origin_a), abs(loc_b - r_origin_b)]
        combined_location = [loc_a, loc_b]
        combined_origin = [r_origin_a, r_origin_b]
        print("Our distance: {}".format(combined_distance))
        while combined_distance != [0, 0]:
            choice = input("Do you want to tick, [y]?")
            safe_location = combined_location
            if choice == "y":
                prev_distance = [our_current_distance_a, our_current_distance_b]
                preserved_location = combined_location
                new_location = list(preserved_location)
                print("Attempting to close distance of {} by manipulating location {}".format(prev_distance, new_location))
                calc_options = [-1, 1]
                list_option = [0, 1]
                the_new_location = self.location_manipulator(new_location, list_option, calc_options)
                print("Our new location is {}".format(the_new_location))
                print("Our original location is {}".format(safe_location))
                print("Our preserved location is: {}".format(preserved_location))
                #new_location[our_choice] += random.choice(calc_options)
                our_current_distance_a = abs(new_location[0] - r_origin_a)
                our_current_distance_b = abs(new_location[1] - r_origin_b)
                combined_distance = [our_current_distance_a, our_current_distance_b]
                print("Our distance now: {}".format(combined_distance))
                if combined_distance[0] < prev_distance[0]:
                    road_path.append(combined_distance)
                    print("Feeding the new location")
                    combined_location = new_location
                elif combined_distance[1] < prev_distance[1]:
                    road_path.append(combined_distance)
                    print("Feeding the new location")
                    combined_location = new_location
                else:
                    print("{} doesn't work so reverting to {}".format(new_location, preserved_location))
                    combined_location = combined_location
        print("Now our path is {}".format(road_path))

        seeker_coordinate = r_origin_a, r_origin_b
        city_coordinate = loc_a, loc_b
        city_origin_coordinate = c_origin_a, c_origin_b
        if seeker_coordinate in road_path:
            road_path.remove(seeker_coordinate)
            self.roads.append(Road(city_coordinate, seeker_coordinate, road_path, city_origin_coordinate))
        #OUR DATAFLOW MODEL IS FUCKED UP, SON
