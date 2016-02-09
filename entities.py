__author__ = 'iamja_000'

class City:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.growth = 0
        print("CITY BORN AT X: {} Y: {} \n Origin X: {} Y: {}".format(self.x, self.y, self.x0, self.y0))