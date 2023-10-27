# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    db.execute("SELECT * FROM orders")
    return db.fetchall()

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    db.execute("SELECT * FROM orders WHERE OrderDate > ? AND OrderDate <= ?", (date_from, date_to))
    return db.fetchall()

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    db.execute("""
        SELECT *, julianday(ShippedDate) - julianday(OrderDate) as TimeDelta
        FROM orders
        ORDER BY TimeDelta ASC
    """)
    return db.fetchall()
