import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS parts 
            (id INTEGER PRIMARY KEY, 
            part text, 
            customer text, 
            retailer text, 
            price float)
            """)
        self.conn.commit()

    def create(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()
    # db.create('processor', 'Vlad', 'amd.by', 2.56)

    def read(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    # db.read() -> все, что есть в БД

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()
    # db.update(4, 'videocard', 'Vera', 'amd.by', 0.56)

    def delete(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()
    # db.delete(6)

    def __del__(self):
        self.conn.close()