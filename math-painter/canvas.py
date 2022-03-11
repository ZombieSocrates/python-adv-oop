import numpy as np 

from PIL import Image 


class Canvas:
    '''A solid color image that serves as the background that users can 
    draw other shapes on in this project.
    '''

    def __init__(self, height:int, width:int, color:str = "white"):
        self.h = height
        self.w = width
        self.default_filename = "canvas.png" 
        self.arr = np.zeros(shape = (self.h, self.w, 3), dtype=np.uint8)
        self.color = color
        self.clear()


    def set_color(self, new_color):
        if new_color not in ["black", "white"]:
            raise ValueError("Canvas must be 'black' or 'white'.")
        self.color  = new_color
        self.clear()


    def clear(self):
        '''Initializes the canvas with a single background color
        '''
        pixel = [0, 0, 0] if self.color == "black" else [255, 255, 255]
        self.arr[:] = pixel


    def save(self, filename:str = None):
        '''Saves whatever is on the canvas to the current directory as a png. 
        If no filename is provided, we use a default canvas.png name
        '''
        outname = filename if filename is not None else self.default_filename
        if not outname.endswith(".png"):
            outname = f"{outname}.png"
        outdata = Image.fromarray(obj = self.arr, mode = "RGB")
        outdata.save(outname)



if __name__ == "__main__":

    canvas_one = Canvas(height = 300, width = 200)
    canvas_one.set_color(new_color = "black")
    canvas_one.save("black_canvas_test")

    canvas_two = Canvas(height = 400, width = 100)
    canvas_two.save()



