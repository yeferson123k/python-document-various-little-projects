import os 

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not fount.")
        return None
    
def save_file(filename, content, mode='w'):
    with open(filename, mode) as file:
        file.write(content)
    print("File saved successfully.")

def append_to_file(filename, content):
    save_file(filename, content, mode='a')
    print("Content appended to the file.")

def delete_file(filename):
    try:
        os.remove(filename)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not fount.")

def main():
    while True:
        print("\n1. Open file\n2. Create bew file\n3. append to file\n4. delete file\n5. Exit")
        choice = input("Enter the filename to open: ")

        if choice == '1':
            filename = input("Enter the filename to open: ")
            content = open_file(filename)
            if content is not None:
                print("\nFile content: ")
                print(content)
        elif choice == '2':
            filename = input("Enter the new filename: ")
            content = input("Enter file content:\n")
            save_file(filename, content)
        elif choice == '3':
            filename = input("Enter the filename to append: ")
            content = input("Enter content to append:\n")
            append_to_file(filename, content)
        elif choice == '4':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option")

if __name__ == "__main__":
    main()