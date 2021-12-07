from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        pass

    def create(self):
        """Function to create a player for the game"""
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Function to move player forward by 10 steps"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
