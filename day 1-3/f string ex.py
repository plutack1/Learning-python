import time
print("hello")
time.sleep(2.0)
# final_age = 90
initial_age = input("what is your current age?")
time_left = 90 - int(initial_age)
time_left *= 12
print(f"you have {time_left} months left")
time_left *= 52
time.sleep(3.0)
print(f"you have {time_left} weeks left")
time_left *= 365
time.sleep(3.0)
print(f"you have {time_left} days left")
