__author__ = 'iamja_000'

from itertools import product
import random

class World:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.terrain_a = []
        self.terrain_b = []
        self.terrain_list = [self.terrain_a, self.terrain_b]
        self.terrain_scatter()
        print(self.terrain_list)



        print("World born with size: {} comprising of {} squares".format(self.x, self.x*self.x))

    def world_coordinates(self):
        w_coord = list(product(range(self.x), range(self.y)))
        return w_coord

    def terrain_scatter(self):
        base_coords = self.world_coordinates()
        for i in base_coords:
            choice = random.randint(0, 1)
            self.terrain_list[choice].append(i)






class Forest(World):
    def __init__(self, x, y):
        World.__init__(self, x, y)
        print("Desert world born! size {} comprising of {} squares".format(self.x, self.x*self.x))