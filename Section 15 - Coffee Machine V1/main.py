import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
            "water": 50,
            "coffee": 18,
        },
        "cost": 3.0,
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
} 


# State variables
validOrder = False

# Variables
coffeeOrder = ""

# Start Screen
print("\n"*20)
print("Welcome to Coff - E!")

## Stage 1: Collect starting input
while not validOrder:
    # Prompt user for what coffee they would like
    coffee_input = input("We serve 'espresso', 'latte', and 'cappuccino' coffees. Please enter your order: ")
    ## Check input
     # Valid coffee order?
    for recipe in MENU:
        if coffee_input == recipe:
            coffeeOrder = coffee_input
            validOrder = True
            break
    # Machine status
    if coffee_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif coffee_input == "off": # Switch the machine off, by exiting the ready loop
        print("Machine powering down...")
        sys.exit() 
         
    if not validOrder and coffee_input != "report":
        print("That's not a valid coffee order, please try again.")   
    # Check for sufficient resources
    elif validOrder and coffee_input != "report":
        for ingredient, quantityRequired in MENU[coffeeOrder]["ingredients"].items():
            quantityAvailable = resources.get(ingredient, 0)
            if quantityRequired > quantityAvailable:
                print(f"Sorry, there is not enough {ingredient}.")
                validOrder = False
                # print(f"{ingredient}: required = {quantityRequired}, available = {quantityAvailable}")
    
    if validOrder:            
        # Request Coins
        print("Please insert your coins.")
        quarter_input = int(input("How many quarters?: "))
        dimes_input = int(input("How many dimes?: "))
        nickles_input = int(input("How many nickles?: "))
        pennies_input = int(input("How many pennies?: "))
        
        available_funds = quarter_input*0.25 + dimes_input*0.1 + nickles_input*0.05 + pennies_input*0.01
        
        order_price = MENU[coffeeOrder]["cost"]
        
        if available_funds < order_price:
            print("Insufficient funds! Money Refunded.")
            available_funds = 0
            validOrder = False
        else:
            # Process funds
            resources["money"] += order_price
            available_funds = available_funds - order_price
            if available_funds > 0:
                print(f"Here is your change: ${available_funds:.2f}")
                available_funds = 0
            # Make coffee
            for ingredient, quantityRequired in MENU[coffeeOrder]["ingredients"].items():
                resources[ingredient] -= quantityRequired
            print("Here is your order. Thank you for purchase!")
            validOrder = False