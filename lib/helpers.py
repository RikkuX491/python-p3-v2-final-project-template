# lib/helpers.py

from models.flight import Flight
from models.booking import Booking

def create_flight():
    airline = input("Enter the airline for the flight > ")
    origin = input("Enter the origin for the flight > ")
    destination = input("Enter the destination for the flight > ")
    price = input("Enter the price for the flight > ")

    try:
        new_flight = Flight.create(airline, origin, destination, float(price))
        print("New flight successfully created! Here are the details for the new flight:")
        print(new_flight)
    except:
        print("Error: Unable to add new flight due to invalid information entered!")

def delete_flight():
    id = input("Enter the id for the flight that you want to delete > ")
    flight = Flight.find_by_id(id)
    
    if flight:
        flight.delete()
        print(f"Flight # {id} was successfully deleted!")
    else:
        print(f"Unable to delete Flight # {id} since this flight does not exist!")

def retrieve_all_flights():
    flights = Flight.get_all()

    if len(flights) > 0:
        print("Here is the information for all of the flights:")
        for flight in flights:
            print(flight)
    else:
        print("There are no flights available!")

def retrieve_flight_by_id():
    id = input("Enter the id for the flight that you want to retrieve > ")
    flight = Flight.find_by_id(id)

    if flight:
        print(f"Here is the information for Flight # {id}:")
        print(flight)
    else:
        print(f"Error: Flight # {id} Not Found!")

def retrieve_flight_bookings():
    id = input("Enter the id for the flight that you want to retrieve bookings for > ")
    flight = Flight.find_by_id(id)

    if flight:
        flight_bookings = flight.bookings()
        if len(flight_bookings) > 0:
            print(f"Here is the information for the bookings for Flight # {id}:")
            for booking in flight_bookings:
                print(booking)
        else:
            print(f"Flight # {id} does not have any bookings!")
    else:
        print(f"Error: Flight # {id} Not Found!")

def create_booking():
    number_of_tickets = input("Enter the number of tickets for the booking > ")
    flight_id = input("Enter the flight_id for the booking > ")

    try:
        new_booking = Booking.create(int(number_of_tickets), int(flight_id))
        print("New booking successfully created! Here are the details for the new booking:")
        print(new_booking)
    except:
        print("Error: Unable to add new booking due to invalid information entered!")

def delete_booking():
    id = input("Enter the id for the booking that you want to delete > ")
    booking = Booking.find_by_id(id)

    if booking:
        booking.delete()
        print(f"Booking # {id} was successfully deleted!")
    else:
        print(f"Unable to delete Booking # {id} since this booking does not exist!")

def retrieve_all_bookings():
    bookings = Booking.get_all()

    if len(bookings) > 0:
        print("Here is the information for all of the bookings:")
        for booking in bookings:
            print(booking)
    else:
        print("There are no bookings available!")

def retrieve_booking_by_id():
    id = input("Enter the id for the booking that you want to retrieve > ")
    booking = Booking.find_by_id(id)

    if booking:
        print(f"Here is the information for the Booking # {id}:")
        print(booking)
    else:
        print(f"Error: Booking # {id} Not Found!")

def retrieve_flight_that_booking_belongs_to():
    id = input("Enter the id for the booking that you want to retrieve the flight for > ")
    booking = Booking.find_by_id(id)

    if booking:
        flight = booking.flight()
        if flight:
            print(f"Here is the information for the flight for Booking # {id}:")
            print(flight)
        else:
            print(f"Booking # {id} does not have a flight!")
    else:
        print(f"Error: Booking # {id} Not Found!")

def exit_program():
    print("Goodbye!")
    exit()