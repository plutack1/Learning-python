from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
keep_on = True
while keep_on:
    choice = input(f"what drink do you want?{my_menu.get_items()} ")
    if choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == "off":
        keep_on = False
    else:
        drink = my_menu.find_drink(choice)
        if my_money_machine.make_payment(drink.cost) and \
                my_coffee_maker.is_resource_sufficient(drink):
            my_coffee_maker.make_coffee(drink)

