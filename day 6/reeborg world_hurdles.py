# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for n in range(1,7):
    move()
    jump()




hurdle 4


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def jump():
    if wall_on_right() and front_is_clear():
        move()
        while wall_on_right() and wall_in_front():
            turn_right()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()


while not at_goal():
    if front_is_clear():
        move()

    elif wall_in_front():
        turn_left()
        jump()



maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_around()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_right() 36