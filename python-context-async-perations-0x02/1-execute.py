import sqlite3

class ExecuteQuery():
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or []

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()


query = "SELECT * FROM users WHERE age > ?"
params = [25]
with ExecuteQuery('practice_db', query, params) as f
    for row in f:
        print row


