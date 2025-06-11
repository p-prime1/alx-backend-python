import sqlite3


def paginate_users(page_size, offset):

    with sqlite3.connect("ALX_prodev") as conn:
        cursor = conn.cursor()
        result = cursor.execute(
            "SELECT * FROM user_data LIMIT ? OFFSET ?", (page_size, offset)
        )
    return result


def lazy_paginate(page_size):
    offset = 0
    while True:
        result = paginate_users(page_size, offset)
        if not result:
            break
        yield result
        offset += page_size
