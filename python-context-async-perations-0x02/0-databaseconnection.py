import sqlite3


class DatabaseConnection:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()


with DatabaseConnection(practice_db) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
