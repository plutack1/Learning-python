import random
import turtle as t
color_list = [(187, 18, 44), (243, 231, 66), (196, 75, 32), (218, 66, 107),
              (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88),
              (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2),
              (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50),
              (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39),
              (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27),
              (234, 171, 164), (162, 212, 176)]
tammy = t.Turtle()
tammy.hideturtle()
my_screen = t.Screen()
tammy.pensize(1)
t.colormode(255)
tammy.shape("turtle")
tammy.speed("fastest")
tammy.penup()
tammy.goto(-250, -200)
tammy.pendown()
distance = 0


def paint_fill():
    """function to draw circle and paint fill with random color"""
    current_color = random.choice(color_list)
    tammy.pen(fillcolor=current_color, pencolor=current_color)
    tammy.begin_fill()
    tammy.circle(10)
    tammy.end_fill()


def horizontal_move():
    """function to space the drawn circles by length 50"""
    tammy.penup()
    tammy.forward(50)
    tammy.pendown()


def vertical_adj(adjustment):
    """function to move to an higher height """
    tammy.penup()
    tammy.setheading(90)
    tammy.forward(adjustment)
    tammy.setheading(0)
    tammy.pendown()


def pen_reset():
    """function to return to origin """
    tammy.penup()
    tammy.goto(-250, -200)
    tammy.pendown()


def painting(adjustment):
    """function to execute 10 * 10 Hirst painting """
    for i1 in range(10):
        for i2 in range(10):
            paint_fill()
            horizontal_move()
        pen_reset()
        adjustment += 50
        vertical_adj(adjustment)



painting(distance)
my_screen.exitonclick()
