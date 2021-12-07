#Calculator

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What's the first number?: "))
  more_calc = True
  seq = 1
  while more_calc is True:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    if seq == 1:
      num2 = float(input("What's the second number?: "))
    elif seq > 1:
      num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    seq += 1

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    prompt = input(f"type 'Y' to continue calculating with {answer}, or type 'N' to start new calculation").lower()
    if prompt == "y":
      more_calc = True
      num1 = answer
    elif prompt == "n":
      more_calc = False
      calculator()
calculator()



