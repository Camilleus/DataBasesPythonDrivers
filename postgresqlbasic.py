pip install psycopg2 
 
import psycopg2 
 
#  Connect to a PostgreSQL database 
conn = psycopg2.connect( 
	dbname="database", 
	user="username", 
	password="password", 
	host="localhost", 
	port="5432" 
) 
 
# Create cursor object to execute database commands and queries 
cur = conn.cursor() 
 
# Create a table 
cur.execute(""" 
	CREATE TABLE users ( 
    	id serial PRIMARY KEY, 
    	name varchar(50), 
    	email varchar(50), 
	) 
""") 
# Make changes to the database 
conn.commit() 
 
# Insert data into a table 
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ", 
(“Bob”, "bob@mail.com")) 
 
# Query the database for all users 
cur.execute("SELECT * FROM users") 
 
rows = cur.fetchall() 
 
# Close communication with the database 
cur.close() 
conn.close()