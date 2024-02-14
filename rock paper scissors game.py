import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please choice rock, paper or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "·It's a tie!"
    elif user == "rock":
        return "You win!" if computer == "scissors" else "Computer win!"
    elif user == "paper":
        return "you win!" if computer == "rock" else "Computer win!"
    elif user == "scissors":
        return "You win!" if computer == "paper" else "Computer win!"
    
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()