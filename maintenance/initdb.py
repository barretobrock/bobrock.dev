"""Initializes the database. Should really only be run once or to refresh"""
import sqlite3
from flask_base import bcrypt

connection = sqlite3.connect('database.db')


with open('maintenance/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.executemany(
    "INSERT INTO user (username, password) VALUES (?, ?)",
    (
        ('admin0', bcrypt.generate_password_hash('hunter2').decode('utf-8')),
        ('user1',  bcrypt.generate_password_hash('password0').decode('utf-8'))
    )
)

cur.executemany(
    "INSERT INTO posts (lang, title, content, user_id) VALUES (?, ?, ?, ?)",
    (
        ('en', 'First Post', 'Content for the first post', 1),
        ('en', 'Second Post', 'Content for the second post', 1),
        ('et', 'Esimene postitus', 'Esimeee postituse aseme', 1)
    )
)

connection.commit()
connection.close()
