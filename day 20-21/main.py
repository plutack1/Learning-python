import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# def move_left():
#     """function to change direction to left"""
#     segments[0].left(90)
#
#
# def move_right():
#     """function to change direction to left"""
#     segments[0].right(90)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
game_on = True
# for position in starting_position:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()




#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num-1].xcor()
#         new_y = segments[seg_num-1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)

# block1 = Turtle(shape="square")
# block2 = Turtle(shape="square")
# block3 = Turtle(shape="square")
# blocks = [block1, block2, block3]
# for block in blocks:
#     block.color("white")
# block2.goto(x=-20, y=0)
# block3.goto(x=-40, y=0)


screen.exitonclick()
