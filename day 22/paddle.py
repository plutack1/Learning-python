from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create(x, y)

    def create(self, x, y):
        self.shape("square")
        self.speed(6)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
