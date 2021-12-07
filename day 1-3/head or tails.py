import random
test_seed = int(input("Create a seed number\n"))
random.seed(test_seed)
random_no = random.randint(1, 2)
if random_no == 1:
    print("Heads")
else:
    print("Tails") 