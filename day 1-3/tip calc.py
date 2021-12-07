import time
print("welcome to the tip calculator")
time.sleep(1.5)
bill = input("what is the total bill?\n")
percentage = input("what percentage tip would you like to give? 10, 12, 15?\n")
split_amount = float(bill) + (int(percentage)/100 * float(bill))
number = input("how many people to split the bill?\n")
indiv_pay = round(split_amount/int(number), 2)
print(f"Each person should pay ${indiv_pay}")
