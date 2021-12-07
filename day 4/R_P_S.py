import random
option = ["ROCK", "PAPER", "SCISSORS"]
selected_option = int(input("type in 0 for rock, 1 for paper, 2 for scissors"))
if 0 <= selected_option < 3:
    option_1 = option[selected_option]
    print("YOU PICK",option_1)
    random.seed(random.randint(1,100))
    number = random.randint(0,2)
    option_2 = option[number]
    print("COMPUTER PICKS",option_2)
    if option_1 == "ROCK" and option_2 == "SCISSORS":
        print ("YOU WIN")
    elif option_1 == "SCISSORS" and option_2 == "PAPER":
        print ("YOU WIN")
    elif option_1 == "PAPER" and option_2 == "ROCK":
        print ("YOU WIN")
    elif option_1 == option_2:
        print ("PLAY AGAIN")

    else:
        print("YOU LOSE")
else:
    print("YOU TYPED IN AN INVALID OPTION")

