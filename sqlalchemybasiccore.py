from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData 
 
 # Create an engine to connect to the database 
engine = create_engine(‘dialect[+driver]://user:password@host/dbname’) 
# Define metadata for the database schema 
metadata_obj = db.MetaData() 
 
# Define a table to store information about users 
users = Table( 
	'users',                                         
	metadata_obj,                                     
	Column(‘id', Integer, primary_key=True),   
	Column('name', String),                     
	Column('email', String),                 
) 
 
# Create the table in the database 
metadata.create_all(engine) 
 
# Insert some data into the table 
connection = engine.connect() 
connection.execute(users.insert(), [ 
	{'name': ‘Bob', 'email': ‘bob@mail.com}, 
	{'name': ‘Elon', 'email': ‘elonl@mail.com}, 
]) 
 
# Query the database to retrieve the inserted data 
result = connection.execute(users.select()) 