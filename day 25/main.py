import turtle as t
import pandas as pd
FONT_VALUE = ("Comic Sans MS", 20, "bold")
screen = t.Screen()
turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtles = [turtle1, turtle2]
for turtle in turtles:
    turtle.hideturtle()
    turtle.penup()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
file = pd.read_csv("50_states.csv")
all_states = file.state.tolist()
correct_guess = []

score = 0
game_on = True

def update_score():
    turtle2.goto(0, 350)
    turtle2.pencolor("blue")
    turtle2.clear()
    turtle2.write(f"SCORE: {score}", align="center", font=FONT_VALUE)
while game_on:
    update_score()
    answer_state = screen.textinput(title="Guess the state", prompt="What's "
                                                                    "another "
                                                                    "state's "
                                                                    "name?")
    if answer_state == "exit":
        break
    table = file[file["state"] == answer_state.capitalize()]
    if len(table) > 0:
        x_cor = int(table.x)
        y_cor = int(table.y)
        if answer_state not in correct_guess:
            turtle1.goto(x_cor, y_cor)
            turtle1.write(answer_state.capitalize())
            score += 1
            update_score()
            correct_guess.append(answer_state.capitalize())

            remaining_state = [state for state in all_states if state not in
                               correct_guess]
            remaining_state_dict = {"state": remaining_state}
            new_table = pd.DataFrame(remaining_state_dict)
            new_table.to_csv("remaining_state.csv")

t.mainloop()