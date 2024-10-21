from models.__init__ import CONN, CURSOR

class Flight:
    
    all = []

    def __init__(self, airline, origin, destination, price):
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.price = price
        self.id = None

    @property
    def airline(self):
        return self._airline
    
    @airline.setter
    def airline(self, value):
        if type(value) == str:
            self._airline = value
        else:
            raise TypeError("Airline must be a string text value!")
        
    @property
    def origin(self):
        return self._origin
    
    @origin.setter
    def origin(self, value):
        if type(value) == str:
            self._origin = value
        else:
            raise TypeError("Origin must be a string text value!")
        
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if type(value) == str:
            self._destination = value
        else:
            raise TypeError("Destination must be a string text value!")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if type(value) in [int, float]:
            self._price = value
        else:
            raise TypeError("Price must be either a float or integer value!")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS flights (
                id INTEGER PRIMARY KEY,
                airline TEXT,
                origin TEXT,
                destination TEXT,
                price REAL
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS flights
        """

        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        flight = cls(row[1], row[2], row[3], row[4])
        flight.id = row[0]
        return flight

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM flights
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM flights
        """

        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO flights (airline, origin, destination, price) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.airline, self.origin, self.destination, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Flight.all.append(self)

    @classmethod
    def create(cls, airline, origin, destination, price):
        flight = cls(airline, origin, destination, price)
        flight.save()
        return flight
    
    def delete(self):
        sql = """
            DELETE FROM flights
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Flight.all = [flight for flight in Flight.all if flight.id != self.id]

    def bookings(self):
        from models.booking import Booking

        sql = """
            SELECT * FROM bookings
            WHERE flight_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Booking.instance_from_db(row) for row in rows]

    def __repr__(self):
        return f"<Flight # {self.id}: Airline = {self.airline}, Origin = {self.origin}, Destination = {self.destination}, Price = {self.price}>"