

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



if __name__ == "__main__":

    foo = Point(3, 5)
    print(foo)
    print(type(foo))