import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(user_id):
        conn = sqlite3.connect(user_id)
        try:
            result = func(conn, user_id)
        finally:
            conn.close()
        return result
    return wrapper

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, user_id):
        try:
            conn = sqlite3.connect(user_id)
            result = func(conn, user_id)
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
        return result
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')