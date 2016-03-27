__author__ = 'iamja_000'

class Vegetation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitality = 1

    def increase_vitality(self):
        self.vitality += 1

    def decrease_vitality(self):
        self.vitality -= 1

    def return_location(self):
        return self.x, self.y



class City:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.growth = 0
        self.age = 0
        print("CITY BORN AT X: {} Y: {} \n Origin X: {} Y: {}".format(self.x, self.y, self.x0, self.y0))

    def add_growth(self):
        self.growth += 1
        print("ADDED GROWTH to city at {} {} with origin {} {}. Growth now {}".format(self.x, self.y, self.x0, self.y0, self.growth))

    def get_location(self):
        return self.x, self.y

    def return_city_origin(self):
        return self.x0, self.y0

    def add_age(self):
        self.age += 1

class Scout:
    def __init__(self, x, y, origina, originb):
        self.paths_taken = []
        self.x = x
        self.y = y
        self.x0 = origina
        self.y0 = originb
        self.period_without_hit = 0
        self.lonely = 0
        print("SCOUT BORN AT X: {} Y: {} \n Origin X: {} Y: {}".format(self.x, self.y, self.x0, self.y0))

    def get_location(self):
        return self.x, self.y

    def return_paths(self):
        return self.paths_taken

    def hit_rate(self):
        return self.period_without_hit

    def add_hit_rate(self):
        self.period_without_hit += 1

    def how_lonely(self):
        return self.lonely

    def more_lonely(self):
        self.lonely += 1

    def return_origin(self):
        return self.x0, self.y0

class Road:
    def __init__(self, origination_point, termination_point, road_list):
        self.road_route = road_list
        self.start_coord_a, self.start_coord_b = origination_point
        self.end_coord_a, self.end_coord_b = termination_point
        print("Road born with origination: {} and termination {} and path of {}".format(origination_point, termination_point, road_list))

    def get_route(self):
        return self.road_route

    def return_start(self):
        return self.start_coord_a, self.start_coord_b

    def return_end(self):
        return self.end_coord_a, self.end_coord_b

