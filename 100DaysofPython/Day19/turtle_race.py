import turtle
from turtle import color
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
colours = ["red", "pink", "blue", "purple", "black", "green"]
y_pos = [100, 60, 20, -20, -60, -100]
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win? Choose a colour: ")
is_race_on = False
all_racers = []


class Racer(turtle.Turtle):
    # def __init__(self, color, x, y):
    def __init__(self, color, x, y):
        super().__init__(shape="turtle")
        self.color(color)
        self.penup()
        self.goto(x=x, y=y)

    def race(self):
        self.forward(random.randint(0, 10))


for i in range(0, 6):
    racer = Racer(colours[i], -230, y_pos[i])
    all_racers.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_colour = racer.pencolor()
            if winning_colour == user_bet:
                print(
                    f"You won! The winning turtle colour was {winning_colour}.")
            else:
                print(
                    f"You lost! The winning turtle colour was {winning_colour}.")
        racer.race()

screen.exitonclick()
