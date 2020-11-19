import turtle
import random

turd = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
turd.speed(0)


def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)


def spirograph(offset):
    for _ in range(int(360 / offset)):
        turd.circle(100)
        turd.color(random_colour())
        turd.setheading(turd.heading() + offset)


spirograph(1)

screen.exitonclick()
