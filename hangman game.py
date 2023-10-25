import random

a = ["  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

     "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

     "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

     "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

     "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

     "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========",
     
     " "]

b = a[::-1]

def choose_word():
    word_list = ["apple", "banana", "cat", "dog", "computer", "laptop"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
    while attempts_left > 0:
        print("\nAttempts left: ", attempts_left)
        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if "_" not in display:
            print("\nCongratulation! You guessed the word: ", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess!")
            print(b[attempts_left])
            attempts_left -= 1
        
    if attempts_left == 0 and "_" in display:
        print("\nSorry, you ran out of attempts. The word was: ", word_to_guess)
        
if __name__ == "__main__":
    hangman()

