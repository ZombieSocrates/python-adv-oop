from canvas import Canvas 
from shapes import Rectangle, Square


if __name__ == "__main__":

	the_canvas = Canvas(height = 300, width = 300, color = "black")
	yellow = [255, 255, 0]
	a_rectangle = Rectangle(x = 30, y = 30, height = 50, width = 20,
		color = yellow)
	a_rectangle.draw(canvas = the_canvas)

	cyan = [0, 255, 255]
	a_square = Square(x = 75, y = 275, side = 25, color = cyan)

	a_square.draw(canvas = the_canvas)

	the_canvas.save("masterpiece.png")