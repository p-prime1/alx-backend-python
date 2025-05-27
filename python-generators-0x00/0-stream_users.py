import sqlite3


def stream_users():
    with sqlite3.connect('ALX_prodev.db') as conn
        cursor = conn.cursor()
        res = cursor.execute("SELECT * FROM user_data")
        for row in res:
            yield row