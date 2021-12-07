from turtle import Turtle
FONT_VALUE = ("Comic Sans MS", 50, "bold")
ALLIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALLIGNMENT,
                   font=FONT_VALUE)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALLIGNMENT,
                   font=FONT_VALUE)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
