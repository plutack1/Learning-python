import random
from art import logo
from art import vs
from game_data import data
print(logo)


def game():
    play_again = False
    random.shuffle(data)
    while play_again is False:
        score = 0
        stop_game = False
        while stop_game is False:
            for i in range(len(data)):
                a = data[i]
                b = data[i+1]
                print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
                print(vs)
                print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
                answer = input("Who has more followers? Type 'A' or 'B':").lower()
                if answer == 'a' and a['follower_count'] >= b["follower_count"]:
                    score += 1
                    print(f"you're right! Current score: {score}")
                elif answer == 'b' and a['follower_count'] <= b["follower_count"]:
                    score += 1
                    print(f"you're right! Current score: {score}")
                else:
                    print(f"sorry, that's wrong. Final score: {score}")
                    stop_game = True
                    play_again = True
                    break
    if play_again is False:
        print("you beat the game with the perfect score")
    try_again = input("Do you want to play again? Type 'Y' or 'N':").lower()
    if try_again == "y":
        game()
    else:
        print("game closed")


game()
