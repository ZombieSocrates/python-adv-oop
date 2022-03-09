import math
import turtle


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


class VisualPoint(Point):

    def __init__(self, x:float, y:float, size:int, hex_code:str = "#002676"):
        super().__init__(x, y)
        self.size = size
        self.color = hex_code


    def draw(self, canvas:turtle.Turtle):

        canvas.penup()
        canvas.goto(x = self.x, y = self.y)
        canvas.pendown()

        canvas.color(self.color)
        canvas.dot(size = self.size)
    



class Rectangle:

    def __init__(self, lower_left:"Point", upper_right:"Point"):
        self.LL = lower_left
        self.UR = upper_right
        self.LR = Point(x = self.UR.x, y = self.LL.y)
        self.UL = Point(x = self.LL.x, y = self.UR.y)
        self.width = self.UR.x - self.LL.x
        self.height = self.UR.y - self.LL.y 


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
        return self.width * self.height


    def contains(self, new_point: "Point"):
        within_x = (self.LL.x <= new_point.x <= self.UR.x)
        within_y = (self.LL.y <= new_point.y <= self.UR.y)
        return within_y and within_y


class VisualRectangle(Rectangle):

    '''VisualRectangle is a Rectangle that can draw itself on a Turtle canvas.
    In other words, it extends the rectangle class with methods that allow it 
    to draw itself on an externally provided canvas. 
    '''

    def __init__(self, lower_left:"Point", upper_right: "Point"):
        '''If you aren't changing anything, it isn't actually necessary to 
        provide this. Just wanted to practice 
        '''
        super().__init__(lower_left, upper_right)
        

    def draw(self, canvas:turtle.Turtle):
        
        canvas.penup()
        canvas.goto(x = self.LL.x, y = self.LL.y)
        canvas.pendown()

        for i in range(2):
            canvas.forward(self.width)
            canvas.left(90)
            canvas.forward(self.height)
            canvas.left(90)

        








if __name__ == "__main__":

    pass

