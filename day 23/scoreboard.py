from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(250, -290)
        self.write(f"{self.score}", align="center",
                   font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"{self.score}", align="center",
                   font=FONT)
