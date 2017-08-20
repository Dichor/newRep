import sqlite3
conn = sqlite3.connect("newDB.db")
cursor = conn.cursor()
cursor.execute("""INSERT INTO users1 SELECT * FROM users2""")
conn.commit()
