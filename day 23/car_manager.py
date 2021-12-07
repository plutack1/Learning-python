import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
VALUE_Y = list(range(-250, 251, 20))

class CarManager:
    def __init__(self):
        self.cars = []
        self.movement = STARTING_MOVE_DISTANCE


    def create(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(x=320, y=random.choice(VALUE_Y))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.movement)

    def speed_up(self):
        self.movement += MOVE_INCREMENT
