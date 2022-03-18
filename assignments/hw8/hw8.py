"""
Name: Arnold
HW8.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] **= 2


def sum_list(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])



def sum_of_squares(nums):
    pass


def starter(weight, wins):
    if (weight >= 150 and weight < 160) and (wins >= 5):
        return True
    if (weight > 199) or (wins > 20):
        return True
    return False


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light blue")
    circle_two.draw(win)

    if_message = Text(Point(5, 2), "The circle overlaps")
    else_message = Text(Point(5, 2), "The circle does not overlap")
    close_message = Text(Point(5,1), "Click again to close")

    comparing_distance = math.sqrt((center.getX() - center2.getX()) ** 2 + (center.getY() - center2.getY() ** 2))
    sum_of_two_radius = radius + radius2

    if comparing_distance < sum_of_two_radius:
        if_message.draw(win)
    else:
        else_message.draw(win)

    close_message.draw(win)
    win.getMouse()


def did_overlap(circle_one, circle_two):
    comparing_distance = math.sqrt((circle_one.getX() - circle_two.getX()) ** 2 + (circle_one.getY() - circle_two.getY() ** 2))
    sum_of_two_radius = circle_one.getRadius() + circle_two.getRadius()
    if comparing_distance < sum_of_two_radius:
        return True
    else:
        return False

if __name__ == '__main__':
    pass
