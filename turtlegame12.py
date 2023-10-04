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

# Module8: A Helping Hand
speed = 1
timeout= time.time() + 10*6

def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def inscreasespeed():
    global speed
    speed += 1
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(inscreasespeed, "Up")

# Module9: Pushing the limits
while True:
    gametime = 0
    if gametime ==6 or time.time() > timeout:
        break
    gametime= gametime - 1
    
    player.forward(speed)
    comp.forward(12)

 # Module10: Bounce Bounce Bounce
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        os.system('afplay bounce.mp3&')
    
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        os.system('afplay bounce.mp3&')
    
    if comp.xcor() > 290 or comp.xcor() <-290:
        comp.right(180)
        os.system('afplay bounce.mp3&')
   
    if comp.ycor() > 290 or comp.ycor() <-290:
        comp.right(180)
        os.system('afplay bounce.mp3&')

    # Module11: Food Flight
    for count in range(maxFoods):
        foods[count].forward(3)
            
        if foods[count].xcor()> 290 or foods[count].xcor() < -290:
            foods[count].right(180)
            os.system('afplay bounce. mp3&')

        if foods[count].ycor() > 290 or foods[count].ycor() <-290:
            foods[count].right(180)
            os.system('afplay bounce.mp3&')

        # Module12: Crash, Bang Omph for Chomp
        if isCollision(player, foods[count]):
            foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            foods[count].right(random.randint(0,360))
            os.system('afplay chomp.mp3&')
            score+=1
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 305)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))  

        # Module13: Crash, Bang, Omph for Crunch
        if isCollision(comp, foods[count]):
            foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            foods[count].right(random.randint(0,360))
            os.system('afplay chomp.mp3&')
            comp_score+=1
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % comp_score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
            
