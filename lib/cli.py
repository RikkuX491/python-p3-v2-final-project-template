# lib/cli.py

from helpers import (
    exit_program,
    initialize_database,
    interact_with_hotel_data,
    interact_with_review_data
)


def main():
    initialize_database()
    
    while(True):
        menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'q'):
            exit_program()
        elif(user_input == 'h'):
            interact_with_hotel_data()
        elif(user_input == 'r'):
            interact_with_review_data()
        else:
            print("Invalid input! Please try again!\n")


def menu():
    print("\nHere's the main menu!")
    print("h: Interact with Hotel data")
    print("r: Interact with Review data")
    print("q: Quit the program\n")


if __name__ == "__main__":
    main()
