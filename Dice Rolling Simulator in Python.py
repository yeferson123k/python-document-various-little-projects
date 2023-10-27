import random

def roll_dice():
    return random .randint(1, 6)

def main():
    print("Welcome to Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        
        dice_result = roll_dice()
        print(f"You roll a {dice_result}")

        play_again = input("Do you want to toll again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main___":
    main()

main()