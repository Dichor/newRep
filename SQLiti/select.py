import sqlite3
conn = sqlite3.connect("newDB.db")
cursor = conn.cursor()
cursor.execute(""" SELECT * FROM users1""")
print(cursor.fetchall())
