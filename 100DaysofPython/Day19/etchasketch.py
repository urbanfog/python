import turtle

turd = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def forward():
    turd.forward(10)


def back():
    turd.back(10)


def right():
    turd.right(15)


def left():
    turd.left(15)


screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=back)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="a", fun=left)


screen.exitonclick()
