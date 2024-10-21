from models.__init__ import CONN, CURSOR

class Booking:

    all = []

    def __init__(self, number_of_tickets, flight_id):
        self.number_of_tickets = number_of_tickets
        self.flight_id = flight_id
        associated_flight = self.flight()
        if(associated_flight):
            self._total_price = associated_flight.price * self.number_of_tickets
        else:
            raise Exception("Cannot set total price since the associated flight was not found!")
        self.id = None

    @property
    def number_of_tickets(self):
        return self._number_of_tickets
    
    @number_of_tickets.setter
    def number_of_tickets(self, value):
        if type(value) == int:
            self._number_of_tickets = value
        else:
            raise TypeError("Number of tickets must be a integer value!")
        
    @property
    def total_price(self):
        return self._total_price
    
    @total_price.setter
    def total_price(self, value):
        if type(value) in [int, float]:
            self._total_price = value
        else:
            raise TypeError("Total price must be either a float or integer value!")
        
    @property
    def flight_id(self):
        return self._flight_id
    
    @flight_id.setter
    def flight_id(self, value):
        if type(value) == int:
            self._flight_id = value
        else:
            raise TypeError("Flight id must be a integer value!")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS bookings (id INTEGER PRIMARY KEY, number_of_tickets INTEGER, total_price REAL, flight_id INTEGER)
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS bookings
        """

        CURSOR.execute(sql)

    def flight(self):
        from models.flight import Flight

        sql = """
            SELECT * FROM flights
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (self.flight_id,)).fetchone()
        if row:
            return Flight.instance_from_db(row)
        else:
            return None
    
    def __repr__(self):
        return f"<Booking # {self.id}: Number of tickets = {self.number_of_tickets}, Total price = {self.total_price}, Flight id = {self.flight_id}>"