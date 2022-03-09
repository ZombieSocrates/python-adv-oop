import turtle

from geometries import Point, Rectangle, VisualPoint, VisualRectangle
from random import randint

RANDINT_RANGE = 150
POINT_SIZE = 10
POINT_COLOR = "#E921CD"


if __name__ == "__main__":

    ll_x = randint(0, RANDINT_RANGE)
    ur_x = ll_x + randint(0, RANDINT_RANGE)
    ll_y = randint(0, RANDINT_RANGE)
    ur_y = ll_y + randint(0, RANDINT_RANGE)
    lower_left = Point(x = ll_x, y = ll_y)
    upper_right = Point(x = ur_x, y = ur_y)
    rectangle = VisualRectangle(lower_left = lower_left, 
        upper_right = upper_right)

    print(f"For this game, imagine a {rectangle}")
    print("Your mission is to guess a point inside this rectangle!")

    user_x = float(input("Please choose an x coordinate for your point: "))
    user_y = float(input("Now please choose a y coordinate for your point: "))
    user_point = VisualPoint(x = user_x, y = user_y, 
        size = POINT_SIZE, hex_code = POINT_COLOR)

    if rectangle.contains(user_point):
        print("Congratulations! You Win!")
        print("\nNow, try guessing the area of the rectangle")
        guess = float(input("I think the area is... "))
        if guess == rectangle.area():
            print("Shoop-da-Woop! You Win!")
        else:
            print(f"I'm sorry, the area is actually {rectangle.area()}")

    else:
        print("Woof...Please Try Again...")


    game_canvas = turtle.Turtle()
    rectangle.draw(canvas = game_canvas)
    user_point.draw(canvas = game_canvas)
    turtle.done()


