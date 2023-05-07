import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock paper scissors): ")

print(f"player: {player}")
print(f"computer: {computer}")


if player == computer :
    print("its a tie")

elif player == "rock" and computer == "scissors":
    print("YOU WIN")

elif player == "paper" and computer == "rock":
    print("YOU WIN")

elif player == "scissors" and computer == "paper":
    print("YOU WIN")

else:
    print("YOU LOSE")