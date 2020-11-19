import turtle
import random

rgb_colors = [
    (217, 168, 77), (79, 110, 154), (115, 161, 210),
    (105, 174, 136), (192, 122, 161), (70, 127, 97),
    (129, 23, 63), (154, 49, 85), (197, 78, 115),
    (160, 162, 54), (219, 203, 124), (129, 116, 166),
    (189, 66, 41), (36, 37, 78), (204, 102, 55),
    (37, 48, 95), (84, 155, 119), (58, 16, 34),
    (226, 173, 199), (21, 43, 31), (50, 17, 12),
    (158, 190, 232), (78, 140, 172), (119, 38, 29),
    (41, 77, 57), (80, 88, 21)]

turd = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(100, 100)
turtle.colormode(255)
turd.speed(0)
turd.width(20)
turd.penup()
turd.setx(-400)
turd.sety(-250)
turd.hideturtle()


for _ in range(10):
    ypos = turd.position()[1]
    turd.setposition(-200, ypos + 50)
    for _ in range(10):
        turd.dot(20, random.choice(rgb_colors))
        turd.forward(50)


screen.exitonclick()
