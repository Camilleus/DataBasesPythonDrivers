pip install cx-Oracle 
 
import cx_Oracle 
 
# Connect to Oracle database 
conn = cx_Oracle.connect('username/password@hostname:port_number/db_name') 
 
# Create a cursor object 
cur = conn.cursor() 
 
# Create a table 
cur.execute('''CREATE TABLE 
                   	Users(id number(10), name varchar2(20), email varchar2(30))''') 
 
# Insert a new row into the user’s table 
cur.execute("INSERT INTO users (name, email) VALUES (:1, :2)", (‘Bob’, ‘bob@mail.com’)) 

# Execute a SQL query 
cur.execute('SELECT * FROM users') 
 
# Fetch all rows 
rows = cur.fetchall() 
 
# Close the cursor and connection 
cursor.close() 
connection.close() 