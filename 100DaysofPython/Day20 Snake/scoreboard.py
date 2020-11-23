from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../../desktop/data.txt") as file:
            self.high_score = int(file.read())
        print(self.high_score)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center",
                   font=("Courier", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("../../../desktop/data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.update_scoreboard()
