import os
import shutil

# Function to create a file
def create_file(file_path):
    try:
        with open(file_path, 'w'):
            pass
        print(f"Created the file at {file_path}")
    except Exception as e:
        print(f"Error creating the file at {file_path}: {e}")

# Function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted the file at {file_path}")
    except Exception as e:
        print(f"Could not delete the file at {file_path}: {e}")

# Function to copy a file to a new location
def copy_file(file_path, new_file_path):
    try:
        shutil.copy(file_path, new_file_path)
        print(f"Copied the file from {file_path} to {new_file_path}")
    except Exception as e:
        print(f"Failed to copy file from {file_path} to {new_file_path}: {e}")

# Function to move a file to a new location
def move_file(file_path, new_file_path):
    try:
        shutil.move(file_path, new_file_path)
        print(f"Successfully moved file from {file_path} to {new_file_path}")
    except Exception as e:
        print(f"Failed to move file from {file_path} to {new_file_path}: {e}")

# Main function to interact with the user
def main():
    while True:
        print("\nSelect an option: ")
        print("1. Create a new file")
        print("2. Delete a file")
        print("3. Copy a file")
        print("4. Move a file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            file_path = input("Enter the file path: ")
            create_file(file_path)
        elif choice == "2":
            file_path = input("Enter the file path: ")
            delete_file(file_path)
        elif choice == "3":
            file_path = input("Enter the file path: ")
            new_file_path = input("Enter the new file path: ")
            copy_file(file_path, new_file_path)
        elif choice == "4":
            file_path = input("Enter the file path: ")
            new_file_path = input("Enter the new file path: ")
            move_file(file_path, new_file_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
