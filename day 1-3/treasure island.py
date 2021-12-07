print("welcome to treasure island")
print("your mission is to fin the treasure")
ans_1 = input("you are at a crossroad. where do you want to go? left or right\n")
if ans_1.lower() == "left":
    print("you came across a swarm of bees.game over")
elif ans_1.lower() == "right":
    ans_2 = input("you come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across\n")
    if ans_2.lower() == "swim":
        print("you drown. Game over")
    elif ans_2.lower() == "wait":
        ans_3 = input("you arrive at the island unharmed. There is a house with 3 doors. one yellow, one red, one green. which colour do you choose\n")
        if ans_3.lower() == "green":
            print("you found the lost treasure")
        elif ans_3.lower() == "red":
            print("you entered a furnace. Game over")
        elif ans_3.lower() == "yellow":
            print("you fell into a pit filled with snakes.Game over")
        else:
            print("invalid response")
    else:
        print("invalid response")
else:
    print("invalid response")
