# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for divider in range(2, number-1):
        if number % divider == 0:
            is_prime = False
    if is_prime is False or number == 1:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")
# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
