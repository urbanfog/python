#####Turtle Intro######

import turtle
import random

turd = turtle.Turtle()
screen = turtle.Screen()


def polygon(sides):
    r = random.randint(0, 256)
    b = random.randint(0, 256)
    g = random.randint(0, 256)
    turd.color((r, b, g))
    turn = 360 / sides
    for _ in range(sides):
        turd.forward(100)
        turd.right(turn)


# Set starting position
turd.penup()
turd.setx(-50)
turd.sety(100)
turd.shape("turtle")
turd.color("red")
screen.colormode(255)
turd.pendown()

# Draw shapes from triangle to nonagon
for _ in range(3, 10):
    polygon(_)

screen.exitonclick()
