import random
def end():
    round = str(input("\nDo you want another round?[y/n]"))
    if round == "y":
        guess_the_number()
    elif round == "n":
        return
    else:
        end()

def guess_the_number():

    print("Welcome to Guess the Number!")
    chose = input("Chose a option write the number:\n1.clasic game(1-100)\n2.custom \n")
    if chose == "1":
        i = 1
        l = 100
        print("Can you guess the number? (between 1 and 100)")
    elif chose == "2":
        i = int(input("Enter your first number range: "))
        l = int(input("Enter your second number range: "))
        number_list = []
        number_list.append(i)
        number_list.append(l)
        if i > l:
            l = int(number_list[0])
            i = int(number_list[1])

    else:
        print('This is Wrong input')
        guess_the_number()

    secret_number = random.randint(i, l)
    attempts = 0

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
                end()
                break
        except ValueError:
            print("Invalid input. Enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
