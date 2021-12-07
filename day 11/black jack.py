import random
def card(total):
    global user_total
    while continue_game is True:
        if total > 21 and 11 in user_card:
            position = []
            index = 0
            for i in user_card:
                index += 1
                if i == 11:
                    x = index - 1
                    position.append(x)
                for i in position:
                    user_card[i] = 1
                    total = sum(user_card)
                    if total > 21:
                        print(f"{user} lose")
                    elif total < 21:
                        option = input("Do you want another card?Y/N\n").lower()
                        if option == "y":
                            x = random.choice(cards)
                            user_card.append(x)
                            user_total = sum(user_card)
                        elif option =="n":
                            user_total = sum(user_card)
    return  user_total
def computer_draw(total):
    global computer_total
    if total > 21 and 11 in computer_card:
        position = []
        index = 0
        for i in user_card:
            index += 1
            if i == 1:
                x = index - 1
                position.append(x)
        for i in position:
            user_card[i] = 1
            total = sum(computer_card)
            if total < 17:
                computer_card.append(random.choice(cards))
                computer_total = sum(computer_card)
            else:
                computer_total = sum(computer_card)
    return computer_total


user = input("what is your name\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = False
user_card = []
computer_card = []
for i in range(2):
    x = random.choice(cards)
    y = random.choice(cards)
    user_card.append(x)
    computer_card.append(y)
print(user_card)
print(computer_card)

natural = [11, 10]

if natural in user_card and computer_card:
    b_jack = True
    print("Draw")
elif natural in user_card:
    print(f"{user} won with {user_card}")
elif natural in computer_card:
    print(f"computer won with {computer_card}")
else:
    continue_game = True
    card(total = sum(user_card))
    continue_game = False
    computer_draw(total = sum(computer_card))
    if computer_total > user_total:
        print("Computer wins")
    else:
        print(f"{user} wins")








