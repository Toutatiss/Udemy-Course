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
        "cost": 1.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
}
resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
} 


# State variables
validOrder = False

# Variables
coffeeOrder = ""

# Start Screen
print("\n"*20)
print("Welcome to Coff - E!")


while not validOrder:
    # Prompt user for what coffee they would like
    user_input = input("We serve 'espresso', 'latte', and 'cappuccino' coffees. Please enter your order: ")
    ## Check input
    # Machine status
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    
    # Maintenance?
    if user_input == "off": # Switch the machine off, by exiting the ready loop

        print("Machine powering down...")
        sys.exit()
    
    # Valid coffee order?
    for recipe in MENU:
        if user_input == recipe:
            coffeeOrder = user_input
            validOrder = True
            break
        
    if not validOrder and user_input != "report":
        print("That's not a valid coffee order, please try again.")


## Continue to next stage
# Check for sufficient resources
for ingredient, quantityRequired in MENU[coffeeOrder]["ingredients"].items():
    quantityAvailable = resources.get(ingredient, 0)
    if quantityRequired > quantityAvailable:
        print(f"Sorry, there is not enough {ingredient}.")
        validOrder = False
    # print(f"{ingredient}: required = {quantityRequired}, available = {quantityAvailable}")


