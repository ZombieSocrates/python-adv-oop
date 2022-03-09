import math

class Point:

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y


    def __str__(self):
        '''Controls what happens when you print a point'''
        return f"Point at Coordinates ({self.x},{self.y})"


    def __repr__(self):
        '''Returns how python would interpret this object'''
        return f"Point(x ={self.x}, y={self.y})"


    def distance_from(self, new_point: "Point"):
        dist_squared = (new_point.x - self.x)**2 + (new_point.y - self.y)**2
        return math.sqrt(dist_squared)





if __name__ == "__main__":

    foo = Point(3, 5)
    print(foo)
    bar = foo.distance_from(new_point = Point(6, 9))
    print(f"Distance between two points: {bar}")