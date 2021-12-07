#program to determine if a number is odd or even\
input_number = int(input("Enter the number\n"))
det = input_number%2
if det == 1:
    print("The number entered is a odd number")
else:
    print("The number is an even number")
