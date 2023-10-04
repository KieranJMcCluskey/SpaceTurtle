# Module1: Importing the Python libraries
import turtle
import math
import random
import os
import time

# Module2: Creating the Game World
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("purple")
wn.bgpic('space-bg.gif')
wn.tracer(3)
            
# Module3: Applying a boarder to the Game World
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
