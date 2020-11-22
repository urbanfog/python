import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ROAD_COORDS = []


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        y_coord = random.choice(ROAD_COORDS)
        dice = random.randint(1, 6)
        if dice == 1:
            car = Car(y_coord)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def create_roads(self):
        for _ in range(-230, 230, 50):
            road = Road(_)
            ROAD_COORDS.append(road.ycor())


class Car(turtle.Turtle):
    def __init__(self, y_coord):
        super().__init__(shape="square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(310, y_coord)


class Road(turtle.Turtle):
    def __init__(self, y_coord):
        super().__init__(shape="square")
        self.penup()
        self.color("grey")
        self.shapesize(stretch_len=40)
        self.goto(0, y_coord)
