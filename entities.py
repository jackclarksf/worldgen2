__author__ = 'iamja_000'

class City:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.growth = 0
        #print("CITY BORN AT X: {} Y: {} \n Origin X: {} Y: {}".format(self.x, self.y, self.x0, self.y0))

    def get_location(self):
        return self.x, self.y

class Scout:
    def __init__(self, x, y, origina, originb):
        self.paths_taken = []
        self.x = x
        self.y = y
        self.x0 = origina
        self.y0 = originb

    def get_location(self):
        return self.x, self.y

    def return_paths(self):
        return self.paths_taken