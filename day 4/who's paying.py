import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
x = len(names) - 1
payee_no = random.randint(0,x)
print(names[payee_no])
#Write your code below this line 👇

