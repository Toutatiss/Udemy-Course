import random

choices = [0, 1, 2]
choices_words = ["Rock", "Paper", "Scissors"]
user_input = int(input("Choose one: Rock = 0, Paper = 1 or Scissors = 2\n"))
computer_input = random.choice(choices)

user_choice = choices_words[user_input]
computer_choice = choices_words[computer_input]

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

outcome = user_input-computer_input
# 2-2 = 0 (D), 2-1 = 1(W), 2-0 = 2(L)
# 1-2 = -1(L), 1-1 = 0(D), 1-0 = 1(W)
# 0-2 = -2(W), 0-1 = -1(L), 0-0 = 0(D)

if outcome == 0:
    print("It's a draw!")
elif outcome == -1 or outcome == 2:
    print("You lost!")
else: 
    print("You won!")