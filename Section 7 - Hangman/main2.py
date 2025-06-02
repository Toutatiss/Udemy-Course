# I want to have another go at coding up hangman. The first go was pretty messy, and missing some functions, but I'm learning a lot!

## Game initialisation

# Libraries
import random
# Word List
word_list = ["aardvark", "baboon", "camel"]

# State Variables
gameRunning = True

# Game Variables
word = random.choice(word_list) # Chooses a word at random from the list
word_length = len(word)
ls_blank_word = ["_"] * word_length
ls_word = list(word)

## Function to initialise the game
def initGame():
    print("\n\nLet's play hangman!")
    blank_word = ''.join(ls_blank_word)
    print(f"Here is your word: {blank_word}")
    print(f"There are {word_length} letters in this word.")

## Function to collect user input
def collectInput():
    lo_user_input = input("Please enter a letter: ") # Collect the input
    lo_user_input = lo_user_input.lower()             # Process the input to lowercase
    return list(lo_user_input)

## Function to process user input
def compareInput():
    for index in range(word_length):                # For each of the letters in the word
        if ls_user_input[0] == ls_word[index]:      # Check if the input matches the letter in the word
            ls_blank_word[index] = ls_user_input[0] # Update the blank
            # Reduce the number of remaining letters
        
def giveFeedback():
    print(f"There are {letters_remaining} number of letters remaining.")

## Game code
initGame()
while gameRunning:
    ls_user_input = collectInput()
    compareInput()
    giveFeedback()
    