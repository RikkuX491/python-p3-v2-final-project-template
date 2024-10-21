# lib/cli.py

from helpers import (
    exit_program,
    create_flight,
    delete_flight,
    retrieve_all_flights,
    retrieve_flight_by_id,
    retrieve_flight_bookings,
    create_booking,
    delete_booking,
    retrieve_all_bookings,
    retrieve_booking_by_id,
    retrieve_flight_that_booking_belongs_to
)

def main():
    while True:
        menu()
        choice = input("> ")
        print(choice)
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_flight()
        elif choice == "2":
            delete_flight()
        elif choice == "3":
            retrieve_all_flights()
        elif choice == "4":
            retrieve_flight_by_id()
        elif choice == "5":
            retrieve_flight_bookings()
        elif choice == "6":
            create_booking()
        elif choice == "7":
            delete_booking()
        elif choice == "8":
            retrieve_all_bookings()
        elif choice == "9":
            retrieve_booking_by_id()
        elif choice == "10":
            retrieve_flight_that_booking_belongs_to()
        else:
            print("Invalid choice")
        input("\nPress 'return' to continue... \n")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new flight")
    print("2. Delete a flight")
    print("3. Retrieve all flights")
    print("4. Retrieve flight by id")
    print("5. Retrieve bookings for a flight")
    print("6. Create new booking")
    print("7. Delete a booking")
    print("8. Retrieve all bookings")
    print("9. Retrieve booking by id")
    print("10. Retrieve flight that booking belongs to")

if __name__ == "__main__":
    main()