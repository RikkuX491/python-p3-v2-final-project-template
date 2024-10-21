from models.__init__ import CONN, CURSOR

class Flight:
    
    all = []

    def __init__(self, airline, origin, destination, price):
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.price = price

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