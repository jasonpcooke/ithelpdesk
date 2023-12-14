import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

# Sample admin data
user_data = ("adminuser@email.com", "adminuser1", "admin", "user", True)

# SQL
sql = "INSERT INTO helpdeskapplication_person (email, password, firstname, surname, isadmin) VALUES(?, ?, ?, ?, ?)"

# Insert data into the table
cursor.execute(sql, user_data)

# Commit the changes and close the connection
connection.commit()
connection.close()