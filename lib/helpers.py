# lib/helpers.py

from models.hotel import Hotel
from models.review import Review

def initialize_database():
    Hotel.create_table()
    Review.create_table()

    Hotel.get_all()
    Review.get_all()

def exit_program():
    print("Goodbye!\n")
    quit()

def interact_with_hotel_data():
    while(True):
        hotel_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            create_hotel()
            break
        elif(user_input == 'r'):
            retrieve_hotels()
            break
        elif(user_input == 'u'):
            update_hotel()
            break
        elif(user_input == 'd'):
            delete_hotel()
            break
        elif(user_input == 'hr'):
            retrieve_hotel_reviews()
            break
        else:
            print("Invalid input! Please try again!\n")

def interact_with_review_data():
    print("You are now interacting with the Review data!")

def hotel_options_menu():
    print("\nHere's the Hotel options menu!")
    print("c: Create a new hotel")
    print("r: Retrieve hotel data")
    print("u: Update a hotel")
    print("d: Delete a hotel")
    print("hr: Retrieve a hotel's reviews\n")

def retrieve_hotels():
    options_for_retrieve_hotels()
    user_input = input("Select an option from the menu: ")

    while(True):
        if(user_input == 'a'):
            print("\nHere are all of the hotels:")
            for hotel in Hotel.all:
                print(hotel)
            # User can press 'return' to continue...
            user_input = input("\nPress 'return' to continue...")
            break
        elif(user_input == '1'):
            while(True):
                try:
                    user_input = input("\nEnter a number for the hotel id to search: ")
                    user_input = int(user_input)
                    hotel = Hotel.find_by_id(user_input)
                    if(hotel):
                        print("\nHere is the hotel you requested:")
                        print(Hotel.find_by_id(user_input))
                    else:
                        print("\nHotel Not Found!")
                    user_input = input("\nPress 'return' to continue...")
                    break
                except:
                    print("Invalid input! Please try again!")
            break
        else:
            print("Invalid input! Please try again!\n")

def options_for_retrieve_hotels():
    print("\nWould you like to retrieve all hotels or just one?")
    print("a: Retrieve all hotels")
    print("1: Retrieve 1 hotel\n")

def create_hotel():
    name = input("Enter a name for the new hotel: ")
    new_hotel = Hotel.create(name)
    print("Here's the information for your new hotel:")
    print(new_hotel)
    user_input = input("\nPress 'return' to continue...")

def update_hotel():
    while(True):
        try:
            user_input = input("\nEnter a number for the hotel id to update: ")
            user_input = int(user_input)
            hotel = Hotel.find_by_id(user_input)
            if(hotel):
                new_hotel_name = input("Enter a new name for the hotel: ")
                hotel.name = new_hotel_name
                hotel.update()
                print("The hotel has been updated:")
                print(hotel)
                user_input = input("\nPress 'return' to continue...")
            else:
                print("\nHotel Not Found!")
            break
        except:
            print("Invalid input! Please try again!")

def delete_hotel():
    while(True):
        try:
            user_input = input("\nEnter a number for the hotel id to delete: ")
            user_input = int(user_input)
            hotel = Hotel.find_by_id(user_input)
            if(hotel):
                hotel.delete()
                print("Hotel successfully deleted!")
            else:
                print("\nHotel Not Found!")
            break
        except:
            print("Invalid input! Please try again!")
    
def retrieve_hotel_reviews():
    while(True):
        try:
            user_input = input("\nEnter a number for the hotel id to get reviews for: ")
            user_input = int(user_input)
            hotel = Hotel.find_by_id(user_input)
            if(hotel):
                print(f"\nHere are the reviews for Hotel # {hotel.id}:")
                print(hotel.reviews())
            else:
                print("\nHotel Not Found!")
            user_input = input("\nPress 'return' to continue...")
            break
        except:
            print("Invalid input! Please try again!")