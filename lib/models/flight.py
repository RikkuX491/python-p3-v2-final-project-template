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
            CREATE TABLE IF NOT EXISTS flights (id INTEGER PRIMARY KEY, airline TEXT, origin TEXT, destination TEXT, price REAL)
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS flights
        """

        CURSOR.execute(sql)