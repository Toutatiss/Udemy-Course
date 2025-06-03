# Import
import random
from art import logo

# Loop state variables
restart = True

# Display splash screen
print("\n"*20)
print(logo)
print("Welcome to Number Guessr!")

while restart:
    print("I'm thinking of a number between (and including) 1 and 100.")

    # Select game difficulty
    selected_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    easy_lives = 10
    hard_lives = 5

    player_lives = (
        easy_lives if selected_difficulty == "easy"
        else hard_lives if selected_difficulty == "hard"
        else 10
    )

    # Generate a number
    number_to_guess = random.randint(1, 100)

    # Functions
    def restartPrompt():
        restart_input = input("Would you like to play again? (y/n): ")
        if restart_input == "y":
            return True
        else:
            return False
    
    # Loop state variables
    enough_lives = True
    won = False

    while enough_lives and not won:
        # Prompt user to guess
        print(f"You have {player_lives} attempt(s) remaining.")
        player_guess = int(input("Make your guess: "))

        # Check user guess and provide feedback
        if player_guess > number_to_guess:
            print("Too high!")
            player_lives -= 1
        elif player_guess < number_to_guess:
            print("Too low!")
            player_lives -= 1
        elif player_guess == number_to_guess:
            print("Correct! You Win!")
            won = True
            restart = restartPrompt()
        if player_lives == 0:
            print("You ran out out lives! You lose!")
            print(f"The correct number was: {number_to_guess}")
            enough_lives = False
            restart = restartPrompt()


        
     
    
    