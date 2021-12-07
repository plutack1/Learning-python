import turtle
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


def forward():
    """function to move turtle by one pace"""
    my_turtle.forward(10)


def backward():
    """function to move turtle by one pace"""
    my_turtle.backward(10)


def clockwise():
    """function to rotate turtle in the clockwise direction"""
    my_turtle.left(10)


def anticlockwise():
    """function to rotate turtle in the clockwise direction"""
    my_turtle.right(10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()
my_screen.onkey(key='w', fun=forward)
my_screen.onkey(key='s', fun=backward)
my_screen.onkey(key='d', fun=clockwise)
my_screen.onkey(key='a', fun=anticlockwise)
my_screen.onkey(key='c', fun=clear)
my_screen.exitonclick()
