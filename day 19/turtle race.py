import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="place a bet", prompt="which turtle will "
                                                        "win the race?"
                                                        "\nEnter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
names = ["ronaldo", "hazard", "salah", "bale", "messi", "mpabbe", "aubameyang"]
val_y = list(range(-90, 91, 30))

for n in range(7):
    names[n] = Turtle(shape="turtle")
    names[n].color(colors[n])
    names[n].penup()
    names[n].goto(x=-230, y=val_y[n])
if user_bet:
    is_race_on = True
while is_race_on:
    for name in names:
        name.forward(random.randint(0, 10))
        if name.xcor() == 230:
            is_race_on = False
            winner = name
            winner_color = winner.pencolor()
            if name.pencolor() == user_bet:
                print(f" You win! {winner_color} won the race")
            else:
                print(f" You lose! {winner_color} won the race")


screen.exitonclick()
