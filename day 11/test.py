import random
user = input("what is your name\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = random.choices(cards, k=2)
computer_card = random.choices(cards, k=2)
print(f"{user} card is {user_card}")
print(f"the computer first card is {computer_card[0]}")


def draw_card():
    random.choice(cards)
    return random.choice(cards)


def show_card():
    print("GAME OVER")
    print(f"{user} card is {user_card}")
    print(f"computer card is {computer_card}")
    return


def game_computer():
    if sum(computer_card) < 17:
        computer_card.append(draw_card())
        if sum(computer_card) < 17:
            game_computer()
            print(f"{user} card is {user_card}")
            print(f"computer card is {computer_card}")
            if sum(computer_card) > 21:
                if 11 in computer_card:
                    position = []
                    index = 0
                    for i in computer_card:
                        index += 1
                        if i == 11:
                            x = index - 1
                            position.append(x)
                            for j in position:
                                computer_card[j] = 1
                                game_computer()
                elif 11 not in computer_card:
                    show_card()
                    print(f"YOU WIN! computer total is over 21")
        elif sum(computer_card) > 21:
            show_card()
            print("BUST! You win! Computer total is over 21")

        else:
            game_computer()
    elif sum(computer_card) >= 17:
        if sum(user_card) == sum(computer_card):
            show_card()
            print("It is a draw")
        elif sum(user_card) == 21:
            show_card()
            print(f"YOU win! Your total is 21")
        elif sum(computer_card) == 21:
            show_card()
            print(f"YOU lose! Computer total is 21")
        elif sum(user_card) > sum(computer_card):
            show_card()
            print(f"YOU WIN! you are closer to 21")
        elif sum(user_card) < sum(computer_card):
            show_card()
            print(f"YOU LOSE! Computer are closer to 21")
    return


def game_user():
    if (10 and 11 in user_card) and (10 and 11 in computer_card):
        draw_card()
        print("It is a draw")
    else:
        if 10 in user_card and 11 in user_card:
            show_card()
            print(f"{user} had a natural! {user} wins")
        elif 10 and 11 in computer_card:
            print(f" Computer had a natural! Computer wins")
        else:
            option = input("Do you want another card?Y/N\n").lower()
            if option == "y":

                x = draw_card()
                print(f"your new card is {x}")
                user_card.append(x)
                print(f"your card is {user_card}")
                if sum(user_card) > 21:
                    if 11 in user_card:
                        position = []
                        index = 0
                        for i in user_card:
                            index += 1
                            if i == 11:
                                x = index - 1
                                position.append(x)
                                for j in position:
                                    user_card[j] = 1
                    elif 11 not in user_card:
                        show_card()
                        print("BUST!You lose! You total is over 21")
                if sum(user_card) < 21:
                    game_user()
            elif option == "n":
                if sum(user_card) > 21:
                    if 11 in user_card:
                        position = []
                        index = 0
                        for i in user_card:
                            index += 1
                            if i == 11:
                                x = index - 1
                                position.append(x)
                                for j in position:
                                    user_card[j] = 1
                game_computer()
    return


game_user()
play_again = input("Do you want to play again?Y/N\n").lower()
if play_again == "y":
    game_user()
elif play_again == "n":
    print("Game has ended")
