buy_another = True
# todo 1. create dictionary for coffee machine
coffee_type = ""
coffee_machine = {
    'water': 300,
    'coffee': 100,
    'milk': 200,
    'money': 0,
}
espresso = {
    'water': 50,
    'coffee': 18,
    'milk': 0,
    'price': 1.50,

}
latte = {
    'water': 200,
    'coffee': 24,
    'milk': 150,
    'price': 2.50,
}
cappuccino = {
    'water': 250,
    'coffee': 24,
    'milk': 100,
    'price': 3.00,
}


def check_drink():
    if coffee_type == "espresso" and espresso['water'] <= coffee_machine['water'] and espresso['coffee'] <= coffee_machine['coffee'] and espresso['milk'] <= coffee_machine['milk']:
        return True
    elif coffee_type == "latte" and latte['water'] <= coffee_machine['water'] and latte['coffee'] <= coffee_machine['coffee'] and latte['milk'] <= coffee_machine['milk']:
        return True
    elif coffee_type == "cappuccino" and cappuccino['water'] <= \
            coffee_machine['water'] and cappuccino['coffee'] <= coffee_machine['coffee'] and cappuccino['milk'] <= coffee_machine['milk']:
        return True
    else:
        if coffee_type == "espresso" and (espresso['water'] > coffee_machine['water'] or espresso['coffee'] > coffee_machine['coffee'] or espresso['milk'] > coffee_machine['milk']):
            print("there is not enough resources")
            check_buy_another()

        elif coffee_type == "latte" and (latte['water'] > coffee_machine['water'] or latte['coffee'] > coffee_machine['coffee'] or latte['milk'] > coffee_machine['milk']):
            print("there is not enough resources")
            check_buy_another()
        elif coffee_type == "cappuccino" and cappuccino['water'] > coffee_machine['water'] and cappuccino['coffee'] > \
                coffee_machine['coffee'] and cappuccino['milk'] > coffee_machine['milk']:
            print("there is not enough resources")
            check_buy_another()

        elif coffee_type == "report":
            print(f"water: {coffee_machine['water']}ml\ncoffee: "
                  f"{coffee_machine['coffee']}ml\nmilk: "
                  f"{coffee_machine['milk']}ml\nmoney: $"
                  f"{format(coffee_machine['money'], '.2f')}")
            coffee()
        else:
            print("You have entered the wrong input")
            return False


def coin_input():
    """function to input the type and quantity of coins at hand and calculate the value in dollars"""
    quarters = int(input("how many quarters?")) * 25
    dimes = int(input("how many dimes?")) * 10
    nickles = int(input("how many nickles?")) * 5
    pennies = int(input("how many pennies?")) * 1
    dollar_value = (quarters + dimes + nickles + pennies)/100
    return dollar_value



def check_money(money):
    global buy_another
    if coffee_type == "espresso" and espresso['price'] <= money:
        return True
    elif coffee_type == "latte" and latte['price'] <= money:
        return True
    elif coffee_type == "cappuccino" and cappuccino['price'] <= money:
        return True
    else:
        print(f"you do not hve enough money\n${money} refunded")
        check_buy_another()


def give_change(money):
    if coffee_type == "espresso" and espresso['price'] < money:
        print(f"Here is ${round(money - espresso['price'], 2)} in change")

    elif coffee_type == "latte" and latte['price'] < money:
        print(f"Here is ${round(money - latte['price'], 2)} in change")

    elif coffee_type == "cappuccino" and cappuccino['price'] < money:
        print(f"Here is ${round(money - cappuccino['price'], 2)} in change")


def coffee_machine_update(money):
    global coffee_machine
    if coffee_type == "espresso" and check_money(money) is True:
        coffee_machine['water'] -= espresso['water']
        coffee_machine['coffee'] -= espresso['coffee']
        coffee_machine['milk'] -= espresso['milk']
        coffee_machine['money'] += round(espresso['price'], 2)
    elif coffee_type == "latte" and check_money(money) is True:
        coffee_machine['water'] -= latte['water']
        coffee_machine['coffee'] -= latte['coffee']
        coffee_machine['milk'] -= latte['milk']
        coffee_machine['money'] += round(latte['price'], 2)
    elif coffee_type == "cappuccino" and check_money(money) is True:
        coffee_machine['water'] -= cappuccino['water']
        coffee_machine['coffee'] -= cappuccino['coffee']
        coffee_machine['milk'] -= cappuccino['milk']
        coffee_machine['money'] += round(cappuccino['price'], 2)


def check_buy_another():
    global buy_another
    option = input("Do you want to buy another?YES or NO").lower()
    if option == "yes":
        buy_another = True
        coffee()
    if option == "no":
        buy_another = False


def coffee():
    global coffee_type
    coffee_type = input("What would you like? (espresso/latte/cappuccino)")
    if check_drink() is True:
        dollar_value = coin_input()
        if check_money(money=dollar_value) is True:
            give_change(money=dollar_value)
            coffee_machine_update(money=dollar_value)
            check_buy_another()


while buy_another is True:
    coffee()


