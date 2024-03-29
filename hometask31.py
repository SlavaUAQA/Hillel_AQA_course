# -*- coding: utf-8 -*-
import sqlite3
import pprint

connection = sqlite3.connect("hometask31.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS boxers (boxer_id INTEGER PRIMARY KEY, name STRING UNIQUE, record STRING, weight INTEGER)")

try:
    cursor.execute("INSERT INTO boxers(boxer_id, name, record, weight) VALUES (1, 'Tyson Fury', '34:0:1', 122)")
except sqlite3.IntegrityError:
    pass

try:
    cursor.execute("INSERT INTO boxers(boxer_id, name, record, weight) VALUES (2, 'Usyk Olexander', '21:0:0', 97)")
except sqlite3.IntegrityError:
    pass

try:
    cursor.execute("INSERT INTO boxers(boxer_id, name, record, weight) VALUES (3, 'Joshua Anthony', '28:3', 118)")
except sqlite3.IntegrityError:
    pass

try:
    cursor.execute("INSERT INTO boxers(boxer_id, name, record, weight) VALUES (4, 'Parker Joseph', '34:3', 115)")
except sqlite3.IntegrityError:
    pass

try:
    cursor.execute("INSERT INTO boxers(boxer_id, name, record, weight) VALUES (5, 'Wilder Dionthay', '43:3:1', 100)")
except sqlite3.IntegrityError:
    pass

result = cursor.execute("SELECT * FROM boxers4 order by weight").fetchall()
pprint.pprint(result)

connection.commit()

cursor.close()
connection.close()
