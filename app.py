#app.py

import sqlite3 # Helps us get our main app.py to talk to our schema.sql database
from flask import Flask, url_for # <-- IMPORTANT: Add url_for here 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # This line makes it so we can access columns by name
    conn.row_factory = sqlite3.Row
    return conn

# create an instance of the flask class 

app = Flask(__name__)

#Define a route for the homepage URL ('/')
@app.route('/')
def home(): #Modified HTML page 

    # Connect to the database 
    conn = get_db_connection()
    # Execute a query to get all products 
    products = conn.execute('SELECT * FROM products').fetchall()
    # Close the cnnection 
    conn.close()
    # Imagine we got username from a database later!
    username = "Charlie"
    #We are adding a link to connect our Home page to our styling sheet 
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Awesome Shop</title>
        <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
    </head>
    <body>
        <h1>Welcome to My shop, {username}!</h1>
        <p>Browse our amazing collection of products.</p>
        <a href="/about">About Us</a>
    </body>
    </html>
    """

    #this is the content that will be sent back to the browser 
    return html

#Defining a route for the about page URL that was placed in the hoempage 
@app.route('/about')
def about():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Us</title>
        <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
    </head>
    <body>
        <h1>About Our Shop</h1>
        <p>Get to know us better and learn about our missison and values.</p>
        <a href="/">Home</a>
    </body>
    </html>
    """
    return html

# This block allows us to run the app directly 
if __name__ == '__main__':
    app.run(debug=True)
