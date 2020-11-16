MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    amount_paid = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return amount_paid


def serve_or_refund(amount_paid):
    change = round(amount_paid - coffee_cost, 2)
    if change >= 0:
        resources["money"] += amount_paid
        resources["money"] -= change
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
        return True
    elif change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False


def select_coffee():
    global coffee_type, coffee_cost, coffee_ingredients

    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "espresso" or request == "latte" or request == "cappucino":
        coffee_type = request
        coffee_cost = MENU[coffee_type]["cost"]
        coffee_ingredients = MENU[coffee_type]["ingredients"]
    elif request == "off":
        return False
    elif request == "report":
        report_status()
        return False
    else:
        print("Invalid entry. Please enter a valid coffee type.")


def report_status():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources():
    '''Check availability of system resources '''
    water = resources['water'] - coffee_ingredients["water"]
    milk = resources['milk'] - coffee_ingredients["milk"]
    coffee = resources['coffee'] - coffee_ingredients["coffee"]
    if water < 0:
        print("Sorry there is not enough water.")
        return False
    elif milk < 0:
        print("Sorry there is not enough milk.")
        return False
    elif coffee < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        # Update system resources for those used
        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee


machine_on = True
coffee_type = ""
coffee_cost = 0.0
coffee_ingredients = {}

while machine_on:
    machine_on = select_coffee()
    machine_on = check_resources()
    if machine_on == False:
        break
    amount_paid = insert_coins()
    serve_or_refund(amount_paid)
