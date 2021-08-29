# Import Sqlite 3 Module
import sqlite3

# Connect to sqlite and create sales database object
connection = sqlite3.connect('sales.db')

# Cursor object to use methods for SQL
cursor = connection.cursor()

# CREATE Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name text(20),
    age INTEGER,
    gender text(7),
    city text(20)
)
""")

# INSERT values into Customer Table
cursor.execute("""
INSERT INTO CUSTOMERS
VALUES(1,'Mark Watson', 30, 'male', 'New York'),
       (2,'Jane Allison', 25, 'female', 'London'),
       (3,'Andrew Jackson', 40, 'male', 'Germany'),
       (4,'Molly Madison', 55, 'female', 'Portugal')
""")


connection.commit()
connection.close()
