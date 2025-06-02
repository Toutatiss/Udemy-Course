# Yet another go, using more help from Angela

# Libraries
import random

# Assets
from words import word_list
from art import hangman_stages, logo

# Main variables
chosen_word = random.choice(word_list)
correct_letters = []
incorrect_letters = []
lives = 6

# State Variables
gameRunning = True

# Startup game
print(logo)

while gameRunning:
    guess = input("Guess a letter: ").lower()
    
    display = ""
    
    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"
            
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not a letter in the word.")
        if lives == 0:
            print("You lose!")
            print(f"The word was: {chosen_word}")
            gameRunning = False
             
    print(display)
    if "_" not in display:
        print("You win!")
        gameRunning = False
        
    print(hangman_stages[lives])
    print(f"You have {lives}/6 lives left")
        
