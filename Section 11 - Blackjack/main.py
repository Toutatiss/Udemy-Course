import random

# Game start
print("\n"*20)
print("Let's play Blackjack! \n\n")

def blackjack():
    # Game Setup
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_dict = {
    "computer": {"cards": [], "score": 0},
    "human": {"cards": [], "score": 0},
    }
    
    # Game functions
    def dealCard(player):
        players_dict[player]["cards"].append(random.choice(available_cards))
        players_dict[player]["score"] = sum(players_dict[player]["cards"])

    def showPlayerCards():
        print(f"\n\n\tYour cards are: {players_dict['human']['cards']}, current score: {players_dict['human']['score']}")
    
    def printScores():
        print(f"\tYour score: {players_dict['human']['score']}")
        print(f"\tComputer score: {players_dict['computer']['score']}")
        
    # Game state variables
    end_game = False

    # First Round
    # Deal cards to player and computer
    dealCard("human")
    dealCard("human")
    dealCard("computer")
    dealCard("computer")

    # Show cards
    showPlayerCards()
    print(f"\tComputer's first card: {players_dict['computer']['cards'][0]}")

    while not end_game:
        # Prompt user to hit or stand
        user_input = input("\n\nType 'y' to get another card, or 'n' to pass: ")
        if user_input == 'n':
            end_game = True
            break
        
        dealCard("human")
        showPlayerCards()
        if players_dict["human"]["score"] >= 21:
            end_game = True
        
    # End game code
    human_score = players_dict["human"]["score"]
    computer_score = players_dict["computer"]["score"]

    if human_score > 21:
        print("\tBust! You lose.")
    else:
        # Further checks:
        while computer_score < 17:
            dealCard("computer")
            computer_score = players_dict["computer"]["score"]
        if computer_score > 21:
            print("\tYou win!")
        elif computer_score > human_score:
            print("\tYou lose.")
        elif computer_score == human_score:
            print("\tIt's a draw!")

    printScores()

    user_input = input("Do you wish to play again? (y/n): ")
    if user_input == 'n':
        return
    else:
        blackjack()
    
blackjack()
    
