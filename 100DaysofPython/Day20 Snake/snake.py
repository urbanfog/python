import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.length = []
        self.create_snake()
        self.head = self.length[0]

    def reset(self):
        for seg in self.length:
            seg.goto(1000, 1000)
        self.length.clear()
        self.create_snake()
        self.head = self.length[0]

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.add_segment(_)

    def add_segment(self, position):
        snek = turtle.Turtle(shape="square")
        snek.color("white")
        snek.penup()
        snek.goto(position)
        self.length.append(snek)

    def extend(self):
        self.add_segment(self.length[-1].position())

    def move(self):
        for seg_num in range(len(self.length) - 1, 0, -1):
            new_x = self.length[seg_num - 1].xcor()
            new_y = self.length[seg_num - 1].ycor()
            self.length[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
