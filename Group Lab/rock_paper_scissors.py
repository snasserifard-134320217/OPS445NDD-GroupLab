import random

options = ["rock", "paper", "scissors"]  # list of options for the computer

print("Welcome to Rock, Paper, Scissors!")
user_option = input("Enter your choice (rock, paper, scissors): ")
computer_option = random.choice(options)  # This will choose a random option from your list for the computer

print(f"You chose {user_option}, computer chose {computer_option}.")

if user_option == computer_option:
    print("It's a tie!")
elif (user_option == "rock" and computer_option == "scissors") or \
     (user_option == "scissors" and computer_option == "paper") or \
     (user_option == "paper" and computer_option == "rock"):
    print("You win!")
else:
    print("You lose!")
