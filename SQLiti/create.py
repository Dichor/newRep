import sqlite3
conn = sqlite3.connect("newDB.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users1
                  (login text, password text, email text)
               """)
cursor.execute("""CREATE TABLE users2
                  (login text, password text, email text)
               """)

