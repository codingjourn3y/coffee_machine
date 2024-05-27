MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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
}

profits = 0
is_on = True

def check_resources(choice):
    for r in resources:
        resources_needed = MENU[choice]["ingredients"][r]
        if resources_needed > resources[r]:
            return False
        else:
            return True


def process_coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many quarters?: ")) * 0.01
    total_amount = quarters + dimes + nickles + pennies
    return total_amount


def check_transaction(choice):
    cost = MENU[choice]["cost"]
    if total_amount < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif total_amount > cost:
        change_back = round(total_amount - cost, 2)
        print(f"Here is ${change_back} dollars in change")
        return True
    else:
        return True


def resources_deducted():
    resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    print(f"Here is your {choice}. Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profits}")
    else:
        if check_resources(choice):
            total_amount = round(process_coins(),2)
            if check_transaction(choice):
                resources_deducted()
                profits += MENU[choice]["cost"]
        else:
            print("Sorry there is not enough water.")
