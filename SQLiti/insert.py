import sqlite3
conn = sqlite3.connect("newDB.db")
cursor = conn.cursor()
cursor.execute(""" INSERT INTO  users1 VALUES
                   ('Ivan', '1234', 'ivan95@mail.ru'),
                   ('Petr', '4321', 'petrov97@mail.ru'),
                   ('Sidr', '0012', 'sidr85@mail.ru')
                   """
              )
cursor.execute(""" INSERT INTO  users2 VALUES
                   ('Grisha', '1234', 'grisha95@mail.ru'),
                   ('Roman', '4321', 'roman97@mail.ru'),
                   ('Alex', '0012', 'alex85@mail.ru'),
                   ('Elena', '02547', 'elena99@mail.ru')
                   """
              )
conn.commit()
