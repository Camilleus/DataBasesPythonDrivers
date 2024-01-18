# pip install sqlite3

import sqlite3 
 
# Create a connection to the database 
conn = sqlite3.connect('test.db') 
 
# Create a cursor object 
cur = conn.cursor() 
 
# Create a table 
cur.execute('''CREATE TABLE users 
         	(id INTEGER NOT NULL PRIMARY KEY, name TEXT, email TEXT)''') 
 
# Insert some data 
cur.execute("INSERT INTO users VALUES ( 'Bob', ’bob@mail.com’)") 
 
# Commit changes 
conn.commit() 
 
# Execute a SQL query 
cur.execute('''SELECT * from users''') 
result = cur.fetchall() 
 
# Close the connection 
conn.close()