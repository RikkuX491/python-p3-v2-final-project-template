from models.__init__ import CONN, CURSOR

class Booking:

    all = []

    def __init__(self, number_of_tickets, total_price, flight_id):
        self.number_of_tickets = number_of_tickets
        self.total_price = total_price
        self.flight_id = flight_id
        self.id = None

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