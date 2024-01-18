# pip install cassandra-driver

from cassandra.cluster import Cluster 
 
# Create a session instance 
cluster = Cluster(['127.0.0.1']) 
session = cluster.connect() 
 
# Create a keyspace 
session.execute("CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}") 
 
# Create a table 
session.execute("CREATE TABLE mykeyspace.mytable (id int PRIMARY KEY, name text, age int)") 
 
# Insert a row 
session.execute("INSERT INTO mykeyspace.mytable (id, name, age) VALUES (1, 'John', 30)")