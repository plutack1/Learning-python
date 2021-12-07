print("welcome to the love calculator!")
name1 = input("what is your name?\n")
name2 = input("what is their name?\n")
T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")
L = name1.lower().count("l") + name2.lower().count("l")
O = name1.lower().count("o") + name2.lower().count("o")
V = name1.lower().count("v") + name2.lower().count("v")
x = T+R+U+E
y = L+O+V+E
score = int(str(x)+str(y))
#print(type(x))
#print(score)
if score<10 or score>90:
    print(f"your score is {score}%, you go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"your score is {score}%, you go alright together")
else:
    print(f"your score is {score}%.")






