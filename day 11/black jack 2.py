import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
computer_card = []
random.choice(cards, k = 2)

keep_drawing = True
while keep_drawing is True:
def draw_card():


    x = random.choice(cards)
    return x
def start():
    user_card.append(random.choice(cards, k = 2))