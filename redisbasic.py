# pip install redis


import redis 
 
# Create a Redis client object 
r = redis.Redis(host='localhost', port=6379, db=0) 
 
# Set a key–value pair 
r.set('name', 'Bob') 
r.set('email', 'bob@mail.com') 
 
# Retrieve the value of the key 
value = r.get('name') 
print(value)  # Output: b'Bob' 
 
# Add an item to a set 
r.sadd('users', 'Bob') 
r.sadd('users', 'bob@mail.com') 
 
# Retrieve the members of the set 
users = r.smembers('users') 
print(users)  # Output: {b'Bob', b'bob@mail.com'} 
 
# Create a list 
r.lpush('users', 'Bob') 
r.lpush('users', 'bob@mail.com') 
 
# Retrieve the list 
users = r.lrange('users', 0, -1) 
print(mylist)  # Output: [b'bob@mail.com', b’Bob'] 
 
# Create a hash 
r.hset('users', name', 'Bob') 
r.hset('users', 'email', 'bob@mail.com')
# Retrieve the hash 
users = r.hgetall('users') 
print(users)  # Output: {b'name': b'Bob', b'email': b'bob@mail.com'}