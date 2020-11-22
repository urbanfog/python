from turtle import Screen, resetscreen, textinput
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOUNDARY = 280

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()

snake = Snake()
food = Food()

game_is_on = True


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time.sleep(3)
print(game_is_on)
snake_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.rand_location()
        snake.extend()
        scoreboard.increase_score()
        snake_speed *= 0.98

    # Detect collision with wall
    if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.length[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
