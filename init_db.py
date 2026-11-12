# init_db.py

import sqlite3

# Establish a connection to the database file
# If it doesn't exist, it will be created.

connection = sqlite3.connect('database.db')

# open the schema.sql file and read its contents
with open('schema.sql') as f:
    connection.executescript(f.read())

# Create a cursor object to execute SQL commands 
cur = connection.cursor()

# Insert some sample data so we have something to look at 
cur.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)",
            ('Classic T-shirt', 15.99, 'A comfortable, 100% cotton t-shirt.')
            )

cur.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)",
            ('Stylish Mug', 9.99, 'Aceramic mug, perfect for your morning coffee.')
            )

# Commit the changes to the database
connection.commit()
# Close the connection 
connection.close()
