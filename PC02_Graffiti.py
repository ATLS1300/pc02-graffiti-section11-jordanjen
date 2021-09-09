#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.pensize(1)

turtle.goto(-15,95)
turtle.down()
turtle.circle(20)

turtle.up()
turtle.pensize(10)
turtle.goto(-125,185)
turtle.down()
turtle.forward(200)
turtle.up()
turtle.goto(-90,185)
turtle.left(90)
turtle.begin_fill()
turtle.down()
turtle.forward(100)
turtle.right(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(100)
turtle.up()
turtle.end_fill()

turtle.pensize(1)
turtle.color("blue")
turtle.goto(20,64)
turtle.right(90)
turtle.down()
turtle.forward(40)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(10)
turtle.up()

turtle.goto(30,64)
turtle.down()
turtle.forward(40)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(10)









#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
