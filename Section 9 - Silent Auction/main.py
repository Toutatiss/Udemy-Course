#Import assets
from art import logo

#Initialise with Title Screen
print(logo)

#Initialise dictionary
bids = {}

#Initialise loop variable
restart = "yes"

while restart != "no":
    # Clear the screen
    print("\n" * 100)
    
    # Ask for a bid
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    # Add bid to the bids dictionary
    bids[name] = bid

    # Ask if there is another person
    restart = input("Are there more bidders? (yes/no) ")
    
#When bidding is complete, calculate the winner
max_bid = 0
for bidder in bids:
    if  bids[bidder] > max_bid:
        max_bid = bids[bidder]
        winner = bidder
        
# Print out winner
print(f"The winner is {winner} with a bid of {max_bid}!")

