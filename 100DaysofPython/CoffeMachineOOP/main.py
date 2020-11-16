from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while machine_on:
    request = input(f"What would you like? ({menu.get_items}): ")

    if request == "espresso" or request == "latte" or request == "cappucino":
        item = menu.find_drink(request)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(item)
        is_sufficent_funds = money_machine.make_payment(item.cost)
        if is_enough_ingredients and is_sufficent_funds:
            coffee_maker.make_coffee(item)

    elif request == "off":
        machine_on = False
        break
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
        machine_on = False
        break
    else:
        print("Invalid entry. Please enter a valid coffee type.")
