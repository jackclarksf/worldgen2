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
        print(list(self.return_dominant()))
        self.terrain_clump()
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
            choice = random.randint(0, 1)
            self.terrain_list[choice].append(i)

    def terrain_clump(self):
        max_list = list(self.return_dominant())
        abs_gap = []
        for i, j in enumerate(max_list):
            if i == len(max_list)-1:
                continue
            else:
                a, b = j
                c, d = max_list[i+1]
                holder_list = []
                if a == c:
                    temp = abs(b-d)
                    abs_gap.append(temp)
                    print("AB {} {} and CD {} {} is and gap is {}".format(a, b, c, d, temp))

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