from expense import Expense  # type: ignore

def main():
    menu()

    # Main loop of the program 
    while True:
        match (user_choice_validation()):
            case 1:
                add_expense()

            case 2:
                view_expense()

            case 3:
                monthly_summary()

            case 4:
                edit_or_delete()

            case 5:
                break

def menu():
    "This function displays the main menu to the users"
    print("Personal Expense Tracker".center(100))
    print("1) Add Expense")
    print("2) View Expenses")
    print("3) Monthly Summary")
    print("4) Edit/Delete Expense")
    print("5) Exit\n")

def user_choice_validation():
    "This function takes the user choice and validates it"
    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            if 6 > user_choice > 0:
                return user_choice
            else:
                print("Choices should be 1 - 5\n")
                continue
        
        except ValueError:
            print("Enter a digit\n")

        except:
            # Exit if an error unrecognize
            print("Error while executing\n")
            return 5

def add_expense():
    "This function adds expenses"
    pass

def view_expense():
    "This function displays the expenses"
    pass

def monthly_summary():
    "This function displays a monthly summary"
    pass

def edit_or_delete():
    "This function edits or deletes user's incorrect entries"
    pass

if __name__ == "__main__":
    main()