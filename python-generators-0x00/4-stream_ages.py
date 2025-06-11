import sqlite3


def stream_user_ages():
    with sqlite3.connect("ALX_prodev.db") as conn:
        cursor = conn.cursor()
        result = cursor.execute("SELECT age FROM user_data")
        for row in result:
            yield row[0]


count = 0
total = 0
for age in stream_user_ages():
    total += age
    count += 1
print(f"Average age of users: {total / count:.2f}")
