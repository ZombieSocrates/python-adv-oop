from canvas import Canvas 
from shapes import Rectangle, Square


if __name__ == "__main__":

    print("Time to draw some shapes, my dudes...")
    print("First let's set up the canvas to draw on")

    user_height = int(input("How tall, in pixels, should the canvas be??  >"))
    user_width = int(input("How wide, in pixels, should the canvas be??  >"))
    canvas_color = None
    while canvas_color is None:
        print("Would you like to draw on a white or black canvas?")
        print("\t1. Black")
        print("\t2. White")
        color_choice = int(input("Please choose with number keys:  >"))
        if color_choice == 1:
            canvas_color = "black"
        if color_choice == 2:
            canvas_color = "white"
    
    user_canvas = Canvas(height = user_height, width = user_width, 
        color = canvas_color)
    print(f"OK, we just set up a {user_canvas} Time to draw!\n")
    is_drawing = True
    while is_drawing:
        print("What type of shape would you like to draw??")
        print("\t1. A Rectangle")
        print("\t2. A Square")
        print("\t3. I'm done drawing")
        draw_choice = int(input("Please choose with number keys:  >"))
        coord_hint = "[type two non-negative integers separated by a comma and a space]"
        color_hint = "[type three integers 0 to 255 separated by a comma and a space]"
        if draw_choice == 1:
            rect_coord = input(f"Upper-left coordinate of the Rectangle? {coord_hint}: >")
            rect_x = int(rect_coord.split(", ")[0])
            rect_y = int(rect_coord.split(", ")[1])
            rect_height = int(input(f"How tall is the rectangle?  >"))
            rect_width = int(input(f"How wide is the rectangle?  >"))
            rect_rgb = input(f"What color is the Rectangle? {color_hint}: >")
            rect_color = [int(v) for v in rect_rgb.split(", ")]
            user_rect = Rectangle(x = rect_x, y = rect_y, height = rect_height, 
                width = rect_width, color = rect_color)
            print(f"Drawing {user_rect}\n")
            user_rect.draw(canvas = user_canvas)
        if draw_choice == 2:
            square_coord = input(f"Upper-left coordinate of the Square? {coord_hint}: >")
            square_x = int(square_coord.split(", ")[0])
            square_y = int(square_coord.split(", ")[1])
            square_side = int(input(f"How long is each sides?  >")) 
            square_rgb = input(f"What color is the Square? {color_hint}: >")
            square_color = [int(v) for v in square_rgb.split(", ")]
            user_square = Square(x = square_x, y = square_y, 
                side = square_side, color = square_color)
            print(f"Drawing {user_square}\n")
            user_square.draw(canvas = user_canvas)
        if draw_choice == 3:
            is_drawing = False

    print("Thanks for drawing! Please type a name to save your canvas to PNG.")
    canvas_file = input("Save my sketch in file named:  >")
    user_canvas.save(canvas_file)