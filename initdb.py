"""Initializes the database. Should really only be run once or to refresh"""
import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.executemany(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    (
        ('First Post', 'Content for the first post'),
        ('Second Post', 'Content for the second post')
    )
)

connection.commit()
connection.close()
