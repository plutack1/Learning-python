import random
ACTUAL_NUMBER = int(random.randint(1, 100))
print(ACTUAL_NUMBER)


def game():
    level = input("choose preferred difficulty\n EASY/HARD\n").lower()
    if level == "easy":
        easy()
    elif level == "hard":
        hard()
    else:
        print("INVALID INPUT\nTRY AGAIN")
        game()
    return


def easy():
    trial = 5
    endgame = False
    print(f"You have {trial} trials")
    while endgame is False:
        guess = int(input("pick a number"))
        print(guess)
        if guess == ACTUAL_NUMBER:
            print("you guessed right\nGAME OVER")
            endgame = True
        else:
            if guess < ACTUAL_NUMBER:
                print("too low")

            elif guess > ACTUAL_NUMBER:
                print("too high")
            trial -= 1
            if trial > 0:
                print(f"You have {trial} trials left")
            if trial == 0:
                print("You have no trial left\nYou failed to guess the number")
                endgame = True


def hard():
    trial = 10
    endgame = False
    print(f"You have {trial} trials")
    while endgame is False:
        guess = int(input("pick a number"))
        print(guess)
        if guess == ACTUAL_NUMBER:
            print("you guessed right\nGAME OVER")
            endgame = True
        else:
            if guess < ACTUAL_NUMBER:
                print("too low")

            elif guess > ACTUAL_NUMBER:
                print("too high")
            trial -= 1
            if trial > 0:
                print(f"You have {trial} trials left")
            if trial == 0:
                print("You have no trial left\nYou failed to guess the number")
                endgame = True


game()
