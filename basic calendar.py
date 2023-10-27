import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def main():
    print("Calender")
    while True:
        print("\nSelect and option: ")
        print("1. Enter calender Data: ")
        print("2. Quit")


        choice = input("Enter your choice: ")

        if choice == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            if 1 <= month <= 12:
                display_calendar(year, month)
            else:
                print("Invalid month. Enter a valid month (1-12)")        
        
        elif choice == '2':
            print("Exiting the Basic Calendar application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()