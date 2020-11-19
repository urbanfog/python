import turtle
import random

turd = turtle.Turtle()
screen = turtle.Screen()
turd.pensize(10)
turtle.colormode(255)
turd.speed(0)
direction = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)


def random_turn(distance):
    turd.setheading(random.choice(direction))


def random_walk(steps, distance):
    for _ in range(steps):
        random_turn(distance)
        turd.color(random_colour())
        turd.forward(distance)


random_walk(300, 20)

screen.exitonclick()
