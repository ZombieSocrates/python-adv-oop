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



class Rectangle:

    def __init__(self, lower_left:"Point", upper_right:"Point"):
        self.LL = lower_left
        self.UR = upper_right
        self.LR = Point(x = self.UR.x, y = self.LL.y)
        self.UL = Point(x = self.LL.x, y = self.UR.y)


    def __str__(self):
        coord_strs = []
        for point in [self.LL, self.LR, self.UR, self.UL]:
            coord_strs.append(point.__str__().split(" ")[-1])
        return f"Rectangle with Coordinates {','.join(coord_strs)}"


    def __repr__(self):
        return f"Rectangle(lower_left={self.LL}, upper_right={self.UR}"

    def area(self):
        '''TODO: validate that this won't be negative
        '''
        width = self.UR.x - self.LL.x
        height = self.UR.y - self.LL.y 
        return width * height


    def contains(self, new_point: "Point"):
        within_x = (self.LL.x <= new_point.x <= self.UR.x)
        within_y = (self.LL.y <= new_point.y <= self.UR.y)
        return within_y and within_y



if __name__ == "__main__":

    p1 = Point(3, 5)
    print(p1)
    p2 = Point(6, 9)
    dist = p1.distance_from(new_point = p2)
    print(f"Distance between two points: {dist}")

    rect = Rectangle(lower_left = p1, upper_right = p2)
    print(rect)
    p3 = Point(4, 8)
    print(f"Is {p3} within this rectangle??")
    print(rect.contains(p3))

    p4 = Point(0, 0)
    print(f"Is {p4} within this rectangle??")
    print(rect.contains(p4))

