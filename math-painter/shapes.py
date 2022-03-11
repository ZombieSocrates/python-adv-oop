from typing import List 


class Rectangle:
    '''A rectangle with a single color that is oriented on its upper left 
    corner and can be drawn on a Canvas object. Just to be super clear about 
    this:

        x: the COLUMN that contains the rectangle's upper-left corner.
        y: the ROW that contains the rectangle's upper-left corner.
        height: how many rows the rectangle spans, top to bottom.
        width: how many columns the reectangle spans, left to right.
        color: a 3-item list representing the RGB fill of the rectangle.
    '''

    def __init__(self, x:int, y:int, height:int, width:int, color:List[int]):
        self.x = self._validate_coordinate(coord = x)
        self.y = self._validate_coordinate(coord = y) 
        self.h = self._validate_dimension(dimension = height) 
        self.w = self._validate_dimension(dimension = width)
        self.color = self._validate_color(color = color)


    def __str__(self):
        shape = self.__class__.__name__
        location = f"located at ({self.x}, {self.y})"
        size = f"{self.h}px tall and {self.w}px wide"
        return f"{shape} that is {location} and is {size}."


    def __repr__(self):
        shape_args = f"x={self.x}, y={self.y}, height={self.h}, width={self.w}"
        return f"Rectangle({shape_args}, color={self.color})"


    def draw(self, canvas:"Canvas"):
        w_end = self.x + self.w
        h_end = self.y + self.h
        canvas.arr[self.y:h_end, self.x:w_end] = self.color


    def _validate_coordinate(self, coord:int):
        '''Any coordinate supplied needs to be a non-negative integer.Returns 
        the coordinate if all checks are passed, throws a ValueError otherwise.
        '''
        if isinstance(coord, int) and coord >= 0:
            return coord 
        raise ValueError("Coordinates must be non-negative integers...")


    def _validate_dimension(self, dimension:int):
        '''Any dimension supplied needs to be a positive integer. Returns th 
        dimension if all checks are passed, throws a ValueError otherwise.
        '''
        if isinstance(dimension, int) and dimension >= 1:
            return dimension
        raise ValueError("Dimensions must be positive integers...")

    
    def _validate_color(self, color:list):
        '''Ensures that users supply color as a list of three integers, each 
        between 0 and 255. Returns the list if all checks are passed.
        '''
        if isinstance(color, list) and len(color) == 3:
            for rgb in color:
                if isinstance(rgb, int) and rgb >= 0 and rgb <= 255:
                    continue
                raise ValueError("Color must be integers between 0 and 255")
            return color
        raise AttributeError("Color must be passed as a 3-item list")
        

class Square(Rectangle):
    '''A square with a single color that is oriented on its upper left corner 
    and can be drawn on a Canvas object. Uses the same coordinate system 
    described in the Rectangle class.
    '''

    def __init__(self, x:int, y:int, side:int, color:List[int]):
        super().__init__(x = x, y = y, height = side, width = side, 
            color = color)


    def __repr__(self):
        shape_args = f"x={self.x}, y={self.y}, side={self.h}"
        return f"Square({shape_args}, color={self.color})"




if __name__ == "__main__":

    foo = Rectangle(x = 5, y = 7, height = 10, width = 3, color = [10, 150, 67])
    bar = Square(x = 50, y = 50, side = 12, color = [4 ,7, 8])

    print("Frankie say relax")
