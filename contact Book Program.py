contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added successfully ")

def search_contact(name):
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print(f"Contact {name} not found")

def display_contacts():
    if contacts:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {phone}")
    else:
        print("The contact book is empty.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contact")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == '3':
        display_contacts()

    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == '5':
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


