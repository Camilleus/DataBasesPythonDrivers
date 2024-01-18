# pip install pymysql

import pymysql 
 
# Connect to the database 
conn= pymysql.connect( 
	host='localhost', 
	port=3306, 
	user='root', 
	password='password', 
	database='database' 
) 
 
# Create a cursor object 
cur = conn.cursor() 
 
# Create a table 
cur.execute(''' 
	CREATE TABLE users ( 
    	id INT NOT NULL AUTO_INCREMENT, 
    	name VARCHAR(100) NOT NULL, 
    	email VARCHAR(100) NOT NULL, 
    	PRIMARY KEY (id) 
	) 
''') 
 
# Commit the transaction 
conn.commit() 
 
# Execute the query to insert data 
cur.execute(''' 
        INSERT INTO users (name, email) VALUES 
	('Elon', 'elon@mail.com'), 
	('Bob', 'bob@mail.com') 
''') 
conn.commit() 
 
# Execute the query to select data 
cur.execute('SELECT * FROM users') 
 
# Fetch the results 
rows = cur.fetchall() 
 
# Close the cursor and connection when finished 
cur.close() 
conn.close() 