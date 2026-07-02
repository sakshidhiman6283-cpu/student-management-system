import random

def play_game():
    print("🎮 Rock-Paper-Scissors Game 🎮")
    print("Options: rock, paper, scissors")

    user_choice = input("Enter your choice: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    elif user_choice in choices:
        print("You lose! 😢")
    else:
        print("Invalid choice! Please select rock, paper, or scissors.")

# Run the game
play_game()
