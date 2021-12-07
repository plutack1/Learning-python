from replit import clear
from art import logo
print(logo)
print("welcome to the secret auction program.")
run_again = True
bidders = {}
while run_again is True:
    name = input("What is your name?")
    bid_value = input("What is your bid?\n$")
    answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if answer == "yes":
        run_again = True
    else:
        run_again = False
    bidders[name] = bid_value
    clear()
highest_bid = max(bidders, key=bidders.get)
print(f"The winner is {highest_bid} with a bid of ${bidders[highest_bid]}")
