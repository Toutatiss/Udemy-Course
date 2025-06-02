import random

# Setup
word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
word_length = len(word)

blank = []
for i in range(word_length):
    blank.append("_")

print("Get ready to play hangman!")
print("Here is your word:")
print(''.join(blank))

# Function to get a letter from the user
def userInput():
    return input("Please enter a letter: ").lower()   # Ask user for a letter, convert to lowercase, return the first character

# Get user input
user_input = userInput()

def checkLetter():
    # Message Flags
    success = False

    # Check if letter is in word
    for index in range(word_length):
        if word[index] == user_input:
            blank[index] = user_input
            return True

# Print feedback message
if checkLetter():
    print("You got a letter!")
else: 
    print("Oh no! You lost a life!")

# Print the blanks
print(''.join(blank))
