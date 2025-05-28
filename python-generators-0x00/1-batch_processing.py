import sqlite3

def stream_users_in_batches(batch_size):
    i = 0
    with sqlite3('ALX_prodev.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM user_data')
        while i < batch size:
            for i in res:
                yield i
        return res

def batch_processing(batch_size):
    i = 0
    with sqlite3('ALX_prodev.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM user_data WHILE age > 25')
        while i < batch_size:
            for i in result:
                yield i
            i += 1