#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.flight import Flight
from models.booking import Booking

def seed_database():
    Booking.drop_table()
    Flight.drop_table()

    Flight.create_table()
    Booking.create_table()

    Flight.create("Emirates", "New Jersey, USA", "Athens, Greece", 1234.56)
    Flight.create("Delta", "New York, NY", "Honolulu, Hawaii", 765.43)
    Flight.create("American Airlines", "New York, USA", "Bermuda", 435.25)

    Booking.create(3, 1)
    Booking.create(4, 2)

seed_database()
print("🌱 Flights and Bookings successfully seeded! 🌱")