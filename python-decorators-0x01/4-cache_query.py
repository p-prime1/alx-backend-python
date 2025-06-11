import time
import sqlite3
import functools


query_cache = {}


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


def cache_query(func):
    @functools.wraps(func)
    def wrapper(query):
        if query in query_cache:
            return query_cache[query]
        result = func(conn, query)
        query_cache[query] = result
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
