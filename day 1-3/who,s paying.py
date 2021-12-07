import random
test_seed= int(input("Create a seed number:\n"))
random.seed(test_seed)
nameasCSV = input("Give me everybody's names, separated by a comma")
names = nameasCSV.split(", ")
#print(names)
#print(random.choice(names))
#or
a = int(len(names))
a-=1
random_choice = random.randint(0, a)
print(f"The person who will pay is {names[random_choice]}")
