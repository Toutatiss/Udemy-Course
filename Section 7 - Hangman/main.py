import random

# Setup
word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
word_length = len(word)
lives = 7
letters_remaining = word_length
gameRunning = True

blank = []
for i in range(word_length):
    blank.append("_")

print("\n\nGet ready to play hangman!")
print("Here is your word:")
print(''.join(blank))

# Functions
def checkLetter():
    # Check if letter is in word
    success = False
    for index in range(word_length):
        if word[index] == user_input:
            blank[index] = user_input
            letters_remaining -= 1
            success = True
    return [success, letters_remaining]

def userInput():
    return input("\n\nPlease enter a letter: ").lower()   # Ask user for a letter, convert to lowercase, return the first character

while gameRunning:
    # Function to get a letter from the user

    # Get user input
    user_input = userInput()

    # Print feedback message
    [success, letters_remaining] = checkLetter()
    if success:
        print(f"\n\nYou got a letter! There are {letters_remaining} letters remaining.")
    else: 
        lives -= 1
        print(f"\n\nOh no! You lost a life! You have {lives} left!")
    # Reset success
    success = False
         
    if lives == 0:
        print("You lost the game!")
        gameRunning = False
    elif letters_remaining == 0:
        print("You won!")
        gameRunning = False
    else:
    # Print the blanks
        print("Guess another letter:")
        print(''.join(blank))

