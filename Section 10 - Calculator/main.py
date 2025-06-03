from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def resetQuery():
    valid_user_reset = False
    while not valid_user_reset:
        user_reset = input("Do you wish to continue using this result, or reset the calculator? (continue/reset): ")
        if user_reset == "reset":
            return True # Case to reset the calculator
        elif user_reset != "continue":
            print("Please provide a valid input.") # Case to request valid input
        else: 
            return False # Case to continue with existing calculation
    

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide, 
}   

# Example of calling a function from a dictionary
# print(operations["*"](4,8))

## SETUP
# Show splash screen
print(logo)
# Create loop conditions
reset = True

## LOOP
while reset:
    while reset:
        # Ask for first number
        first_number = int(input("Enter your first number: "))
        # Ask for operation
        chosen_operation = input("Enter your operation, (+, -, * or /): ")
        # Ask for second number
        second_number = int(input("Enter your second number: "))
        # Perform and display calculation
        calculation = operations[chosen_operation](first_number,second_number)
        print(f"The result is: {calculation}")
        
        # Ask if you want to continue, or reset the calculator
        # If reset, go to start of loop and clear screen (nah, I don't want to)
        reset = resetQuery()

    while not reset:
        # If continue, ask for operation
        first_number = calculation
        chosen_operation = input("Enter your operation, (+, -, * or /): ")
        # Then ask for second number
        second_number = int(input("Enter your second number: "))
        # Perform and display calculation
        calculation = operations[chosen_operation](first_number,second_number)
        print(f"The result is: {calculation}")
        # Return to the ask part of the loop
        reset = resetQuery()
