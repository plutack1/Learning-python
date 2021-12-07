bill=0
print("hello, what pizza size do you want")
pizza_size = input("s = small pizza m = medium pizza l=large pizza\n")
if pizza_size == "s":
    bill=int(15)
    print(f"small pizza cost ${bill}")
    add_pepperoni = input("do you want pepperoni? y or n\n")
    if add_pepperoni == "y":
        bill +=2
    extra_cheese = input("do you want extra cheese? y or n\n")
    if extra_cheese == "y":
        bill +=1
    print(f"your total bill is ${bill}")
elif  pizza_size == "m":
    bill=int(20)
    print(f"small pizza cost ${bill}")
    add_pepperoni = input("do you want pepperoni? y or n\n")
    if add_pepperoni == "y":
        bill +=3
    extra_cheese = input("do you want extra cheese? y or n\n")
    if extra_cheese == "y":
        bill +=1
    print(f"your total bill is ${bill}")
elif pizza_size == "l":
    bill=int(25)
    print(f"small pizza cost ${bill}")
    add_pepperoni = input("do you want pepperoni? y or n\n")
    if add_pepperoni == "y":
        bill +=3
    extra_cheese = input("do you want extra cheese? y or n\n")
    if extra_cheese == "y":
        bill +=1
    print(f"your total bill is ${bill}")
else:
    print("you have not made an order")






