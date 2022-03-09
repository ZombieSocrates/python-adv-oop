from geometries import Point, Rectangle
from random import randint


if __name__ == "__main__":

    ll_x = randint(0, 15)
    ll_y = randint(0, 15)
    lower_left = Point(x = ll_x, y = ll_y)
    upper_right = Point(x = ll_x + randint(0, 15), y = ll_y + randint(0,15))
    rectangle = Rectangle(lower_left = lower_left, upper_right = upper_right)

    print(f"For this game, imagine a {rectangle}")
    print("Your mission is to guess a point inside this rectangle!")


    while True:

        new_x = float(input("Please choose an x coordinate for your point: "))
        new_y = float(input("Now please choose a y coordinate for your point: "))

        new_point = Point(x = new_x, y = new_y)

        if rectangle.contains(new_point):
            print("Congratulations! You win!")
        else:
            print("Woof...Please try again...")

