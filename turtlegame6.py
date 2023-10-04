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

# Module4: Chomp the green space Turtle
player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)

# Module5: Crunch the pink space Turtle
comp = turtle.Turtle()
comp.color('hotpink')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Module6: Keeping Score
mypen2= turtle.Turtle()
mypen2.color("red")
mypen2.hideturtle()

score= 0
comp_score= 0

# Module7: The Great Biscuit Hunt
maxFoods = 6
foods = []
for count in range(maxFoods):
    foods.append (turtle.Turtle())
    foods[count].color("orange")
    foods[count].shape("circle")
    foods[count].shapesize(.5)
    foods[count].penup()
    foods[count].speed(0)
foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
