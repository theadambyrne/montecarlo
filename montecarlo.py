import turtle
import time
import random

turtle.hideturtle()
turtle.speed('fastest')

def move(heading, stepSize):
    turtle.setheading(heading)
    turtle.forward(stepSize)

def randomWalk(stepSize, steps):
    directions = (east, north, west, south) = (0, 90, 180, 270)
    for i in range(steps):
        move(random.choice(directions), stepSize)

for i in range(10):
    randomWalk(15, 100)
