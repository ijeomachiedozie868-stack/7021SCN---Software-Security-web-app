-- schema.sql

-- First, drop tables if they exist to start with a clean slate
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- Create the users table 
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL, -- the UNIQUE ensures that every value in the username column must be different.
    password TEXT NOT NULL
);

-- Create the products table 
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- This defines a column that must contain text and cannot be empty.
    price REAL NOT NULL, -- This is for numbers that can have decimal points, like prices.
    description TEXT NOT NULL
);