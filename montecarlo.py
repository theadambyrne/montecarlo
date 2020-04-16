import turtle
import time
import random

class Node:
    def __init__(self, steps):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed('fastest')
        self.turtle.pensize(10)
        self.steps = steps
        self.r = random.random()
        self.g = random.random()
        self.b = random.random()
        self.turtle.color(self.r,self.g,self.b)

    def move(self, heading):
        self.turtle.setheading(heading)
        self.turtle.forward(30)

    def randomWalk(self):
        directions = (east, north, west, south) = (0, 90, 180, 270)
        for i in range(self.steps):
            self.move(random.choice(directions))

for i in range(10):
    x = Node(100)
    x.randomWalk()

time.sleep(10)
