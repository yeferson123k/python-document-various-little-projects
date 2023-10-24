import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("Can you guess the numeber? (between 1 and 100)")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulation! you guesed the number {secret_number} in {attempts}")
                break
        except ValueError:
            print("Invalid input. Enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
    