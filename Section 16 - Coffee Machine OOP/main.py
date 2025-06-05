from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import sys

coffeeMenu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

user_command = ""
drinkOrder = None

# 0. Setup screen
print("\n"*20)
print("Welcome to Coff-E!")

while drinkOrder == None:
    # 1. Prompt user for what coffee they would like
    user_command = input(f"What kind of coffee would you like? ({coffeeMenu.get_items()}): ")

    # 2. Turn off machine on "off" prompt
    if user_command == "off":
        print("Machine powering down...")
        sys.exit() 

    # 3. Print report on "report" prompt
    elif user_command == "report":
        coffeeMaker.report()
        moneyMachine.report()
        drinkOrder = None

    # Check for valid coffee order
    else:
        drinkOrder = coffeeMenu.find_drink(user_command)
        if drinkOrder == None:
            print("No valid drink entered!")
        else:
            # 4. Check for sufficient resources
            sufficientResources = coffeeMaker.is_resource_sufficient(drinkOrder)
            if not sufficientResources:
                drinkOrder = None
            else:
                # 5. Process coins + check transaction successful, if so make coffee
                successfulPayment = moneyMachine.make_payment(drinkOrder.cost)
                if successfulPayment:
                    coffeeMaker.make_coffee(drinkOrder)
                    drinkOrder = None