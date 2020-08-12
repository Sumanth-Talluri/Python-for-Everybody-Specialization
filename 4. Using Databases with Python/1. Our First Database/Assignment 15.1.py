import sqlite3

db = sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Mara', 28)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Otto', 33)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Fyn', 31)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)''')

# Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')


user1 = cursor.fetchone()
print(f"The first row in the resulting record set : {user1[0]}")

db.commit()
db.close()
