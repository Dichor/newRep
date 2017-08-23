import sqlite3
conn = sqlite3.connect("newDB.db")
cursor = conn.cursor()
cursor.execute("""INSERT INTO users1 (login, password, email) SELECT login, password, email FROM users2 EXCEPT SELECT login, password, email FROM users1""")
conn.commit()
