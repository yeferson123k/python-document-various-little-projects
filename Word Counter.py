#word input phrase 
"""def word_count(text):
    words = text.split()

    word_count = len(words)

    return word_count

if __name__ == "__main__":
    input_text = input("Enter a sentence to piece of text: ")
    count = word_count(input_text)
    print(f"Word count: {count}")"""

#file text

def word_count_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return -1

if __name__ == "__main__":
    file_path = input("Enter the path to the .txt file: ")
    count = word_count_in_file(file_path)

    if count == -1:
        print("File not found.")
    else:
        print(f"Word count: {count}")
        