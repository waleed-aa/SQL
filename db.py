import sqlite3

#Connect to sqlite and create sales db file
#connection = sqlite3.connect('sales.db')

# Cursor object to invoke methods for SQL
#cursor = connection.cursor()


class Customer:

    def __init__(self, cust_id=-1, name="", age=-1, gender="", city=""):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.connection = sqlite3.connect('sales.db')
        self.cursor = self.connection.cursor()


    def retrieve_customer(self, cust_id):
        self.cursor.execute(""" 
        SELECT *
        FROM CUSTOMERS
        WHERE customer_id = {}""".format(cust_id))

        results = self.cursor.fetchone()

        self.cust_id = cust_id
        self.name = results[1]
        self.age = results[2]
        self.gender = results[3]
        self.city = results[4]
        self.connection = sqlite3.connect('sales.db')
        self.cursor = self.connection.cursor()

    def add_customer(self):
        self.cursor.execute("""
        INSERT INTO CUSTOMERS
        VALUES ({}, '{}', {}, '{}', '{}')
        """.format(self.cust_id, self.name, self.age, self.gender, self.city,))

        self.connection.commit()


p1 = Customer(5, 'John', 40, 'male', 'Brazil')


connection = sqlite3.connect('sales.db')
cursor = connection.cursor()
p1.add_customer()
cursor.execute("SELECT * FROM CUSTOMERS")
result_set = cursor.fetchall()
print(result_set)
connection.close()


# Instantiate a person object
c1 = Customer()
c1.retrieve_customer()
print(c1.age)

