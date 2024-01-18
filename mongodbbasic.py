import pymongo 
 
# Create a client, database, and collection instances 
client = pymongo.MongoClient('mongodb://localhost:27017/') 
db = client['my_database'] 
collection = db['my_collection'] 
 
# Insert a document 
document = {'name': Bob, 'email': ‘bob@mail.com’} 
result = collection.insert_one(document) 
 
# Find a document 
query = {'name': 'Bob'} 
result = collection.find_one(query) 
 
# Update a document 
query = {'name': ‘Bob’} 
new_values = {'$set': {'email': ‘bob_new@mail.com’}} 
result = collection.update_one(query, new_values)