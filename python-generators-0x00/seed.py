#!/usr/bin/python3
import sqlite3


def create_database(conn):
    conn = sqlite3.connect("ALX_prodev.db")
    return conn


def connect_db():
    conn = sqlite3.connect("ALX_prodev.db")
    return conn


def connect_to_prodev():
    conn = sqlite3.connect("ALX_prodev.db")
    cursor = conn.cursor()
    return cursor


def create_table(connection):
    cursor = connection.cursor()
    cursor = connection.execute(
        """CREATE TABLE IF NOT EXISTS user_data (
        user_id TEXT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL)
        """
    )
    connection.commit()


def insert_data(connection, data):
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO  user_data (user_id, name, email, age) VALUES (?, ?, ?, ?)""",
        data,
    )
    connection.commit()
