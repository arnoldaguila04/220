"""
Name: Arnold Aguila
hw4.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *

def square():

    # Window Start
    win = GraphWin("Square", 500, 500)
    win.setBackground("Grey")
    windowText = Text(Point(250,480), "Click to draw a square.")
    windowText.setSize(18)
    windowText.draw(win)

    # Purpose
    for i in range(7):
        center = win.getMouse()
        pt1 = Point(center.getX() - 25, center.getY() - 25)
        pt2 = Point(center.getX() + 25, center.getY() + 25)
        rec = Rectangle(pt1, pt2)
        rec.setFill("red")
        rec.draw(win)

    # Window Closing
    completeText = Text(Point(250,250), "Click again to close.")
    completeText.setSize(18)
    completeText.draw(win)
    win.getMouse()
    win.close()
square()

def rectangle():
    # Window/ Opening
    win = GraphWin("Rectangle", 600, 600)

    # Purpose
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    rect = Rectangle(pt1,pt2)
    rect.setFill("green")
    rect.draw(win)

    # Purpose Equation
    width = pt2.getX() - pt1.getX()
    length = pt2.getY() - pt1.getY()
    area = length * width
    perimeter = 2 * (length + width)

    # Purpose Answer
    perimeterText= Text(Point(300,500), "Perimeter: " + str(perimeter))
    areaText= Text(Point(300, 550), "Area: " + str(area))
    perimeterText.draw(win)
    areaText.draw(win)

    # Window/Closing
    windowText = Text(Point(300, 300), "Click again to close")
    windowText.draw(win)
    win.getMouse()
    win.close()
    print(width, length)
rectangle()

def circle():
    # Window Open
    win = GraphWin("Circle", 600, 600)

    # Purpose
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    ed = math.sqrt((pt2.getX() - pt1.getX())**2 + (pt2.getY() - pt1.getY())**2)
    circ = Circle(pt1, ed)
    circ.setFill("Light Blue")
    circ.draw(win)

    # Window Close
    ansText = Text(Point(300, 550), "Radius: " + str(ed))
    closeText = Text(Point(300,300), "Click again to close.")
    ansText.draw(win)
    closeText.draw(win)
    win.getMouse()
    win.close()
circle()

def pi2():
    n = eval(input("Enter number of sequence: "))
    num = 4
    denom = 1
    total = 0
    for i in range(n):
        total = total + num/denom
        denom = denom + 2
        num = num * -1
    accuracy = math.pi - total
    print("Pi approximation: ", total)
    print("Accuracy: ", accuracy)
pi2()
