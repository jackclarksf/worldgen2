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
        print("Test clump")
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
        min_list = list(self.return_submissive())
        for i, j in enumerate(min_list):
            print(i)
            print(j)



    def return_dominant(self):
        return max(self.terrain_list, key=len)

    def return_submissive(self):
        return min(self.terrain_list, key=len)







class Forest(World):
    def __init__(self, x, y):
        World.__init__(self, x, y)
        print("Desert world born! size {} comprising of {} squares".format(self.x, self.x*self.x))