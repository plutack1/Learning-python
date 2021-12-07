import random
seed_number= input("type in a random number\n")
random.seed(seed_number)
random_number = random.randint(0,1)
if (random_number == 0):
    print("Heads")
else:
    print("Tails")