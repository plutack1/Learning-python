import turtle
from turtle import Turtle, Screen
import random
from faker import Factory
turtle.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("black")
my_turtle.speed("fastest")
my_turtle.pensize(2)
# color = Factory.create()
# for n in range(100):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
# for n in range(3, 11):
#     ang =  360/n
#     for times in range(n):
#         my_turtle.forward(100)
#         my_turtle.right(ang)
# direction = [90, 180, 270, 360]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = (r, g, b)
    return color_code
#
#
# def random_work(direction):
#     for no_of_times in range(200):
#         # my_turtle.color(color.hex_color())
#         my_turtle.color(random_color())
#         angle = random.choice(direction)
#         my_turtle.right(angle)
#         my_turtle.forward(30)

#  random_work(direction)
def spirograph():
    n_times = 60
    current_heading = 0.0


    for i in range(n_times):
        my_turtle.circle(100)
        my_turtle.setheading(current_heading)
        current_heading += 360 / n_times
        my_turtle.color(random_color())




spirograph()
my_screen = Screen()
my_screen.exitonclick()
