"""
from graphics import *

### Open a graphics window
win = GraphWin("Shapes")

### Draw a red circle
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

### Put a textual label in the center of the circle
label = Text(center, 'Red Circle')
label.draw(win)

### Draw a square using a rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)

### Draw a line segment using a Line object
line = Line(Point(20,30), Point(180,165))
line.draw(win)

### Draw an oval using the Oval object
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)


input()


p = Point(50,50)
p.move(10,0)

p.getX()
p.getY()


#for d in [3,1,4,1,5]:
    #print(d, end=" ")

# In the command line
"My name is {1} and I am {0} years old". formant("eric", 7)
"My name is {0.:10} and I am P1{ years old".format("Erid", 7)
"I have ${}.{}".format(dollars, cents)

open(<filename>, <mode>)
"r"/"w" read and write

# example: data.txt

open("data.txt","r")

my.file = open("data.text","r")

my_text = my_file. read()"a;sldfja;lfjk"
                . readline() ----> "a;sldkfja;ldkfja;ld"
                . readline()  ----> [";alsdkjfa;lsdjf /n ", a;sldkfjas;ldfjk /n, ....]