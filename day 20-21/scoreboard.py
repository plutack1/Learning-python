from turtle import Turtle
FONT_VALUE = ("Arial", 14, "bold")
ALLIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("green")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} Highscore:{self.highscore}",
                   align=ALLIGNMENT, font=FONT_VALUE)

    # def gameover(self):
    #     self.clear()
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f"Game Over\nscore:{self.score}", align=ALLIGNMENT,
    #                font=FONT_VALUE)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()