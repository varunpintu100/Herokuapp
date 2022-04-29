import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#query to create a table -- to create a auto incrementing coloumn we need to add the following
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"

cursor.execute(create_table)

connection.commit()

connection.close()

