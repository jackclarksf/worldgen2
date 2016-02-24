__author__ = 'iamja_000'

__author__ = 'iamja_000'

from itertools import product, starmap
import random

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