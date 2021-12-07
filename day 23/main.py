import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

loop = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create a car once iin six loops
    loop += 1
    if loop % 6 == 0:
        car_manager.create()
    car_manager.move()
    # detect when the turtle collides with the car
    for car in car_manager.cars:
        if player.distance(car) < 20 :
            game_is_on = False
            scoreboard.game_over()

    # detect if turtle gets to the finish line and reset the game
    if player.reset_position() is True:
        scoreboard.score += 1
        car_manager.speed_up()
    scoreboard.update_scoreboard()

screen.exitonclick()
