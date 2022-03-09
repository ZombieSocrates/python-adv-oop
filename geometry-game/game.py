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

    new_x = float(input("Please choose an x coordinate for your point: "))
    new_y = float(input("Now please choose a y coordinate for your point: "))

    new_point = Point(x = new_x, y = new_y)

    if rectangle.contains(new_point):
        print("Congratulations! You Win!")
        print("\nNow, try guessing the area of the rectangle")
        guess = float(input("I think the area is... "))
        if guess == rectangle.area():
            print("Shoop-da-Woop! You Win!")
        else:
            print(f"I'm sorry, the area is actually {rectangle.area()}")

    else:
        print("Woof...Please Try Again...")

