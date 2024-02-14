import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "@$#&*{}[],=-().+;:'/"

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if length <8:
        print("Password length should be at least 8 characters.")
        return
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        if password:
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")