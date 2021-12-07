from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
l_paddle = Paddle(x=-380, y=0)
r_paddle = Paddle(x=380, y=0)
ball = Ball()
game_on = True
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


while game_on is True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if not -290 < ball.ycor() < 290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 355 or ball.distance(
            l_paddle) < 50 and ball.xcor() < -355:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.l_point()
            print(scoreboard.l_score)
        if ball.xcor() < -400:
            scoreboard.r_point()
        ball.reset_ball()
screen.exitonclick()
